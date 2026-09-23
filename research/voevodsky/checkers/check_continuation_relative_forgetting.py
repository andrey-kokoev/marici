"""Same public image, different future audit continuations on owning tail box."""
from fractions import Fraction as Q
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3];OUT=ROOT/'research/voevodsky/results'
def obs(x):return sum(x),sum(v*Q(1,128**j) for j,v in enumerate(x))
def history(t,route):
 # Parallel line segments parameterized by t in [0,1]; direction is a source
 # kernel vector (-1/128,129/128,-1), scaled to avoid negative coordinates.
 return (Q(t),Q(1),Q(1)) if route==0 else (Q(t)+Q(1,129),Q(0),Q(1)+Q(128,129))
checks=0
for t in (Q(0),Q(1,4),Q(1,2),Q(3,4),Q(1)):
 a,b=history(t,0),history(t,1)
 assert obs(a)==obs(b)
 assert all(0<=v<=100+2*j for x in (a,b) for j,v in enumerate(x))
 assert a[1]==1 and b[1]==0
 for bound in (Q(1),Q(2),Q(5,2),Q(3)):
  assert (obs(a)[0]<=bound)==(obs(b)[0]<=bound);checks+=1
# Histories are explicit rational source-linear predicates, expressible in
# the full audit schema. Neither declares one chosen lift to be actual.
report={'passed':True,'source_m':3,'histories':[
 {'name':'E','constraints':['x1=1','x2=1','0<=x0<=1'],'lift':['t','1','1']},
 {'name':'F','constraints':['x1=0','x2=257/129','1/129<=x0<=130/129'],'lift':['t+1/129','0','257/129']}],
 'common_public_segment':{'U':'t+2','V':'t+1/128+1/16384','parameter':'0<=t<=1'},
 'distinguishing_continuation':{'frame':'x1<=0','E':'INCONSISTENT','F':'unchanged, nonempty'},
 'public_refinement_checks':checks,
 'theorem':'Equal public images remain equal after any sequence of predicates depending only on the public observation; audit re-exposure or evidence on x1 can distinguish the histories.',
 'scope':'Exact affine identities prove all real parameters; samples are implementation controls. Not an actual-source or authenticated evidence claim.'}
(OUT/'continuation-relative-forgetting.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
