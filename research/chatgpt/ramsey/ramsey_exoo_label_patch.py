"""Localize the chart22 backbone: choose subsets D of the nine anchor labels and keep only exterior vertices whose entire address is contained in D. For an exterior independent set J, available anchors give a ten-set iff |J|>|union signatures|; root gives one iff |J|>=9. SAT compute each patch's exact forced links; propagate between equal-size patches only after the whole round. Reference graph used as known legal model to query backbone, never to fix a candidate edge."""
from itertools import combinations
from ramsey_exoo_address_closure import chart,edges,Path,json
from pysat.solvers import Solver
from functools import lru_cache

def run():
    A,X=chart(22);E=edges();sig=dict((v,s) for s,v in X);V=sorted(sig);pairs=list(combinations(V,2));idx={p:i+1 for i,p in enumerate(pairs)};known={p for p in pairs if sig[p[0]]&sig[p[1]]};assert all(p not in E for p in known);stages=[]
    def patch(D,base,omit=None,proper_only=False,keep_root=True):
        U=[v for v in V if v!=omit and not sig[v]&~D];P=list(combinations(U,2));pending={p for p in P if p not in base};forced={};C=[[idx[p] if p in E else -idx[p]] for p in P if p in base];C+=[[-idx[i,j],-idx[i,k],-idx[j,k]] for i,j,k in combinations(U,3)];learn=0
        with Solver(name='g4',bootstrap_with=C) as sat:
            sat.set_phases([idx[p] if p in E else -idx[p] for p in P]);
            while pending:
                sat.add_clause([(-1 if p in E else 1)*idx[p] for p in sorted(pending)])
                while sat.solve():
                    m=set(sat.get_model());adj={v:0 for v in U}
                    for (i,j) in P:
                        if idx[i,j] in m:adj[i]|=1<<j;adj[j]|=1<<i
                    I=[(0,0)];bad=[]
                    for v in U:
                        add=[]
                        for s,u in I:
                            if s&adj[v]:continue
                            t=s|1<<v;g=u|sig[v];n=t.bit_count()
                            if (not proper_only or g!=511) and ((keep_root and n>=9) or n>g.bit_count()):bad.append(t)
                            else:add.append((t,g))
                        I.extend(add)
                    if not bad:
                        pending={p for p in pending if (idx[p] in m)==(p in E)};break
                    for t in bad:sat.add_clause([idx[p] for p in combinations([v for v in U if t>>v&1],2)])
                    learn+=len(bad)
                else:break
        return pending,learn
    for d in range(2,10):
        new={};lr=0
        for D in range(512):
            if D.bit_count()!=d:continue
            f,l=patch(D,known);lr+=l
            for p in f:new.setdefault(p,D)
        if d==9:
            controls={}
            for name,omit,pr,kr in [('delete35',35,False,True),('proper_joint',None,True,True),('no_root',None,False,False),('proper_joint_delete35',35,True,True)]:
                # Reset to input facts: inherited proper-patch consequences may depend on the omitted vertex.
                init={p for p in pairs if sig[p[0]]&sig[p[1]]};ff,ll=patch(511,init,omit,pr,kr);op=[p for p in pairs if omit not in p and p not in init|ff];controls[name]=dict(open=op,learned=ll);print(name,len(op),sum(35 not in p for p in op),ll,flush=True)
        known.update(new);opened=[p for p in pairs if p not in known];stages.append(dict(size=d,learned=lr,forced=[(p,D) for p,D in sorted(new.items())],open=opened));print(d,len(new),len(opened),sum(35 not in p for p in opened),lr,flush=True)
    assert len(opened)==14 and all(35 in p for p in opened)
    # Independent check of the smallest counterfactual. Removing 35 permits erasing red 4--32.
    assert sig[4]|sig[32]==sig[35] and sig[4]&sig[32]==0 and sig[35].bit_count()==2 and (4,32) in E
    alt=E-{(4,32)};I=[0]
    for v in range(39):
        if v!=35:
            h=sum(1<<w for w in range(39) if tuple(sorted((v,w))) in alt);I += [s|1<<v for s in I if not s&h]
    assert max(s.bit_count() for s in I)==9
    return dict(anchors=A,stages=stages,controls=controls,forced_pair_after_return=[4,32],independent_ten_without_pair=[4,32,35]+[a for i,a in enumerate(A) if not sig[35]>>i&1])
if __name__=='__main__':Path(__file__).with_suffix('.json').write_text(json.dumps(run())+'\n')
