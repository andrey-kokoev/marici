#!/usr/bin/env python3
"""Show that the apparent Pauli endpoint orientation is a rephasing gauge artifact."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_pauli_endpoint_orientation_gauge_hostile_certificate_20260908.json');args=p.parse_args();a,b,theta=s.symbols('a b theta',real=True,positive=True);I=s.I;checks=0
 D=s.diag(2*b,2*a);sv=s.Matrix([1,1]);dv=s.Matrix([-1,1]);N=s.sqrt(2*(a+b));xw=sv/N;xj=s.exp(I*theta)*dv/(2*N)
 nw=s.simplify((xw.conjugate().T*D*xw)[0]);nj=s.simplify((xj.conjugate().T*D*xj)[0]);cross=s.simplify((xw.conjugate().T*D*xj)[0])
 assert nw==1 and nj==s.Rational(1,4);checks+=2
 expected=s.exp(I*theta)*(a-b)/(2*(a+b));assert s.simplify(cross-expected)==0;checks+=1
 assert s.simplify(cross.subs(theta,0)-(a-b)/(2*(a+b)))==0;checks+=1
 assert s.simplify(cross.subs(theta,s.pi/2)-I*(a-b)/(2*(a+b)))==0;checks+=1
 assert s.simplify(cross.subs(theta,-s.pi/2)+I*(a-b)/(2*(a+b)))==0;checks+=1
 out={'schema':'marici.rh.pauli-endpoint-orientation-gauge-hostile.v1','status':'endpoint_orientation_baseline_withdrawn','checks':checks,'rephased_odd_vector':'x_j(theta)=e^(i theta)(-1,1)/(2sqrt(2(a+b)))','fixed_norms':['||x_w||^2=1','||x_j(theta)||^2=1/4'],'mixed_pairing':'e^(i theta)(a-b)/(2(a+b))','claim':'the imaginary cross previously called h_Pauli is created by an arbitrary phase choice and is not an invariant orientation supplied by the Pauli endpoint Gram','consequence':'do not subtract h_Pauli from the Euler odd current; the full Euler orientation must come from the independently typed Stokes/Fourier/tail constructor','supersedes':'the residual interpretation in check_marici_rh_naive_pauli_wall_odd_mapping_hostile_20260908.py; that checker remains a hostile to the chosen theta=pi/2 mapping only','boundary':'a source quarter-turn can fix theta, but that authority is external to the Pauli norm'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'mixed_phase_is_free':True}))
if __name__=='__main__':main()
