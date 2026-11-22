"""Exact five-row cover after six-set screen. Compare rooted-link certificates with full five-set obligations (a row missed by any three of four ports). Find rows required even in an unrestricted-size certificate, and in every minimum one."""
from ramsey_capacity_transfer_78 import D,json,decode,inds,bits
from pysat.card import CardEnc,EncType
from pysat.solvers import Solver
from collections import Counter

def minimum(patterns,T):
    forced={v.bit_length()-1 for v in patterns if v.bit_count()==1};F=sum(1<<i for i in forced);minimal=[]
    for s in sorted((s for s in patterns if not s&F),key=int.bit_count):
        if all(s&t!=t for t in minimal):minimal.append(s)
    U=sorted({i for s in minimal for i in bits(s)});idx={v:j+1 for j,v in enumerate(U)};C=[[idx[i] for i in bits(s)] for s in minimal];lo=0;hi=len(U)
    def clauses(k):return C+CardEnc.atmost(list(idx.values()),k,encoding=EncType.seqcounter).clauses if U else C
    while lo<hi:
        k=(lo+hi)//2
        with Solver(name='g4',bootstrap_with=clauses(k)) as sat:
            if sat.solve():hi=k
            else:lo=k+1
    with Solver(name='g4',bootstrap_with=clauses(lo)) as sat:
        assert sat.solve();m=set(sat.get_model() or []);extra=[i for i in U if idx[i] in m];always=[i for i in extra if not sat.solve(assumptions=[-idx[i]])]
    cert=forced|set(extra);assert len(extra)==lo and all(any(s>>i&1 for i in cert) for s in patterns);return dict(rows=[T[i] for i in sorted(cert)],forced=[T[i] for i in sorted(forced)],all_min=[T[i] for i in sorted(forced|set(always))])

def run():
    cases=json.loads((D/'ramsey_witness_row_basis.json').read_text());drops={r['parent']:r['deleted'] for r in json.loads((D/'ramsey_bare_core_rank.json').read_text())};lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for r in cases:
        p,A=r['parent'],r['first'];G=decode(lines[p-1]);vs=[i for i in range(22) if i!=drops[p]];H=[sum(1<<j for j,y in enumerate(vs) if G[x]>>y&1) for x in vs];I=inds(H);six=[t for t in I if t.bit_count()==6];T=[t for t in I if t.bit_count()==5];S=[s for s in I if all(s>>v&1 or s&h for v,h in enumerate(H)) and all((s|A)&t for t in six)];miss=lambda s,ts:sum(1<<j for j,t in enumerate(ts) if not t&s);p6=[miss(s,six) for s in S];adj=[sum(1<<j for j in range(i,len(S)) if not x&p6[j]) for i,x in enumerate(p6)];q=[miss(s,T) for s in S];a=miss(A,T);root=set();full=set();num=0
        for i,N in enumerate(adj):
            for j in bits(N):
                for k in bits(N&adj[j]):
                    b,c,d=q[i],q[j],q[k];h=a&((b&c)|(b&d)|(c&d));assert h;root.add(h);full.add(h|(b&c&d));num+=1
        u,v=minimum(root,T),minimum(full,T);out.append(dict(parent=p,first=A,trips=num,root=u,full=v,local=r['triples']));print(p,len(u['rows']),len(v['rows']),len(v['forced']),flush=True)
    return out
if __name__=='__main__':
    z=run();(D/'ramsey_global_five_basis.json').write_text(json.dumps(z)+'\n')
