"""Transport each core vertex across a one-vertex exchange: fix the intersection and map the lost vertex to its replacement. Check all edges and a generating set of closed walks per component."""
from itertools import combinations
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results'
def main():
    E=set(map(tuple,json.loads((D/'ramsey_39_glue_vs_circle.json').read_text())['plus_edges']));U=set(range(35));plus=lambda a,b:tuple(sorted((a,b))) in E
    cores={};adj={}
    for d in (4,9,29):
        for t in range(35):
            for shape,off in [('P',(0,1,2,3)),('C',(-2,0,1,3))]:
                q={(d*(t+i))%35 for i in off};c={v for v in U-q if not any(plus(v,w) for w in q)};assert len(c)==13 and all(sum(plus(v,w) for w in c)==4 for v in c);cores[d,t,shape]=c
    for a,b in combinations(cores,2):
        c,h=cores[a],cores[b]
        # Only evaluate root-exchange edges from the previously verified normal form, not arbitrary intersections.
        if a[0]!=b[0]:continue
        i,j=a[1],b[1];x,y=a[2],b[2]
        if not ((x==y=='P' and (i-j)%35 in (1,34)) or (x!=y and ((j-i) if x=='P' else (i-j))%35 in (0,2))):continue
        u,=c-h;v,=h-c;assert all(plus(u,w)==plus(v,w) for w in c&h);adj[a,b]=(u,v);adj[b,a]=(v,u)
    assert len(adj)==630
    def loop(path):
        assert path[0]==path[-1];cs=sorted(cores[path[0]]);image=cs[:]
        for a,b in zip(path,path[1:]):
            u,v=adj[a,b];image=[v if z==u else z for z in image]
        f=dict(zip(cs,image));assert set(image)==set(cs);cycles=[]
        while f:
            v=next(iter(f));row=[]
            while v in f:row.append(v);v=f.pop(v)
            assert v==row[0];cycles.append(row)
        return cycles
    wraps={};squares=0
    for d in (4,9,29):
        p=lambda i:(d,i%35,'P');c=lambda i:(d,i%35,'C');wraps[d]=loop([p(i) for i in range(36)])
        for i in range(35):
            assert all(len(z)==1 for z in loop([p(i),p(i+1),p(i+2),c(i+2),p(i)]));squares+=1
    for cs in wraps.values():
        order,=cs;assert len(order)==13 and all(plus(order[i],order[j])==(min(j-i,13+i-j) in (1,5)) for i,j in combinations(range(13),2))
    out=dict(exchange_isomorphisms=len(adj)//2,squares_identity=squares,wrap_cycles=wraps,induced_core_circular_distances=[1,5]);print(out);(D/'ramsey_39_core_transport.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
