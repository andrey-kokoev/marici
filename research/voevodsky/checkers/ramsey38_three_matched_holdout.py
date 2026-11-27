"""Freeze graph edits, three meshes, and attachment orders before full extension census."""
from ramsey38_three_matched_stars import predict
from ramsey38_three_releases import P as prior,prev,json,sys,graph,setup,add,key,gzip,prepare,permutations,compare,faces
from pathlib import Path
P=prev.out/'ramsey38_three_matched_holdout_predictions.json';R=prev.out/'ramsey38_three_matched_holdout_comparison.json'
protocol='After record 1759 through 6000, first ten canonical novel arrays with a legal triple promotion and eligible boundary chain, at most one root per record. No outcome-based selection. Same matched-star constructor, append one or two tetrahedra at each step, fixed rank and at most one pin. Freeze complete plans. Compare every ordered original edge-row triple against unrestricted seven-label append-only shellable census.'
def freeze(after=1759,excluded=(),dest=P,description=protocol,annotate=None,done=lambda es:len(es)==10,limit=6000):
    es=[];seen={key(*setup(graph(e['word']),e['u'])) for path in (prior,*excluded) for e in json.loads(path.read_text())['cases']};scanned=0
    with gzip.open(prev.catalogue,'rt') as fp:
        for i,line in enumerate(fp,1):
            if i<=after:continue
            if i>limit:break
            w=line.strip();g=graph(w)
            for u in sorted(g):
                if len(g[u])!=7:continue
                L,rs,m=setup(g,u)
                if len(m)<3 or max(map(int.bit_count,rs.values()))>4 or sum(s.bit_count()==2 for s in rs.values())<3:continue
                k=key(L,rs,m)
                if k in seen or not any(setup(add(add(g,a),b),u)[2] for a in m for b in setup(add(g,a),u)[2]):continue
                seen.add(k);scanned+=1;_,rows,_,_,_,chains=prepare(g,u)
                if not chains:continue
                picks,counts=predict(g,u);plans=[]
                for q in picks:
                    a=set(map(frozenset,q['mesh']));stages=[]
                    for s,bd in enumerate(q['shells']):
                        seq=q['additions'][s-1] if s else [];a.update(map(frozenset,seq));stages.append(dict(bd=bd,cells=faces(a),append=seq))
                    plans.append(dict(goal=q['goal'],moves=q['moves'],stages=stages,pin=q['pin'],first_only_sizes=q['first_only_sizes'],sizes=q['sizes']))
                if annotate:annotate(L,plans)
                es.append(dict(record=i,u=u,word=w,requests=len(list(permutations(rows,3))),chains=len(chains),counts=counts,plans=plans));print(i,u,len(plans),flush=True);break
            if done(es):break
    assert es;prev.save(dest,dict(protocol=description,scanned=scanned,constructor_sha=prev.sha(Path(__file__).with_name('ramsey38_three_matched_stars.py').read_bytes()),cases=es))
if __name__=='__main__':
    if sys.argv[1]=='freeze':freeze()
    elif sys.argv[1]=='compare':compare(P,R)
