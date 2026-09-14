#!/usr/bin/env python3
"""Exact finite hostile: Adams grade raising is not full heat-time dilation."""
import json
from fractions import Fraction
from pathlib import Path

def main():
 # Formal heat variables x_k=e^{-t(k log p)^2}; under t->r^2t, x_k -> x_(rk).
 # Full dilated trace sums x_(rk) with original coefficients over every k.
 # Adams image of the original grade carrier occupies only target labels divisible by r.
 r=2;source_grades=[1,2,3];adams_target=[r*k for k in source_grades];full_target_grades=[1,2,3,4,5,6]
 omitted=[k for k in full_target_grades if k not in adams_target]
 assert omitted==[1,3,5]
 # Exact positive formal coefficients show omitted contribution cannot vanish identically.
 coeff={k:Fraction(1,k) for k in full_target_grades};omitted_mass=sum(coeff[k] for k in omitted);assert omitted_mass>0
 result={'schema':'marici.voevodsky.Adams-CP-heat-trace-crossing-no-go.v1','Adams_action':'k -> r k','heat_dilation':'exp(-t(k log p)^2) -> exp(-(r^2 t)(k log p)^2)=exp(-t(rk log p)^2)','fixture':{'r':r,'source_grades':source_grades,'Adams_target_support':adams_target,'full_heat_target_support':full_target_grades,'nondivisible_omitted_grades':omitted,'positive_omitted_formal_mass':str(omitted_mass)},'exact_full_heat_identity':False,'reason':'Adams lands on the divisible-grade subspace, whereas the full heat observer at the dilated time includes contributions indexed by every source grade.','surviving_statement':'Adams CP conjugation gives a positive coherent subchannel of heat dilation, not the complete endpoint-gamma-prime heat semigroup.'}
 out=Path(__file__).parents[1]/'results'/'Adams_CP_heat_trace_crossing_no_go.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
