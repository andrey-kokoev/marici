"""The all-four-label exterior cell z and root see no other exterior core cells; each sees a blue four in P. Their common blue core H contains the other 16 exterior cells and R=P minus the two fours. H is legal (3,7). Enumerate oriented marked pocket pairs and exact lower-catalogue candidate graphs; no isomorphisms of completions assumed. Dedup embeddings by their 5-set for counts; full cross-edge assignment not claimed."""
from ramsey_cube_face_pocket import P,a,Q,rep,orbit,aut,CAT,decode
import json,gzip,itertools,collections,math
F=(1<<13)-1;catalog21=CAT.parent/'r37_21.g6.gz';layers=collections.defaultdict(list);hist=collections.Counter();w=bytes((i-63).bit_count() if 63<=i<127 else 0 for i in range(256))
for n,ls in [(21,gzip.open(catalog21,'rb')),(22,(CAT/'r37_22.g6').read_bytes().splitlines())]:
 for ix,l in enumerate(ls):
  s=l.strip();e=sum(s[1:].translate(w));hist[n,e]+=1
  if e<=54:layers[n,e].append((ix,s.decode()))
shapes={};rows=[]
for q in rep:
 st=[p for p in aut if sum(1<<p[i] for i in range(13) if q>>i&1)==q];seen=set()
 for t in Q:
  if t in seen:continue
  equiv={sum(1<<p[i] for i in range(13) if t>>i&1) for p in st};seen|=equiv;k=(t&q).bit_count();
  if k>1:continue
  r=[i for i in range(13) if not (t|q)>>i&1];d=[sum(a[i]>>j&1 for j in r) for i in r];n=16+len(r);e=30+4*len(r)+sum(d)//2;assert n==21 or e<60;z=dict(q=q,t=t,orbit_marked=len(equiv),overlap=k,n=n,e=e,degree_R=d,catalogue=hist[n,e]);rows.append(z)
  if not hist[n,e]:continue
  # Five-vertex residuals in this catalogue all forests with maximum degree <=2; confirm whether degrees distinguish isomorphism types before using this shortcut.
  ds=tuple(sorted(d)) # canonical adjacency key below
  typ=min(sum((a[i]>>j&1)<<(u*(u-1)//2+v) for u,i in enumerate(rr) for v,j in enumerate(rr[:u])) for rr in itertools.permutations(r));z['type']=typ
  shapes[typ]=dict(e=e,degree=ds)
print('layers',[(k,n) for k,n in sorted(hist.items()) if k[0]==21 and k[1]<=54],flush=True)
# enumerate subsets in H by required full degrees. Directly check that every vertex has exactly four neighbors outside R. For five vertices, classify the surviving induced subgraphs exactly.
canon={}
for typ,sh in shapes.items():
 ds=sh['degree'];dem=collections.Counter(ds);matches=[];total=0
 for ix,src in layers[21,sh['e']]:
  g=decode(src);sets=[list(itertools.combinations([i for i,v in enumerate(g) if v.bit_count()==d+4],k)) for d,k in dem.items()];ct=0
  for parts in itertools.product(*sets):
   r=sum(1<<i for pp in parts for i in pp);vs=sum((list(p) for p in parts),[])
   if any((g[i]&~r).bit_count()!=4 for i in vs):continue
   # Only possible degree collision here: P3 + K2 vs 4-cycle or triangle patterns. Triangle-free, use explicit canonicalization cached by small mask.
   bits=sum(((g[i]>>j)&1)<<(u*(u-1)//2+v) for u,i in enumerate(vs) for v,j in enumerate(vs[:u]));
   if bits not in canon:
    canon[bits]=min(sum(((bits>>(max(i,j)*(max(i,j)-1)//2+min(i,j)))&1)<<(u*(u-1)//2+v) for u,i in enumerate(rr) for v,j in enumerate(rr[:u])) for rr in itertools.permutations(range(5)))
   if canon[bits]==typ:ct+=1
  if ct:matches.append((ix,ct));total+=ct
 sh.update(parents=len(matches),subsets=total,matches=matches);print(typ,sh['e'],len(matches),total,flush=True)
(P/'ramsey_face_double_root.json').write_text(json.dumps(dict(marked=rows,shapes=shapes,edge_hist={str(k):v for k,v in hist.items()}))+'\n')
