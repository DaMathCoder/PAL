# PAL — Protein Assembly Language

**PAL** is a domain-specific programming language for designing synthetic proteins using programmable biological instructions. By writing simple, readable PAL code, you can define modular proteins that compile into **injectable mRNA sequences**, ready to be translated into functional proteins inside living cells.

Whether you're a synthetic biologist, a bioinformatics researcher, or an educator, PAL lets you express the logic of biological design in a structured, programmable format — just like coding a computer, but in molecules.

---

## 🧬 What is PAL?

PAL treats proteins like programmable machines. You describe what a protein should do (bind DNA, catalyze a reaction, glow, etc.), and the PAL compiler translates that into the **RNA sequence** that will make a real protein with those functions.

It abstracts complex biochemical logic into human-readable code:
- `BIND DNA` adds a DNA-binding motif
- `SIGNAL NUCLEUS` adds a nuclear localization tag
- `ATC GFP` appends a green fluorescent domain

This simplifies protein design into three main layers:
1. **High-level PAL code** — readable, modular instructions
2. **RNA sequence** — the biological blueprint
3. **Protein output** — the functional molecule inside a cell

---

## 🚀 Features

- ✅ Write high-level **biological instructions** like:
  - `BIND ATP`
  - `MOTOR JUMP`
  - `SIGNAL NUCLEUS`
  - `CATALYZE PHOSPHORYLATION`
- ✅ Define **modular protein functions** using `FUNC` and `END FUNC`
- ✅ Use `CALL` to reuse and sequence complex behaviors
- ✅ Compile to **injectable mRNA** including:
  - m7G 5′ Cap
  - Open Reading Frame (ORF)
  - Poly-A tail
- ✅ Codon-to-function mapping with full **motif-level control**
- ✅ Simulate, analyze, or synthesize output mRNA
- ✅ Ideal for:
  - Synthetic biology education
  - Bioengineering prototyping
  - Genetic circuit simulation
  - Artistic or speculative biology design

---

# PAL — Protein Assembly Language

**PAL** is a domain-specific programming language for designing synthetic proteins using programmable biological instructions.  
It compiles high-level "protein code" into real mRNA that cells can read — creating programmable proteins from reusable modules like motors, sensors, tags, and catalytic domains.

---

## ⚙️ Installation

PAL is written in **pure Python**, with no complex dependencies.

Clone the project manually:

```bash
git clone https://github.com/yourusername/pal.git
cd pal
pip install -r requirements.txt  # optional
```

# 🧚 PAL — Program Proteins Like Software

**PAL (Protein Assembly Language)** lets you design synthetic proteins with modular logic and expressiveness—like code for biology.

Design the next generation of life, one codon at a time.

---

## 📦 Installation

```bash
pip install pal-language  # Coming soon to PyPI!
```

---

## 📄 Example — Create a Programmable Protein

Write a PAL program to build a synthetic protein with two modular functions:

```pal
FUNC SENSOR
    BIND ATP
    SIGNAL CYTOPLASM
END FUNC

FUNC EFFECTOR
    CATALYZE PHOSPHORYLATION
    MOTOR JUMP
END FUNC

START
CALL SENSOR
CALL EFFECTOR
ATC GFP
END
```

---

## 🐍 Compile It in Python

Use the PAL compiler to convert your code to mRNA:

```python
from pal import compile_pal_to_mrna_with_functions

code = """
FUNC SENSOR
    BIND ATP
    SIGNAL CYTOPLASM
END FUNC

FUNC EFFECTOR
    CATALYZE PHOSPHORYLATION
    MOTOR JUMP
END FUNC

START
CALL SENSOR
CALL EFFECTOR
ATC GFP
END
"""

mRNA = compile_pal_to_mrna_with_functions(code)
print("mRNA Output:\n", mRNA)
```

---

## 📚 Instruction Set

| Instruction                | Effect                             |
| -------------------------- | ---------------------------------- |
| `BIND DNA`                 | Adds a DNA-binding motif           |
| `SIGNAL NUCLEUS`           | Adds a nuclear localization tag    |
| `CATALYZE PHOSPHORYLATION` | Adds kinase activity               |
| `MOTOR JUMP`               | Adds motor domain for motion       |
| `ATC GFP`                  | Attaches green fluorescent protein |
| `LINK`                     | Adds linker region between domains |

🛠 To add more instructions, edit the `INSTRUCTION_TO_MOTIF` dictionary in `instructions.py`.

---

## 📪 Output Format

Compiling a PAL program produces:

* ✅ Full mRNA sequence starting with a 5′ Cap (`m7G-`)
* ✅ Motif codons translated from PAL instructions
* ✅ Stop codon and Poly-A tail (`-AAA...`) for stability
* ✅ *(Optional)* Translated amino acid chain for inspection

---

## 🔬 External Tools

Use the generated mRNA with:

* [ExPASy Translate](https://web.expasy.org/translate/) — Translate mRNA to protein
* [AlphaFold](https://alphafold.ebi.ac.uk/) / ColabFold — Predict 3D structure
* [BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi) — Compare with known proteins
* [RNAfold](http://rna.tbi.univie.ac.at/cgi-bin/RNAWebSuite/RNAfold.cgi) — Predict mRNA structure

---

## 🗂 Project Structure

```
pal/
  __init__.py
  compiler.py         # Compiles PAL to RNA
  instructions.py     # Instruction → motif mappings
  utils.py            # Codon helpers

examples/
  Glow_In_The_Dark.py
  CRISPR_Protein.py
  Self_Assembly_Motor.py

README.md
LICENSE
```

---

## 📈 Roadmap

✅ Basic PAL → mRNA compiler
✅ Instruction → motif → codon conversion
✅ Support for function definitions and reuse
⏳ Conditional logic and loop support
⏳ RNA secondary structure visualization
⏳ DNA plasmid output for cloning
⏳ Web IDE with visual debugging
⏳ Full synthetic biology simulator backend

---

## 🤝 Contributing

We welcome contributions from:

🧬 Biohackers · 🧪 Scientists · 💻 Developers
🎓 Educators · 🧠 Dreamers

### Get Started

1. Fork this repo
2. Create a new feature branch
3. Add/improve PAL functionality
4. Submit a pull request

💡 Suggest new motifs, domains, or functions—PAL grows with your imagination!

---

## 📜 License

This project is licensed under the **MIT License**.
See the `LICENSE` file for full terms.

---

## 👨‍🎓 Contact

GitHub — [github.com/DaMathCoder/pal](https://github.com/DaMathCoder/pal)

---

🧚 **PAL — Protein Assembly Language**
Design biology like you write code.
