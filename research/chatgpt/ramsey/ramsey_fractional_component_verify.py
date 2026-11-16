"""Integer-verifiable fractional exclusion certificates for each exactly
isomorphism-distinct graph in a closed edge-rewiring component.
No claim this component equals McKay's complete 2,576 graph catalogue.
"""
from itertools import combinations
from pathlib import Path
import json
import numpy as np
from scipy.optimize import linprog
from ramsey_fractional_port_certificate import independent_fives,verify

SRC=Path('/mnt/data/ramsey_port_rewire_components_results.json')
DST=Path('/mnt/data/ramsey_fractional_component_certificates.json')

def find(A,den=1000):
 F=independent_fives(A)
 M=np.array([[(f&g)==0 for f in F] for g in F],dtype=np.uint8)
 fit=linprog(-np.ones(len(F)),A_ub=M,b_ub=np.ones(len(F)),bounds=(0,None),method='highs')
 assert fit.success,(fit.status,fit.message)
 y=-fit.ineqlin.marginals
 y=np.where(y>1e-9,np.ceil(y*den+1e-7),0).astype(np.int64)
 weights={str(F[j]):int(y[j]) for j in range(len(F)) if y[j]>0}
 res=verify(A,weights,den)
 return {'A':A,'denominator':den,'weights':weights,'lp_numeric':-fit.fun,'checks':res}

def main():
 source=json.loads(SRC.read_text())
 assert source['closed'] and source['isoclasses']==39
 checks=[find(g[2]) for g in source['details']]
 maxw=max(sum(c['weights'].values())/c['denominator'] for c in checks)
 print('All',len(checks),'exact rational certificates passed; maximum rounded weight',maxw)
 obj={'description':'verified 39-class rewiring-closed union, NOT exhaustive McKay catalogue','classes':len(checks),'max_rational_weight':maxw,'certificates':checks}
 DST.write_text(json.dumps(obj,indent=2))
 print(DST)

if __name__=='__main__':main()
