"""Reciprocal index: each marked side gives two catalogue requests to the opposite base. Require both and also the reverse requests. Reduce placements by base automorphisms and interchange of outer roots before gluing. Index is conservative unless marked embeddings agree on Z."""
from ramsey_k33_22_deck import *
from functools import lru_cache
@lru_cache(None)
def autos(i):return ig.Graph(16,[(u,v) for u,v in comb(range(16),2) if H[i][u]>>v&1]).get_automorphisms_vf2()
def morph(m,p):return sum(1<<p[v] for v in range(16) if m>>v&1)
H=graphs()
def build():
 deck=json.loads((T/'k22deck.json').read_text());rev=collections.defaultdict(set);edges=[sum(map(int.bit_count,g))//2 for g in H]
 for d in deck:
  j=d['i'];e=d['e'];
  for p in d['panels']:rev[edges[j],e,tuple(sorted(1+s.bit_count() for s in p))].add(j)
 idx=collections.defaultdict(list);done=set();n=0;w=0;old=None
 for l in (T/'k22sides.txt').open():
  i,a,b,c,opp,e1,e2=map(int,l.split());v=(a,min(b,c),max(b,c));
  if i!=old:done=set();old=i
  if v in done:continue
  done.add(v);h=H[i];sg=lambda y,z:tuple(sorted(8-(s&(a|y)).bit_count() for k,s in enumerate(h) if z&~(a|y)&1<<k));js=rev[opp,e1,sg(b,c)]&rev[opp,e2,sg(c,b)];
  if not js:continue
  for p in autos(i):u1=morph(b,p);u2=morph(c,p);done.add((morph(a,p),min(u1,u2),max(u1,u2)))
  n+=1
  for j in js:idx[i,j].append((a,b,c,e1,e2));w+=1
 rec=[(i,j,vs,idx[j,i]) for (i,j),vs in list(idx.items()) if i<=j and (j,i) in idx];print('one direction',n,w,'mutual blocks',len(rec),'pairs',sum(len(x)*len(y) for i,j,x,y in rec),flush=True);(T/'k22mutual.json').write_text(json.dumps(rec)+'\n');(P/'ramsey_k33_22_mutual_counts.json').write_text(json.dumps(dict(one_direction=n,one_direction_base_choices=w,mutual_blocks=len(rec),ordered_pairs_within_blocks=sum(len(x)*len(y) for i,j,x,y in rec)))+'\n')
if __name__=='__main__':build()
