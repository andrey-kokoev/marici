"""Audit four-and-higher marked-hyperplane concurrences in the C4 source terms."""
import itertools,json
from collections import Counter
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
SOURCE=ROOT/"research/benincasa/results/four-site-qg-seven-mark-weight-page.json"
OUT=ROOT/"research/benincasa/results/four-site-qg-higher-concurrence-audit.json"
def rank(rows):
 if not rows:return 0
 a=[[Fraction(x) for x in row] for row in rows];r=0
 for c in range(4):
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
 marks=term["distinct_marks"]; rows=[x["normal"] for x in marks]; conc=[];counts=Counter()
 for size in range(4,len(marks)+1):
  for sub in itertools.combinations(range(len(marks)),size):
   r=rank([rows[i] for i in sub])
   if r<=3:
    counts[(size,r)]+=1;conc.append({"subset":sub,"labels":[marks[i]["labels"] for i in sub],"rank":r,"intersection_dimension":3-r})
 key=(len(marks),tuple(sorted(counts.items())));profiles[key]+=1
 packets.append({"term_index":term["term_index"],"geometric_marks":len(marks),"higher_concurrences":conc,"counts":[{"subset_size":k[0],"rank":k[1],"count":v} for k,v in sorted(counts.items())]})
packet={"schema":"marici.benincasa.four_site_qg_higher_concurrence_audit.v1","profile_census":[{"geometric_marks":k[0],"counts":[{"subset_size":a[0],"rank":a[1],"count":v} for a,v in k[1]],"term_count":n} for k,n in sorted(profiles.items())],"term_packets":packets}
OUT.write_text(json.dumps(packet,indent=2)+"\n")
print(json.dumps({"profiles":packet["profile_census"]}))
