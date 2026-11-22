"""Orient overlap e from its first to second occurrence: a companion sharing an endpoint in the first duad pins the tail, one in the second pins the head. Report failures rather than breaking ties. No square-rim, color, or native input to orient()."""
from ramsey_two_visit_overlap_reader import cycle,m,P,X,r,D,json
from itertools import permutations

def orient(ds,labels):
    out=[]
    for i,src in enumerate(ds):
        dst=ds[(i+2)%len(ds)];a,b=map(lambda d:set(P[d]),(src,dst));k,=a&b;ka,=a-{k};kb,=b-{k};e=labels[k];u,v=set(labels[ka])&set(e),set(labels[kb])&set(e);options=[q for q in (tuple(e),tuple(reversed(e))) if (not u or q[0] in u) and (not v or q[1] in v)];assert len(options)==1;out.append(dict(arrow=options[0],tail_pinned=bool(u),head_pinned=bool(v),companions=[labels[ka],labels[kb]]))
    return out

def run():
    ds=cycle(m)[::2];out=[]
    for d in (ds,[r[v] for v in ds]):
        steps=orient(d,X);arrows=[s['arrow'] for s in steps];rim=arrows[:4];assert all(rim[i][1]==rim[(i+1)%4][0] for i in range(4));u,v=arrows[-1];via,=[b for a,b in rim if a==u and (b,v) in rim];c,e=steps[-1]['companions'];q,=set(c)&set(e);assert via==1 and q==4 and (v,q) in rim and (q,u) in rim
        for perm in permutations((1,2,3,4)):
            g=lambda a:perm[a-1];moved=orient(d,[tuple(map(g,e)) for e in X]);assert [w['arrow'] for w in moved]==[tuple(map(g,t)) for t in arrows]
        out.append(dict(steps=steps,rim_midpoint=via,companion_midpoint=q))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_oriented_overlap_reader.json').write_text(json.dumps(out)+'\n')
