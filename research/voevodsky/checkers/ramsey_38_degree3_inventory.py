"""Exhaust minimum-degree-3 root presentations of order-20 edge-45 cores over the stored 16-core catalogue. Every pair of supports must cover all blue fives, and their triple must cover all fours. Count resistant isomorphism types by canonical labeling. Optional inclusive edge-count bounds for resumable strata."""
import sys,gzip,json,itertools,collections,time,igraph as ig
from ramsey_retention_slice import CAT,D,decode,check
P=D.parent;lo,hi=map(int,sys.argv[1:3]);out={};hist=collections.Counter();res_types={};all_types=set()
target=49 if '--49' in sys.argv else 48 if '--48' in sys.argv else 47 if '--47' in sys.argv else 46 if '--46' in sys.argv else 45
aug={int(h,16) for h in json.load(gzip.open(P/'ramsey_38_layer47_deletable.json.gz'))} if target==47 else set()
for line in gzip.open(CAT.parent/'r36_16.g6.gz','rt'):
 a=decode(line.strip());e=sum(v.bit_count() for v in a)//2;budget=target-3-e
 if not lo<=e<=hi or budget<6:continue
 hist['catalogue_rows']+=1;I=[0]
 for j,v in enumerate(a):I += [s|1<<j for s in I if not s&v]
 S=[s for s in I if 2<=s.bit_count()<=min(5,budget-4)];Q4=[q for q in I if q.bit_count()==4];Q5=[q for q in I if q.bit_count()==5];miss=lambda s,Q:sum(1<<j for j,q in enumerate(Q) if not s&q);m4=[miss(s,Q4) for s in S];m5=[miss(s,Q5) for s in S];G=[set() for s in S];sizes=[s.bit_count() for s in S];
 for i,si in enumerate(sizes):
  for j in range(i,len(S)):
   if si+sizes[j]<=budget-2 and not m5[i]&m5[j]:G[i].add(j)
 for i,adj in enumerate(G):
  for j in adj:
   for k in adj&G[j]:
    if sizes[i]+sizes[j]+sizes[k]!=budget or m4[i]&m4[j]&m4[k]:continue
    b=a.copy()+[0]*4
    for t,s in enumerate((S[i],S[j],S[k]),16):
     b[t]=s|1<<19;b[19]|=1<<t
     for h in range(16):
      if s>>h&1:b[h]|=1<<t
    if min(v.bit_count() for v in b)!=3:continue
    E=[(u,v) for u,v in itertools.combinations(range(20),2) if b[u]>>v&1];gr=ig.Graph(20,E);key=sum(1<<(max(u,v)*(max(u,v)-1)//2+min(u,v)) for u,v in gr.permute_vertices(gr.canonical_permutation()).get_edgelist());hist['rooted_presentations']+=1
    if key in all_types:continue
    all_types.add(key)
    if target>=48 or key in aug:continue
    assert check(b,2**20-1,3,7);I2=[0]
    for h,v in enumerate(b):I2 += [q|1<<h for q in I2 if not q&v]
    blue5=[q for q in I2 if q.bit_count()==5];
    resistant=all(any(not q&(b[u]|b[v]|1<<u|1<<v) for q in blue5) for u,v in E)
    if target==47:assert resistant
    if resistant:res_types[key]=b
if target>=48:
 with gzip.open(P/f'ramsey_38_d3_{target}_{lo}_{hi}.json.gz','wt') as f:json.dump(sorted(map(hex,all_types)),f)
 print(lo,hi,hist,len(all_types));sys.exit()
out=dict(stratum=[lo,hi],stats=hist,types=len(all_types),resistant=list(res_types.values()));print(lo,hi,hist,len(all_types),len(res_types));(P/f"ramsey_38_degree3_inventory_{lo}_{hi}{'_'+str(target) if target!=45 else ''}.json").write_text(json.dumps(out)+'\n')
