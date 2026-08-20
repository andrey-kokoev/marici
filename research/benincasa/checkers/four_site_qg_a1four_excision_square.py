"""Integral local excision square for one four-node boundary-sum mark."""
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/four-site-qg-a1four-excision-square.json"

# Representative mark y1+y2=0.  Its four nodes are
# [1:-1:eps3:eps4].  On the mark, use
# A=y3^2-y1^2 and B=y4^2-y3^2.  In chart y1=1,
# det d(A,B)/d(y3,y4)=4 eps3 eps4.
nodes=[]
for e3,e4 in itertools.product((-1,1),repeat=2):
    jac=4*e3*e4
    orientation=1 if jac>0 else -1
    total_parity=(-1)*e3*e4
    nodes.append({"point":[1,-1,e3,e4],"jacobian":jac,"orientation":orientation,"total_parity":total_parity})

diag=[row["orientation"] for row in nodes]
assert diag==[1,-1,-1,1]
assert all(row["orientation"]==-row["total_parity"] for row in nodes)
determinant=1
for x in diag: determinant*=x
assert determinant==1

# The exceptional-root basis and the four node occurrences are independently
# free rank-four lattices.  The source-oriented local map is diagonal.
matrix=[[diag[i] if i==j else 0 for j in range(4)] for i in range(4)]

packet={
 "schema":"marici.benincasa.four_site_qg_a1four_excision_square.v1",
 "mark":"y1+y2=0",
 "conic_coordinates":["A=y3^2-y1^2","B=y4^2-y3^2"],
 "ordered_nodes":nodes,
 "root_to_node_matrix":matrix,
 "determinant":determinant,
 "unimodular":True,
 "orientation_vs_total_parity":"orientation = - total_parity on eps2=-1",
 "cech_augmentation_compatibility":"each oriented root maps to the corresponding node augmentation with the displayed sign",
 "cyclic_transport":"the same determinant-one square holds for every labelled boundary-sum mark after cyclic relabelling",
 "new_integral_index":False,
}
OUT.write_text(json.dumps(packet,indent=2)+"\n")
print(json.dumps({"matrix":matrix,"determinant":determinant,"unimodular":True}))
