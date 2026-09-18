#!/usr/bin/env python3
"""Bounded numerical search for positive preimages of history-2 B/alpha2 target point."""
from pathlib import Path
import json,numpy as np
from scipy.optimize import least_squares
ROOT=Path(__file__).resolve().parents[3];Z=np.array([[float(t**k) for k in range(6)] for t in range(1,9)])
def target(logv):
 a1,a3,a4,a5,a6,a7,a8=np.exp(logv);C=np.array([[1,a1,0,a3+a4,a4*a5,a4*a6,a4*a7,0],[0,0,0,1,a5,a6,a7,a8]],float);Y=C@Z;P=Y[:,[0,1]];N=np.linalg.solve(P,Y);return np.array([N[i,j] for i in range(2) for j in range(2,6)])[:7]
base=np.array([2,5,7,11,13,17,19.]);truth=np.log(base);goal=target(truth);rng=np.random.default_rng(1729);sol=[];residuals=[]
for trial in range(32):
 x0=truth if trial==0 else truth+rng.normal(0,1.5,7);x0=np.clip(x0,-5.9,5.9);r=least_squares(lambda x:target(x)-goal,x0,bounds=(-6,6),max_nfev=500,xtol=1e-12,ftol=1e-12,gtol=1e-12)
 residuals.append(float(np.linalg.norm(r.fun)))
 if residuals[-1]<1e-8 and np.all(np.abs(r.x)<30):
  v=np.exp(r.x)
  if not any(np.linalg.norm(np.log(v/w))<1e-5 for w in sol):sol.append(v)
checks={'known_solution_recovered':any(np.linalg.norm(np.log(v/base))<1e-5 for v in sol),'all_converged_positive_solutions_one_cluster':len(sol)==1,'best_residual_below_1e_10':min(residuals)<1e-10};out={'schema':'marici.nima.n8-singleton-B2-positive-fiber-search.v1','starts':32,'converged_starts':sum(r<1e-8 for r in residuals),'positive_solution_clusters':len(sol),'solutions':[v.tolist() for v in sol],'best_residual':min(residuals),'checks':checks,'passed':all(checks.values()),'claim_boundary':'Bounded numerical hostile only. Failure to find another positive preimage is not a proof of positive injectivity or algebraic degree one.'};p=ROOT/'research/nima/results/n8-singleton-B2-positive-fiber-search.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
