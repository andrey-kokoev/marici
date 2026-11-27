from ramsey_flank_singleton import *
from ramsey_relative_sign_joint_context import build

def run(first):
    rows=[s for s in combinations(range(8),3) if min(s[1]-s[0],s[2]-s[1])>=2];count=Counter();gs=Counter();out=[]
    for ss in combinations(rows,5):
        es=[i for i,(a,b) in enumerate(ports) if not set(ss[a])&set(ss[b])];
        if len(es)!=2:continue
        count['families']+=1;S=grow(ss,first);M=[sum(1<<v for v in s) for s in S];w=[]
        for e in es:
            a,b=ports[e];u=511^(M[a]|M[b]);adj=u&(u>>1)
            if adj.bit_count()!=1:break
            gap=adj.bit_length();others=[j for j in range(5) if j not in (a,b) and not M[j]&u];T=next((sorted((a,b,h,k)) for h,k in combinations(others,2) if not set(ports[es[1-es.index(e)]])<={a,b,h,k}),None)
            if T is None:break
            w.append((gap,u,T))
        if len(w)!=2 or w[0][0]!=w[1][0]:continue
        gap=w[0][0];f=3<<(gap-1);count['double_geometry']+=1;full=sum(1<<n for n in es);E=[sum(1<<e for e in es if all(p>>i&1 for i in ports[e])) for p in range(32)];U=[sum(1<<i for i in set().union(*(S[j] for j in range(5) if p>>j&1))) for p in range(32)]
        def safe(c,blocked,avoid,n):return all(E[p]&c or U[p]&avoid or I[511&~(U[p]|blocked)]+p.bit_count()<n for p in range(32))
        cols=[0,1<<es[0],1<<es[1],full];parents=[safe(c,0,0,7) for c in cols];assert parents==[verdict(graph(9,S,c)) for c in cols];
        if not all(parents[1:]):count['parent_excluded']+=1;continue
        predicted=safe(full,f,0,6) and safe(full,f|f<<1|f>>1,f,5);actual=[verdict(build({gap:()},S,c)) for c in cols];assert actual==[False,False,False,predicted];
        if not predicted:count['competing_obstruction']+=1;continue
        count['usable']+=1;gs[gap]+=1;out.append(dict(rows=[[x+1 for x in s] for s in ss],gap=gap,parents=parents,edges=[[v+1 for v in ports[e]] for e in es],witnesses=[dict(old_sites=[v+1 for v in range(9) if u>>v&1],ports=[v+1 for v in t]) for g,u,t in w]))
    if first==1:
        prev=json.loads((D.parent/'ramsey_conditional_probe_types.json').read_text())['cases'];key=lambda c:(tuple(map(tuple,c['rows'])),c['gap']);assert set(map(key,out))=={key(c) for c in prev if all('E' in r['counts'] for r in c['only_first_then_only_second'])}
    print(first,count,gs,out[:1]);return dict(first=first,counts=count,reading_gaps=gs,cases=out)
if __name__=='__main__':save(D.parent/'ramsey_double_flank_geometry.json',dict(protocol_sha=sha256((D.parent/'ramsey_double_flank_geometry_protocol.md').read_bytes()).hexdigest(),charts=[run(1),run(4)]))
