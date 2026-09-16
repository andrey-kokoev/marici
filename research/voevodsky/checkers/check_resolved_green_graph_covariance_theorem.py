"""Exact finite fixture for covariance of a resolved direct-sum graph form."""
import json,sys
from pathlib import Path
try: import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s
F=s.Matrix([[0,-s.Rational(1,2)],[2,0]]);P=s.diag(1,-1);D=s.diag(1,s.Rational(1,4))
# Three independently retained ports, each carrying the same typed local action.
R=s.Matrix.vstack(s.eye(2),2*s.eye(2),3*s.eye(2))
G=s.simplify(R.T*s.diag(D,D,D)*R)
UF=s.diag(F,F,F);UP=s.diag(P,P,P)
# The three retained ports carry the same typed source action.
L=(R.T*R).inv()*R.T
UF_R=s.diag(F,F,F);UP_R=s.diag(P,P,P)
checks={'F_D_unitary':F.T*D*F==D,'P_D_unitary':P.T*D*P==D,'left_inverse':L*R==s.eye(2),'F_intertwining':UF_R*R==R*F,'P_intertwining':UP_R*R==R*P,'graph_F_covariance':s.simplify(F.T*G*F-G)==s.zeros(2),'graph_P_covariance':s.simplify(P.T*G*P-G)==s.zeros(2)}
out={'base_metric':str(D.tolist()),'source_F':str(F.tolist()),'source_P':str(P.tolist()),'resolved_map_fixture':str(R.tolist()),'pullback_green':str(G.tolist()),'checks':checks,'passed':all(checks.values()),'theorem':'For a resolved graph R with target metric J, R F=U_F R and U_F^* J U_F=J imply F^*R^*JR F=R^*JR; similarly for reflection. The exact fixture verifies this implication for three independently retained ports.','rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'resolved-green-graph-covariance-theorem.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
