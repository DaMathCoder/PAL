## How to Design a Protein Using PAL

This guide walks you through creating a custom protein using PAL (Protein Assembly Language) — from writing the code to generating injectable mRNA.

---

### Step 1: Define Your Protein’s Functional Domains

Proteins often have modular domains (e.g., DNA-binding, enzymatic, signaling). In PAL, you define these as functions using biological instructions.

Example — define a DNA-binding domain:

```pal
FUNC DNA_BINDING_DOMAIN
    BIND DNA
    SIGNAL NUCLEUS
END FUNC

# Protein Assembly Language (PAL) - Quickstart Guide

This README walks you through creating and compiling protein designs using PAL, a simple language for programming protein domains and functions.

---

## Step 2: Compose the Main Program

Use the `START` block to sequence your protein’s functions and attach any tags (e.g., GFP for visualization):

```pal
START
CALL DNA_BINDING_DOMAIN
ATC GFP
END

## Step 3: Write Your Full PAL Program

In this step, define your protein’s functional domains as separate `FUNC` blocks, then combine them in the `START` block to create the full protein sequence.

### Define Domain Functions

Each domain encapsulates a specific protein function:

```pal
FUNC DNA_BINDING_DOMAIN
    BIND DNA
    SIGNAL NUCLEUS
END FUNC

FUNC PHOSPHORYLATION_DOMAIN
    CATALYZE PHOSPHORYLATION
    SIGNAL CYTOPLASM
END FUNC

## Step 4: Compile PAL to mRNA

After writing your PAL program, convert it into an injectable mRNA sequence using the provided Python compiler function.

### Use the Compiler

Import the compiler and pass your PAL code as a string:

```python
from pal import compile_pal_to_mrna_with_functions

pal_code = """
FUNC DNA_BINDING_DOMAIN
    BIND DNA
    SIGNAL NUCLEUS
END FUNC

FUNC PHOSPHORYLATION_DOMAIN
    CATALYZE PHOSPHORYLATION
    SIGNAL CYTOPLASM
END FUNC

START
CALL DNA_BINDING_DOMAIN
CALL PHOSPHORYLATION_DOMAIN
ATC GFP
END
"""

mrna = compile_pal_to_mrna_with_functions(pal_code)
print("Injectable mRNA sequence:\n", mrna)

## Step 5: Validate the mRNA Sequence

Before using your mRNA sequence in experiments, ensure its quality and correctness.

### What to Check

- **5′ m7G Cap and Poly-A Tail:** Confirm the sequence includes these modifications to enhance stability and translation efficiency.
- **Correct Protein Translation:** Use tools like [ExPASy Translate](https://web.expasy.org/translate/) to verify the mRNA sequence translates into the expected amino acid sequence.
- **Protein Structure Prediction (Optional):** Run the predicted amino acid sequence through structure prediction tools such as [AlphaFold](https://alphafold.ebi.ac.uk/) to assess proper folding and functionality.

### Tips

- Always verify codon optimization for your target expression system.
- Validate each iteration before moving on to lab work to save time and resources.

## Still Need Help?

If you have questions or run into issues, here are some ways to get assistance:

- **Join our Community:** Connect with other PAL users to share tips and ask questions.
- **Open an Issue on GitHub:** Report bugs, request features, or ask for help by opening an issue at our [GitHub repository](https://github.com/DaMathCoder/pal).
- **Read the Documentation:** Visit our [official docs](https://palproject.org/docs) for detailed guides and API references.
- **Contact the Developer:** If you want updates, tips, or want to help make PAL.

##change the world
We’re here to help you design the proteins of tomorrow, today!
