## PAL Instruction Set Reference

Below is the full list of currently supported PAL instructions. Each instruction corresponds to a specific biological function or domain, represented internally by unique RNA motifs (codons). Use these instructions to build modular, functional protein programs.

| Instruction               | Description                                          | Notes                                      |
|---------------------------|------------------------------------------------------|--------------------------------------------|
| `BIND DNA`                | Bind the protein to DNA sequences                     | Essential for DNA-targeting domains        |
| `SIGNAL NUCLEUS`          | Target the protein to the cell nucleus                | Adds nuclear localization signal (NLS)    |
| `CATALYZE PHOSPHORYLATION`| Catalyze phosphorylation of target molecules         | Activates enzymatic kinase activity        |
| `MOTOR JUMP`              | Activate motor domain to induce jumping or movement  | Useful for motor proteins                   |
| `LINK`                    | Add flexible linker peptide region                    | Connects protein domains smoothly          |
| `ATC GFP`                 | Attach green fluorescent protein domain               | Enables visualization via fluorescence     |
| `BIND RNA`                | Bind to specific RNA sequences                         | For RNA-binding proteins (add motif to dict) |
| `SIGNAL CYTOPLASM`        | Localize protein to the cytoplasm                      | Directs cellular localization               |
| `CATALYZE DEAMINATION`    | Catalyze deamination reactions                         | For editing or metabolic functions          |
| `MOTOR WALK`              | Enable walking motor activity                          | Motor protein movement                      |
| `ATC HIS_TAG`             | Attach Histidine tag for purification                  | Enables protein purification                |
| `BIND LIGAND`             | Bind small molecule ligand                             | For receptor or sensor proteins             |
| `CATALYZE MUTATION`       | Catalyze mutation or DNA editing                       | For gene editing functions                   |

---

### Notes:

- The instruction set can be extended by modifying the `INSTRUCTION_TO_MOTIF` mapping in the source code.
- Unsupported instructions will cause compilation warnings.
- Complex logic (like conditionals or loops) is planned for future PAL versions.
- This is not all instructions

---

Use these instructions in your PAL code to create precise and powerful protein behaviors!
