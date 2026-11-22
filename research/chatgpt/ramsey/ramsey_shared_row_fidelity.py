"""Do learned rows recognize every maximal port multiset? Find smallest exact augmentation holding learned rows fixed, and globally indispensable rows via singleton violations."""
from ramsey_global_five_basis import minimum,D,json,inds,decode,bits
from collections import Counter

def audit(H,warm,basis_solver=None):
    I=inds(H);M=sorted(s for s in I if all(s>>j&1 or s&h for j,h in enumerate(H)));six=[s for s in I if s.bit_count()==6];T=sorted(s for s in I if s.bit_count() in (4,5));is5=sum(1<<i for i,t in enumerate(T) if t.bit_count()==5);warmmask=sum(1<<i for i,t in enumerate(T) if t in warm);p=[sum(1<<j for j,t in enumerate(six) if not s&t) for s in M];miss=[sum(1<<j for j,t in enumerate(T) if not s&t) for s in M];adj=[sum(1<<j for j in range(i,len(M)) if not x&p[j]) for i,x in enumerate(p)];esc=set();forced=0;cnt=Counter();ex=None
    for i,N in enumerate(adj):
        a=miss[i]
        for j in bits(N):
            b=miss[j];N2=N&adj[j];ab=a&b
            for k in bits(N2):
                c=miss[k];three=ab&c;two=(ab|((a|b)&c))&is5
                for l in bits(N2&adj[k]):
                    d=miss[l];v=(three&is5)|(two&d)|(three&d);tag='legal' if not v else 'caught' if v&warmmask else 'escape';cnt[tag]+=1
                    if v and not v&(v-1):forced|=v
                    if tag=='escape':
                        esc.add(v)
                        if ex is None:ex=dict(ports=[M[x] for x in (i,j,k,l)],violations=[T[x] for x in bits(v)])
    if basis_solver is not None:return basis_solver(esc,T)
    aug=minimum(esc,T)['rows'];assert all(any(v>>T.index(t)&1 for t in aug) for v in esc);return dict(counts=cnt,warm=len(warm),extra=aug,forced=[T[i] for i in bits(forced)],forced_learned=(warmmask&forced).bit_count(),example=ex)

def run():
    prev=json.loads((D/'ramsey_blind_row_builder.json').read_text());lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for r in prev:
        G=decode(lines[r['parent']-1]);V=[i for i in range(22) if i!=r['deleted']];H=[sum(1<<j for j,y in enumerate(V) if G[x]>>y&1) for x in V];out.append(dict(parent=r['parent'],deleted=r['deleted'],**audit(H,{t for s in r['warm'] for t in s['learned']})))
    return out
if __name__=='__main__':
    z=run();print(sum((r['counts'] for r in z),Counter()),Counter(len(r['extra']) for r in z));print(sum(len(r['forced']) for r in z),sum(r['forced_learned'] for r in z));(D/'ramsey_shared_row_fidelity.json').write_text(json.dumps(z)+'\n')
