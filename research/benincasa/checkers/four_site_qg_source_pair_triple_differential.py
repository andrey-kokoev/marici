"""Component-resolved pair-to-triple differential for actual C4 source marks."""
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
SOURCE=ROOT/"research/benincasa/results/four-site-qg-pair-curve-types.json"
OUT=ROOT/"research/benincasa/results/four-site-qg-source-pair-triple-differential.json"

def rank(m):
 if not m or not m[0]:return 0
 a=[[Fraction(x) for x in row] for row in m];r=0
 for c in range(len(a[0])):
  p=next((i for i in range(r,len(a)) if a[i][c]),None)
  if p is None:continue
  a[r],a[p]=a[p],a[r];q=a[r][c];a[r]=[x/q for x in a[r]]
  for i in range(len(a)):
   if i!=r and a[i][c]:
    q=a[i][c];a[i]=[x-q*y for x,y in zip(a[i],a[r])]
  r+=1
 return r

source=json.loads(SOURCE.read_text());packets=[];profiles=Counter()
for term in source["term_packets"]:
 # Recover geometric marks as equivalence classes of label lists appearing in pairs.
 mark_keys=sorted({tuple(side) for pair in term["pairs"] for side in pair["marks"]})
 mi={k:i for i,k in enumerate(mark_keys)}
 pair_info={}
 for p in term["pairs"]:
  i,j=sorted((mi[tuple(p["marks"][0])],mi[tuple(p["marks"][1])]))
  pair_info[(i,j)]={"type":p["curve_type"],"hit_nodes":set(map(tuple,p["shared_nodes"]))}
 # Node-hit set of a mark is recovered as union of its pairwise shared-node sets.
 mark_hits=[set() for _ in mark_keys]
 for (i,j),p in pair_info.items():
  mark_hits[i]|=p["hit_nodes"];mark_hits[j]|=p["hit_nodes"]
 # Smooth mark has no hits. Nodal marks have four, but pair unions may recover all.
 pairs=sorted(pair_info)
 columns=[]
 for pair in pairs:
  typ=pair_info[pair]["type"]
  if typ.startswith("split"): columns.extend([(pair,"+"),(pair,"-")])
  else: columns.append((pair,"diag"))
 cpos={c:i for i,c in enumerate(columns)}
 triples=list(itertools.combinations(range(len(mark_keys)),3));rows=[];triple_meta=[]
 for t in triples:
  common=set.intersection(*(mark_hits[i] for i in t)) if all(mark_hits[i] for i in t) else set()
  assert len(common)<=1
  sheets=["ram"] if common else ["+","-"]
  for s in sheets:rows.append((t,s))
  triple_meta.append({"triple":t,"shared_node_count":len(common),"target_sheets":sheets})
 rpos={r:i for i,r in enumerate(rows)}
 matrix=[[0]*len(columns) for _ in rows]
 for tmeta in triple_meta:
  t=tuple(tmeta["triple"]); faces=[(t[1],t[2]),(t[0],t[2]),(t[0],t[1])]; signs=[1,-1,1]
  for face,sgn in zip(faces,signs):
   typ=pair_info[face]["type"]
   if tmeta["target_sheets"]==["ram"]:
    if typ.startswith("split"):
     for s in ("+","-"):matrix[rpos[(t,"ram")]][cpos[(face,s)]]=sgn
    else: matrix[rpos[(t,"ram")]][cpos[(face,"diag")]]=sgn
   else:
    if typ.startswith("split"):
     for s in ("+","-"):matrix[rpos[(t,s)]][cpos[(face,s)]]=sgn
    else:
     for s in ("+","-"):matrix[rpos[(t,s)]][cpos[(face,"diag")]]=sgn
 rr=rank(matrix);coker=len(rows)-rr
 branch=sum(x["shared_node_count"] for x in triple_meta);off=len(triples)-branch
 profiles[(len(mark_keys),branch,off,len(columns),len(rows),rr,coker)]+=1
 packets.append({"term_index":term["term_index"],"geometric_marks":len(mark_keys),"pair_H0_columns":len(columns),"triple_target_rows":len(rows),"branch_node_triples":branch,"off_branch_triples":off,"differential_rank":rr,"cokernel_rank":coker,"triple_meta":triple_meta})

packet={"schema":"marici.benincasa.four_site_qg_source_pair_triple_differential.v1","profile_census":[{"geometric_marks":k[0],"branch_node_triples":k[1],"off_branch_triples":k[2],"pair_H0_columns":k[3],"triple_rows":k[4],"rank":k[5],"W6_cokernel":k[6],"term_count":v} for k,v in sorted(profiles.items())],"map_convention":"split pair components map sheetwise off branch and both map to the ramification point on branch; connected elliptic H0 maps diagonally","term_packets":packets}
OUT.write_text(json.dumps(packet,indent=2)+"\n")
print(json.dumps({"profiles":packet["profile_census"]}))
