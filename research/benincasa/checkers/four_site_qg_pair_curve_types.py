"""Classify pair-intersection curves in the source seven-mark C4 packets."""
import itertools
import json
import math
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
MARKS=ROOT/"research/benincasa/results/four-site-qg-mark-section-types.json"
INC=ROOT/"research/benincasa/results/four-site-qg-node-marked-incidence.json"
OUT=ROOT/"research/benincasa/results/four-site-qg-pair-curve-types.json"

def facets(n=4):
 out={}
 for length in range(1,n):
  for start in range(n):
   sites={(start+k)%n for k in range(length)};v=[0]*n
   for e in range(n):
    if ((e in sites)!=(((e+1)%n) in sites)):v[e]=1
   out["g_"+"".join(str(i+1) for i in sorted(sites))]=v
 for e in range(n):
  v=[0]*n;v[e]=2;out[f"G_minus_e{e+1}{(e+1)%n+1}"]=v
 return out
def norm(v):
 g=0
 for x in v:g=math.gcd(g,abs(x))
 v=tuple(x//g for x in v);f=next(x for x in v if x)
 return tuple(-x for x in v) if f<0 else v

marks=json.loads(MARKS.read_text());inc=json.loads(INC.read_text());forms=facets();packets=[];profiles=Counter()
for mt,it in zip(marks["term_packets"],inc["records"]):
 assert mt["term_index"]==it["term_index"]
 groups={}
 for label in mt["labels"]:groups.setdefault(norm(forms[label]),[]).append(label)
 distinct=[]
 for n,labels in sorted(groups.items()):
  hit={tuple(row["point"]) for row in it["nodes"] if any(label in row["vanishing_labels"] for label in labels)}
  types={mt["types"][label] for label in labels};assert len(types)==1
  distinct.append({"normal":n,"labels":sorted(labels),"type":next(iter(types)),"hit_nodes":sorted(hit)})
 pair_rows=[];counter=Counter()
 for i,j in itertools.combinations(range(len(distinct)),2):
  a,b=distinct[i],distinct[j];shared=sorted(set(map(tuple,a["hit_nodes"]))&set(map(tuple,b["hit_nodes"])))
  if len(shared)==0: curve="smooth elliptic double cover"
  elif len(shared)==2: curve="split rational deck pair from two double branch roots"
  else: raise AssertionError((len(shared),a,b))
  counter[curve]+=1
  pair_rows.append({"marks":[a["labels"],b["labels"]],"shared_node_count":len(shared),"shared_nodes":shared,"curve_type":curve})
 key=(len(distinct),counter["smooth elliptic double cover"],counter["split rational deck pair from two double branch roots"])
 profiles[key]+=1
 packets.append({"term_index":mt["term_index"],"geometric_mark_count":len(distinct),"pair_type_counts":dict(counter),"pairs":pair_rows})

packet={"schema":"marici.benincasa.four_site_qg_pair_curve_types.v1","profile_census":[{"geometric_marks":k[0],"elliptic_pairs":k[1],"split_rational_pairs":k[2],"term_count":v} for k,v in sorted(profiles.items())],"split_normal_form":"quartic on P1 with two double roots equals unit*(l1*l2)^2; its double cover is a Kummer-twisted pair of rational components","term_packets":packets}
OUT.write_text(json.dumps(packet,indent=2)+"\n")
print(json.dumps({"profiles":packet["profile_census"]}))
