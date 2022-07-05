from typing import Any, Optional

from texttable import Texttable

available_compounds = [
    "ADP",
    "ATP",
    "STI",
    "ZID",
    "DPM",
    "XP9",
    "18W",
    "29P",
]


def argument(*args: str, **kwargs: Any) -> tuple[tuple[str], dict[str, Any]]:
    """Helper function for subcommands to take arguments.

    Args:
        *args: variable length argument list
        **kwargs: arbitrary keyword arguments

    Returns:
        tuple[tuple[str], dict[str, Any]]: all arguments as a tuple
    """
    return args, kwargs


def subcommand(*subparser_args, parent):
    def decorator(func):
        parser = parent.add_parser(func.__name__, description=func.__doc__)

        for args, kwargs in subparser_args:
            parser.add_argument(*args, **kwargs)

        parser.set_defaults(func=func)

    return decorator


def pretty_print_table(
    data: list[list[Any]],
    max_width: Optional[int] = 0,
) -> None:
    """Draws beautiful table for data.

    Args:
        data (list[list[Any]]): table content, including header row
        max_width (int, optional): max width of the table. Default value is 0
    """
    text_table = Texttable(max_width=max_width)
    text_table.add_rows(data)

    print(text_table.draw())


def truncate_sequence(
    sequence: str,
    width: Optional[int] = 13,
) -> str:
    """Truncates sequence according to the width and instead of last 3 characters adds `...`.

    Args:
        sequence (str): sequence that should be truncated
        width (int, optional): truncation width. Default value is 13

    Returns:
        str: truncated sequence
    """
    if len(sequence) > width:
        return f"{sequence[:width-3]}..."

    return sequence
