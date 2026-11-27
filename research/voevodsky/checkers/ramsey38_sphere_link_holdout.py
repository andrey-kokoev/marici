"""Enriched prospective trial: at least one eligible boundary chain loses a rim vertex."""
from ramsey38_three_route_novelty import previous,P as last
from ramsey38_three_matched_holdout import prior,predict,compare,prepare,setup,graph,key,gzip,add,prev,json,sys,permutations,faces
from ramsey38_three_releases import solve
from collections import Counter
P=prev.out/'ramsey38_sphere_link_predictions.json';R=prev.out/'ramsey38_sphere_link_comparison.json';S=prev.out/'ramsey38_sphere_link_scores.json'
protocol='First eight new canonical eligible arrays after 6000 through 24000, one per record, with some eligible edit/boundary chain losing a boundary vertex between stages. No filling or plan required for eligibility. Freeze both algorithms; score full meshes and append-only routes including requiring a boundary vertex to become interior. Same one/two-cell collar budget. Exhaustive census has no collar length cap.'
def rim(b):
    m=0
    for f in b:m|=f
    return m
def freeze():
    seen={key(*setup(graph(e['word']),e['u'])) for p in (prior,previous,last) for e in json.loads(p.read_text())['cases']};es=[]
    with gzip.open(prev.catalogue,'rt') as fp:
        for i,line in enumerate(fp,1):
            if i<=6000:continue
            if i>24000:break
            w=line.strip();g=graph(w)
            for u in sorted(g):
                if len(g[u])!=7:continue
                L,rs,m=setup(g,u)
                if len(m)<3 or max(map(int.bit_count,rs.values()))>4 or sum(s.bit_count()==2 for s in rs.values())<3:continue
                k=key(L,rs,m)
                if k in seen or not any(setup(add(add(g,a),b),u)[2] for a in m for b in setup(add(g,a),u)[2]):continue
                seen.add(k);_,rows,_,_,_,chains=prepare(g,u)
                if not any(any(rim(b)&~rim(c) for s,t in zip(ss,ss[1:]) for b in s for c in t) for _,_,ss in chains):continue
                def make(mode):
                    ps,_=predict(g,u,allow_interior=mode);out=[]
                    for p in ps:
                        a=set(map(frozenset,p['mesh']));zs=[]
                        for j,bd in enumerate(p['shells']):
                            seq=p['additions'][j-1] if j else [];a.update(map(frozenset,seq));zs.append(dict(bd=bd,cells=faces(a),append=seq))
                        out.append(dict(goal=p['goal'],moves=p['moves'],stages=zs))
                    return out
                a,b=make(False),make(True);es.append(dict(record=i,word=w,u=u,requests=len(list(permutations(rows,3))),control=a,plans=b));print(i,u,len(a),len(b),flush=True);break
            if len(es)==8:break
    assert es;prev.save(P,dict(protocol=protocol,cases=es))
def check():
    compare(P,R);cnt=Counter();records=[]
    for e,z in zip(json.loads(P.read_text())['cases'],json.loads(R.read_text())['cases'],strict=True):
        valid=set(map(tuple,z['verified']));ok={tuple(p['goal']):p for p in e['plans'] if tuple(p['goal']) in valid};assert all(ok.get(tuple(p['goal']))==p for p in e['control']),'verify differing control plans separately';cnt['control_verified']+=len(e['control']);cnt['sphere_verified']+=len(valid);cnt['feasible']+=len(z['feasible']);cnt['requests']+=e['requests'];buried=lambda p:any(rim(a['bd'])&~rim(b['bd']) for a,b in zip(p['stages'],p['stages'][1:]));pos={tuple(p['goal']) for p in z['feasible'] if buried(p)}
        if len(pos)<len(z['feasible']):pos={tuple(p['goal']) for p in solve(graph(e['word']),e['u'],True,require_burial=True)[0]}
        hits={j for j,p in ok.items() if buried(p)};assert hits<=pos;cnt['burial_feasible']+=len(pos);cnt['burial_verified']+=len(hits);records.append(dict(record=e['record'],burial_goals=sorted(pos),burial_hits=sorted(hits)))
    print(cnt);prev.save(S,dict(comparison_sha=prev.sha(R.read_bytes()),counts=dict(cnt),results=records))
if __name__=='__main__':{'freeze':freeze,'compare':check}[sys.argv[1]]()
