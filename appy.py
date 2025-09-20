from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.EnumerateStereoisomers import EnumerateStereoisomers, StereoEnumerationOptions

# ==============================
# 1. Crear molécula desde un SMILES
# ==============================
# Ejemplo: glucosa (varios centros quirales), ácido láctico, 2-buteno
smiles = "CC(O)C(=O)O"  # Ácido láctico
mol = Chem.MolFromSmiles(smiles)

# ==============================
# 2. Detectar centros quirales
# ==============================
chiral_centers = Chem.FindMolChiralCenters(mol, includeUnassigned=True)
print("Centros quirales encontrados:")
for idx, conf in chiral_centers:
    print(f" - Átomo {idx} ({mol.GetAtomWithIdx(idx).GetSymbol()}) -> {conf}")

# ==============================
# 3. Enumerar TODOS los estereoisómeros
# ==============================
opts = StereoEnumerationOptions(onlyUnassigned=True, includeEnumerations=True)
isomers = tuple(EnumerateStereoisomers(mol, options=opts))
print(f"\nNúmero de estereoisómeros generados: {len(isomers)}")

# ==============================
# 4. Mostrar los estereoisómeros en imágenes
# ==============================
img = Draw.MolsToGridImage(isomers, molsPerRow=4, subImgSize=(200, 200), legends=[Chem.MolToSmiles(m) for m in isomers])
img.show()
