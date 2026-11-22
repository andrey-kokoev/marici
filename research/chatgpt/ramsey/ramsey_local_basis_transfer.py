"""Evaluate saved twelve-choice certificates away from their witnesses. Condition on ALL six-set compatibility tests, then count partner multisets surviving the selected rows. Compare uniform random eligible row sets matched by row size."""
from ramsey_capacity_transfer_78 import D,json,decode,inds,bits
from random import Random
from statistics import median

def run():
    cases=json.loads((D/'ramsey_witness_row_basis.json').read_text());drops={r['parent']:r['deleted'] for r in json.loads((D/'ramsey_bare_core_rank.json').read_text())};lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[];rng=Random(102919)
    for r in cases:
        p,A=r['parent'],r['first'];G=decode(lines[p-1]);vs=[i for i in range(22) if i!=drops[p]];H=[sum(1<<j for j,y in enumerate(vs) if G[x]>>y&1) for x in vs];I=inds(H);W=set(r['witness']);six=[t for t in I if t.bit_count()==6];S=[s for s in I if all(s>>v&1 or s&h for v,h in enumerate(H)) and all((s|A)&t for t in six)];n=len(S);F=(1<<n)-1;assert W<=set(S);inside=sum(1<<i for i,s in enumerate(S) if s in W);five=[t for t in I if t.bit_count()==5 and not A&t];col={t:sum(1<<i for i,s in enumerate(S) if not s&t) for t in six+five};
        def graph(rows,base):
            adj=list(base)
            for t in rows:
                m=col[t]
                for i in bits(m):adj[i]&=~m
            return adj
        def count(adj):
            hist=[0]*4
            for i,N in enumerate(adj):
                for j in bits(N&~((1<<i)-1)):
                    K=N&adj[j]&~((1<<j)-1);z=int(S[i] in W)+int(S[j] in W);hist[z]+=(K&~inside).bit_count();hist[z+1]+=(K&inside).bit_count()
            return hist
        raw=[F]*n;pair=graph(six,raw);cert=r['triples'];left=count(graph(cert,pair));assert left[3]==0 and not any(count(graph(five,pair)));alts=[]
        for t in cert:
            same=[u for u,h in col.items() if u.bit_count()==t.bit_count() and h&inside==col[t]&inside];alts.append(max(same,key=lambda u:(col[u].bit_count(),-u)))
        eligible=[t for t in five if col[t].bit_count()>=1];k=sum(t.bit_count()==5 for t in cert);random_left=[count(graph(rng.sample(eligible,k),pair))[0] for _ in range(24)];out.append(dict(parent=p,first=A,raw=count(raw),screen=count(pair),local=left,substitutes=alts,swapped=count(graph(alts,pair)),random_left=random_left,unconditional=count(graph(cert,raw))))
    return out
if __name__=='__main__':
    z=run();(D/'ramsey_local_basis_transfer.json').write_text(json.dumps(z)+'\n');print({k:[sum(r[k][i] for r in z) for i in range(4)] for k in ('raw','unconditional','screen','local','swapped')});print(sum(median(r['random_left']) for r in z),sum(r['local'][0]<median(r['random_left']) for r in z),sum(not r['local'][0] for r in z));print(sum(r['swapped'][0]<r['local'][0] for r in z),sum(r['swapped'][0]>r['local'][0] for r in z))
