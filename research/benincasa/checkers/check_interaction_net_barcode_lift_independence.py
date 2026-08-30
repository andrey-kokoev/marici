#!/usr/bin/env python3
"""Hostile test: finite-field barcode rows do not determine a unique optical analysis row."""
from __future__ import annotations
from fractions import Fraction
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
src=ROOT/"research"/"benincasa"/"results"/"interaction-net-barcode-basis-export-p32009.json"
p=json.loads(src.read_text(encoding="utf-8")); prime=p["prime"]
blocks=p["adapted_depth3_quotient_basis"]
rows=[(name,i,row) for name in ("first_death_rows","second_death_rows","through_depth6_rows")
      for i,row in enumerate(blocks[name]) if len(row["indices"])>=2]
name,i,row=rows[0]
indices=row["indices"]; residues=row["values"]
def balanced(x): return x-prime if x>prime//2 else x
a=[balanced(x) for x in residues]
b=list(a); b[0]+=prime
j,k=0,1
w=[0]*len(a); w[j]=a[k]; w[k]=-a[j]
dot=lambda x,y:sum(u*v for u,v in zip(x,y))
na=dot(a,a); nb=dot(b,b); ab=dot(a,b)
distance=Fraction(2*(na*nb-ab*ab),na*nb)
dark_a=dot(a,w); response_b=dot(b,w)
checks={
 "same_finite_field_row":all((x-y)%prime==0 for x,y in zip(a,b)),
 "support_preserved":all(x!=0 for x in a) and all(x!=0 for x in b),
 "not_projectively_equal":a[j]*b[k]-a[k]*b[j]!=0,
 "normalized_projectors_differ":distance>0,
 "dark_input_for_balanced_lift":dark_a==0,
 "same_input_visible_for_shifted_lift":response_b!=0,
}
out={
 "schema":"marici.barcode-characteristic-zero-lift-hostile.v1","prime":prime,
 "source_block":name,"source_row_index":i,"source_indices":indices,
 "balanced_lift":a,"shifted_lift":b,
 "witness_input":w,
 "projector_frobenius_distance_squared":{"numerator":distance.numerator,"denominator":distance.denominator},
 "responses":{"balanced":dark_a,"shifted":response_b},
 "checks":checks,"passed":all(checks.values()),
 "conclusion":"the_finite_field_barcode_packet_alone_does_not_determine_a_lift_independent_normalized_optical_readout",
}
path=ROOT/"research"/"benincasa"/"results"/"interaction-net-barcode-lift-hostile-p32009.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
if not out["passed"]:raise SystemExit(1)
