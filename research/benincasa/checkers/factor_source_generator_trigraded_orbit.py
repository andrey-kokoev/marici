#!/usr/bin/env python3
"""Factor the trigraded orbit census into occurrence and K-fiber marginals."""
from __future__ import annotations
import json, sys
from collections import Counter
from pathlib import Path
path=Path(sys.argv[1])
packet=json.loads(path.read_text(encoding="utf-8"))
ko=Counter(); k=Counter(); o=Counter(); fiber=Counter()
for term in packet["hilbert_terms"]:
    mult=term["multiplicity"]; kp=term["k_pole"]; od=term["occurrence_degree"]; a,b=term["fiber_degree"]
    ko[(kp,od)]+=mult; k[kp]+=mult; o[od]+=mult; fiber[(kp,a,b)]+=mult
rows=[{"k_pole":kp,"occurrence_degree":od,"multiplicity":n} for (kp,od),n in sorted(ko.items())]
# Test rank-one factorization of the K x occurrence count matrix.
ks=sorted(k); os=sorted(o)
base=ko[(ks[0],os[0])]
factorizes=all(ko[(i,j)]*base==ko[(i,os[0])]*ko[(ks[0],j)] for i in ks for j in os)
out={
 "schema":"marici.trigraded-orbit-factorization.v1",
 "source":str(path),
 "total_rank":sum(ko.values()),
 "k_marginal":{str(x):k[x] for x in ks},
 "occurrence_marginal":{str(x):o[x] for x in os},
 "k_occurrence_table":rows,
 "k_occurrence_rank_one_factorization":factorizes,
 "normalized_occurrence_coefficients":[ko[(ks[0],j)]//base for j in os],
 "normalized_k_coefficients":[ko[(i,os[0])]//base for i in ks],
 "passed":factorizes,
}
target=path.with_name(path.stem+"-factorization.json")
target.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
if not out["passed"]: raise SystemExit(1)
