"""Function to determine the RNA complement of a given DNA sequence.

This script replaces each nucleotide in a DNA strand with its RNA complement:
G -> C, C -> G, T -> A, A -> U.
"""


def to_rna(dna_strand: str) -> str:
    """Convert a DNA strand to its RNA complement.

    This function replaces each DNA nucleotide with its RNA complement:
    - G -> C
    - C -> G
    - T -> A
    - A -> U

    Args:
        dna_strand (str): The DNA strand to be converted.

    Returns:
        str: The RNA complement of the given DNA strand.

    """
    dna_to_rna_mapping: dict[str, str] = {"G": "C", "C": "G", "T": "A", "A": "U"}

    rna_strand: str = "".join(
        dna_to_rna_mapping[nucleotide] for nucleotide in dna_strand
    )

    return rna_strand
