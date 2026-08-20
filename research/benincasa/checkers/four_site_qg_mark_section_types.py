"""Classify source marked hyperplane sections of the C4 quartic double solid."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/four-site-qg-node-marked-incidence.json"
OUT = ROOT / "research/benincasa/results/four-site-qg-mark-section-types.json"

source=json.loads(SOURCE.read_text())
term_packets=[]; profile=Counter(); label_types={}
for term in source["records"]:
    labels=sorted({label for row in term["nodes"] for label in row["vanishing_labels"]} | {f"g_{i}" for i in range(1,5)} | set(term["additional_labels"]))
    # Count sign nodes met by each label from the occurrence records.
    hits={label:sum(label in row["vanishing_labels"] for row in term["nodes"]) for label in labels}
    # Every retained source mark is either a two-edge boundary sum (4 hits)
    # or a spanning-path single-edge normal (0 hits).
    assert set(hits.values()) <= {0,4}
    types={label:("smooth-benchmark candidate" if n==0 else "four-node two-conic section") for label,n in hits.items()}
    for label,t in types.items(): label_types[label]=t
    counts=Counter(types.values())
    profile[(counts["smooth-benchmark candidate"],counts["four-node two-conic section"])]+=1
    term_packets.append({"term_index":term["term_index"],"labels":labels,"node_hits":hits,"types":types})

# Boundary-sum representative y1+y2=0 forces Delta1=y2^2-y1^2=0.
# The remaining branch is q(A,B), A=y3^2-y1^2, B=y4^2-y3^2.  For a generic
# 2x2 symmetric restriction [[a,b],[b,c]], q=aA^2+2bAB+cB^2 factors over
# the quadratic splitting field into two distinct diagonal conics.
witness={"a":2,"b":1,"c":3}
binary_discriminant=(2*witness["b"])**2-4*witness["a"]*witness["c"]
assert binary_discriminant==-20

packet={
 "schema":"marici.benincasa.four_site_qg_mark_section_types.v1",
 "term_count":len(term_packets),
 "term_type_profiles":[{"zero_node_marks":k[0],"four_node_marks":k[1],"term_count":v} for k,v in sorted(profile.items())],
 "label_types":dict(sorted(label_types.items())),
 "boundary_sum_normal_form":{
   "mark":"y1+y2=0",
   "forced_difference":"Delta1=0",
   "remaining_variables":["A=y3^2-y1^2","B=y4^2-y3^2"],
   "branch":"a*A^2+2*b*A*B+c*B^2",
   "generic_factorization":"two distinct diagonal conics over the quadratic splitting field",
   "intersection_count":4,
   "intersection_nodes":"the four sign nodes with epsilon2=-1",
   "witness_binary_discriminant":binary_discriminant,
 },
 "single_edge_normal":"y_e=0; misses all eight sign nodes and retains the smooth-section benchmark generically",
 "term_packets":term_packets,
}
OUT.write_text(json.dumps(packet,indent=2)+"\n")
print(json.dumps({"profiles":packet["term_type_profiles"],"boundary_discriminant":binary_discriminant}))
