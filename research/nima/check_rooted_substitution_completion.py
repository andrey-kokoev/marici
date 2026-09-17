#!/usr/bin/env python3
"""Exact finite witness for strict completion naturality of rooted convolution."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
N=8;t=3
packets=[tuple(v) for v in itertools.product(range(3),repeat=4)]
def conv(a,b,n=N):
 out=[0]*(n+1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):
   if i+j<=n:out[i+j]+=x*y
 return tuple(out)
def pad(a):return tuple(a)+(0,)*(N+1-len(a))
def q(a):return sum(x*t**i for i,x in enumerate(a))
def cut(a,X):return tuple(x if i<=X else 0 for i,x in enumerate(a))
submultiplicative=all(q(conv(pad(a),pad(b)))<=q(pad(a))*q(pad(b)) for a in packets for b in packets)
associative=all(conv(conv(pad(a),pad(b)),pad(c))==conv(pad(a),conv(pad(b),pad(c))) for a,b,c in itertools.product(packets[:12],repeat=3))
cutoff_strict=all(cut(conv(pad(a),pad(b)),X)==cut(conv(cut(pad(a),X),cut(pad(b),X)),X) for a in packets for b in packets for X in range(4))
ternary_bound=all(q(conv(conv(pad(a),pad(b)),pad(c)))<=q(pad(a))*q(pad(b))*q(pad(c)) for a,b,c in itertools.product(packets[:12],repeat=3))
checks={'weighted_convolution_submultiplicative':submultiplicative,'parenthesization_independent':associative,'downward_cutoff_has_no_leakage':cutoff_strict,'rooted_ternary_bound':ternary_bound}
out={'schema':'marici.nima.rooted-substitution-completion.v1','model':'N-graded valuation monoid with exact integer exponential weight','parameters':{'max_degree':N,'weight_base':t,'packets_checked':len(packets)},'theorem':'q_delta(ev_tau)<=product_v q_delta(c_v), hence the rooted operad action extends uniquely and strictly through projective completion','checks':checks,'passed':all(checks.values()),'scope':'finite hostile witness plus general seminorm proof in rooted-substitution-is-continuous-on-the-projective-exponential-completion.md'}
p=ROOT/'research/nima/results/rooted-substitution-completion.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
