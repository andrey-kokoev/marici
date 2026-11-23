"""Edge-surgery and obstruction attribution for a fixed pair of actual outputs."""
from ramsey38_direction_readout import forks,C,J,E,S,W,D,json
from itertools import combinations
from collections import Counter
from functools import lru_cache
from ramsey38_matching_continuations import data,ls
H=data[0][0];m=130;zone={e for c in (C,J) for f in forks(c) for e in f};mask=sum(1<<e for e in zone);lo,hi=W[5],W[6];v=lo^hi;pair=lambda e:tuple(8+j for j in E[e]);changed=[pair(e) for e in zone if v>>e&1];inpairs=lambda s,a,b:s>>a&1 and s>>b&1
@lru_cache(None)
def run(w):
 h=data[5][0][:]
 for e in range(len(E)):
  if (w^lo)>>e&1:a,b=pair(e);h[a]^=1<<b;h[b]^=1<<a
 I=[0]
 for i,g in enumerate(h):
  if not m>>i&1:I.extend([s|1<<i for s in I if not s&g]);
 T=[s for s in I if s.bit_count()==7];valid=max(map(int.bit_count,I))<=7 and not any(h[a]&h[b]&~m for a,b in combinations(range(27),2) if not ((1<<a|1<<b)&m) and h[a]>>b&1);F={s for s in I if s.bit_count()<=5 and all(not H[i]&s for i in ls(s)) and all(s&t for t in T)};M=[s for s in F if not any(s!=q and s&q==q for q in F)];return h,T,F,dict(valid_core=valid,fives=sum(s.bit_count()==5 for s in F),fours=[ls(s) for s in sorted(F) if s.bit_count()==4],minimal_fives=[ls(s) for s in sorted(M) if s.bit_count()==5])
o=dict(changed_fork_edges=sorted(changed),total_changed=(hi^lo).bit_count(),cases={k:run(w)[3] for k,w in dict(low=lo,high=hi,low_with_high_forks=lo^(v&mask),high_with_low_forks=hi^(v&mask)).items()});ws=[]
for s in sorted(run(hi)[2]-run(lo)[2]):
 if s.bit_count()!=5:continue
 h,t,_,_=run(lo);clashes=[(a,b) for a,b in combinations(ls(s),2) if h[a]>>b&1];miss=[q for q in t if not q&s];killed=lambda q:any(inpairs(q,a,b) for a,b in changed if run(hi)[0][a]>>b&1);ws.append(dict(support=ls(s),low_conflicts=clashes,missed=len(miss),missed_destroyed_by_high_fork_edges=sum(map(killed,miss)),survives_without_high_forks=s in run(hi^(v&mask))[2],works_on_low_with_high_forks=s in run(lo^(v&mask))[2]))
o['witnesses']=ws
# A common missed seven and the actual added red edges that break it.
ss=[sum(1<<i for i in U) for U in ([0,9,10,12,17],[0,10,12,17,24])];q=min(q for q in run(lo)[1] if all(not q&s for s in ss));o['shared_missed_seven']=ls(q);o['high_red_edges_inside']=list((a,b) for a,b in combinations(ls(q),2) if run(hi)[0][a]>>b&1);print(o);(D/'ramsey38_fork_intervention.json').write_text(json.dumps(o,indent=2)+'\n')
