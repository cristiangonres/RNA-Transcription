"""RNA_TRANSCRIPTION Determine the RNA complement of a given DNA sequence"""

def to_rna(dna_strand: str) -> str:
    """The DNA sequence is shifted for RNA complement.

    :param text: str - dna strand.
    :return: str - RNA complement.
    """
    
    transcribed = { "G" : "C", "C" : "G", "T" : "A", "A" : "U" }
    return "".join([transcribed[nucleotide] for nucleotide in dna_strand])


print(to_rna("GA"))