"""Bare-core fractional port supply for target (3,8). Maximize total multiplicity of maximal independent supports subject to miss budgets. For deciding four ports only rows of sizes 4..6 matter. Rational primal/dual bounds for the truncated capacity; cap at 4 when interpreting a positive test."""
from ramsey_capacity_transfer_78 import D,json,inds,decode
from ramsey_fractional_partner_barrier import Q,np,linprog,Counter

def run():
    src=json.loads((D/'ramsey_capacity_transfer_78.json').read_text())['catalogue'];lines=(D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines();out=[]
    for idx,line in enumerate(lines,1):
        H=decode(line);I=inds(H);M=sorted(s for s in I if all(s>>v&1 or s&h for v,h in enumerate(H)));T=[t for t in I if 4<=t.bit_count()<=6];B=[7-t.bit_count() for t in T];mat=np.array([[int(not t&s) for s in M] for t in T]);lp=linprog(-np.ones(len(M)),A_ub=mat,b_ub=B,method='highs');assert lp.success;rat=lambda f:Q(float(f)).limit_denominator(100000);x={s:rat(w) for s,w in zip(M,lp.x) if w>1e-8};y={t:rat(-w) for t,w in zip(T,lp.ineqlin.marginals) if w< -1e-8};
        # Integer floor/ceil at high precision for rigorous threshold bounds away from exact 4.
        from math import ceil,floor
        if abs(-lp.fun-4)>1e-7:
            x={s:Q(floor(float(w)*10**7),10**7) for s,w in x.items()};y={t:Q(ceil(float(w)*10**7),10**7) for t,w in y.items()}
        sx=max(sum(w for s,w in x.items() if not t&s)/Q(b) for t,b in zip(T,B));sy=min(sum(w for t,w in y.items() if not t&s) for s in M);lo=sum(x.values())/sx;hi=sum((7-t.bit_count())*w for t,w in y.items())/sy;ok=bool(src[idx-1]['counts'].get('valid'));assert lo>=4 or hi<4 or ok;assert not ok or hi>=4;out.append(dict(record=idx,legal=ok,lower=str(lo),upper=str(hi),objective=-lp.fun,price={t:str(w/sy) for t,w in y.items()} if hi<4 else None));
        if idx%25==0:print(idx,flush=True)
    return out
if __name__=='__main__':
    z=run();(D/'ramsey_core_fractional_supply.json').write_text(json.dumps(z)+'\n');print(Counter((r['legal'],Q(r['upper'])<4) for r in z));print(min(r['objective'] for r in z),max(r['objective'] for r in z))
