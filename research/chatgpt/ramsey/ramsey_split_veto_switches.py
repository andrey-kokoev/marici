"""Attribute vetoes by their collision vertices; then release the single orientation bit. Each touched outsider keeps exactly one endpoint-compatible colour, invisible vertices remain uncoloured. Exact CNF checks full diversity and independence, minimize switches vs two copies."""
from ramsey_orientation_veto import D,json,graph,inds,bits,prove,gzip,Counter
from ramsey_capacity_transfer_78 import verify,grow,combinations
from pysat.solvers import Solver
from pysat.card import CardEnc

def run():
    prev=json.loads((D/'ramsey_orientation_veto.json').read_text());ls=gzip.decompress((D/'pauli-realization-catalogues/r38_27.g6.gz').read_bytes()).splitlines();tab=[{m:v for m,v in r['table']} for r in prove()];out=[]
    for rec in prev:
        p=rec['record'];H=graph(ls[p-1]);I=inds(H);T=[s for s in I if s.bit_count()>=5];n=len(H)
        for r in rec['rows']:
            if r['tag'] not in ('split veto','same veto'):continue
            W=r['seed'];a=next(bits(W));b=next(bits(H[a]&W));c,d=bits(W^(1<<a|1<<b));V=(a,b,c,d);col=r['collision'];ends=[1<<i|1<<j for i in (a,b) for j in (c,d)];S=[ends.copy(),ends.copy()];dom={};C=[]
            for u in range(n):
                if W>>u&1:continue
                profile=sum(1<<i for i,v in enumerate(V) if H[u]>>v&1);choices=[t[profile] for t in tab];
                if not profile:continue
                colors=[c.bit_length()-1 for c in choices];dom[u]=list(dict.fromkeys(colors))
                for j,h in enumerate(colors):S[j][h]|=1<<u
                lits=[4*u+h+1 for h in dom[u]];C.append(lits);C.extend([[-x,-y] for x,y in combinations(lits,2)])
            rr=[{t for t in T if t.bit_count()==7 and sum(bool(t&s) for s in v)<3} for v in S];assert sorted(map(len,rr))==sorted(r['counts']);best=min(((t&col).bit_count()+(u&col&~t).bit_count(),t,u) for t in rr[0] for u in rr[1]);
            for u,cs in dom.items():
                for v in bits(H[u]):
                    if v>u and v in dom:C.extend([[-(4*u+h+1),-(4*v+h+1)] for h in set(cs)&set(dom[v])])
            priv=[u for u in dom if len(dom[u])==2];reach={u:{u} for u in priv}
            for u in priv:
                for v in priv:
                    if H[u]>>v&1 and dom[u][1]==dom[v][0]:reach[u].add(v)
            for v in priv:
                for u in priv:
                    if v in reach[u]:reach[u]|=reach[v]
            blocks={tuple(sorted(v for v in reach[u] if u in reach[v])) for u in priv};C6=C.copy()
            for t in T:
                for ps in combinations(range(4),9-t.bit_count()):
                    if any(t&ends[h] for h in ps):continue
                    clause=[4*u+h+1 for u in bits(t) if u in dom for h in ps if h in dom[u]];C.append(clause)
                    if t.bit_count()==7:C6.append(clause)
            with Solver(name='g3',bootstrap_with=C6) as sat:top_ok=sat.solve()
            cost=None;witness=None
            with Solver(name='g3',bootstrap_with=C) as sat:ok=sat.solve()
            if ok:
                for k in range(n+1):
                    for base in S:
                        lits=[-(4*u+next(h for h in cs if base[h]>>u&1)+1) for u,cs in dom.items() if len(cs)>1];cn=CardEnc.atmost(lits,k,top_id=4*n) if k<len(lits) else None
                        with Solver(name='g3',bootstrap_with=C+(cn.clauses if cn else [])) as sat:
                            if not sat.solve():continue
                            model=set(sat.get_model());witness=[s|sum(1<<u for u,cs in dom.items() if h in cs and 4*u+h+1 in model) for h,s in enumerate(ends)];verify(grow(H,witness),9);cost=k;break
                    if cost is not None:break
            out.append(dict(record=p,seed=W,tag=r['tag'],blocks=sorted(blocks),top_ok=top_ok,collision=col,minimum_collision_union=best[0],vetoes=best[1:],cost=cost,witness=witness))
    return out
if __name__=='__main__':
    z=run();print(Counter((r['tag'],r['minimum_collision_union']) for r in z));print(Counter((r['tag'],r['cost']) for r in z));print(next((r for r in z if r['tag']=='split veto' and r['collision'].bit_count()==1),None));(D/'ramsey_split_veto_switches.json').write_text(json.dumps(z)+'\n')
