#!/usr/bin/env python3
"""Classify reciprocal-invariant three-port Green forms with overlap radical."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_relative_three_port_green_classification_certificate_20260908.json');args=p.parse_args();a,c,lo,le=s.symbols('a c lambda_odd lambda_even',real=True);checks=0
 G=s.Matrix([[a,-a-c,c],[-a-c,a,c],[c,c,-2*c]])
 r=s.Matrix([1,1,1]);v=s.Matrix([1,-1,0]);u=s.Matrix([1,1,-2]);S=s.Matrix([[0,1,0],[1,0,0],[0,0,1]])
 assert G*r==s.zeros(3,1);checks+=1
 assert S.T*G*S==G;checks+=1
 assert s.simplify(G*v-(2*a+c)*v)==s.zeros(3,1);checks+=1
 assert s.simplify(G*u-(-3*c)*u)==s.zeros(3,1);checks+=1
 sol={c:-le/3,a:lo/2+le/6};Gnorm=s.simplify(G.subs(sol))
 assert s.simplify(Gnorm*v-lo*v)==s.zeros(3,1);checks+=1
 assert s.simplify(Gnorm*u-le*u)==s.zeros(3,1);checks+=1
 assert Gnorm*r==s.zeros(3,1);checks+=1
 out={'schema':'marici.rh.relative-three-port-green-classification.v1','status':'classified_up_to_even_odd_energies','checks':checks,'basis':['F_in','F_out','W_const'],'overlap_radical':'span(1,1,1)','reciprocal_action':'swap F_in and F_out; fix W_const','general_matrix':[[str(e) for e in G.row(i)] for i in range(3)],'odd_vector':'(1,-1,0), eigenvalue 2a+c','even_vector':'(1,1,-2), eigenvalue -3c','normalized_matrix':[[str(e) for e in Gnorm.row(i)] for i in range(3)],'positivity':'lambda_odd>=0 and lambda_even>=0','claim':'overlap conservation plus reciprocal invariance reduce the relative Green form to two energies; fixing source even and odd energies determines it uniquely','boundary':'the source identification of lambda_even and lambda_odd with the fixed theta wall and odd history norms remains to be proved'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'free_parameters':['lambda_even','lambda_odd']}))
if __name__=='__main__':main()
