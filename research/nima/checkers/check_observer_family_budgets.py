"""Exact envelope and forward-error regressions, not new observer admission."""
from pathlib import Path
from fractions import Fraction as Q
import runpy
import json

ROOT=Path(__file__).resolve().parents[3]
b=runpy.run_path(str(ROOT/'research/nima/checkers/check_seven_event_factorization_descent.py'))


def main():
    # A genuine homogeneous I^2 source shape used for one-corner witnesses.
    relation=b['chain_product']([b['relation']((0,1),1),b['relation']((2,3),0)])
    assert len(relation)==8
    assert all(len(word)==4 and sum(marks)==1 for word,marks in relation)
    # Scalar unit source coordinates are rational test fixtures only.
    tests=((Q(1),Q(-2),Q(3),Q(0),Q(2)),
           (Q(-3),Q(1),Q(0),Q(4),Q(-1)),
           (Q(2),Q(3),Q(-1),Q(1),Q(5)))
    W=tuple(Q(2**c) for c in range(5))
    M=Q(7)
    envelope=tuple(max(abs(row[c]) for row in tests) for c in range(5))
    identities=0
    for H in range(5):
        tail=range(H,5)
        exact=max(abs(row[c])/W[c] for row in tests for c in tail)
        assert exact==max(envelope[c]/W[c] for c in tail)
        j,c=max(((j,c) for j in range(len(tests)) for c in tail),
                key=lambda jc:abs(tests[jc[0]][jc[1]])/W[jc[1]])
        witness=[Q(0)]*5
        witness[c]=M/W[c]
        assert sum(W[k]*abs(v) for k,v in enumerate(witness))==M
        assert abs(sum(tests[j][k]*v for k,v in enumerate(witness)))==M*exact
        identities+=1
    thresholds=0
    for kappa in range(4):
        for eta in range(1,6):
            for H in range(1,10):
                ratios=[Q(h)**(kappa-eta) for h in range(H+1,H+10)]
                if eta>kappa:assert max(ratios)==Q(H+1)**(kappa-eta)
                elif eta==kappa:assert all(v==1 for v in ratios)
                else:assert ratios[-1]>ratios[0]
                thresholds+=1
    # Model exact response A=identity, finite response diagonal 1-e_c.
    x=(Q(1,8),Q(-1,16),Q(1,32),Q(1,64),Q(-1,128))
    prior=sum(W[c]*abs(x[c]) for c in range(5))
    errors=(Q(1,20),Q(1,30),Q(1,40),Q(1,50),Q(1,60))
    perturb=Q(1,1000);noise=Q(1,2000)
    forward=0
    for H in range(1,5):
        candidate=[x[c]+((-1)**c)*perturb for c in range(H)]
        measured=[(1-errors[c])*candidate[c]+noise for c in range(H)]
        tau=max(envelope[c]/W[c] for c in range(H,5))
        beta=max(envelope[c]*errors[c]/W[c] for c in range(H))
        G=max(envelope[c]*(1-errors[c]) for c in range(H))
        T=max(envelope[c] for c in range(H))
        budget=prior*(tau+beta)+G*H*perturb+T*H*noise
        for row in tests:
            exact=sum(row[c]*x[c] for c in range(5))
            observed=sum(row[c]*measured[c] for c in range(H))
            assert abs(observed-exact)<=budget
            forward+=1
    result={'passed':True,'weighted_envelope_and_attainment_checks':identities,
            'height_threshold_checks':thresholds,'forward_budget_checks':forward,
            'actual_homogeneous_relation_terms':len(relation),
            'scope':'Rational norm fixtures verify the criterion algebra, not growth or descent of an unspecified analytical observer family.'}
    out=ROOT/'research/nima/results/observer-family-budgets.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
