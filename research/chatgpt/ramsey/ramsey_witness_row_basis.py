"""Exact minimum old-row bases: preserve every conflict edge vs merely refute every triple of a selected 12-partner witness. Compare with unrestricted incompatible families."""
from ramsey_capacity_transfer_78 import D,json,decode,inds,bits
from itertools import combinations
from pysat.solvers import Solver
from pysat.card import CardEnc,EncType
from collections import Counter

def basis(cols,U,need):
    cols=list(cols);effects={sum(1<<i for i,s in enumerate(U) if (s&c).bit_count()>=need):c for c in cols};F=(1<<len(U))-1;cs=[]
    for e in sorted(effects,key=int.bit_count,reverse=True):
        if e and all(e&h!=e for h in cs):cs.append(e)
    C=[[j+1 for j,e in enumerate(cs) if e>>i&1] for i in range(len(U))];lo=0;hi=len(cs)
    while lo<hi:
        k=(lo+hi)//2;card=CardEnc.atmost(list(range(1,len(cs)+1)),k,encoding=EncType.seqcounter)
        with Solver(name='g4',bootstrap_with=C+card.clauses) as sat:
            if sat.solve():hi=k
            else:lo=k+1
    card=CardEnc.atmost(list(range(1,len(cs)+1)),lo,encoding=EncType.seqcounter)
    with Solver(name='g4',bootstrap_with=C+card.clauses) as sat:
        assert sat.solve();model=set(sat.get_model());sel=[effects[e] for j,e in enumerate(cs,1) if j in model];assert len(sel)==lo and all(any((c&s).bit_count()>=need for c in sel) for s in U);return sel

def run():
    links=json.loads((D/'ramsey_common_partner_pattern.json').read_text())['hosts'];hard=json.loads((D/'ramsey_uniform_partner_search.json').read_text());drops={r['parent']:r['deleted'] for r in json.loads((D/'ramsey_bare_core_rank.json').read_text())};lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for r,h in zip(links,hard):
        p,A=r['parent'],r['first'];assert (p,A)==(h['parent'],h['first']);V=r['original'].get('0',h['witness']);G=decode(lines[p-1]);vs=[i for i in range(22) if i!=drops[p]];H=[sum(1<<j for j,y in enumerate(vs) if G[x]>>y&1) for x in vs];rows=[t for t in inds(H) if t.bit_count()==6 or t.bit_count()==5 and not t&A];cols={sum(1<<i for i,s in enumerate(V) if not t&s):t for t in rows};pairs=[(1<<i|1<<j) for i,j in combinations(range(12),2) if any(not (1<<i|1<<j)&~c for c in cols)];trip=[sum(1<<i for i in u) for u in combinations(range(12),3)];graphcols=[s for s in range(1<<12) if 2<=s.bit_count()<=4 and all((1<<i|1<<j) in pairs for i,j in combinations(bits(s),2))];res={}
        for tag,univ in [('pairs',pairs),('triples',trip)]:
            res[tag]=[cols[c] for c in basis(cols,univ,2)];res['ideal_'+tag]=basis(graphcols,univ,2)
        out.append(dict(parent=p,first=A,P=bool(r['original']),witness=V,**res));print(p,[len(s) for s in res.values()],flush=True)
    return out
if __name__=='__main__':
    z=run();(D/'ramsey_witness_row_basis.json').write_text(json.dumps(z)+'\n');print(Counter((r['P'],len(r['pairs']),len(r['triples'])) for r in z))
