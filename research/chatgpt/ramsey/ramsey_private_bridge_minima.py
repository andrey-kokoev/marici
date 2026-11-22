"""Enumerate ALL minimum sets of doubly used private neighbours; block a bridge set, not a full solution. Classify pair shape and whether the extra overlapping vertices reproduce a second square seed."""
from ramsey_invisible_region_repairs import audit,D,json,graph,inds,bits,prove,gzip,Counter,CardEnc,Solver,grow,verify
from functools import reduce
from operator import and_
from itertools import combinations

def run():
    cases=json.loads((D/'ramsey_invisible_region_repairs.json').read_text());ls=gzip.decompress((D/'pauli-realization-catalogues/r38_27.g6.gz').read_bytes()).splitlines();tab=[dict(r['table']) for r in prove()];out=[];last=None
    for r in cases:
        if not r['full'] or r['multi_z'] or r['full_no_z']:continue
        p,W=r['record'],r['seed'];
        if p!=last:H=graph(ls[p-1]);T=[t for t in inds(H) if t.bit_count()>=5];last=p
        def analyze(C,dom,ends,Z):
            n=len(H);priv=[u for u,v in dom.items() if len(v)==2];labels=[5*n+1+u for u in priv];F=C.copy()
            for u,y in zip(priv,labels):
                a,b=[4*u+1+h for h in dom[u]];F.extend([[-a,-b,y],[-y,a],[-y,b]])
            opts=[]
            for k in range(1,len(priv)+1):
                cn=CardEnc.atmost(labels,k,top_id=6*n);base=F+cn.clauses
                with Solver(name='g4',bootstrap_with=base) as sat:
                    while sat.solve():
                        m=set(sat.get_model());P=[u for u,y in zip(priv,labels) if y in m];assert len(P)==k;sat.add_clause([-(5*n+1+u) for u in P]);S=[e|sum(1<<u for u,hs in dom.items() if h in hs and 4*u+1+h in m) for h,e in enumerate(ends)];verify(grow(H,S),9);dups=[sum(1<<h for h in dom[u]) for u in P];opts.append(dict(bridges=P,masks=dups,ports=S))
                if opts:break
            assert opts;sets=[set(x['bridges']) for x in opts];forced=sorted(set.intersection(*sets));eligible=[u for u in priv if H[u].bit_count()<=6]
            with Solver(name='g4',bootstrap_with=F) as sat:always=[u for u in forced if not sat.solve(assumptions=[-(5*n+1+u)])];possible=[u for u in eligible if sat.solve(assumptions=[5*n+1+u])]
            return dict(k=k,forced=forced,always=always,eligible=eligible,possible=possible,options=opts)
        ans=audit(H,T,W,tab,analyze)
        def topcheck(C,dom,ends,Z):
            with Solver(name='g4',bootstrap_with=C) as sat:
                return [u for u in ans['always'] if all(not sat.solve(assumptions=[-(4*u+h+1)]) for h in dom[u])]
        ans['top_forced']=audit(H,[t for t in T if t.bit_count()==7],W,tab,topcheck);out.append(dict(record=p,seed=W,**ans))
    return out
if __name__=='__main__':
    z=run();print(Counter(r['k'] for r in z),Counter(len(r['options']) for r in z),Counter(len(r['forced']) for r in z));print(Counter(tuple(sorted(Counter(x['masks']).values())) for r in z for x in r['options']));(D/'ramsey_private_bridge_minima.json').write_text(json.dumps(z)+'\n')
