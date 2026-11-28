"""Test whether one new clique causes infeasibility. Partial models enforce only the selected blue demands, but always enforce triangles and red degree cap including the restored row."""
from ramsey_cube_degree_release import G,D,induced,prepare,demands,json
from itertools import combinations

def audit():
    x=json.loads((D.parent/'ramsey_cube_degree_release.json').read_text());labels=json.loads((D.parent/'ramsey_cube_unlock_free_row.json').read_text())['core_labels'];a=induced(G,labels);cuts=list(map(tuple,x['cuts']));s=sum(1<<j for j in x['row']);old=sorted(demands(prepare(a,cuts,s)[0],s));out=[]
    for e in [(0,11),(4,16),(11,14)]:
        b,_,E=prepare(a,cuts+[e],s);qall=sorted(demands(b,s));new=sorted(set(qall)-set(old));assert set(old)<=set(qall) and all(all(q>>j&1 for j in e) for q in new);M={q:frozenset(edge for edge in E if all(q>>i&1 for i in edge)) for q in qall}
        def model(qs):
            ds=[]
            for d in sorted({M[q] for q in qs},key=lambda x:(len(x),sorted(x))):
                if not any(v<=d for v in ds):ds.append(d)
            g=b[:]+[s]
            for i in range(26):g[i]|=(s>>i&1)<<26
            def rec(g,ds,chosen):
                if not ds:
                    assert all(v.bit_count()<=7 for v in g) and all(not(g[i]&g[j]) for i,j in combinations(range(27),2) if g[i]>>j&1) and all(M[q].intersection(chosen) for q in qs);return chosen
                d=min(([p for p in d if all(g[i].bit_count()<7 for i in p) and not g[p[0]]&g[p[1]]] for d in ds),key=len)
                for i,j in sorted(d,key=lambda p:(-sum(p in v for v in ds),p)):
                    v=g[:];v[i]|=1<<j;v[j]|=1<<i;z=rec(v,[c for c in ds if (i,j) not in c],chosen+[(i,j)])
                    if z is not None:return z
            return rec(g,ds,[])
        def shrink(qs):
            core=list(qs);assert model(core) is None
            for q in qs:
                trial=[v for v in core if v!=q]
                if model(trial) is None:core=trial
            return core
        oldw=model(old);veto=None if oldw is None else [q for q in new if model(old+[q]) is None];assert model(qall) is None
        core=shrink(old) if oldw is None else shrink(old+([veto[0]] if veto else new));out.append(dict(third=e,old_count=len(old),new_count=len(new),old_witness=oldw,single_vetoes=veto,minimal_core=[dict(sites=[i for i in range(26) if q>>i&1],new=q in new,options=sorted(M[q])) for q in core]));print(e,'old_sat',oldw is not None,'vetoes',None if veto is None else len(veto),'core',len(core),'new_in_core',sum(q in new for q in core))
    (D.parent/'ramsey_cube_single_veto.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
