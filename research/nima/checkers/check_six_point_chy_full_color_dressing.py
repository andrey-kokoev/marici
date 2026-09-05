from __future__ import annotations
import itertools,json
from collections import defaultdict
from pathlib import Path
import sympy as sp
import check_six_point_chy_yang_mills_pfaffian as ym
from check_six_point_chy_all_ddm_gluon_components import kernel,pt_matrix
from check_six_point_nmhv_universal_ddm_dressing import basis_orders,half_ladder_trace

ROOT=Path(__file__).resolve().parents[3];RESULT=ROOT/"research/nima/results/six-point-chy-full-color-dressing.json"
def dress(basis,amps,mutate=None):
 out=defaultdict(lambda:sp.Integer(0))
 for order in basis:
  sign=-1 if order==mutate else 1
  for word,c in half_ladder_trace(order).items():out[word]+=sign*c*amps[order]
 return {w:sp.cancel(v) for w,v in out.items() if sp.cancel(v)!=0}
def main():
 I,Z,inv,base_pt,detprime=ym.setup();b16=basis_orders(1,6);b26=basis_orders(2,6);orders=set(b16+b26);pts={o:pt_matrix(o,Z,I) for o in orders};rows=[]
 for negative in itertools.combinations(range(1,7),3):
  K=kernel(negative,I,Z,inv,detprime);amps={o:sp.cancel(sp.trace(pts[o]*K)) for o in orders};left=dress(b16,amps);right=dress(b26,amps);keys=set(left)|set(right);residual=sum(sp.cancel(left.get(w,0)-right.get(w,0))!=0 for w in keys)
  rows.append({"negative_helicity_legs":list(negative),"ddm_basis_independent":residual==0,"residual_word_count":residual,"nonzero_color_word_count":len(left)})
 target=(1,2,3);K=kernel(target,I,Z,inv,detprime);amps={o:sp.cancel(sp.trace(pts[o]*K)) for o in orders};hostile=dress(b16,amps,mutate=b16[0]);control=dress(b26,amps);hostile_count=sum(sp.cancel(hostile.get(w,0)-control.get(w,0))!=0 for w in set(hostile)|set(control))
 checks={"all_20_worldsheet_derived_color_dressings_basis_independent":all(r["ddm_basis_independent"] for r in rows),"all_components_retain_nonzero_color_words":all(r["nonzero_color_word_count"]>0 for r in rows),"hostile_color_sign_flip_detected":hostile_count>0}
 out={"schema":"marici.nima.six_point_chy_full_color_dressing.result.v1","status":"passed" if all(checks.values()) else "failed","checks":checks,"components":rows,"hostile_residual_word_count":hostile_count,"claim_boundary":"The exact CHY reduced-Pfaffian residues are contracted directly with free-Lie DDM half ladders for all 20 pure-gluon six-point NMHV helicity components. Endpoint-basis equality is tested in the free cyclic trace-word module at one rational fixture. This does not cover non-gluon supermultiplet states or establish novelty beyond known CHY/DDM structures."}
 RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
 if out["status"]!="passed":raise SystemExit(1)
if __name__=="__main__":main()
