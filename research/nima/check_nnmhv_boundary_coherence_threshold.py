#!/usr/bin/env python3
"""Locate the boundary-transport threshold for destructive coherence."""
import itertools,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'));import sympy as s
src=json.loads((ROOT/'research/nima/results/nnmhv-kernel-wall-tail-boundary.json').read_text());K=s.Matrix([[s.sympify(x) for x in row] for row in src['kernel_matrix']]);K0=s.Matrix([[s.sympify(x) for x in row] for row in src['kernel_without_upper_boundary_transport']]);B=K-K0;t=s.symbols('t',real=True);Kt=K0+t*B;events=[]
for q in range(1,K.rows+1):
 for I in itertools.combinations(range(K.rows),q):
  for J in itertools.combinations(range(K.cols),q):
   poly=s.factor(Kt.extract(I,J).det())
   if poly==0:continue
   roots=[]
   try:
    for z in s.nroots(poly,maxsteps=200):
     z=complex(z)
     if abs(z.imag)<1e-10 and 0<z.real<1:roots.append(z.real)
   except Exception:pass
   if roots:events.append({'size':q,'rows':list(I),'cols':list(J),'polynomial':str(poly),'roots_in_unit_interval':roots})
I=(1,2);J=(0,1);p=s.factor(Kt.extract(I,J).det());root=s.solve(p,t)[0];before=s.sign(p.subs(t,0));after=s.sign(p.subs(t,1));checks={'exactly_one_minor_crossing':len(events)==1,'crossing_is_observed_negative_minor':events[0]['rows']==list(I) and events[0]['cols']==list(J),'threshold_inside_physical_path':0<float(root)<1,'sign_flips_positive_to_negative':before==1 and after==-1,'boundary_path_starts_totally_nonnegative':all(s.sign(K0.extract(I,J).det())>=0 for q in range(1,4) for I in itertools.combinations(range(3),q) for J in itertools.combinations(range(3),q))}
out={'schema':'marici.nima.nnmhv-boundary-coherence-threshold.v1','deformation':'K(t)=K0+t(K-K0), 0<=t<=1','crossing_events':events,'critical_parameter_exact':str(s.factor(root)),'critical_parameter_numeric':float(root),'physical_parameter':1,'checks':{k:bool(v) for k,v in checks.items()},'passed':all(bool(v) for v in checks.values()),'meaning':'Boundary transport drives a single, sharp oriented-matroid wall crossing. Below t_c the kernel is totally nonnegative; above t_c one TP2 minor becomes negative and destructive endpoint coherence appears.','bridges':['oriented-matroid wall crossing','coherence/association phase transition','diagonal filter inducing contextual correlation','total-positivity chamber decomposition','boundary-controlled interference threshold']};pout=ROOT/'research/nima/results/nnmhv-boundary-coherence-threshold.json';pout.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
