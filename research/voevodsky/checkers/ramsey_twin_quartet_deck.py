"""Three blue roots with four shared red neighbors. The 16 common blue vertices H are legal (3,6). Each root and its four private red neighbors W added to H induce a catalogued 21-vertex (3,7) graph (common blue neighbors of the opposite two roots). The marked root has degree 4 in that graph, so recover every allowed attachment to H from its closed-neighborhood deletion deck. Match all three extensions on the SAME labeled H, not just the same predecessor order. Codegree <=4 forbids any common private red neighbor of two roots. Repeated-quartet branch only."""
import igraph as ig,itertools,json,gzip,collections,sys
from ramsey_retention_slice import D,CAT,decode
P=D.parent;comb=itertools.combinations

def patterns():
 out={};raw=0
 for z in json.loads((P/'ramsey_twin_quartet_pocket.json').read_text())['survive']:
  v=z['left']+z['right'];es=[(j,i) for i,m in enumerate(v,4) for j in range(4) if m>>j&1];xs=[(i+4,j+4) for i in range(4) for j in range(4,8) if not v[i]&v[j]]
  for k in range(7,min(10,len(xs))+1):
   for t in comb(xs,k):
    ee=es+list(t);g=ig.Graph(12,ee)
    if max(g.degree())>4 or g.independence_number()>4:continue
    raw+=1;key=tuple(sorted(g.permute_vertices(g.canonical_permutation(color=[0]*4+[1]*4+[2]*4)).get_edgelist()));out.setdefault(key,ee)
 return list(out.values()),raw

def join():
 pats,raw=patterns();fams=[];need=set();
 for es in pats:
  g=ig.Graph(12,es);groups=[list(range(i,i+4)) for i in (0,4,8)];typ=[(44+sum((i not in w and j not in w) for i,j in es),tuple(sorted(7-g.degree(i) for i in w))) for w in groups];need.update(typ);fams.append((es,groups,typ))
 print('pockets',raw,len(pats),'deck layers',sorted(need),flush=True);deck=collections.defaultdict(lambda:collections.defaultdict(set));ed={x for x,y in need};ct=collections.Counter();bits=bytes((x-63).bit_count() if 63<=x<127 else 0 for x in range(256))
 for line in gzip.open(CAT.parent/'r37_21.g6.gz','rb'):
  l=line.strip();e=sum(l[1:].translate(bits));
  if e not in ed:continue
  a=decode(l.decode());
  for r,s in enumerate(a):
   if s.bit_count()!=4:continue
   w=[j for j in range(21) if s>>j&1];typ=(e,tuple(sorted(a[j].bit_count()-1 for j in w)))
   if typ not in need:continue
   vs=[j for j in range(21) if j!=r and not s>>j&1];g=ig.Graph(16,[(i,j) for i,j in comb(range(16),2) if a[vs[i]]>>vs[j]&1]);perm=g.canonical_permutation();gg=g.permute_vertices(perm);key=tuple(sorted(gg.get_edgelist()));# igraph permute_vertices takes NEW vertex i from OLD perm[i]; transport old vertex to new via inverse.
   inv={x:j for j,x in enumerate(perm)};mask=lambda z:sum(1<<inv[i] for i,h in enumerate(vs) if a[z]>>h&1);ms=tuple(sorted(mask(j) for j in w));assert all(not any((v>>i&1) and (v>>j&1) for i,j in key) for v in ms);deck[typ][key].add(ms);ct[e]+=1
 print('decks',ct,flush=True);rec=[]
 for es,groups,typ in fams:
  base=set.intersection(*(set(deck[t]) for t in typ));g=ig.Graph(12,es);solutions=0;surv=[]
  for key in base:
   aut=ig.Graph(16,key).get_automorphisms_vf2();opts=[]
   for w,t in zip(groups,typ):
    sizes=tuple(7-g.degree(j) for j in w);panels=set()
    for row in deck[t][key]:
     for p in aut:
      new=tuple(sum(1<<p[i] for i in range(16) if s>>i&1) for s in row)
      panels.update(v for v in itertools.permutations(new) if tuple(x.bit_count() for x in v)==sizes)
    opts.append(sorted(panels))
   # Fix a first panel modulo automorphisms of H only (do not fix any W labels).
   order=sorted(range(3),key=lambda j:len(opts[j]));a,b,c=order;used=set();cross=lambda i,j,x,y:all(not x[g1]&y[g2] for g1,s in enumerate(groups[i]) for g2,t in enumerate(groups[j]) if g.are_adjacent(s,t));found=False
   for A in opts[a]:
    if A in used:continue
    used.update(tuple(sum(1<<p[i] for i in range(16) if s>>i&1) for s in A) for p in aut);bs=[B for B in opts[b] if cross(a,b,A,B)];
    if not bs:continue
    for C in opts[c]:
     if cross(a,c,A,C) and any(cross(b,c,B,C) for B in bs):found=True;break
    if found:break
   if found:surv.append(key)
  rec.append(dict(es=es,typ=typ,base=len(base),simultaneous=len(surv)));print(rec[-1]['base'],len(surv),flush=True)
 (P/'ramsey_twin_quartet_deck.json').write_text(json.dumps(dict(raw=raw,deck_counts=ct,pockets=rec))+'\n')
if __name__=='__main__':join()
