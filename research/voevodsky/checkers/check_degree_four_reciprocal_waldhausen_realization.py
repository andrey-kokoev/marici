"""Exact nonzero degree-four Waldhausen/cone realization with reciprocal duality."""
import json,sys
from itertools import combinations
from pathlib import Path
try:
 import sympy as s
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import sympy as s

R=[s.Matrix([[0,1],[1,0]]),
   s.Matrix([[0,1,0],[1,0,0],[0,0,-1]]),
   s.Matrix([[1,0],[0,-1]]),
   s.Matrix([[0,1,0],[1,0,0],[0,0,1]]),
   s.Matrix([[0,1],[1,0]])]
Fplus=[s.Matrix([[1,2],[0,1],[1,-1]]),
       s.Matrix([[2,0,1],[-1,1,0]]),
       s.Matrix([[1,0],[2,-1],[0,1]]),
       s.Matrix([[1,-1,2],[0,1,1]])]
Fminus=[R[i+1]*Fplus[i]*R[i] for i in range(4)]

def comp(edges,i,j):
 out=edges[i]
 for a in range(i+1,j): out=edges[a]*out
 return out

def diag(A,B): return s.diag(A,B)
def cone_d(F):
 # Cone(F): target in degree 0, source in degree 1.
 return s.zeros(F.rows+F.cols,F.rows+F.cols).row_join(s.zeros(F.rows+F.cols,0)) if False else s.BlockMatrix([[s.zeros(F.rows),F],[s.zeros(F.cols,F.rows),s.zeros(F.cols)]]).as_explicit()
def cone_R(i,j): return diag(R[j],R[i])

intervals={}
for i in range(5):
 for j in range(i+1,5):
  P=comp(Fplus,i,j);M=comp(Fminus,i,j)
  assert R[j]*P==M*R[i]
  assert cone_R(i,j)*cone_d(P)==cone_d(M)*cone_R(i,j)
  intervals[(i,j)]=(P,M)

rows=[]
for i,j,k in combinations(range(5),3):
 fijP,fijM=intervals[(i,j)];fjkP,fjkM=intervals[(j,k)];fikP,fikM=intervals[(i,k)]
 # Cone(fij) -> Cone(fik), and Cone(fik) -> Cone(fjk).
 aP=diag(fjkP,s.eye(R[i].rows));aM=diag(fjkM,s.eye(R[i].rows))
 bP=diag(s.eye(R[k].rows),fijP);bM=diag(s.eye(R[k].rows),fijM)
 chain_a=(cone_d(fikP)*aP==aP*cone_d(fijP))
 chain_b=(cone_d(fjkP)*bP==bP*cone_d(fikP))
 nat_a=(cone_R(i,k)*aP==aM*cone_R(i,j))
 nat_b=(cone_R(j,k)*bP==bM*cone_R(i,k))
 # Degree +1 homotopy H: Y_j(deg 0) -> Y_j(deg 1).
 H=s.zeros(R[k].rows+R[j].rows,R[j].rows+R[i].rows)
 H[R[k].rows:R[k].rows+R[j].rows,0:R[j].rows]=s.eye(R[j].rows)
 null=(bP*aP==cone_d(fjkP)*H+H*cone_d(fijP))
 Hm=s.zeros(R[k].rows+R[j].rows,R[j].rows+R[i].rows)
 Hm[R[k].rows:R[k].rows+R[j].rows,0:R[j].rows]=s.eye(R[j].rows)
 null_m=(bM*aM==cone_d(fjkM)*Hm+Hm*cone_d(fijM))
 nat_H=(cone_R(j,k)*H==Hm*cone_R(i,j))
 ok=all([chain_a,chain_b,nat_a,nat_b,null,null_m,nat_H])
 rows.append({'triple':[i,j,k],'first_map_chain':chain_a,'second_map_chain':chain_b,'first_map_reciprocal':nat_a,'second_map_reciprocal':nat_b,'composite_nullhomotopic_plus':null,'composite_nullhomotopic_minus':null_m,'homotopy_reciprocal':nat_H,'exact':ok})

# Every parenthesization of the fourfold composite agrees strictly.
a,b,c,d=Fplus
parenthesizations=[d*(c*(b*a)),d*((c*b)*a),(d*c)*(b*a),(d*(c*b))*a,((d*c)*b)*a]
assoc=all(x==parenthesizations[0] for x in parenthesizations[1:])
out={'schema':'marici.voevodsky.degree-four-reciprocal-waldhausen-realization.v1','vertices':5,'generating_edges':4,'interval_objects':len(intervals),'octahedral_triples':len(rows),'all_interval_reciprocal':True,'all_cone_differentials_reciprocal':True,'all_parenthesizations_equal':assoc,'triple_rows':rows,'all_exact':assoc and all(x['exact'] for x in rows),'analytic_scope':'finite-dimensional bounded operators; graph domains are entire and all ranges are closed','claim_boundary':'A nonzero exact degree-four local realization and uniform interval formula, not the global esd_7 lattice or unbounded completion theorem.'}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'degree-four-reciprocal-waldhausen-realization.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
