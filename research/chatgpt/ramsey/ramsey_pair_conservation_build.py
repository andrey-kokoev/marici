"""Generate exact signed-pair incidence obstruction certificates on all 39 R(3,6;16,33) residuals.
Requires numpy/scipy for finding candidate coefficients. Verification is independent in companion standard-library script.
"""
from collections import Counter
from itertools import combinations
from pathlib import Path
from math import floor
import numpy as np
from scipy.optimize import linprog
import json
from ramsey_r37_full_catalogue_audit import data_rows,decode_graph6,indep_sets,EXPECTED_SHA

CAT='/mnt/data/r36_16.g6.gz'
Q=10**7
R=10**6
positive_duals=[]
records=[]
for index, row in enumerate(data_rows(CAT),1):
    H=decode_graph6(row)
    if sum(x.bit_count() for x in H)!=66: continue
    F=indep_sets(H,5)
    pairs=[(u,v) for u,v in combinations(range(16),2) if not ((H[u]>>v)&1)]
    assert len(pairs)==87
    P=np.array([[(I>>u&1) and (I>>v&1) for u,v in pairs] for I in F],dtype=np.int64)
    D=np.array([[(I&T)==0 for I in F] for T in F],dtype=np.int64)
    B=D@P
    counts=P.sum(axis=0)
    posres=linprog(counts,A_ub=-B,b_ub=-np.ones(len(F)),bounds=(0,None),method='highs')
    assert posres.success
    res=linprog(counts,A_ub=np.vstack([-B,-P]),b_ub=np.r_[-np.ones(len(F)),np.zeros(len(F))],
                bounds=[(None,None)]*len(pairs),method='highs')
    assert res.success and res.fun<6-1e-6,(index,res.message,res.fun)
    # Round to Q-scale and add +1 to every pair weight; every 5-set has 10 independent pairs,
    # hence all resulting 5-set weights are strictly positive even after signed rounding.
    coeff=[int(round(float(x)*Q))+1 for x in res.x]
    z=P@np.asarray(coeff,dtype=np.int64)
    coverage=D@z
    m=int(coverage.min()); W=int(z.sum()); gap=6*m-W
    assert min(z)>=0 and m>0 and gap>0,(index,int(min(z)),m,gap)
    records.append({'source_index':index,'graph6':row.decode(),
       'signed_pair_coefficients':{f'{u},{v}':c for (u,v),c in zip(pairs,coeff) if c!=0},
       'pair_scale':Q,'min_five_weight':int(z.min()),'min_coverage':m,'total_weight':W,'exact_margin':gap,
       'mass_ratio':W/m,'lp_numerical':float(res.fun),'positive_pair_lp':float(posres.fun)})
    if posres.fun >=6+1e-7:
        dual=linprog(-np.ones(len(F)),A_ub=B.T,b_ub=counts,bounds=(0,None),method='highs')
        assert dual.success and abs(-dual.fun-posres.fun)<1e-6
        # Since B has only nonnegative counts, downward rounding preserves B.T @ x <= counts.
        w=np.array([max(0,int(floor(float(x)*R-1e-7))) for x in dual.x],dtype=np.int64)
        assert int(w.sum())>6*R,(index,int(w.sum()),6*R)
        assert (B.T@w<=counts*R).all()
        positive_duals.append({'source_index':index,'graph6':row.decode(),'denominator':R,
            'dual_weights':{str(F[i]):int(x) for i,x in enumerate(w) if x>0},
            'numerator':int(w.sum()),'objective':int(w.sum())/R})
    print(index,len(F),'signed',round(W/m,8),'pos',round(posres.fun,8),'gap',gap,'duality?',len(positive_duals),flush=True)
assert len(records)==39
assert len(positive_duals)==6, len(positive_duals)
root=Path('/mnt/data')
(root/'ramsey_pair_conservation_certificates.json').write_text(json.dumps({'dataset_sha256':EXPECTED_SHA,'pair_scale':Q,
  'records':records,'nonnegative_pair_duality_obstructions':positive_duals},indent=2)+'\n')
print('VERIFIED 39 signed / 6 nonnegative-pair impossible', 'maxmass',max(x['mass_ratio'] for x in records),
      'minmargin', min(x['exact_margin'] for x in records))
