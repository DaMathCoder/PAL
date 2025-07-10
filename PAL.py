# pal_all_in_one.py

# --- Amino acid codons ---

AA_TO_CODON = {
    "MET": "AUG", "ALA": "GCU", "GLY": "GGU", "LYS": "AAA", "CYS": "UGU", "THR": "ACU",
    "SER": "UCU", "TYR": "UAU", "PHE": "UUU", "LEU": "UUA", "VAL": "GUU", "GLU": "GAA",
    "ASP": "GAU", "ARG": "CGU", "ASN": "AAU", "GLN": "CAA", "PRO": "CCU", "HIS": "CAU",
    "ILE": "AUU", "TRP": "UGG", "STOP": "UAA"
}

# --- Instruction motifs ---

INSTRUCTION_TO_MOTIF = {
    # Basic and structural
    "START":             ["MET"],
    "END":               ["STOP"],
    "AA":                [],  # handled separately
    "SEQ":               [],  # handled separately
    "LINK":              ["GLY", "GLY", "GLY"],
    "FOLD HELIX":        ["ALA", "GLU", "ALA", "GLU"],
    "FOLD SHEET":        ["VAL", "ILE", "TYR"],
    "FOLD TURN":         ["PRO", "GLY", "SER"],
    
    # Binding motifs
    "BIND ATP":          ["GLY", "LYS", "GLY", "LYS"],
    "BIND DNA":          ["ARG", "ARG", "GLY", "GLU"],
    "BIND RNA":          ["ARG", "SER", "GLY", "ASN"],
    "BIND PROTEIN":      ["LEU", "ILE", "VAL", "GLY"],
    "BIND LIPID":        ["LEU", "ALA", "PHE", "ILE"],
    "BIND CALCIUM":      ["ASP", "GLU", "ASP", "GLU"],
    "BIND IRON":         ["HIS", "HIS", "GLU", "GLU"],
    
    # Catalysis and enzymatic functions
    "CATALYZE PHOSPHORYLATION": ["GLU", "LYS", "ASP"],
    "CATALYZE HYDROLYSIS":       ["SER", "HIS", "ASP"],
    "CATALYZE OXIDATION":        ["CYS", "HIS", "GLU"],
    "CATALYZE REDUCTION":        ["CYS", "TYR", "SER"],
    "CATALYZE TRANSFERASE":      ["GLU", "HIS", "LYS"],
    
    # Sensory and signaling
    "SENSE LIGHT":         ["TRP", "SER", "ASP"],
    "SENSE TEMP":          ["GLY", "ALA", "ASP"],
    "SENSE CHEMICAL":      ["ASN", "GLN", "SER"],
    "SENSE PRESSURE":      ["VAL", "ILE", "THR"],
    "SENSE MAGNETIC":      ["HIS", "GLU", "CYS"],
    "SENSE ELECTRICAL":    ["ARG", "LYS", "ASP"],
    "SIGNAL NUCLEUS":      ["ARG", "LYS", "LYS", "ARG"],
    "SIGNAL MEMBRANE":     ["LEU", "LEU", "ILE"],
    "SIGNAL SECRETION":    ["MET", "ALA", "ALA", "VAL"],
    "SIGNAL CYTOPLASM":    ["ALA", "GLY", "SER"],
    
    # Motor and movement
    "MOTOR WALK":          ["LYS", "GLU", "GLY", "ALA"],
    "MOTOR JUMP":          ["VAL", "ILE", "LEU", "PHE"],
    "MOTOR ROTATE":        ["PRO", "GLY", "GLU", "ALA"],
    "MOTOR SLIDE":         ["ALA", "VAL", "GLY", "ILE"],
    "MOTOR CONTRACT":      ["GLY", "SER", "ALA", "THR"],
    "MOTOR EXPAND":        ["GLU", "GLU", "GLY", "SER"],
    
    # Transport and localization
    "TRANSPORT MITO":      ["ARG", "LEU", "LEU", "ALA"],
    "TRANSPORT NUCLEUS":   ["ARG", "ARG", "LYS", "ARG"],
    "TRANSPORT VESICLE":   ["LEU", "ILE", "VAL", "GLY"],
    "ANCHOR MEMBRANE":     ["LEU", "VAL", "ILE", "PHE"],
    "ANCHOR CYTOSKELETON":["ALA", "GLY", "SER", "VAL"],
    
    # Modification sites
    "MODIFY PHOS":         ["THR"],
    "MODIFY METH":         ["ARG"],
    "MODIFY ACETYL":       ["LYS"],
    "MODIFY UBIQUITIN":    ["LYS", "GLY", "GLY"],
    "MODIFY SUMO":         ["LYS", "GLU", "GLY"],
    
    # Apoptosis and regulation
    "KILL":                ["ASP", "GLU", "VAL", "ASP"],
    "INHIBIT APOPTOSIS":   ["SER", "PRO", "GLU", "ARG"],
    "REGULATE TRANSCRIPTION": ["ARG", "GLU", "SER", "GLY"],
    "REGULATE TRANSLATION":  ["LYS", "ALA", "GLU", "ASP"],
    
    # Protein-protein interactions
    "DIMERIZE":            ["LEU", "LEU", "GLU", "GLU"],
    "OLIGOMERIZE":         ["GLY", "SER", "GLY", "SER"],
    "CHAPERONE":           ["ALA", "ARG", "GLU", "SER"],
    
    # DNA repair
    "REPAIR DNA":          ["GLU", "HIS", "LYS", "ASP"],
    "REPAIR RNA":          ["SER", "LYS", "GLN", "ASP"],
    
    # Fluorescent domains and tags
    "ATC GFP":             ["GLY", "GLY", "GLY", "MET", "GLY", "GLY", "THR"],
    "ATC RFP":             ["GLY", "GLY", "GLY", "ARG", "ALA", "GLY", "THR"],
    "ATC LUCIFERASE":      ["ALA", "GLY", "MET", "THR", "GLY", "SER"],
    
    # Degradation tags
    "TAG FOR DEGRADATION": ["PRO", "GLU", "GLU", "GLY"],
    "DEGRADE":             ["LYS", "GLY", "GLY"],
    
    # Miscellaneous complex behaviors
    "IMMUNE EVASION":      ["SER", "ARG", "GLY", "ASP"],
    "HORMONE BINDING":     ["TYR", "ALA", "GLU", "GLY"],
    "METABOLIC SWITCH":    ["GLN", "GLU", "ALA", "SER"],
    "NEURON SIGNALING":    ["ARG", "GLU", "GLY", "THR"],
    "MEMBRANE FUSION":     ["VAL", "ILE", "GLY", "ALA"],
    "CELL DIVISION":       ["GLY", "SER", "ALA", "LEU"],
    "DNA PACKAGING":       ["ARG", "LYS", "ARG", "GLY"],
    "RNA SPLICING":        ["SER", "ARG", "LYS", "GLU"],
    "PROTEIN FOLDING":     ["ALA", "GLU", "SER", "GLY"],
    "OXIDATIVE STRESS RESPONSE": ["CYS", "GLU", "ASP", "SER"],
    "CYTOSKELETON REARRANGE": ["GLY", "ALA", "VAL", "SER"],
    "CELL MOTILITY":       ["VAL", "LEU", "ILE", "ALA"],
    "ANTIBODY BINDING":    ["TYR", "GLY", "SER", "ARG"],
    "VIRAL ENTRY":         ["ASP", "ARG", "GLU", "ILE"],
    "PLANT PHOTOSYNTHESIS": ["ALA", "GLY", "SER", "TYR"],
    "BACTERIAL TOXIN":     ["LEU", "VAL", "GLY", "CYS"],
    "CHEMOTAXIS":          ["ASP", "GLU", "ARG", "LYS"],
}


# --- Utility function to convert AA list to RNA string ---

def translate_aa_to_rna(motif):
    rna = []
    for aa in motif:
        codon = AA_TO_CODON.get(aa)
        if not codon:
            raise ValueError(f"Unknown amino acid: {aa}")
        rna.append(codon)
    return "".join(rna)

# --- Function parser ---

def parse_functions(lines):
    functions = {}
    current_func = None
    body = []

    for line in lines:
        line = line.strip()
        if line.upper().startswith("FUNC "):
            current_func = line[5:].strip().upper()
            body = []
        elif line.upper() == "END FUNC":
            if current_func:
                functions[current_func] = body
                current_func = None
                body = []
        elif current_func:
            body.append(line)
    return functions

# --- Compiler: PAL to mRNA ---

def mRNA_Compile(pal_code):
    lines = pal_code.strip().splitlines()
    functions = parse_functions(lines)

    main_code = []
    in_func = False
    for line in lines:
        if line.upper().startswith("FUNC "):
            in_func = True
        elif line.upper() == "END FUNC":
            in_func = False
        elif not in_func:
            main_code.append(line.strip())

    mrna_seq = []

    def compile_line(line):
        line_upper = line.upper()
        if line_upper.startswith("CALL "):
            func_name = line_upper[5:].strip()
            if func_name not in functions:
                print(f"Warning: Unknown function '{func_name}'")
                return
            for func_line in functions[func_name]:
                compile_line(func_line)
        elif line_upper == "START":
            mrna_seq.append(AA_TO_CODON["MET"])
        elif line_upper == "END":
            mrna_seq.append(AA_TO_CODON["STOP"])
        elif line_upper.startswith("AA "):
            aa = line.split()[1].upper()
            codon = AA_TO_CODON.get(aa)
            if codon:
                mrna_seq.append(codon)
            else:
                print(f"Warning: Unknown amino acid '{aa}'")
        elif line_upper.startswith("SEQ "):
            for aa in line.split()[1:]:
                codon = AA_TO_CODON.get(aa.upper())
                if codon:
                    mrna_seq.append(codon)
                else:
                    print(f"Warning: Unknown amino acid '{aa}'")
        else:
            motif = INSTRUCTION_TO_MOTIF.get(line_upper)
            if motif:
                mrna_seq.append(translate_aa_to_rna(motif))
            else:
                print(f"Warning: Unknown instruction '{line}'")

    for line in main_code:
        if line:
            compile_line(line)

    return "".join(mrna_seq)

def wrap_mrna_for_eukaryotes(mrna: str) -> str:
    cap = "m7G"
    tail = "AAA(x98)"
    return f"{cap}-{mrna}-{tail}"
