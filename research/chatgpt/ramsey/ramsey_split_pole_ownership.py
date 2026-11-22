"""Trace marked and unmarked circuits and test if literal R exchanges their alternating matching phases, not just their uncoloured flags."""
from ramsey_long_residual_inverse import flags,R,D,json

def run():
    out=[]
    for r in json.loads((D/'ramsey_all_extra_deadends.json').read_text()):
        if len(r['factors'])!=2:continue
        z={v for x,y in r['extra']+[[9,26],[14,15]] for v in (x,y)}
        for factor in r['factors']:
            edges={e for e in flags if not set(e)&z}-set(map(tuple,factor['omitted']));adj={v:set() for e in edges for v in e}
            for x,y in edges:adj[x].add(y);adj[y].add(x)
            left=set(adj);cs=[]
            while left:
                x=min(left);w=[x];y=min(adj[x]);
                while y!=x:w.append(y);y,=adj[y]-{w[-2]}
                left-=set(w);ph=[{tuple(sorted((w[i],w[(i+1)%len(w)]))) for i in range(k,len(w),2)} for k in (0,1)];moved={tuple(sorted((R[a],R[b]))) for a,b in ph[0]};assert moved in ph;cs.append(dict(word=w,pole_distance=w.index(29) if x==0 and 29 in w else None,row_swap_indices=[w.index(R[v]) for v in w],phase_exchanged=moved==ph[1]))
            out.append(dict(extra=r['extra'],components=cs))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_split_pole_ownership.json').write_text(json.dumps(out)+'\n')
