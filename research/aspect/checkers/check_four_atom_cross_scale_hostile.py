import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"four_atom_cross_scale_hostile.json"


def polynomial(w): return w**4+4*w**3+4*w+1


def main():
    # Multiplying the symmetric transform by 4w^2 gives this reciprocal polynomial.
    coefficients=[1,4,0,4,1]
    reciprocal=coefficients==list(reversed(coefficients))
    signs={"P(-1)":polynomial(-1),"P(0)":polynomial(0)}
    off_seam_root_forced=signs=={"P(-1)":-6,"P(0)":1}
    reciprocal_partner_forced=reciprocal and off_seam_root_forced
    pairwise_reflection_balanced=True
    pairwise_balance_insufficient=pairwise_reflection_balanced and reciprocal_partner_forced
    assert pairwise_balance_insufficient
    out={"schema":"marici.aspect.four-atom-cross-scale-hostile.v1","status":"pass",
         "atoms":[-2,-1,1,2],"weights":["1/4","1","1","1/4"],
         "cleared_transform_coefficients":coefficients,"reciprocal_polynomial":reciprocal,
         "exact_sign_witness":signs,"off_seam_reciprocal_root_pair_forced":reciprocal_partner_forced,
         "pairwise_reciprocal_balance_is_sufficient":False,
         "required_new_attribute":"relation among multiple reflected scale pairs constraining cross-scale interference",
         "rung_five_disposition":"defer until a source-derived multiscale invariant and operational constructor are supplied"}
    RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out,sort_keys=True))


if __name__=="__main__":main()
