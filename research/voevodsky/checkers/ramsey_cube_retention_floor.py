"""Exact edge-floor retention test; any root of the constructed cube endpoint, arbitrary vertex relabeling."""
from itertools import combinations
from collections import Counter,defaultdict
from ramsey_cube_construct35 import G
from ramsey_retention_slice import CAT,D,decode
import json,gzip

def induced(a,V):return [sum(1<<j for j,h in enumerate(V) if a[i]>>h&1) for i in V]
def deg(a):return tuple(sorted(x.bit_count() for x in a))
def wl(a):return tuple(sorted((s.bit_count(),tuple(sorted(a[j].bit_count() for j in range(len(a)) if s>>j&1))) for s in a))
def iso(a,b):
    # Compare row colors then all adjacencies; no hash used as a positive verdict.
    sig=lambda A:[(s.bit_count(),tuple(sorted(A[j].bit_count() for j in range(len(A)) if s>>j&1))) for s in A];aa,bb=sig(a),sig(b);cs=[[j for j,h in enumerate(bb) if h==v] for v in aa];order=sorted(range(len(a)),key=lambda i:len(cs[i]));f={}
    def dfs(k,used):
        if k==len(a):return [f[i] for i in range(len(a))]
        i=order[k]
        for j in cs[i]:
            if used>>j&1 or any((a[i]>>u&1)!=(b[j]>>v&1) for u,v in f.items()):continue
            f[i]=j;r=dfs(k+1,used|1<<j)
            if r is not None:return r
            del f[i]
    return dfs(0,0)

def audit():
    targets=defaultdict(list);shapes=set();hist=Counter();before=Counter();first=None;records=[];w=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)])
    for r,s in enumerate(G):
        V=[i for i in range(35) if i!=r and not s>>i&1];b=induced(G,V);assert len(b)==26 and sum(v.bit_count() for v in b)==152;targets[wl(b)].append((r,V,b));shapes.add(deg(b))
    with gzip.open(CAT/'r38_27.g6.gz','rb') as fh:
        for idx,l in enumerate(fh):
            s=l.strip();e=sum(s[1:].translate(w));assert e>=85
            if e!=85:continue
            a=decode(s.decode());rec=Counter();rec['record']=idx
            for z,n in enumerate(a):
                if n.bit_count()!=7:continue
                rec['deletions']+=1;vs=[j for j in range(27) if j!=z];b=induced(a,vs);es=[(i,j) for i,j in combinations(range(26),2) if b[i]>>j&1];assert len(es)==78;ds=deg(b);before[ds.count(4),ds.count(7)]+=1
                assert ds.count(4)<2 or ds.count(7)<8
                for (i,j),(h,k) in combinations(es,2):
                    rec['trials']+=1;c=b[:];c[i]^=1<<j;c[j]^=1<<i;c[h]^=1<<k;c[k]^=1<<h
                    if deg(c) not in shapes:continue
                    rec['degree_pass']+=1;ts=targets.get(wl(c),[])
                    if not ts:continue
                    rec['neighbor_degree_pass']+=1
                    for r,V,target in ts:
                        f=iso(c,target)
                        if f is not None:
                            rec['iso_pass']+=1
                            if first is None:first=dict(record=idx,deleted=z,removed=[[vs[i],vs[j]],[vs[h],vs[k]]],root=r,mapping=dict(zip(vs,[V[u] for u in f])))
                            break
            records.append(dict(rec));hist.update({k:v for k,v in rec.items() if k!='record'})
    assert len(records)==4;out=dict(deletion_profiles=[dict(degree4=k[0],degree7=k[1],cases=n) for k,n in sorted(before.items())],target_roots=len(G),target_degree_profiles=[dict(Counter(k)) for k in sorted(shapes)],records=records,counts=hist,first=first);print(out);(D.parent/'ramsey_cube_retention_floor.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
