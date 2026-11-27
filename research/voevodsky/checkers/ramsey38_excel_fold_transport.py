"""Literal graph operation hypothesis for one mirrored Excel fold (not compression itself)."""
from ramsey38_excel_square_transfer import graph,setup,prev,gzip,json,Counter,combinations,sys
from itertools import permutations
from functools import lru_cache
P=prev.out/'ramsey38_fold_transport_protocol.json';R=prev.out/'ramsey38_fold_transport_results.json'
rule=dict(start=310065,records=128,root='least degree-seven vertex per consecutive catalogue record; no row filter',words=['BRBBRBBR','BRBBRBRB'],marks='Column 1 remains root; allow all permutations of its seven red neighbors. Two distinct named outside rows realize the two words exactly. Keep both row names, all column names, root, core edges and every other incidence fixed.',operation='Exchange the two rows only on columns 7,8: remove two red edges and add the opposite two. Prediction: a witnessed reversible Excel alternative gives a legal (3,8) coloring after this switch. Falsifier: explicit red triangle or independent eight.',control='Compare existence under free column bijection with the unordered signature-only rule: two size-three rows share exactly two labels. Count each graph row pair once, not each labeling.')

def defect(g):
    vs=sorted(g)
    for a in vs:
        for b in g[a]:
            common=g[a]&g[b]
            if common:return 'red_triangle',[a,b,min(common)]
    def independent(cand,path):
        if len(path)==8:return path
        while len(path)+len(cand)>=8:
            v=min(cand);cand=cand-{v};hit=independent(cand-g[v],path+[v])
            if hit:return hit
    hit=independent(set(vs),[]);return ('blue_eight',hit) if hit else ('legal',[])

def run():
    assert json.loads(P.read_text())==rule;words=rule['words'];proj=[]
    for perm in permutations(range(7)):
        masks=tuple(sum(1<<j for j,ch in zip(perm,w[1:]) if ch=='R') for w in words);proj.append(masks)
    orbit=Counter(tuple(sorted(ms)) for ms in proj);assert len(orbit)==210 and set(orbit.values())=={24};cnt=Counter();examples={}
    with gzip.open(prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i<rule['start']:continue
            if i>=rule['start']+rule['records']:break
            g=graph(line.strip());cnt['records']+=1;u=next((u for u in sorted(g) if len(g[u])==7),None)
            if u is None:continue
            cnt['eligible_roots']+=1;L,r,_=setup(g,u);found=False
            for x,y in combinations(sorted(r),2):
                s,t=r[x],r[y];match=tuple(sorted((s,t))) in orbit;assert match==(s.bit_count()==t.bit_count()==3 and (s&t).bit_count()==2)
                if not match:continue
                found=True;a=L[(s&~t).bit_length()-1];b=L[(t&~s).bit_length()-1];h={j:set(ns) for j,ns in g.items()}
                for v,w in [(x,a),(y,b)]:h[v].remove(w);h[w].remove(v)
                for v,w in [(x,b),(y,a)]:h[v].add(w);h[w].add(v)
                k,cert=defect(h);cnt[k]+=1
                m=next(j for j,ms in enumerate(proj) if set(ms)=={s,t});perm=next(p for j,p in enumerate(permutations(L)) if j==m);row_order=[x,y] if proj[m]==(s,t) else [y,x];examples.setdefault(k,dict(record=i,root=u,columns=[u,*perm],rows=row_order,remove=[[x,a],[y,b]],add=[[x,b],[y,a]],defect=cert))
            cnt['roots_with_fold']+=found
    print(cnt,examples);prev.save(R,dict(protocol_sha=prev.sha(P.read_bytes()),orbit_size=len(orbit),labelings_per_pair=24,counts=dict(cnt),examples=examples))
if __name__=='__main__':{'freeze':lambda:prev.save(P,rule),'test':run}[sys.argv[1]]()
