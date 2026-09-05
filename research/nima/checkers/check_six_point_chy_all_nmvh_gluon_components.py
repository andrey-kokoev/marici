from __future__ import annotations
import itertools,json
from pathlib import Path
import sympy as sp
import check_six_point_nmhv_ordering_relations as rel
from check_six_point_chy_yang_mills_pfaffian import setup,chy

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/nima/results/six-point-chy-all-nmhv-gluon-components.json"

def main():
 I,Z,inv,PT,detprime=setup();rows=[];old=rel.TARGET
 try:
  for negative in itertools.combinations(range(1,7),3):
   rel.TARGET=negative
   worldsheet=chy(negative,I,Z,inv,PT,detprime)
   twistor=rel.amplitude(rel.LABELS)
   residual=sp.cancel(worldsheet-twistor)
   rows.append({"negative_helicity_legs":list(negative),"worldsheet":str(worldsheet),"momentum_twistor":str(twistor),"residual":str(residual),"matches":residual==0})
 finally: rel.TARGET=old
 checks={"all_20_nmvh_gluon_components_match":all(r["matches"] for r in rows),"all_worldsheet_components_nonzero":all(r["worldsheet"]!="0" for r in rows),"exactly_20_components":len(rows)==20}
 out={"schema":"marici.nima.six_point_chy_all_nmhv_gluon_components.result.v1","status":"passed" if all(checks.values()) else "failed","checks":checks,"components":rows,"claim_boundary":"Exact CHY reduced-Pfaffian global residues match the momentum-twistor construction for all 20 pure-gluon six-point NMHV helicity assignments at one rational fixture. This does not cover non-gluon supermultiplet components or additional kinematic fixtures."}
 RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
 if out["status"]!="passed":raise SystemExit(1)
if __name__=="__main__":main()
