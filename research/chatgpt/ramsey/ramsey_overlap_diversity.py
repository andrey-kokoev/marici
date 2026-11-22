"""Exact diversity hierarchy on nonregular cores; separate existence of DISJOINT valid nonmaximal supports by SAT (maximal enlargement need not preserve disjointness). Minimize number of old vertices carrying multiple colors."""
from ramsey_capacity_transfer_78 import D,json,inds,bits,decode,verify,grow,Counter,combinations
from pysat.card import CardEnc
from pysat.solvers import Solver

def run():
    lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();cat=json.loads((D/'ramsey_capacity_transfer_78.json').read_text())['catalogue'];out=[]
    for idx,line in enumerate(lines,1):
        H=decode(line);n=len(H)
        if all(h.bit_count()==6 for h in H):continue
        I=inds(H);M=[s for s in I if all(s>>i&1 or s&h for i,h in enumerate(H))];T={k:[t for t in I if t.bit_count()==k] for k in (4,5,6)};w,q,p=([sum(1<<i for i,t in enumerate(T[k]) if not s&t) for s in M] for k in (4,5,6));adj=[sum(1<<j for j in range(i,len(M)) if not a&p[j]) for i,a in enumerate(p)];ct=[0,0,0,0];minmax=None;cap=[sum(1<<v for v,h in enumerate(H) if h.bit_count()>=k) for k in (4,5,6)]
        for i,N in enumerate(adj):
            for j in bits(N):
                common=N&adj[j];ab=M[i]&M[j];ij=q[i]&q[j]
                for k in bits(common):
                    tails=common&adj[k];ct[0]+=tails.bit_count();abc=ab&M[k];twice=ab|((M[i]|M[j])&M[k]);ban=(abc&cap[0])|(twice&cap[1]);ban5=ij|((q[i]|q[j])&q[k]);ban4=w[i]&w[j]&w[k]
                    for l in bits(tails):
                        if abc&cap[1] or M[l]&ban:continue
                        ct[1]+=1
                        if ij&q[k] or ban5&q[l]:continue
                        ct[2]+=1
                        if ban4&w[l]:continue
                        ct[3]+=1;c=(twice|((M[i]|M[j]|M[k])&M[l])).bit_count();minmax=c if minmax is None else min(c,minmax)
        assert ct[3]==cat[idx-1]['counts'].get('valid',0);row=dict(record=idx,counts=ct,maximal_min=minmax)
        if ct[3]:
            C=[[-(i+n*k+1),-(j+n*k+1)] for i,j in combinations(range(n),2) if H[i]>>j&1 for k in range(4)]
            for k,ts in T.items():
                for t in ts:
                    for ps in combinations(range(4),8-k):C.append([1+s*n+i for s in ps for i in bits(t)])
            labels=[4*n+i+1 for i in range(n)];C.extend([-(1+a*n+i),-(1+b*n+i),labels[i]] for a,b in combinations(range(4),2) for i in range(n))
            for cost in range(minmax+1):
                with Solver(name='g4',bootstrap_with=C+CardEnc.atmost(labels,cost).clauses) as sat:
                    if not sat.solve():continue
                    m=set(sat.get_model());S=[sum(1<<i for i in range(n) if 1+i+n*k in m) for k in range(4)];verify(grow(H,S),8);assert sum(sum(s>>i&1 for s in S)>1 for i in range(n))==cost;row.update(true_min=cost,witness=S);break
            assert 'true_min' in row
        out.append(row)
    return out
if __name__=='__main__':
    z=run();print([[sum(r['counts'][i] for r in z),sum(r['counts'][i]>0 for r in z)] for i in range(4)]);print(Counter((r['maximal_min'],r['true_min']) for r in z if 'true_min' in r));(D/'ramsey_overlap_diversity.json').write_text(json.dumps(z)+'\n')
