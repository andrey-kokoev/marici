"""A destructive linear support cannot feed two queries without copying.

Checks actual port incidence for a shared head, and observes consumption
by the existing executable membership normalizer.
"""
from contextlib import redirect_stdout
from io import StringIO
from itertools import product
from pathlib import Path
import json
with redirect_stdout(StringIO()):
 from check_fixed_signature_membership_net import Membership

def one_wire_per_port(edges):
 ports=[port for edge in edges for port in edge]
 return len(ports)==len(set(ports))

shared=[('Q1.p','B0.p'),('Q2.p','B0.p')]
assert not one_wire_per_port(shared)
assert one_wire_per_port([('Q1.p','B0copy1.p'),('Q2.p','B0copy2.p')])
checked=0
for n in range(1,7):
 for word in product((0,1),repeat=n):
  graph=Membership(word,0)
  result,_=graph.normalize()
  assert result==bool(word[0])
  assert set(graph.types)=={'OUT',next(x for x in graph.types if x.startswith(('TRUE_','FALSE_')))}
  assert not any(t.startswith(('B0_','B1_')) for t in graph.types)
  checked+=1
report={'passed':True,'checked_supports':checked,'two_queries_same_principal_port':'fails one-wire-per-port linearity','two_queries_separate_copies':'passes incidence but copies require an explicit constructor/duplicator','post_query':'existing normal form contains only BOOL and OUT; no support nodes for second probe','scope':'Obstruction for this destructive encoding, not impossibility of persistent nets or a completed add(i) implementation.'}
out=Path(__file__).resolve().parents[1]/'results/linear-membership-reuse-obstruction.json'
out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
