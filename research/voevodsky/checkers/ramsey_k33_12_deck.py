"""Build the otherwise missing 15-vertex side types by compulsory marked deletion from the 21-catalogue. The single doubled pair on the 16-side determines the edge layer, center degree 5 and five neighbor degrees. Export every matching five-support attachment in canonical 15-coordinates. No completeness assumption about a separate order-15 catalogue."""
from ramsey_k33_22_deck import *

def build():
 H=graphs();need=set();raw=collections.Counter();
 for l in (T/'k12sides.txt').read_text().splitlines():
  i,a,b,c,ed,e=map(int,l.split());sig=tuple(sorted(8-(h&(b|c)).bit_count() for j,h in enumerate(H[i]) if a>>j&1));need.add((e,sig));raw[e]+=1
 trans=bytes((x-63).bit_count() if 63<=x<127 else 0 for x in range(256));bases={};basegraphs=[];out=collections.defaultdict(set);ct=collections.Counter();maxe=max(e for e,s in need)
 for line in gzip.open(CAT.parent/'r37_21.g6.gz','rb'):
  l=line.strip();e=sum(l[1:].translate(trans));
  if e>maxe:continue
  g=decode(l.decode());ds=list(map(int.bit_count,g))
  for r,s in enumerate(g):
   if ds[r]!=5:continue
   w=[j for j in range(21) if s>>j&1];sig=tuple(sorted(ds[j] for j in w))
   if (e,sig) not in need:continue
   vs=[j for j in range(21) if j!=r and not s>>j&1];key,p=canonical(g,vs)
   if key not in bases:
    idx=bases[key]=len(bases);a=[0]*15
    for u,v in key:a[u]|=1<<v;a[v]|=1<<u
    basegraphs.append(a)
   idx=bases[key];row=tuple(sorted(sum(1<<u for u,j in enumerate(p) if g[x]>>vs[j]&1) for x in w));out[idx,e].add(row);ct[e]+=1
 (T/'k12graphs15.txt').write_text(''.join(' '.join(map(str,a))+'\n' for a in basegraphs));(T/'k12deck5.json').write_text(json.dumps([dict(i=i,e=e,panels=sorted(v)) for (i,e),v in out.items()])+'\n');print(raw,ct,len(bases),flush=True);(P/'ramsey_k33_12_deck_counts.json').write_text(json.dumps(dict(raw=raw,degree5_marks=ct,base_types=len(bases)))+'\n')
if __name__=='__main__':build()
