from PAL import mRNA_Compile, wrap_mrna_for_eukaryotes

pal_code = """
FUNC CRISPR_EDIT
    BIND DNA                 
    SIGNAL NUCLEUS           
    CATALYZE PHOSPHORYLATION 
END FUNC

START
CALL CRISPR_EDIT
ATC GFP                    
END

"""

mrna = mRNA_Compile(pal_code)
injectable = wrap_mrna_for_eukaryotes(mrna)
print("Universal CRISPR Protein v1", injectable)
