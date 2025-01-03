"""Function to calculate the Hamming distance between two DNA strands."""


def distance(strand_a: str, strand_b: str) -> int:
    """Calculate the Hamming distance between two DNA strands.

    The function compares two DNA strands and counts the number of differences
    between them. If the strands are of unequal length, a ValueError is raised.

    Args:
        strand_a (str): The first DNA strand.
        strand_b (str): The second DNA strand.

    Returns:
        int: The Hamming distance between the two strands.

    Raises:
        ValueError: If the strands are not of equal length.

    """
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    hamming_distance: int = sum(
        1
        for nucleotide_a, nucleotide_b in zip(strand_a, strand_b)
        if nucleotide_a != nucleotide_b
    )

    return hamming_distance
