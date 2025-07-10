# PAL — Protein Assembly Language

PAL is a domain-specific programming language to design synthetic proteins by writing instructions that compile to mRNA sequences.  
It lets you create programmable proteins with functional modules — motors, sensors, binding sites, and more — by assembling biological motifs like amino acid sequences.

---

## Features

- Write high-level biological instructions like `BIND ATP`, `MOTOR JUMP`, `SIGNAL NUCLEUS`
- Define reusable functions/modules with `FUNC`/`END FUNC` and call them via `CALL`
- Compile PAL code to mRNA sequences ready for synthesis or simulation
- Designed for synthetic biology education, bioinformatics research, and protein engineering prototyping

---

## Installation

Clone this repo and install dependencies (if any):

```bash
git clone https://github.com/yourusername/pal.git
cd pal
pip install -r requirements.txt  # if you add dependencies
