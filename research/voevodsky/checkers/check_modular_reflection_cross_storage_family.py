"""Exact classification of scalar modular-reflection cross storages."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
r=s.symbols('r',real=True)
P=s.Matrix([[1,r],[r,1]])
H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
diag=s.simplify(H.T*P*H)
out={'cross_storage':'K=rho R, after identifying the two half-line fibers by modular reflection R','reduced_matrix':str(P.tolist()),'even_odd_diagonalization':str(diag.tolist()),'eigenvalues':['1+rho','1-rho'],'positive_iff':'-1 <= rho <= 1','strictly_positive_iff':'-1 < rho < 1','rho_plus_one':'odd channel is radical','rho_minus_one':'even channel is radical','rho_zero':'two sheets are uncoupled','conclusion':'Modular reflection and positivity leave a continuum of cross storages. They do not select the physical Clark coupling.','rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'modular-reflection-cross-storage-family.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
