"""Fresh append-only triples requiring stage-two burial and third-stage retention."""
from ramsey38_sphere_link_holdout import P as sphere,prior,previous,last,prev,json,sys,graph,key,setup,add,gzip,prepare,predict,compare,permutations,faces,rim
from itertools import product
P=prev.out/'ramsey38_early_interior_predictions.json';R=prev.out/'ramsey38_early_interior_comparison.json'
protocol='After 20466 through 60000, first eight canonical new roots (one per record) with a legal three-promotion chain and nested release sets whose boundary masks allow a vertex on stage-one rim and off BOTH subsequent rims. No fill or prediction used to select. All ordered original edge-row triples. Require same label actually move inside at stage two and remain inside at stage three. Sphere-link constructor <=2 new cells each step; independent unrestricted attachment census.'
def early(bs):
    if len(bs)<2:return True
    lost=rim(bs[0])&~rim(bs[1]);return bool(lost if len(bs)==2 else lost&~rim(bs[2]))
def eligible(ss):return any(a&~(b|c) for a,b,c in product(*(set(map(rim,s)) for s in ss)))
def freeze():
    seen={key(*setup(graph(e['word']),e['u'])) for path in (prior,previous,last,sphere) for e in json.loads(path.read_text())['cases']};es=[]
    with gzip.open(prev.catalogue,'rt') as fp:
        for i,line in enumerate(fp,1):
            if i<=20466:continue
            if i>60000:break
            w=line.strip();g=graph(w)
            for u in sorted(g):
                if len(g[u])!=7:continue
                L,rs,m=setup(g,u)
                if len(m)<3 or max(map(int.bit_count,rs.values()))>4 or sum(s.bit_count()==2 for s in rs.values())<3:continue
                k=key(L,rs,m)
                if k in seen or not any(setup(add(add(g,a),b),u)[2] for a in m for b in setup(add(g,a),u)[2]):continue
                seen.add(k);_,rows,_,_,_,chains=prepare(g,u)
                if not any(eligible(ss) for _,_,ss in chains):continue
                ps,_=predict(g,u,allow_interior=True,boundary_filter=early);plans=[]
                for p in ps:
                    a=set(map(frozenset,p['mesh']));zs=[]
                    for j,bd in enumerate(p['shells']):
                        seq=p['additions'][j-1] if j else [];a.update(map(frozenset,seq));zs.append(dict(bd=bd,cells=faces(a),append=seq))
                    lost=rim(zs[0]['bd'])&~(rim(zs[1]['bd'])|rim(zs[2]['bd']));labels=[v for k,v in enumerate(L) if lost>>k&1];assert labels and all(not set(labels)&set(t) for t in zs[2]['append']);plans.append(dict(goal=p['goal'],moves=p['moves'],stages=zs,buried=labels))
                es.append(dict(record=i,word=w,u=u,requests=len(list(permutations(rows,3))),plans=plans));print(i,u,len(plans),flush=True);break
            if len(es)==8:break
    prev.save(P,dict(protocol=protocol,cases=es))
if __name__=='__main__':
    if sys.argv[1]=='freeze':freeze()
    elif sys.argv[1]=='compare':compare(P,R,boundary_filter=early)
