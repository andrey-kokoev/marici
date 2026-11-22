"""Held-out catalogue cores: six fixed pairs from first saved valid attachment per core. Compute all legal thirds (not just maximal), and exact singleton/pair-obligation coverage of impossible maximal thirds."""
from itertools import combinations
from ramsey_capacity_transfer_78 import decode,D,json,inds,bits
from statistics import median

def run():
    cat=json.loads((D/'ramsey_capacity_transfer_78.json').read_text())['catalogue'];exclude={r['record'] for r in json.loads((D/'ramsey_sat_learning_batch.json').read_text())};lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for idx,r in enumerate(cat,1):
        if idx in exclude or 'valid' not in r['examples']:continue
        H=decode(lines[idx-1]);n=len(H);I=sorted(inds(H));M=[s for s in I if all(s>>i&1 or s&h for i,h in enumerate(H))];F=(1<<len(I))-1;cols=[sum(1<<j for j,s in enumerate(I) if s>>i&1) for i in range(n)];T=[s for s in I if s.bit_count()>=4];hit={}
        for t in T:
            mask=0
            for i in bits(t):mask|=cols[i]
            hit[t]=mask
        maxbits=sum(1<<I.index(m) for m in M);S=r['examples']['valid']['supports']
        for a,b in sorted({tuple(sorted(q)) for q in combinations(S,2)}):
            req=[];each=F
            for t in T:
                z=7-t.bit_count()-int(not a&t)-int(not b&t);assert z>=0
                if not z:each&=hit[t]
                elif z==1:req.append(t)
            feasible=0
            for i in bits(each&maxbits):
                fourth=I[i];thirds=each
                for t in req:
                    if not fourth&t:thirds&=hit[t]
                feasible|=thirds
            assert feasible;bad=maxbits&~feasible;sing=both=0;obs=[]
            for i,c in enumerate(cols):
                if not feasible&~c:sing|=bad&~c;obs.append([i])
            both=sing
            for i,j in combinations(range(n),2):
                c=cols[i]|cols[j]
                if not feasible&~c:both|=bad&~c;obs.append([i,j])
            out.append(dict(record=idx,pair=[a,b],bad=bad.bit_count(),one=sing.bit_count(),two=both.bit_count(),good=feasible.bit_count(),obligations=obs))
    return out
if __name__=='__main__':
    z=run();print(len(set(r['record'] for r in z)),len(z),[sum(r[k] for r in z) for k in ['bad','one','two']],sum(2*r['two']>r['bad'] for r in z));r=min(z,key=lambda r:r['two']/r['bad']);print({k:v for k,v in r.items() if k!='obligations'});(D/'ramsey_small_obligation_holdout.json').write_text(json.dumps(z)+'\n')
