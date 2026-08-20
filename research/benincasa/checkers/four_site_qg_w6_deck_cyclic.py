"""Deck eigencokernels and cyclic assembly of the corrected C4 W6 layer."""
import itertools
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
PAIRS=ROOT/"research/benincasa/results/four-site-qg-pair-curve-types.json"
TRIPLES=ROOT/"research/benincasa/results/four-site-qg-source-pair-triple-differential.json"
OUT=ROOT/"research/benincasa/results/four-site-qg-w6-deck-cyclic.json"

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

pairs=json.loads(PAIRS.read_text());triples=json.loads(TRIPLES.read_text());packets=[];profiles=Counter()
for pp,tp in zip(pairs["term_packets"],triples["term_packets"]):
 assert pp["term_index"]==tp["term_index"]
 mark_keys=sorted({tuple(side) for p in pp["pairs"] for side in p["marks"]});mi={k:i for i,k in enumerate(mark_keys)}
 pair_type={}
 for p in pp["pairs"]:
  edge=tuple(sorted((mi[tuple(p["marks"][0])],mi[tuple(p["marks"][1])])))
  pair_type[edge]="split" if p["curve_type"].startswith("split") else "elliptic"
 edges=sorted(pair_type);triples_list=[tuple(x["triple"]) for x in tp["triple_meta"]]
 # Deck-plus: one column per pair and one row per triple, ordinary signed incidence.
 plus=[[0]*len(edges) for _ in triples_list];epos={e:i for i,e in enumerate(edges)}
 for ri,t in enumerate(triples_list):
  for face,sgn in zip([(t[1],t[2]),(t[0],t[2]),(t[0],t[1])],[1,-1,1]):plus[ri][epos[face]]=sgn
 # Deck-minus: one column per split pair and one row per off-branch triple.
 split=[e for e in edges if pair_type[e]=="split"];spos={e:i for i,e in enumerate(split)}
 off=[tuple(x["triple"]) for x in tp["triple_meta"] if x["shared_node_count"]==0]
 minus=[[0]*len(split) for _ in off]
 for ri,t in enumerate(off):
  for face,sgn in zip([(t[1],t[2]),(t[0],t[2]),(t[0],t[1])],[1,-1,1]):
   if face in spos:minus[ri][spos[face]]=sgn
 rp,rm=rank(plus),rank(minus);cp=len(plus)-rp;cm=len(minus)-rm
 assert cp+cm==tp["cokernel_rank"]
 profiles[(len(mark_keys),cp,cm)]+=1
 packets.append({"term_index":pp["term_index"],"geometric_marks":len(mark_keys),"deck_plus":{"rows":len(plus),"columns":len(edges),"rank":rp,"cokernel":cp},"deck_minus":{"rows":len(minus),"columns":len(split),"rank":rm,"cokernel":cm}})

profile_rows=[{"geometric_marks":k[0],"W6_plus":k[1],"W6_minus":k[2],"term_count":v,"cyclic_orbits":v//4} for k,v in sorted(profiles.items())]
plus_total=sum(x["W6_plus"]*x["term_count"] for x in profile_rows);minus_total=sum(x["W6_minus"]*x["term_count"] for x in profile_rows)
packet={"schema":"marici.benincasa.four_site_qg_w6_deck_cyclic.v1","profile_census":profile_rows,"global_term_sum":{"W6_plus":plus_total,"W6_minus":minus_total,"total":plus_total+minus_total},"C4_characters":{"deck_plus":[plus_total,0,0,0],"deck_minus":[minus_total,0,0,0]},"cyclic_statement":"Each profile count is a union of free C4 term orbits; each orbit assembles as Q[C4] tensor its representative deck eigencokernel.","term_packets":packets}
OUT.write_text(json.dumps(packet,indent=2)+"\n")
print(json.dumps({"profiles":profile_rows,"global":packet["global_term_sum"],"characters":packet["C4_characters"]}))
