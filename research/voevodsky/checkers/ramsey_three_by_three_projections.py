"""Assume a red K3,3. Outside it a vertex sees at most one side and at most two roots there. Each pair on either side has at most one private double (codegree <=4). Let a,b count double cells on the two sides; neutral cells Z number a+b-1. Side X plus Z induces a legal (3,6) type on 14+b vertices, supporting three blue 5-sets S_i. If S_i,S_j intersect, common blue to roots i,j induces a legal 21-type with 44+k edges where k counts edges between S_i and S_j excluding the intersection. The third root's degree and its neighbor degrees inside that type are determined by the data on this side. Enumerate marked (3,6) projections and test these catalogue signatures (unseen high edge layers conservatively admitted when capped). Keep all types modulo actual automorphisms; do not equate separate extensions with compatibility."""
from ramsey_retention_slice import CAT,D,decode
import itertools,json,gzip,collections,sys,igraph as ig
P=D.parent;comb=itertools.combinations

def marks(maxe=57):
 path=P/f'ramsey_21_marks_through_{maxe}.json'
 if path.exists():return {tuple(r) for r in json.loads(path.read_text())}
 tab=set();trans=bytes((x-63).bit_count() if 63<=x<127 else 0 for x in range(256))
 for line in gzip.open(CAT.parent/'r37_21.g6.gz','rb'):
  l=line.strip();e=sum(l[1:].translate(trans));
  if e>maxe:continue
  g=decode(l.decode());d=[s.bit_count() for s in g]
  for i,v in enumerate(g):
   if d[i] not in (3,4,5):continue
   tab.add((e,*sorted(d[j] for j in range(21) if v>>j&1)))
 path.write_text(json.dumps(sorted(tab))+'\n');return tab

def side(arg):
 ix,h,cap=arg;S=[0];n=len(h);mask=(1<<n)-1;tab=marks(cap)
 for j,v in enumerate(h):S.extend([s|1<<j for s in S if not s&v]);
 S=[s for s in S if s.bit_count()==5];G=ig.Graph(n,[(j,k) for j,k in comb(range(n),2) if h[j]>>k&1]);ps=G.get_automorphisms_vf2();maps=[{s:sum(1<<p[i] for i in range(n) if s>>i&1) for s in S} for p in ps];opts={s:[] for s in S};cross={}
 for s,t in comb(S,2):
  u=s&t
  if u.bit_count()>1:continue
  k=sum((h[i]&t).bit_count() for i in range(n) if s>>i&1);assert k>=5-u.bit_count()
  if u and k<7:continue
  opts[s].append(t);cross[s,t]=cross[t,s]=k
 raw=collections.Counter();wins=collections.Counter();orbits=[];seen=set()
 for s in S:
  for ti,t in enumerate(opts[s]):
   for u in opts[s][ti+1:]:
    if (t,u) not in cross or s&t&u:continue
    w=(s,t,u);a=sum(bool(x&y) for x,y in comb(w,2));raw[a]+=1
    for i in range(3):
     x,y,z=w[i],w[(i+1)%3],w[(i+2)%3]
     if y&z:
      e=44+cross[y,z];sig=(e,*sorted(8-(h[j]&(y|z)).bit_count() for j in range(n) if (x&~(y|z))>>j&1))
      if e<=cap and sig not in tab:break
    else:
     wins[a]+=1
     if a==3 and n==17:
      q=tuple(sorted(w));
      if q not in seen:seen.update(tuple(sorted(p[x] for x in w)) for p in maps);orbits.append(q)
 return dict(ix=ix,raw=raw,wins=wins,ss=orbits)
if __name__=='__main__':
 from concurrent.futures import ProcessPoolExecutor
 n=int(sys.argv[1]);cap=int(sys.argv[2]);marks(cap);H=list(map(decode,(CAT/'r36_17.g6').read_text().splitlines())) if n==17 else [decode(l.strip()) for l in gzip.open(CAT.parent/'r36_16.g6.gz','rt')];
 with ProcessPoolExecutor(8) as ex:rs=list(ex.map(side,[(i,h,cap) for i,h in enumerate(H)],chunksize=4));
 print(n,{a:sum(z['wins'].get(a,0) for z in rs) for a in range(4)},sum(len(z['ss']) for z in rs));(P/f'ramsey_three_by_three_proj_{n}.json').write_text(json.dumps(rs)+'\n')
