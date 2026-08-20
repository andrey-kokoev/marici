"""Generic logarithmic E1 weight-page budgets for all 28 seven-mark C4 terms."""
import itertools
import json
import math
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/four-site-qg-mark-section-types.json"
OUT = ROOT / "research/benincasa/results/four-site-qg-seven-mark-weight-page.json"


def facets(n=4):
    out={}
    for length in range(1,n):
        for start in range(n):
            sites={(start+k)%n for k in range(length)}; edge=[0]*n
            for e in range(n):
                if ((e in sites)!=(((e+1)%n) in sites)): edge[e]=1
            out["g_"+"".join(str(i+1) for i in sorted(sites))]=edge
    for e in range(n):
        edge=[0]*n;edge[e]=2;out[f"G_minus_e{e+1}{(e+1)%n+1}"]=edge
    return out


def normal(v):
    g=0
    for x in v:g=math.gcd(g,abs(x))
    v=tuple(x//g for x in v)
    first=next(x for x in v if x)
    return tuple(-x for x in v) if first<0 else v


source=json.loads(SOURCE.read_text()); forms=facets(); packets=[]; census=Counter()
for term in source["term_packets"]:
    groups={}
    for label in term["labels"]:
        groups.setdefault(normal(forms[label]),[]).append(label)
    distinct=[]
    for n,labels in sorted(groups.items()):
        types={term["types"][label] for label in labels}
        assert len(types)==1
        distinct.append({"normal":n,"labels":sorted(labels),"type":next(iter(types))})
    smooth=sum(x["type"]=="smooth-benchmark candidate" for x in distinct)
    nodal=len(distinct)-smooth; m=len(distinct)
    weight3=20
    weight4=7*smooth+3*nodal
    elliptic_pairs=math.comb(m,2)
    weight5=2*elliptic_pairs
    triple_base_points=math.comb(m,3)
    weight6=2*triple_base_points
    key=(m,smooth,nodal,weight4,weight5,weight6)
    census[key]+=1
    packets.append({"term_index":term["term_index"],"distinct_marks":distinct,"occurrence_mark_count":7,"geometric_mark_count":m,"smooth_mark_count":smooth,"four_node_mark_count":nodal,"generic_E1_weight_ranks":{"W3_middle":weight3,"W4_surface_primitive":weight4,"W5_pair_elliptic":weight5,"W6_triple_deck_tate":weight6},"generic_pair_count":elliptic_pairs,"generic_triple_base_count":triple_base_points})

packet={
 "schema":"marici.benincasa.four_site_qg_seven_mark_weight_page.v1",
 "term_count":len(packets),
 "profile_census":[{"geometric_marks":k[0],"smooth_marks":k[1],"four_node_marks":k[2],"W4":k[3],"W5":k[4],"W6":k[5],"term_count":v} for k,v in sorted(census.items())],
 "typing":{"W3":"quartic-double-solid H3, rank20","W4":"primitive E7/A1^3 surface Gysin kernels","W5":"rank-two elliptic H1 per distinct pair","W6":"two deck points per generic distinct triple"},
 "warning":"These are generic E1/associated-graded budgets, not final complement cohomology; incidence differentials and branch collisions remain to be computed.",
 "term_packets":packets,
}
OUT.write_text(json.dumps(packet,indent=2)+"\n")
print(json.dumps({"profiles":packet["profile_census"]}))
