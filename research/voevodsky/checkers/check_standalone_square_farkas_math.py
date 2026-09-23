"""Self-contained rational Farkas checks: no owner, graph or audit imports."""
from fractions import Fraction as Q
from pathlib import Path
import json
rows=(((-Q(1),Q(0)),Q(0)),((Q(1),Q(0)),Q(1)),((Q(0),-Q(1)),Q(0)),((Q(0),Q(1)),Q(1)))
p=(Q(1),Q(2),Q(0),Q(0));q=(Q(0),Q(1),Q(1),Q(1))
def evaluate(m):return tuple(sum(rows[i][0][j]*m[i] for i in range(4)) for j in (0,1)),sum(rows[i][1]*m[i] for i in range(4))
assert min((*p,*q))>=0 and evaluate(p)==evaluate(q)==((Q(1),Q(0)),Q(2))
k=tuple(q[i]-p[i] for i in range(4))
assert evaluate(k)==((Q(0),Q(0)),Q(0)) and k!= (0,0,0,0)
assert tuple(p[i]+k[i] for i in range(4))==q
# Endpoint/local comparison proof is mathematical and needs no alleged issuer.
report={'passed':True,'local_math':'P,Q distinct nonnegative square-row proofs of x<=2; signed q-p zero normal/bound','imports':['fractions.Fraction','pathlib.Path','json'],'communication_or_owner_inputs':False,'publication':'BLOCKED_NO_SOURCE_ISSUER','analytic_correspondence':'DEFERRED_NO_AUTHORITY_MAP','scope':'Frozen explicit 4-row matrix mathematical inference only; no claim rows issued by source owner.'}
out=Path(__file__).resolve().parents[1]/'results/standalone-square-farkas-math.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
