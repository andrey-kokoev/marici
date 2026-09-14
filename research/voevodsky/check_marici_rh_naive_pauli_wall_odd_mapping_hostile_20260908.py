#!/usr/bin/env python3
"""Test the simplest normalized Pauli wall/odd domain vectors against Euler orientation."""
import argparse,json,math
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_naive_pauli_wall_odd_mapping_hostile_certificate_20260908.json');args=p.parse_args();a,b,h=s.symbols('a b h',positive=True);I=s.I;checks=0
 D=s.diag(2*b,2*a);sv=s.Matrix([1,1]);dv=s.Matrix([-1,1]);N=s.sqrt(2*(a+b));xw=sv/N;xj=I*dv/(2*N)
 assert s.simplify((xw.conjugate().T*D*xw)[0]-1)==0;checks+=1
 assert s.simplify((xj.conjugate().T*D*xj)[0]-s.Rational(1,4))==0;checks+=1
 cross_source=s.simplify((xw.conjugate().T*D*xj)[0])
 w=s.Matrix([s.Rational(1,2),s.Rational(1,2)]);j=s.Matrix([s.Rational(1,4),-s.Rational(1,4)]);H=s.Matrix([[2,I*h],[-I*h,2]])
 cross_target=s.simplify((w.conjugate().T*H*j)[0])
 assert s.simplify(cross_source-I*(a-b)/(2*(a+b)))==0;checks+=1
 assert s.simplify(cross_target+I*h/4)==0;checks+=1
 required=s.simplify(2*(b-a)/(a+b))
 # p=2 numerical Stieltjes scout values.
 aa=0.637405002217635112636240829881;bb=0.973571176349066980268480987606
 h_geom=float(required.subs({a:aa,b:bb}));h_euler=math.log(2)*2**-.5/(1-2**-.5)
 assert abs(h_geom-h_euler)>1;checks+=1
 out={'schema':'marici.rh.naive-pauli-wall-odd-mapping-hostile.v1','status':'naive_normalized_pauli_mapping_rejected','checks':checks,'domain_wall':'(1,1)/sqrt(2(a+b))','domain_odd':'i(-1,1)/(2sqrt(2(a+b)))','norms':['1','1/4'],'source_cross':'i(a-b)/(2(a+b))','target_cross':'-ih/4','required_orientation':'h=2(b-a)/(a+b)','p2_geometric_h':h_geom,'p2_euler_h':h_euler,'residual':h_euler-h_geom,'claim':'the arbitrary phase choice theta=pi/2 on the norm-matched Pauli difference vector does not reproduce the Euler odd current at p=2','consequence':'endpoint Pauli norms do not select an orientation; the full odd coordinate must come from the independently typed Stokes/Fourier/tail feature','boundary':'the displayed residual is phase-gauge-dependent and must not be treated as an invariant Schur correction'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'p2_geometric_h':h_geom,'p2_euler_h':h_euler,'residual':h_euler-h_geom}))
if __name__=='__main__':main()
