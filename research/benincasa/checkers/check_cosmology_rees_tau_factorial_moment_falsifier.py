#!/usr/bin/env python3
"""Falsify separable factorial-geometric moments using the K recurrence."""
import json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results';P=101
# lambda(i,j)=i!j!u^i v^j.  The x^4 term of K has coefficient 9 at the source point.
# After division by lambda(i,j), K multiplication contains 9*u^4*(i+1)...(i+4).
def rising(i,n):
 z=1
 for h in range(1,n+1):z=z*(i+h)%P
 return z
# Fourth finite difference isolates 4!*9*u^4, nonzero for every u != 0.
res=[]
for u in range(1,P):
 vals=[9*pow(u,4,P)*rising(i,4)%P for i in range(5)]
 for _ in range(4):vals=[(b-a)%P for a,b in zip(vals,vals[1:])]
 res.append(vals[0])
assert all(x==9*24%P*pow(u,4,P)%P for u,x in zip(range(1,P),res)) and all(res)
out={'schema':'marici.benincasa.cosmology-rees-tau-factorial-moment-falsifier.v1','ansatz':'lambda_g(k,l,(i,j))=C_g a^k product b_s^l_s i! j! u^i v^j','derivative_advantage':'i lambda(i-1,j)=lambda(i,j)/u removes explicit i dependence from the derivative term','K_obstruction':'the source K coefficient at monomial (4,0) is 9, so the normalized K recurrence has leading i^4 coefficient 9 a u^4','fourth_difference':'4!*9*a*u^4, nonzero when normalization and K shifting require a,u nonzero','nonzero_u_values_tested_mod101':100,'zero_obstructions':0,'disposition':'separable factorial-geometric moments repair the derivative shift but violate K multiplication for arbitrary exponent','survivor':'a coupled residue functional whose moments satisfy the full K and q quotient recurrences rather than a separable closed form','passed':True};(R/'cosmology_rees_tau_factorial_moment_falsifier.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
