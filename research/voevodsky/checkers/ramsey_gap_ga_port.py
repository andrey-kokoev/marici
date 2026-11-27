from ramsey_repair_next_seam import graph,check,sevens,grow,D,combinations,sha256,json
from collections import Counter

def gp(a,b):
    out=Counter()
    for x,v in a.items():
        for y,w in b.items():
            n=sum((y% (1<<j)).bit_count() for j in range(x.bit_length()) if x>>j&1);out[x^y]+=v*w*(-1)**n
    return {k:v for k,v in out.items() if v}
def vector(v):return {1<<i:x for i,x in enumerate(v) if x}
def frames():
    vs=((1,1,1),(1,-1,-1),(-1,1,-1),(-1,-1,1));gens=[]
    for j in range(3):
        n=vector([a-b for a,b in zip(vs[j],vs[j+1])]);norm,=gp(n,n).values();p=[]
        for v in vs:
            nv=gp(gp(n,vector(v)),n);p.append(next(i for i,w in enumerate(vs) if nv==vector([-norm*x for x in w])))
        assert p[j]==j+1 and p[j+1]==j;gens.append(p)
    group={tuple(range(4))};old=set()
    while old!=group:
        old=group;group=old|{tuple(g[i] for i in p) for g in gens for p in old}
    return len(group),sum(all(abs(a-b)==1 for a,b in zip(p,p[1:])) for p in group)
def run():
    src=D.parent/'ramsey_port_repair_orbits.json';data=json.loads(src.read_text());ss=grow(tuple(tuple(x-1 for x in s) for s in data['supports']),data['gap']);pairs=list(combinations(range(5),2));mats=[];grades=[];fail={}
    for idx,rep in enumerate(data['representatives']):
        es=[(i-1,j-1) for i,j in rep['edits']];bs=[{(1<<i)|(1<<j):1} for i,j in es];grades.append([x.bit_count() for x in gp(*bs)]);col=sum(1<<pairs.index(e) for e in es);legal=[]
        for k in range(10):
            T=grow(ss,k)
            for p in range(5):
                t=[tuple(s)+( (k,) if i==p else ()) for i,s in enumerate(T)];G=graph(10,t,col);ok=check(G,32767,3,7);move=(k,p+1)
                if ok:legal.append(move)
                else:
                    tri=next((q for q in combinations(range(15),3) if all(G[i]>>j&1 for i,j in combinations(q,2))),None);q=tri or next(sevens(G));fail[idx,move]=dict(color='red' if tri else 'blue',sites=[i+1 for i in q if i<10],ports=[i-9 for i in q if i>=10])
        mats.append(set(legal))
    a,b=mats;diff=[dict(move=m,reject=fail[int(m in a),m]) for m in sorted(a^b)];swapped={(k,{2:3,3:2}.get(p,p)) for k,p in b};out=dict(frames=frames(),port_product_grades=grades,legal=[sorted(a),sorted(b)],symmetric_difference=len(diff),difference_after_port_exchange=len(a^swapped),differences=diff,protocol_sha=sha256((D.parent/'ramsey_gap_ga_port_protocol.md').read_bytes()).hexdigest());print(out);dest=D.parent/'ramsey_gap_ga_port.json';s=json.dumps(out,indent=2)+'\n';assert not dest.exists() or dest.read_text()==s;dest.write_text(s)
if __name__=='__main__':run()
