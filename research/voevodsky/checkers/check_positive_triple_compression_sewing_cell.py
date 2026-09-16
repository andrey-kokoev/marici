"""Exact finite noncommuting audit of the positive triple-compression sewing cell."""
import json,sys
from pathlib import Path
try:
 import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
P=s.diag(1,1,0,0);Q=s.zeros(4)
for a,b in ((0,2),(1,3)):
 Q[a,a]=s.Rational(9,25);Q[a,b]=Q[b,a]=s.Rational(12,25);Q[b,b]=s.Rational(16,25)
# A deliberately fails to commute with P.
A=s.Matrix([[1,2,0,1],[0,1,1,0],[1,0,1,-1],[0,1,0,2]])
H=A*A.T;I=s.eye(4);B=P*Q*P
T=s.trace(P*Q*H);Pos=s.trace(P*Q*P*H);Sew=s.trace(P*Q*(I-P)*H)
comm=P*H-H*P;trans=P*Q*(I-P);factor=-s.trace(P*Q*(I-P)*comm*P)
hs_trans=s.trace(trans*trans.T);hs_comm=s.trace(((I-P)*comm*P)*((I-P)*comm*P).T)
checks={'P_projection':P*P==P,'Q_projection':Q*Q==Q,'positive_feature_gram':Pos==s.trace((Q*P*A).T*(Q*P*A)),'product_trace_decomposition':T==Pos+Sew,'sewing_commutator_factorization':Sew==factor,'prolate_transition_identity':hs_trans==s.trace(B-B*B),'observer_noncommuting':comm!=s.zeros(4),'cauchy_schwarz_squared':Sew**2<=hs_trans*hs_comm}
checks={k:bool(v) for k,v in checks.items()}
out={'schema':'marici.voevodsky.positive-triple-compression-sewing-cell.v1','product_trace':str(T),'positive_triple_compression':str(Pos),'sewing_term':str(Sew),'prolate_transition_mass':str(hs_trans),'observer_boundary_mass':str(hs_comm),'checks':checks,'all_exact':all(checks.values()),'meaning':'The physical product trace splits exactly into a positive triple-compression Gram and a sewing pairing between the prolate transition and observer boundary commutator.','next_gate':'Construct the bulk projection inside the triple-compression feature and prove convergence of the recentered sewing pairing.'}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'positive-triple-compression-sewing-cell.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
