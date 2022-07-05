import logging
from typing import Any

import requests


LOGGER = logging.getLogger(__name__)


class CompoundLoader:
    """Helper class for loading of compounds summaries from `ebi-ac-uk` API."""

    def __init__(self, available_compounds: list[str]) -> None:
        """Initializes compounds that are available to load.

        Args:
            available_compounds (list[str]): list of available compounds
        """
        self.available_compounds = available_compounds

    def get_compound_summary(self, compound: str) -> dict[str, Any]:
        """Loads summary of compound.

        Args:
            compound (str): compound hetcode

        Raises:
            SystemExit: if compoud argument is not in available compounds list

        Returns:
            dict[str, Any]: summary of compound
        """
        if compound.upper() not in self.available_compounds:
            warning_message = "Unsupported compound name"
            LOGGER.warning(warning_message)
            raise SystemExit(f"Warning: {warning_message}")

        compound = compound.upper()

        LOGGER.info("Loading of summary of %s started", compound)

        url = f"https://www.ebi.ac.uk/pdbe/graph-api/compound/summary/{compound}"
        response = requests.get(url)
        compound_info = response.json()[compound][0]

        summary = {
            "compound": compound,
            "name": compound_info["name"],
            "formula": compound_info["formula"],
            "inchi": compound_info["inchi"],
            "inchi_key": compound_info["inchi_key"],
            "smiles": compound_info["smiles"],
            "cross_links_count": len(compound_info["cross_links"]),
        }

        LOGGER.info("Summary of %s loaded successfully", compound)

        return summary
