#!/usr/bin/env python3
"""Independent finite-field verification of the source-labelled barcode export."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
PATH=ROOT/"research"/"benincasa"/"results"/"interaction-net-barcode-basis-export-p32009.json"
p=json.loads(PATH.read_text(encoding="utf-8")); P=p["prime"]
def row(x):return {i:v%P for i,v in zip(x["indices"],x["values"]) if v%P}
def rank(rows):
    piv={}
    for src in rows:
        v=dict(src)
        for q,b in sorted(piv.items()):
            a=v.get(q,0)
            if a:
                for k,x in b.items():
                    y=(v.get(k,0)-a*x)%P
                    if y:v[k]=y
                    else:v.pop(k,None)
        if v:
            q=min(v); inv=pow(v[q],-1,P); piv[q]={k:x*inv%P for k,x in v.items()}
    return len(piv)
def dot(a,b):return sum(x*b.get(k,0) for k,x in a.items())%P
a=p["adapted_depth3_quotient_basis"]
primal3=[row(x) for name in ("first_death_rows","second_death_rows","through_depth6_rows") for x in a[name]]
dual3=[row(x) for x in p["dual_pairing_matrices"]["depth3_adapted_duals"]]
em=[row(x) for x in p["depth4_emergence_complement_rows"]]
dem=[row(x) for x in p["dual_pairing_matrices"]["depth4_emergence_duals"]]
tr={k:[row(x) for x in v["rows"]] for k,v in p["transition_matrices"].items()}
ct={k:[row(x) for x in v["rows"]] for k,v in p["chart_transports"].items()}
checks={
 "label_counts":len(p["source_label_order_depth3"])==4800 and len(p["source_label_order_depth4"])==9120,
 "sparse_rows_well_formed":all(x["indices"]==sorted(set(x["indices"])) and len(x["indices"])==len(x["values"]) and all(v%P for v in x["values"])
   for block in [a["first_death_rows"],a["second_death_rows"],a["through_depth6_rows"],p["depth4_emergence_complement_rows"],
                 p["dual_pairing_matrices"]["depth3_adapted_duals"],p["dual_pairing_matrices"]["depth4_emergence_duals"]]
   for x in block),
 "adapted_rank":rank(primal3)==53,
 "block_counts":[len(a["first_death_rows"]),len(a["second_death_rows"]),len(a["through_depth6_rows"])]==[20,6,27],
 "transition_ranks":{k:rank(v) for k,v in tr.items()}=={"depth3_to4":33,"depth3_to5":27,"depth3_to6":27},
 "first_death_zero_t4":all(not r for r in tr["depth3_to4"][:20]),
 "second_death_pattern":rank(tr["depth3_to4"][20:26])==6 and all(not r for r in tr["depth3_to5"][20:26]),
 "survivor_pattern":rank(tr["depth3_to6"][26:])==27,
 "emergence_count_rank":len(em)==1353 and rank(em)==1353,
 "dual3_identity":all(dot(primal3[i],dual3[j])==(1 if i==j else 0) for i in range(53) for j in range(53)),
 "dual4_identity":all(dot(em[i],dem[j])==(1 if i==j else 0) for i in range(1353) for j in range(1353)),
 "chart_ranks":{k:rank(v) for k,v in ct.items()}=={"G12_to_G31_depth3":53,"G12_to_G31_depth4":1386},
 "chart_depth3_flags":rank(ct["G12_to_G31_depth3"][:20])==20 and rank(ct["G12_to_G31_depth3"][:26])==26 and rank(ct["G12_to_G31_depth3"][26:])==27,
 "chart_depth4_flags":rank(ct["G12_to_G31_depth4"][:33])==33 and rank(ct["G12_to_G31_depth4"][33:])==1353,
}
out={"schema":"marici.interaction-net-barcode-basis-verification.v1","passed":all(checks.values()),"checks":checks}
print(json.dumps(out,indent=2))
if not out["passed"]:raise SystemExit(1)
