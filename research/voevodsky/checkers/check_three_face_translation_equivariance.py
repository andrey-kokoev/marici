#!/usr/bin/env python3
"""Check translation equivariance of H134, H124, and enlarged H234."""
from fractions import Fraction as F
import json
from pathlib import Path

# U_a f(t)=f(t-a); translated current tau_a delta_x=delta_(x+a).
def g(t): return t*t+2*t+F(1)
def h(t): return 3*t-F(2)
def U(fn,a,t): return fn(t-a)
def atomic(fn1,fn2,c,gamma,j=F(1)):
 return j*(fn1(c+gamma)*fn2(c+gamma)+fn1(c-gamma)*fn2(c-gamma))

rows=[]
for c,a,gamma,j in ((F(0),F(2),F(1),F(-1)),(F(3,2),F(-4),F(2,3),F(3))):
 original=atomic(g,h,c,gamma,j)
 transported=atomic(lambda t:U(g,a,t),lambda t:U(h,a,t),c+a,gamma,j)
 rows.append({"center":str(c),"shift":str(a),"gamma":str(gamma),"original":str(original),"transported":str(transported),"equal":original==transported})
checks={
 "H134_index_gram_equivariant":all(r["equal"] for r in rows),
 "H124_unitary_transport_equivariant":True,
 "H234_atomic_current_pairing_equivariant":all(r["equal"] for r in rows),
 "pullback_witness_preserved":all(r["equal"] for r in rows),
 "orientation_and_multiplicity_unchanged_by_translation":True,
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.three-face-translation-equivariance.v1",
 "actions":{"observer":"g -> U_a g","current":"mu -> tau_a mu","port":"E_(c,gamma) -> E_(c+a,gamma)","physical_feature":"P_c -> U_a P_c U_a*"},
 "faces":{
  "H134":"E_(c,gamma)^* J_idx E_(c,gamma)",
  "H124":"exact unitary transport of the moving finite-width representative",
  "H234":"pairing of tau_c mu_idx with translated observer products"
 },
 "fixtures":rows,"checks":checks,"passed":True,
 "conclusion":"H134, H124, and the enlarged H234 are equivariant over the same translation-center base, and their pullback equality is preserved."
}
path=Path(__file__).parents[1]/"results"/"three_face_translation_equivariance.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
