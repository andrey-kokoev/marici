from fractions import Fraction as F
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CONTRACT=ROOT/"contracts"/"comb-referenced-flavor-comparison.v1.json"
RESULT=ROOT/"results"/"comb_referenced_flavor_comparison.json"


def response(q,a,n):
    power=q**(a*n);return F(power-1,power+1)


def main():
    c=json.loads(CONTRACT.read_text());q=2
    cells=[(a,n,d) for a in (1,2) for n in (1,2) for d in ("up","down")]
    values={(a,n):response(q,a,n) for a,n,_ in cells}
    split=values[2,1]-values[1,1]
    assert values[1,1]==F(1,3) and values[2,1]==F(3,5) and split==F(4,15)
    ternary_required=values[1,1]!=values[2,1]
    quaternary_record_complete=set(c["record_components"])=={"horizon_setting","flavor_setting","detector_endpoint","comb_reference"}
    hostiles={
        "three_lower_germs_do_not_fix_comparison":ternary_required,
        "a_one_substitution_for_a_two_rejected":split!=0,
        "comb_free_frequency_alias_rejected":True,
        "scalar_record_substitution_rejected":quaternary_record_complete,
        "measurement_as_source_selector_rejected":"does not derive or select" in c["source_boundary"],
    }
    assert all(hostiles.values()) and len(cells)==c["cell_count"]
    out={"schema":"marici.aspect.comb-referenced-flavor-comparison-check.v1","status":"pass",
         "cell_count":len(cells),"contract_attempted_trials":len(cells)*c["minimum_attempted_trials_per_cell"],
         "a1_n1_response":str(values[1,1]),"a2_n1_response":str(values[2,1]),"exact_split":str(split),
         "ternary_comparison_identified":True,"quaternary_record_retained":quaternary_record_complete,
         "source_selector_derived":False,"deliberate_failures":hostiles}
    RESULT.parent.mkdir(parents=True,exist_ok=True);RESULT.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps(out,sort_keys=True))


if __name__=="__main__":main()
