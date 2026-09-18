#!/usr/bin/env python3
"""Exact algebraic celestial map and physical-real-slice obstruction."""
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/'research/nima'))
import sympy as s
from dual_spinor_kinematics import momentum_conserving_kinematics
rows=[]
for n in range(6,13):
 lam,til,x=momentum_conserving_kinematics([(1,j*j+j+1) for j in range(1,n+1)],[(1,j**3+2*j+1) for j in range(1,n-1)])
 legs=[];recon=True
 for i in range(1,n+1):
  z=s.factor(lam[i][1]/lam[i][0]);zb=s.factor(til[i][1]/til[i][0]);omega=s.factor(lam[i][0]*til[i][0]);p=lam[i]*til[i].T;pc=omega*s.Matrix([[1,zb],[z,z*zb]]);recon &= s.simplify(p-pc)==s.zeros(2);legs.append((omega,z,zb))
 psum=sum((lam[i]*til[i].T for i in range(1,n+1)),s.zeros(2));real_positive=all(v[0].is_real is True and v[0]>0 and s.conjugate(v[1])==v[2] for v in legs)
 rows.append({'n':n,'exact_reconstruction':bool(recon),'momentum_conservation':psum==s.zeros(2),'physical_real_positive_slice':bool(real_positive),'nonpositive_energy_legs':sum(not (w.is_real is True and w>0) for w,z,zb in legs),'reality_mismatch_legs':sum(s.conjugate(z)!=zb for w,z,zb in legs)})
checks={'exact_complex_celestial_map':all(r['exact_reconstruction'] for r in rows),'momentum_conserved':all(r['momentum_conservation'] for r in rows),'test_kinematics_not_physical_real_slice':all(not r['physical_real_positive_slice'] for r in rows)}
out={'schema':'marici.nima.spinor-to-celestial-generator-map.v1','map':'lambda=(lambda0,lambda1), tilde=(t0,t1) -> omega=lambda0*t0, z=lambda1/lambda0, zbar=t1/t0','reconstruction':'p=lambda tilde^T=omega [[1,zbar],[z,z*zbar]]','rows':rows,'checks':checks,'passed':all(checks.values()),'conclusion':'A source-derived algebraic map exists to complexified celestial momentum data and preserves momentum conservation. The exact rational fixtures do not lie on the positive-energy Lorentzian real slice, so they do not define physical Bondi radiative generators.','additional_missing_data':['external helicity assignment for the extracted component','Bondi shear/news normalization','radiative symplectic form','soft-frequency family approaching omega=0','cluster-dependent chain map beyond the common external-leg configuration'],'claim_boundary':'This is a kinematic map for external legs, constant across history/cluster generators. It is not a map to physical null-infinity phase space.'};p=ROOT/'research/nima/results/spinor-to-celestial-generator-map.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
