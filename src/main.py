from argparse import ArgumentParser, Namespace
import logging
import time
from tqdm import tqdm

from compounds_database import CompoundsDatabase
from compound_loader import CompoundLoader
from utils import (
    available_compounds,
    argument,
    subcommand,
    pretty_print_table,
    truncate_sequence,
)

logging.basicConfig(
    filename="logfile.log",
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

cli = ArgumentParser()
subparsers = cli.add_subparsers(dest="subcommand")


@subcommand(
    argument(
        "-c",
        "--compound",
        type=str,
        default=None,
        help="Compound that should be load.",
    ),
    parent=subparsers,
)
def get(
    args: Namespace,
    database: CompoundsDatabase,
) -> None:
    """Loads compounds from API and stores them into database.

    Args:
        args (Namespace): arguments of subcommand
        database (CompoundsDatabase): database object to store data into it
    """
    if args.compound is None:
        compounds = available_compounds
    else:
        compounds = [args.compound]

    for compound in tqdm(compounds, desc="Downloading compound(s)"):
        compound_loader = CompoundLoader(available_compounds)
        summary = compound_loader.get_compound_summary(compound)
        database.insert_data(*summary.values())

        time.sleep(1)


@subcommand(
    argument(
        "-mw",
        "--max_width",
        type=int,
        default=0,
        help=(
            "Max width of the table. if set to 0, "
            "size is unlimited, therefore cells won't be wrapped."
        ),
    ),
    parent=subparsers,
)
def print_table(args: Namespace, database: CompoundsDatabase) -> None:
    """Print table.

    Args:
        args (Namespace): arguments of subcommand
        database (CompoundsDatabase): database object where data is stored
    """
    rows = database.select_data()
    data = [
        [
            "ID",
            "Compound",
            "Name",
            "Formula",
            "InChI",
            "InChIKey",
            "SMILES",
            "Cross Links Count",
        ],
    ]

    for row in rows:
        processed_row = []

        for field in row:
            if isinstance(field, str):
                processed_row.append(truncate_sequence(field))
            else:
                processed_row.append(field)

        data.append(processed_row)

    pretty_print_table(data, max_width=args.max_width)


if __name__ == "__main__":
    db = CompoundsDatabase()
    db.create_table()

    parsed_args = cli.parse_args()

    if parsed_args.subcommand is None:
        cli.print_help()
    else:
        parsed_args.func(parsed_args, db)
