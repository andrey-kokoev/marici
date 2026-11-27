"""Diagnose final-only commitments rejected by matched stars on paired pivot holdout."""
from ramsey38_large_pivot_holdout import P,R,prev,json,sys
from ramsey38_mesh_single_pin import reduce_domains,graph,setup,disks,shelling,faces
from ramsey38_shared_twist10 import face_assignments,combinations
from ramsey38_append_531_routes import extend

def run():
    ver=json.loads(R.read_text());assert ver['prediction_sha']==prev.sha(P.read_bytes());truth={(r['record'],r['j'],r['l']):r for r in ver['results']};out=[]
    for e in json.loads(P.read_text())['cases']:
        L,rs,_=setup(graph(e['word']),e['u']);dec=lambda m:frozenset(a for i,a in enumerate(L) if m>>i&1)
        for d in e['requests']:
            q=d['commit'];v=truth[e['record'],d['j'],d['l']]
            if not q or v['commit_ok']:continue
            assert not v['routes'];x,a=q['first'];y,b=q['second'];rr={**rs,x:rs[x]|1<<L.index(a)};tip=dec(rs[x])|{q['tip']};extra=set(map(frozenset,q['collar']));r1=set(map(dec,rr.values()))|{tip};rr[y]|=1<<L.index(b);r2=set(map(dec,rr.values()))|extra|{tip};B=set(map(dec,q['bd']));F=set(map(dec,q['end']));I={i:disks(L,i,B,r1) for i in L};J={i:disks(L,i,F,r2) for i in L};D={i:[s for s in I[i] if not s&extra and s|{t for t in extra if i in t} in J[i]] for i in L}
            core=None
            for n in range(1,len(L)+1):
                for g in combinations(L,n):
                    N,k=reduce_domains({i:D[i] for i in g})
                    if not all(N.values()):core=g;break
                if core:break
            def balls(req,bd):return [frozenset(ts) for ts in face_assignments(L,req,bd) if shelling(ts)]
            starts=balls(r1,B);ends=balls(r2,F);pairs=[(s,t) for s in starts for t in ends];nested=sum(extend(s,t) is not None for s,t in pairs);assert not nested and core;best=min(((len(s-t),len(t-s)) for s,t in pairs),default=None);sizes=lambda D:{i:len(v) for i,v in D.items()};res=dict(record=e['record'],j=d['j'],l=d['l'],core=core,collar=q['collar'],initial=sizes(I),final=sizes(J),paired=sizes(D),initial_balls=len(starts),final_balls=len(ends),best_edit=best)
            if len(core)==1:
                i=core[0];res['core_vertex']=dict(initial=[faces(s) for s in I[i]],final=[faces(s) for s in J[i]],required_add=faces(t for t in extra if i in t));res['unavoidable_old_cells_missing_at_end']=faces(set.intersection(*(set(s) for s in starts))-set.union(*(set(t) for t in ends)))
            if len(core)==2:
                i,j=core;res['edge_orders_as_cells']=[sorted({tuple(tuple(sorted(t)) for t in sorted((t for t in s if b in t),key=sorted)) for s in D[a]}) for a,b in [(i,j),(j,i)]]
            print(res,flush=True);out.append(res)
    assert len(out)==5;prev.save(prev.out/'ramsey38_unmatched_collar_witnesses.json',dict(comparison_sha=prev.sha(R.read_bytes()),cases=out))
if __name__=='__main__':run()
