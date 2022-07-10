import logging

from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
)
from sqlalchemy.engine.row import LegacyRow
from sqlalchemy.exc import IntegrityError


LOGGER = logging.getLogger(__name__)

class CompoundsDatabase:
    """Creates database for compounds. Performs `insert` and `select` queries."""

    def __init__(self) -> None:
        """Initializes database."""
        self.engine = create_engine("postgresql+psycopg2://general_user:password@db:5432/compounds")
        self.compounds = None

    def create_table(self) -> None:
        """Creates `compounds` table to store summaries of compounds."""
        metadata = MetaData()

        # The lengths of Strings were chosen according to compounds
        # That should be used in this project
        self.compounds = Table(
            "compounds",
            metadata,
            Column("id", Integer, primary_key=True),
            Column("compound", String(3), unique=True),
            Column("name", String(160)),
            Column("formula", String(20)),
            Column("inchi", String(310)),
            Column("inchi_key", String(27)),
            Column("smiles", String(100)),
            Column("cross_links_count", Integer),
        )

        metadata.create_all(self.engine)

    def insert_data(
        self,
        compound: str,
        name: str,
        formula: str,
        inchi: str,
        inchi_key: str,
        smiles: str,
        cross_links_count: int,
    ) -> None:
        """Inserts data into `compounds` table.

        Args:
            compound (str): compound hetcode
            name (str): compound name
            formula (str): compound formula
            inchi (str): InChI representation of compound
            inchi_key (str): InChIKey of compound's InChI representation
            smiles (str): SMILES representation of compound
            cross_links_count (int): number of cross links of compound
        """
        with self.engine.connect() as connection:
            try:
                query = self.compounds.insert().values(
                    compound=compound,
                    name=name,
                    formula=formula,
                    inchi=inchi,
                    inchi_key=inchi_key,
                    smiles=smiles,
                    cross_links_count=cross_links_count,
                )

                connection.execute(query)
            except IntegrityError:
                LOGGER.exception("Failed to insert duplicate compound")

    def select_data(self) -> list[LegacyRow]:
        """Select all rows from `compounds` table.

        Returns:
            list[LegacyRow]: content of `compounds` table
        """
        with self.engine.connect() as connection:
            query = self.compounds.select()
            result = list(connection.execute(query))

        return result
