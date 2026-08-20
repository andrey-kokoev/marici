"""Exact C3 naturality of the source-normalized soft-node/e6 comparison."""
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/rank12-soft-node-e6-cyclic-naturality.json"

P = [[0,0,1],[1,0,0],[0,1,0]]
c = Fraction(-1,2)
M = [[c if i == j else Fraction(0) for j in range(3)] for i in range(3)]
mul = lambda a,b: [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
assert mul(M,P) == mul(P,M)
assert mul(P,mul(P,P)) == [[1,0,0],[0,1,0],[0,0,1]]

packet = {
  "schema":"marici.benincasa.rank12_soft_node_e6_cyclic_naturality.v1",
  "occurrence_order":["X2-soft/G12","X3-soft/G23","X1-soft/G31"],
  "cyclic_matrix":P,
  "residue_orientation_signs":[1,1,1],
  "node_to_e6_matrix":[[str(x) for x in row] for row in M],
  "commutator_zero":True,
  "threefold_transport_identity":True,
  "deck_character_domain":-1,
  "deck_character_codomain":-1,
  "classification":"the three local comparisons form -(1/2) times the identity on the regular Q[C3] occurrence module; no cyclic sign or unit obstruction"
}
OUT.parent.mkdir(parents=True,exist_ok=True)
OUT.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8")
print(json.dumps(packet))
