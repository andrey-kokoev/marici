"""Check the logarithmic Gysin coefficient on the oriented blow-up of (u,v,p)=0."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_corner_blowup_log_gysin_unit.json'

def valuation_after_blowup(monomial):
    # u=rU, v=rV, p=rP: exceptional valuation is total center order.
    return sum(monomial)

def main():
    vals={'u':valuation_after_blowup((1,0,0)),'v':valuation_after_blowup((0,1,0)),'p':valuation_after_blowup((0,0,1))}
    assert vals=={'u':1,'v':1,'p':1}
    residue_dlog_p=vals['p']
    exceptional_face_coefficient=1
    column=[residue_dlog_p,exceptional_face_coefficient]
    D=[[1,-1],[-1,1],[1,-1]]
    residual=[sum(row[j]*column[j] for j in range(2)) for row in D]
    assert column==[1,1] and residual==[0,0,0]
    reversed_column=[-x for x in column]
    assert [sum(row[j]*reversed_column[j] for j in range(2)) for row in D]==[0,0,0]
    out={'schema':'marici.voevodsky.cosmology-corner-blowup-log-gysin-unit.v1','status':'blowup_valuation_forces_unit_log_gysin_column_conditionally_on_Xi_normalization','local_blowup':'u=rU, v=rV, p=rP for Bl_(u,v,p)(A3)','exceptional_valuations':vals,'logarithmic_residue':'Res_E(dlog p)=ord_E(p)=1','exceptional_face_coefficient':1,'column_rows_Xi_minusSigma':column,'residue_boundary':residual,'orientation_reversed_column':reversed_column,'decision':'The oriented corner blow-up supplies the previously missing unit Xi_log comparison: p is a primitive center coordinate, so its exceptional valuation is one. Coupled to the oriented exceptional face, the forced chain column is (1,1).','source_gate':'Promotion is valid only if Xi_log is the source-normalized logarithmic divisor class dlog(p); this normalization must be verified against the rank-26/relative carrier chain map.','limitations':['local blow-up/Gysin calculation, not yet a full total-complex chain map','does not prove compatibility with the rank-26 absorption quotient','does not construct a relative Bockstein or physical period'],'passed':True}
    OUT.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
