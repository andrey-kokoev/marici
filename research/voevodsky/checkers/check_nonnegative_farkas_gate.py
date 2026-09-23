"""Exact equations alone do not make a Farkas implication proof."""
from fractions import Fraction as Q
from pathlib import Path
import json
rows=(((-1,0),Q(0)),((1,0),Q(1)),((0,-1),Q(0)),((0,1),Q(1)))
def check(m,c,target):
 normal=tuple(sum(m[i]*rows[i][0][j] for i in range(4)) for j in (0,1))
 bound=sum(m[i]*rows[i][1] for i in range(4))+c
 return {'equations':(normal,bound)==target,'nonnegative':all(x>=0 for x in (*m,c))}
negative_multiplier=check((Q(-1),Q(0),Q(0),Q(0)),Q(0),((Q(1),Q(0)),Q(0)))
negative_surplus=check((Q(0),Q(1),Q(0),Q(0)),Q(-1),((Q(1),Q(0)),Q(0)))
valid_p=(Q(0),Q(1),Q(0),Q(0));valid_q=(Q(1),Q(2),Q(0),Q(0))
p=check(valid_p,Q(1),((Q(1),Q(0)),Q(2)))
q=check(valid_q,Q(0),((Q(1),Q(0)),Q(2)))
delta=tuple(valid_p[i]-valid_q[i] for i in range(4))
assert negative_multiplier==negative_surplus=={'equations':True,'nonnegative':False}
assert p==q=={'equations':True,'nonnegative':True} and any(x<0 for x in delta)
assert tuple(valid_q[i]+delta[i] for i in range(4))==valid_p
report={'passed':True,'negative_multiplier':'exact equation but invalid implication packet','negative_surplus':'exact equation but invalid implication packet','two_valid_endpoint_proofs':'x<=2 each exact and nonnegative','signed_endpoint_delta':list(map(str,delta)),'signed_delta_role':'comparison relation only, not standalone Farkas implication','scope':'Local exact algebra, no source-owner grant or analytic role assignment.'}
out=Path(__file__).resolve().parents[1]/'results/nonnegative-farkas-gate.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
