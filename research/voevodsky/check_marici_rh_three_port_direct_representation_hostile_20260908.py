#!/usr/bin/env python3
"""Show the normalized three-port form cannot directly equal a general endpoint Gram."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_three_port_direct_representation_hostile_certificate_20260908.json');args=p.parse_args();a,b,c,h=s.symbols('a b c h',real=True);I=s.I;checks=0
 Graw=s.Matrix([[a,c+I*h],[c-I*h,b]])
 H=s.Matrix([[2,I*h],[-I*h,2]])
 diff=s.simplify(Graw-H)
 assert diff==s.Matrix([[a-2,c],[c,b-2]]);checks+=1
 sol=s.solve([a-2,b-2,c],[a,b,c],dict=True)
 assert sol==[{a:2,b:2,c:0}];checks+=1
 X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,I],[-I,0]])
 pauli=s.simplify(X*Graw*X+Y*Graw*Y)
 assert pauli==s.diag(2*b,2*a);checks+=1
 # The Pauli sum erases both c and h, so orientation must remain in separately
 # typed outputs or in a Schur-return cell.
 assert all(not entry.has(c,h) for entry in pauli);checks+=1
 out={'schema':'marici.rh.three-port-direct-representation-hostile.v1','status':'direct_gram_identification_rejected','checks':checks,'raw_endpoint_gram':'[[a,c+ih],[c-ih,b]]','normalized_three_port_quotient':'[[2,ih],[-ih,2]]','equality_conditions':['a=2','b=2','c=0'],'pauli_sum':'diag(2b,2a)','claim':'the normalized three-port quotient cannot directly represent the prime-dependent raw Stieltjes endpoint Gram except in a special nongeneric case','consequence':'the three-port matrix is an oriented auxiliary/Schur target; the quadratic theorem must pass through the two-output Pauli dilation and retain its outputs separately','boundary':'the hostile does not rule out a prime-dependent typed embedding or uniformly equivalent comparison after Pauli dilation'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'pauli_sum':'diag(2b,2a)'}))
if __name__=='__main__':main()
