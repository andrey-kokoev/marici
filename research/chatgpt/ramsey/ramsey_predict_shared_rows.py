"""No missing-triple enumeration: domain propagation on three unnamed missing ports. Negate one last-port obligation R by requiring the first |R|-3 slots to hit it (symmetry). Row-capacity propagation to contradiction proves R compulsory."""
from ramsey_capacity_transfer_78 import D,json,decode,inds,bits
from functools import lru_cache
from collections import Counter

def run():
    prev=json.loads((D/'ramsey_unique_five_last_port.json').read_text());drops={r['parent']:r['deleted'] for r in json.loads((D/'ramsey_intrinsic_attachment_basis.json').read_text())};lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for p in sorted({r['parent'] for r in prev}):
        G=decode(lines[p-1]);V=[i for i in range(22) if i!=drops[p]];H=[sum(1<<j for j,y in enumerate(V) if G[x]>>y&1) for x in V];I=inds(H);M=sorted(s for s in I if all(s>>i&1 or s&h for i,h in enumerate(H)));F=(1<<len(M))-1;T=[t for t in I if 4<=t.bit_count()<=6];W=sum(1<<j for j,t in enumerate(T) if t.bit_count()==6);Z=sum(1<<j for j,t in enumerate(T) if t.bit_count()==5);ms=[sum(1<<j for j,t in enumerate(T) if not t&s) for s in M];hit=[sum(1<<j for j,s in enumerate(M) if s&t) for t in T];
        @lru_cache(maxsize=50000)
        def mustmiss(d):
            i=next(bits(d));a=ms[i]
            for j in bits(d^(1<<i)):a&=ms[j]
            return a
        @lru_cache(maxsize=50000)
        def restrict(d,rows):
            for i in bits(rows):
                d&=hit[i]
                if not d:break
            return d
        for r in (r for r in prev if r['parent']==p):
            t=r['t'];j=T.index(t);base=F^hit[j];other=Z^(1<<j);pred=[];surv=F
            for i,s in enumerate(T):
                h=s.bit_count()-3;d=[base&hit[i]]*h+[base]*(3-h)
                while all(d):
                    a,b,c=map(mustmiss,d);new=[restrict(x,((y|z)&W)|(y&z&other)) for x,y,z in zip(d,(b,a,a),(c,c,b))];
                    if new==d:break
                    d=new
                if not all(d):pred.append(s);surv&=hit[i]
            assert len(pred)<=r['shared_rows'] and surv.bit_count()>=r['shared_candidates'];out.append(dict(parent=p,t=t,predicted=pred,candidates=surv.bit_count(),actual_shared=r['shared_rows'],actual_candidates=r['shared_candidates'],extendible=r['extendible']))
        print(p,flush=True)
    return out
if __name__=='__main__':
    z=run();print(sum(len(r['predicted']) for r in z),sum(r['actual_shared'] for r in z),sum(not r['candidates'] for r in z),sum(r['candidates']==r['actual_candidates'] for r in z));(D/'ramsey_predict_shared_rows.json').write_text(json.dumps(z)+'\n')
