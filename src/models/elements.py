type ElementRow = tuple[str, str, int, int, float | None]

# (symbol, name, period/row, group/col, pauling_en)
ELEMENTS: list[ElementRow] = [
    # Period 1
    ("H", "Hydrogen", 1, 1, 2.20), ("He", "Helium", 1, 18, None),

    # Period 2
    ("Li", "Lithium", 2, 1, 0.98), ("Be", "Beryllium", 2, 2, 1.57),
    ("B", "Boron", 2, 13, 2.04), ("C", "Carbon", 2, 14, 2.55),
    ("N", "Nitrogen", 2, 15, 3.04), ("O", "Oxygen", 2, 16, 3.44),
    ("F", "Fluorine", 2, 17, 3.98), ("Ne", "Neon", 2, 18, None),

    # Period 3
    ("Na", "Sodium", 3, 1, 0.93), ("Mg", "Magnesium", 3, 2, 1.31),
    ("Al", "Aluminum", 3, 13, 1.61), ("Si", "Silicon", 3, 14, 1.90),
    ("P", "Phosphorus", 3, 15, 2.19), ("S", "Sulfur", 3, 16, 2.58),
    ("Cl", "Chlorine", 3, 17, 3.16), ("Ar", "Argon", 3, 18, None),

    # Period 4
    ("K", "Potassium", 4, 1, 0.82), ("Ca", "Calcium", 4, 2, 1.00),
    ("Sc", "Scandium", 4, 3, 1.36), ("Ti", "Titanium", 4, 4, 1.54),
    ("V", "Vanadium", 4, 5, 1.63), ("Cr", "Chromium", 4, 6, 1.66),
    ("Mn", "Manganese", 4, 7, 1.55), ("Fe", "Iron", 4, 8, 1.83),
    ("Co", "Cobalt", 4, 9, 1.88), ("Ni", "Nickel", 4, 10, 1.91),
    ("Cu", "Copper", 4, 11, 1.90), ("Zn", "Zinc", 4, 12, 1.65),
    ("Ga", "Gallium", 4, 13, 1.81), ("Ge", "Germanium", 4, 14, 2.01),
    ("As", "Arsenic", 4, 15, 2.18), ("Se", "Selenium", 4, 16, 2.55),
    ("Br", "Bromine", 4, 17, 2.96), ("Kr", "Krypton", 4, 18, None),

    # Period 5
    ("Rb", "Rubidium", 5, 1, 0.82), ("Sr", "Strontium", 5, 2, 0.95),
    ("Y", "Yttrium", 5, 3, 1.22), ("Zr", "Zirconium", 5, 4, 1.33),
    ("Nb", "Niobium", 5, 5, 1.6), ("Mo", "Molybdenum", 5, 6, 2.16),
    ("Tc", "Technetium", 5, 7, 1.9), ("Ru", "Ruthenium", 5, 8, 2.2),
    ("Rh", "Rhodium", 5, 9, 2.28), ("Pd", "Palladium", 5, 10, 2.20),
    ("Ag", "Silver", 5, 11, 1.93), ("Cd", "Cadmium", 5, 12, 1.69),
    ("In", "Indium", 5, 13, 1.78), ("Sn", "Tin", 5, 14, 1.96),
    ("Sb", "Antimony", 5, 15, 2.05), ("Te", "Tellurium", 5, 16, 2.1),
    ("I", "Iodine", 5, 17, 2.66), ("Xe", "Xenon", 5, 18, None),

    # Period 6 (La in f-block row below)
    ("Cs", "Cesium", 6, 1, 0.79), ("Ba", "Barium", 6, 2, 0.89),
    ("Hf", "Hafnium", 6, 4, 1.3), ("Ta", "Tantalum", 6, 5, 1.5),
    ("W", "Tungsten", 6, 6, 2.36), ("Re", "Rhenium", 6, 7, 1.9),
    ("Os", "Osmium", 6, 8, 2.2), ("Ir", "Iridium", 6, 9, 2.20),
    ("Pt", "Platinum", 6, 10, 2.28), ("Au", "Gold", 6, 11, 2.54),
    ("Hg", "Mercury", 6, 12, 2.00), ("Tl", "Thallium", 6, 13, 1.62),
    ("Pb", "Lead", 6, 14, 2.33), ("Bi", "Bismuth", 6, 15, 2.02),
    ("Po", "Polonium", 6, 16, 2.0), ("At", "Astatine", 6, 17, 2.2),
    ("Rn", "Radon", 6, 18, None),

    # Period 7 (Ac in f-block row below)
    ("Fr", "Francium", 7, 1, 0.7), ("Ra", "Radium", 7, 2, 0.9),
    ("Rf", "Rutherfordium", 7, 4, None), ("Db", "Dubnium", 7, 5, None),
    ("Sg", "Seaborgium", 7, 6, None), ("Bh", "Bohrium", 7, 7, None),
    ("Hs", "Hassium", 7, 8, None), ("Mt", "Meitnerium", 7, 9, None),
    ("Ds", "Darmstadtium", 7, 10, None), ("Rg", "Roentgenium", 7, 11, None),
    ("Cn", "Copernicium", 7, 12, None), ("Nh", "Nihonium", 7, 13, None),
    ("Fl", "Flerovium", 7, 14, None), ("Mc", "Moscovium", 7, 15, None),
    ("Lv", "Livermorium", 7, 16, None), ("Ts", "Tennessine", 7, 17, None),
    ("Og", "Oganesson", 7, 18, None),

    # Lanthanides — row 8, cols 3-17
    ("La", "Lanthanum", 8, 3, 1.10), ("Ce", "Cerium", 8, 4, 1.12),
    ("Pr", "Praseodymium", 8, 5, 1.13), ("Nd", "Neodymium", 8, 6, 1.14),
    ("Pm", "Promethium", 8, 7, 1.13), ("Sm", "Samarium", 8, 8, 1.17),
    ("Eu", "Europium", 8, 9, 1.2), ("Gd", "Gadolinium", 8, 10, 1.2),
    ("Tb", "Terbium", 8, 11, 1.2), ("Dy", "Dysprosium", 8, 12, 1.22),
    ("Ho", "Holmium", 8, 13, 1.23), ("Er", "Erbium", 8, 14, 1.24),
    ("Tm", "Thulium", 8, 15, 1.25), ("Yb", "Ytterbium", 8, 16, 1.1),
    ("Lu", "Lutetium", 8, 17, 1.27),

    # Actinides — row 9, cols 3-17
    ("Ac", "Actinium", 9, 3, 1.1), ("Th", "Thorium", 9, 4, 1.3),
    ("Pa", "Protactinium", 9, 5, 1.5), ("U", "Uranium", 9, 6, 1.38),
    ("Np", "Neptunium", 9, 7, 1.36), ("Pu", "Plutonium", 9, 8, 1.28),
    ("Am", "Americium", 9, 9, 1.13), ("Cm", "Curium", 9, 10, 1.28),
    ("Bk", "Berkelium", 9, 11, 1.3), ("Cf", "Californium", 9, 12, 1.3),
    ("Es", "Einsteinium", 9, 13, 1.3), ("Fm", "Fermium", 9, 14, 1.3),
    ("Md", "Mendelevium", 9, 15, 1.3), ("No", "Nobelium", 9, 16, 1.3),
    ("Lr", "Lawrencium", 9, 17, None),
]