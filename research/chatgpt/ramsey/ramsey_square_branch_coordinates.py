"""Quotient surviving port supports by exact continuation lists. Which signatures coincide in the old core? Factor six-set solutions into Cartesian boxes; distinguish direct incompatibilities from implied ones."""
from ramsey_rooted_square_propagation import D,json,decode,inds,bits,test,Counter,product,combinations
from math import prod
from functools import reduce
from operator import and_

def audit(dom,L,E,miss,W):
    U=[list(bits(l)) for l in L];groups=[];types=[];direct=Counter()
    for i,us in enumerate(U):
        ds={}
        for x in us:
            sig=tuple(E[i,j][x]&L[j] for j in range(4) if j!=i);ds.setdefault(sig,[]).append(x)
        groups.append(list(ds.values()))
        for xs in ds.values():
            if len(xs)<2:continue
            raw={miss[dom[i][x]][2] for x in xs};external=0
            for j in range(4):
                if i!=j:
                    for y in U[j]:external|=miss[dom[j][y]][2]
            observable={s&external for s in raw};types.append(dict(size=len(xs),raw=len(raw),observable=len(observable)))
    for i,j in combinations(range(4),2):
        for x,y in product(U[i],U[j]):
            s,t=dom[i][x],dom[j][y];over=bool(s&t&~W);row=bool(miss[s][2]&miss[t][2]);kept=bool(E[i,j][x]>>y&1);assert not kept or not(over or row);direct['allowed' if kept else 'both' if over and row else 'shared_vertex' if over else 'missed_six' if row else 'implied']+=1
    boxes=[]
    for v in product(*(range(len(g)) for g in groups)):
        vs=[groups[i][b][0] for i,b in enumerate(v)]
        if all(E[i,j][vs[i]]>>vs[j]&1 for i,j in combinations(range(4),2)):boxes.append(v)
    disjoint=all(all(a!=b for a,b in zip(v,w)) for v,w in combinations(boxes,2));return dict(groups=[[[dom[i][x] for x in xs] for xs in g] for i,g in enumerate(groups)],boxes=boxes,nontrivial=types,exclusions=direct,separated=disjoint,expanded=sum(prod(len(groups[i][v[i]]) for i in range(4)) for v in boxes))

def run():
    prev=json.loads((D/'ramsey_rooted_square_propagation.json').read_text());lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[];last=None
    for r in prev:
        if not r['pc']:continue
        idx=r['record'];W=r['seed']
        if idx!=last:
            H=decode(lines[idx-1]);I=inds(H);T=[[t for t in I if t.bit_count()==k] for k in (4,5,6)];miss={s:[sum(1<<j for j,t in enumerate(ts) if not s&t) for ts in T] for s in I};last=idx
        ans={};test(H,I,miss,W,lambda d,l,e:ans.update(audit(d,l,e,miss,W)));assert ans['expanded']==r['six'];
        if len(ans['boxes'])==2:
            a,b=[[reduce(and_,ans['groups'][i][v[i]])&~W for i in range(4)] for v in ans['boxes']];moves=[[j for j,y in enumerate(b) if x&y] for x in a];assert all(len(js)==1 for js in moves);ans['move']=[js[0] for js in moves];ans['anchors']=[a[i]&b[j] for i,j in enumerate(ans['move'])]
        out.append(dict(record=idx,seed=W,**ans))
    return out
if __name__=='__main__':
    z=run();print(Counter((len(r['boxes']),r['separated']) for r in z));print(Counter((t['raw']==1,t['observable']==1) for r in z for t in r['nontrivial']));print(sum((r['exclusions'] for r in z),Counter()));(D/'ramsey_square_branch_coordinates.json').write_text(json.dumps(z)+'\n')
