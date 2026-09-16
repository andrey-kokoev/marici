"""Exact obstruction: source compression can destroy C34 common-remainder positivity."""
import json,sys
from pathlib import Path
try:
 import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
# Import the exact canonical fixture without executing its report block.
ns={};src=(Path(__file__).with_name('check_relative_c34_metric_minimalization_gate.py')).read_text();exec(src.split("checks=")[0],ns)
P,Q=ns['P'],ns['Q']
A=s.Matrix([[-3,-3],[3,3],[-1,-3],[1,3]])
Pc=s.simplify(A.T*P*A);Qc=s.simplify(A.T*Q*A);D=Pc-Qc
root=s.sqrt(5)
# D has eigenvalues (-144 +- 72 sqrt(5))/25, of opposite signs.
absD=s.Matrix([[504*root/s.Integer(125),288*root/s.Integer(125)],[288*root/s.Integer(125),216*root/s.Integer(125)]])
K=s.simplify((Pc+Qc-absD)/2);det=s.simplify(K.det());trace=s.simplify(s.trace(K))
checks={'compression_rank_two':A.rank()==2,'compressed_grams_positive':bool(Pc.is_positive_definite and Qc.is_positive_definite),'absolute_value_square':s.simplify(absD*absD-D*D)==s.zeros(2),'absolute_value_positive':absD.is_positive_definite,'forced_remainder_has_negative_determinant':bool(det<0),'compressed_polarities_noncommuting':Pc*Qc!=Qc*Pc}
out={'schema':'marici.voevodsky.c34-minimalization-compression-obstruction.v1','compression':[[int(x) for x in row] for row in A.tolist()],'compressed_P':[[str(x) for x in row] for row in Pc.tolist()],'compressed_Q':[[str(x) for x in row] for row in Qc.tolist()],'signed_D':[[str(x) for x in row] for row in D.tolist()],'forced_remainder':[[str(x) for x in row] for row in K.tolist()],'forced_remainder_determinant':str(det),'forced_remainder_determinant_decimal':float(det),'forced_remainder_trace':str(trace),'checks':checks,'all_exact':all(checks.values()),'consequence':'The canonical principal-angle gate is not stable under an arbitrary source-labelled observer/regulator compression. External transport needs a reducing or absolute-value-compatible compression theorem.','next_gate':'Prove the actual transported observer/regulator maps reduce the signed block, or directly bound the negative part of the compressed forced remainder.'}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'c34-minimalization-compression-obstruction.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
