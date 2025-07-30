massa_atom = {
     "H": 1.01, "He": 4.00, "Li": 6.94, "Be": 9.01, "B": 10.81, "C": 12.01, "N": 14.01, "O": 16.00, "F": 19.00, "Ne": 20.18,
    "Na": 22.99, "Mg": 24.31, "Al": 26.98, "Si": 28.09, "P": 30.97, "S": 32.07, "Cl": 35.45, "Ar": 39.95,
    "K": 39.10, "Ca": 40.08, "Sc": 44.96, "Ti": 47.87, "V": 50.94, "Cr": 52.00, "Mn": 54.94, "Fe": 55.85,
    "Co": 58.93, "Ni": 58.69, "Cu": 63.55, "Zn": 65.38, "Ga": 69.72, "Ge": 72.63, "As": 74.92, "Se": 78.97,
    "Br": 79.90, "Kr": 83.80, "Rb": 85.47, "Sr": 87.62, "Y": 88.91, "Zr": 91.22, "Nb": 92.91, "Mo": 95.95,
    "Tc": 98.00, "Ru": 101.1, "Rh": 102.9, "Pd": 106.4, "Ag": 107.9, "Cd": 112.4, "In": 114.8, "Sn": 118.7,
    "Sb": 121.8, "Te": 127.6, "I": 126.9, "Xe": 131.3, "Cs": 132.9, "Ba": 137.3, "La": 138.9, "Ce": 140.1,
    "Pr": 140.9, "Nd": 144.2, "Pm": 145.0, "Sm": 150.4, "Eu": 152.0, "Gd": 157.3, "Tb": 158.9, "Dy": 162.5,
    "Ho": 164.9, "Er": 167.3, "Tm": 168.9, "Yb": 173.0, "Lu": 175.0, "Hf": 178.5, "Ta": 180.9, "W": 183.8,
    "Re": 186.2, "Os": 190.2, "Ir": 192.2, "Pt": 195.1, "Au": 197.0, "Hg": 200.6, "Tl": 204.4, "Pb": 207.2,
    "Bi": 208.9, "Po": 209.0, "At": 210.0, "Rn": 222.0, "Fr": 223.0, "Ra": 226.0, "Ac": 227.0, "Th": 232.0,
    "Pa": 231.0, "U": 238.0, "Np": 237.0, "Pu": 244.0, "Am": 243.0, "Cm": 247.0, "Bk": 247.0, "Cf": 251.0,
    "Es": 252.0, "Fm": 257.0, "Md": 258.0, "No": 259.0, "Lr": 262.0, "Rf": 267.0, "Db": 270.0, "Sg": 271.0,
    "Bh": 270.0, "Hs": 277.0, "Mt": 276.0, "Ds": 281.0, "Rg": 280.0, "Cn": 285.0, "Nh": 284.0, "Fl": 289.0,
    "Mc": 288.0, "Lv": 293.0, "Ts": 294.0, "Og": 294.0
}

elemen_periodik = [
    # Baris 1
    [{"simbol": "H", "deskripsi": "Digunakan dalam bahan bakar roket dan sebagai komponen air.", "status": "nonlogam",  "golongan": "nonlogam", "nama": "Hidrogen", "nomor_atom": 1}] + [{}]*16 + [{"simbol": "He", "deskripsi": "Digunakan untuk balon dan pendinginan magnet superkonduktor.", "status": "nonlogam",  "nama": "Helium", "nomor_atom": 2,  "golongan": "gas mulia"}],
    
    # Baris 2
    [{"simbol": "Li", "deskripsi": "Dipakai pada baterai lithium dan pengobatan bipolar.", "status": "logam",  "nama": "Litium", "nomor_atom": 3,  "golongan": "logam alkali"},
     {"simbol": "Be", "deskripsi": "Digunakan dalam paduan logam dan jendela sinar-X.", "status": "logam",  "nama": "Berilium", "nomor_atom": 4,  "golongan": "logam alkali tanah"}] + [{}]*10 + 
    [{"simbol": "B", "deskripsi": "Penting dalam produksi fiberglass dan sabun boraks.", "status": "metaloid",  "nama": "Boron", "nomor_atom": 5,  "golongan": "metaloid"},
     {"simbol": "C", "deskripsi": "Unsur utama dalam senyawa organik dan kehidupan.", "status": "nonlogam",  "nama": "Karbon", "nomor_atom": 6,  "golongan": "nonlogam"},
     {"simbol": "N", "deskripsi": "Komponen utama udara, digunakan dalam pupuk.", "status": "nonlogam",  "nama": "Nitrogen", "nomor_atom": 7,  "golongan": "nonlogam"},
     {"simbol": "O", "deskripsi": "Diperlukan untuk pernapasan dan pembakaran.", "status": "nonlogam",  "golongan": "nonlogam", "nama": "Oksigen", "nomor_atom": 8},
     {"simbol": "F", "deskripsi": "Digunakan dalam pasta gigi dan bahan kimia industri.", "status": "nonlogam",  "nama": "Fluorin", "nomor_atom": 9,  "golongan": "halogen"},
     {"simbol": "Ne", "deskripsi": "Gas mulia digunakan untuk lampu neon.", "status": "nonlogam",  "nama": "Neon", "nomor_atom": 10,  "golongan": "gas mulia"}],
    
    # Baris 3
    [{"simbol": "Na", "deskripsi": "Digunakan dalam pembuatan kaca dan sabun.", "status": "logam",  "golongan": "logam alkali", "nama": "Natrium", "nomor_atom": 11},
     {"simbol": "Mg", "deskripsi": "Penting dalam paduan logam ringan dan kembang api.", "status": "logam",  "nama": "Magnesium", "nomor_atom": 12,  "golongan": "logam alkali tanah"}] + [{}]*10 +
    [{"simbol": "Al", "deskripsi": "Bahan ringan untuk pesawat, kaleng, dan kabel.", "status": "logam",  "nama": "Aluminium", "nomor_atom": 13,  "golongan": "logam pasca transisi"},
     {"simbol": "Si", "deskripsi": "Digunakan dalam chip komputer dan panel surya.", "status": "metaloid",  "nama": "Silikon", "nomor_atom": 14,  "golongan": "metaloid"},
     {"simbol": "P", "deskripsi": "Komponen penting dalam DNA dan pupuk.", "status": "nonlogam",  "nama": "Fosfor", "nomor_atom": 15,  "golongan": "nonlogam"},
     {"simbol": "S", "deskripsi": "Dipakai dalam produksi asam sulfat dan pupuk.", "status": "nonlogam",  "nama": "Sulfur", "nomor_atom": 16,  "golongan": "nonlogam"},
     {"simbol": "Cl", "deskripsi": "Digunakan dalam disinfektan dan produksi PVC.", "status": "nonlogam",  "golongan": "halogen", "nama": "Klorin", "nomor_atom": 17},
     {"simbol": "Ar", "deskripsi": "Digunakan sebagai gas pelindung dalam pengelasan.", "status": "nonlogam",  "nama": "Argon", "nomor_atom": 18,  "golongan": "gas mulia"}],

    # Baris 4
    [{"simbol": "K", "deskripsi": "Penting untuk keseimbangan elektrolit dan pupuk.", "status": "logam",  "nama": "Kalium", "nomor_atom": 19,  "golongan": "logam alkali"},
     {"simbol": "Ca", "deskripsi": "Komponen utama tulang dan semen.", "status": "logam",  "nama": "Kalsium", "nomor_atom": 20,  "golongan": "logam alkali tanah"},
     {"simbol": "Sc", "nama": "Skandium", "nomor_atom": 21,  "golongan": "logam transisi"},
     {"simbol": "Ti", "nama": "Titanium", "nomor_atom": 22,  "golongan": "logam transisi"},
     {"simbol": "V", "nama": "Vanadium", "nomor_atom": 23,  "golongan": "logam transisi"},
     {"simbol": "Cr", "nama": "Kromium", "nomor_atom": 24,  "golongan": "logam transisi"},
     {"simbol": "Mn", "nama": "Mangan", "nomor_atom": 25,  "golongan": "logam transisi"},
     {"simbol": "Fe", "deskripsi": "Digunakan dalam baja dan konstruksi.", "status": "logam",  "nama": "Besi", "nomor_atom": 26,  "golongan": "logam transisi"},
     {"simbol": "Co", "nama": "Kobalt", "nomor_atom": 27,  "golongan": "logam transisi"},
     {"simbol": "Ni", "nama": "Nikel", "nomor_atom": 28,  "golongan": "logam transisi"},
     {"simbol": "Cu", "deskripsi": "Konduktor listrik dan pipa air.", "status": "logam",  "nama": "Tembaga", "nomor_atom": 29,  "golongan": "logam transisi"},
     {"simbol": "Zn", "deskripsi": "Dipakai untuk pelapisan logam dan pembuatan baterai.", "status": "logam",  "nama": "Seng", "nomor_atom": 30,  "golongan": "logam transisi"},
     {"simbol": "Ga", "nama": "Galium", "nomor_atom": 31,  "golongan": "logam pasca transisi"},
     {"simbol": "Ge", "nama": "Germanium", "nomor_atom": 32,  "golongan": "metaloid"},
     {"simbol": "As", "nama": "Arsen", "nomor_atom": 33,  "golongan": "metaloid"},
     {"simbol": "Se", "nama": "Selenium", "nomor_atom": 34,  "golongan": "nonlogam"},
     {"simbol": "Br", "deskripsi": "Digunakan dalam fotografi dan pestisida.", "status": "nonlogam",  "nama": "Bromin", "nomor_atom": 35,  "golongan": "halogen"},
     {"simbol": "Kr", "nama": "Kripton", "nomor_atom": 36,  "golongan": "gas mulia"}],

    # Baris 5
    [{"simbol": "Rb", "nama": "Rubidium", "nomor_atom": 37,  "golongan": "logam alkali"},
     {"simbol": "Sr", "nama": "Stronsium", "nomor_atom": 38,  "golongan": "logam alkali tanah"},
     {"simbol": "Y", "nama": "Itrium", "nomor_atom": 39,  "golongan": "logam transisi"},
     {"simbol": "Zr", "nama": "Zirkonium", "nomor_atom": 40,  "golongan": "logam transisi"},
     {"simbol": "Nb", "nama": "Niobium", "nomor_atom": 41,  "golongan": "logam transisi"},
     {"simbol": "Mo", "nama": "Molibdenum", "nomor_atom": 42,  "golongan": "logam transisi"},
     {"simbol": "Tc", "nama": "Teknesium", "nomor_atom": 43,  "golongan": "logam transisi"},
     {"simbol": "Ru", "nama": "Rutenium", "nomor_atom": 44,  "golongan": "logam transisi"},
     {"simbol": "Rh", "nama": "Rodium", "nomor_atom": 45,  "golongan": "logam transisi"},
     {"simbol": "Pd", "nama": "Palladium", "nomor_atom": 46,  "golongan": "logam transisi"},
     {"simbol": "Ag", "nama": "Perak", "nomor_atom": 47,  "golongan": "logam transisi"},
     {"simbol": "Cd", "nama": "Kadmium", "nomor_atom": 48,  "golongan": "logam transisi"},
     {"simbol": "In", "nama": "Indium", "nomor_atom": 49,  "golongan": "logam pasca transisi"},
     {"simbol": "Sn", "nama": "Timah", "nomor_atom": 50,  "golongan": "logam pasca transisi"},
     {"simbol": "Sb", "nama": "Antimon", "nomor_atom": 51,  "golongan": "metaloid"},
     {"simbol": "Te", "nama": "Telurium", "nomor_atom": 52,  "golongan": "metaloid"},
     {"simbol": "I", "deskripsi": "Digunakan dalam disinfektan dan garam beryodium.", "status": "nonlogam",  "nama": "Iodin", "nomor_atom": 53,  "golongan": "halogen"},
     {"simbol": "Xe", "nama": "Xenon", "nomor_atom": 54,  "golongan": "gas mulia"}],

    # Baris 6
    [{"simbol": "Cs", "nama": "Sesium", "nomor_atom": 55,  "golongan": "logam alkali"},
     {"simbol": "Ba", "nama": "Barium", "nomor_atom": 56,  "golongan": "logam alkali tanah"}] +
     [{"simbol": ""}] * 2 +
     [{"simbol": "La", "nama": "Lantanum", "nomor_atom": 57,  "golongan": "lanthanida"},
      {"simbol": "Ce", "nama": "Serium", "nomor_atom": 58,  "golongan": "lanthanida"},
      {"simbol": "Pr", "nama": "Praseodimium", "nomor_atom": 59,  "golongan": "lanthanida"},
      {"simbol": "Nd", "nama": "Neodimium", "nomor_atom": 60,  "golongan": "lanthanida"},
      {"simbol": "Pm", "nama": "Prometium", "nomor_atom": 61,  "golongan": "lanthanida"},
      {"simbol": "Sm", "nama": "Samarium", "nomor_atom": 62,  "golongan": "lanthanida"},
      {"simbol": "Eu", "nama": "Europium", "nomor_atom": 63,  "golongan": "lanthanida"},
      {"simbol": "Gd", "nama": "Gadolinium", "nomor_atom": 64,  "golongan": "lanthanida"},
      {"simbol": "Tb", "nama": "Terbium", "nomor_atom": 65,  "golongan": "lanthanida"},
      {"simbol": "Dy", "nama": "Disprosium", "nomor_atom": 66,  "golongan": "lanthanida"},
      {"simbol": "Ho", "nama": "Holmium", "nomor_atom": 67,  "golongan": "lanthanida"},
      {"simbol": "Er", "nama": "Erbium", "nomor_atom": 68,  "golongan": "lanthanida"},
      {"simbol": "Tm", "nama": "Tulium", "nomor_atom": 69,  "golongan": "lanthanida"},
      {"simbol": "Yb", "nama": "Ytterbium", "nomor_atom": 70,  "golongan": "lanthanida"},
      {"simbol": "Lu", "nama": "Lutesium", "nomor_atom": 71,  "golongan": "lanthanida"}] +
     [{"simbol": "Hf", "nama": "Hafnium", "nomor_atom": 72,  "golongan": "logam transisi"},
      {"simbol": "Ta", "nama": "Tantalum", "nomor_atom": 73,  "golongan": "logam transisi"},
      {"simbol": "W", "nama": "Wolfram", "nomor_atom": 74,  "golongan": "logam transisi"},
      {"simbol": "Re", "nama": "Renium", "nomor_atom": 75,  "golongan": "logam transisi"},
      {"simbol": "Os", "nama": "Osmium", "nomor_atom": 76,  "golongan": "logam transisi"},
      {"simbol": "Ir", "nama": "Iridium", "nomor_atom": 77,  "golongan": "logam transisi"},
      {"simbol": "Pt", "nama": "Platina", "nomor_atom": 78,  "golongan": "logam transisi"},
      {"simbol": "Au", "nama": "Emas", "nomor_atom": 79,  "golongan": "logam transisi"},
      {"simbol": "Hg", "nama": "Raksa", "nomor_atom": 80,  "golongan": "logam transisi"},
      {"simbol": "Tl", "nama": "Talium", "nomor_atom": 81,  "golongan": "logam pasca transisi"},
      {"simbol": "Pb", "nama": "Timbal", "nomor_atom": 82,  "golongan": "logam pasca transisi"},
      {"simbol": "Bi", "nama": "Bismut", "nomor_atom": 83,  "golongan": "logam pasca transisi"},
      {"simbol": "Po", "nama": "Polonium", "nomor_atom": 84,  "golongan": "metaloid"},
      {"simbol": "At", "nama": "Astatin", "nomor_atom": 85,  "golongan": "halogen"},
      {"simbol": "Rn", "nama": "Radon", "nomor_atom": 86,  "golongan": "gas mulia"}],

    # Baris 7
    [{"simbol": "Fr", "nama": "Fransium", "nomor_atom": 87,  "golongan": "logam alkali"},
     {"simbol": "Ra", "nama": "Radium", "nomor_atom": 88,  "golongan": "logam alkali tanah"}] +
     [{"simbol": ""}] * 2 +
     [{"simbol": "Ac", "nama": "Aktinium", "nomor_atom": 89,  "golongan": "aktinida"},
      {"simbol": "Th", "nama": "Torium", "nomor_atom": 90,  "golongan": "aktinida"},
      {"simbol": "Pa", "nama": "Protaktinium", "nomor_atom": 91,  "golongan": "aktinida"},
      {"simbol": "U", "deskripsi": "Bahan bakar reaktor nuklir.", "status": "logam",  "nama": "Uranium", "nomor_atom": 92,  "golongan": "aktinida"},
      {"simbol": "Np", "nama": "Neptunium", "nomor_atom": 93,  "golongan": "aktinida"},
      {"simbol": "Pu", "nama": "Plutonium", "nomor_atom": 94,  "golongan": "aktinida"},
      {"simbol": "Am", "nama": "Amerisium", "nomor_atom": 95,  "golongan": "aktinida"},
      {"simbol": "Cm", "nama": "Kurium", "nomor_atom": 96,  "golongan": "aktinida"},
      {"simbol": "Bk", "nama": "Berkelium", "nomor_atom": 97,  "golongan": "aktinida"},
      {"simbol": "Cf", "nama": "Kalifornium", "nomor_atom": 98,  "golongan": "aktinida"},
      {"simbol": "Es", "nama": "Einsteinium", "nomor_atom": 99,  "golongan": "aktinida"},
      {"simbol": "Fm", "nama": "Fermium", "nomor_atom": 100,  "golongan": "aktinida"},
      {"simbol": "Md", "nama": "Mendelevium", "nomor_atom": 101,  "golongan": "aktinida"},
      {"simbol": "No", "nama": "Nobelium", "nomor_atom": 102,  "golongan": "aktinida"},
      {"simbol": "Lr", "nama": "Lawrensium", "nomor_atom": 103,  "golongan": "aktinida"}] +
     [{"simbol": "Rf", "nama": "Rutherfordium", "nomor_atom": 104,  "golongan": "logam transisi"},
      {"simbol": "Db", "nama": "Dubnium", "nomor_atom": 105,  "golongan": "logam transisi"},
      {"simbol": "Sg", "nama": "Seaborgium", "nomor_atom": 106,  "golongan": "logam transisi"},
      {"simbol": "Bh", "nama": "Bohrium", "nomor_atom": 107,  "golongan": "logam transisi"},
      {"simbol": "Hs", "nama": "Hassium", "nomor_atom": 108,  "golongan": "logam transisi"},
      {"simbol": "Mt", "nama": "Meitnerium", "nomor_atom": 109,  "golongan": "logam transisi"},
      {"simbol": "Ds", "nama": "Darmstadtium", "nomor_atom": 110,  "golongan": "logam transisi"},
      {"simbol": "Rg", "nama": "Roentgenium", "nomor_atom": 111,  "golongan": "logam transisi"},
      {"simbol": "Cn", "nama": "Kopernisium", "nomor_atom": 112,  "golongan": "logam transisi"},
      {"simbol": "Nh", "nama": "Nihonium", "nomor_atom": 113,  "golongan": "logam pasca transisi"},
      {"simbol": "Fl", "nama": "Flerovium", "nomor_atom": 114,  "golongan": "logam pasca transisi"},
      {"simbol": "Mc", "nama": "Moskovium", "nomor_atom": 115,  "golongan": "logam pasca transisi"},
      {"simbol": "Lv", "nama": "Livermorium", "nomor_atom": 116,  "golongan": "logam pasca transisi"},
      {"simbol": "Ts", "nama": "Tenesin", "nomor_atom": 117,  "golongan": "halogen"},
      {"simbol": "Og", "nama": "Oganesson", "nomor_atom": 118,  "golongan": "gas mulia"}]
]

Ar_tiap_unsur = massa_atom
