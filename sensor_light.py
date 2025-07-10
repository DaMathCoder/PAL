from PAL import mRNA_Compile, wrap_mrna_for_eukaryotes

pal_code = """
START
SENSE LIGHT
SIGNAL CYTOPLASM
ATC GFP
END
"""

mrna = mRNA_Compile(pal_code)
injectable = wrap_mrna_for_eukaryotes(mrna)
print("glow in the dark protein:", injectable)
