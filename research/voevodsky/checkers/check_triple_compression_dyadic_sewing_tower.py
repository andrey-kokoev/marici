"""Exact Gram conservation and depth-constant sewing for B=PQP."""
import json,sys
from pathlib import Path
try:
 import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
P=s.diag(1,1,0,0);Q=s.zeros(4)
for a,b in ((0,2),(1,3)):
 Q[a,a]=s.Rational(9,25);Q[a,b]=Q[b,a]=s.Rational(12,25);Q[b,b]=s.Rational(16,25)
A=s.Matrix([[1,2,0,1],[0,1,1,0],[1,0,1,-1],[0,1,0,2]]);H=A*A.T;I=s.eye(4);B=P*Q*P
positive=s.trace(B*H);product=s.trace(P*Q*H);sewing=s.trace(P*Q*(I-P)*H)
rows=[]
for n in range(1,6):
 gram=B**(2**n)
 for j in range(n):gram+=B**(2**j)*(I-B**(2**j))
 exact=s.simplify(gram-B)==s.zeros(4)
 rows.append({'depth':n,'bulk_exponent':2**n,'defect_slots':n,'operator_gram_conserved':exact,'scalar_gram':str(s.trace(gram*H)),'product_equals_gram_plus_sewing':product==s.trace(gram*H)+sewing})
# Polynomial successor composition on the bulk slot: two splits preserve its Gram.
t=s.symbols('t');poly=[s.factor(t**(2**n)+sum(t**(2**j)*(1-t**(2**j)) for j in range(n))-t) for n in range(1,6)]
checks={'B_positive_contraction':B.is_positive_semidefinite and (I-B).is_positive_semidefinite,'initial_positive_gram':positive==s.trace((Q*P*A).T*(Q*P*A)),'physical_decomposition':product==positive+sewing,'all_depth_grams_conserved':all(r['operator_gram_conserved'] for r in rows),'sewing_constant_at_all_depths':all(r['product_equals_gram_plus_sewing'] for r in rows),'polynomial_telescoping':all(x==0 for x in poly)}
out={'schema':'marici.voevodsky.triple-compression-dyadic-sewing-tower.v1','positive_gram':str(positive),'sewing':str(sewing),'product_trace':str(product),'depth_rows':rows,'checks':{k:bool(v) for k,v in checks.items()},'all_exact':all(bool(v) for v in checks.values()),'meaning':'The soft dyadic tower over B=PQP preserves the positive triple-compression Gram exactly, and the same physical sewing cell attaches at every depth.','next_gate':'Prove convergence of the recentered sewing pairing and compatibility of cutoff correspondences with the strict depth isometries.'}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'triple-compression-dyadic-sewing-tower.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
