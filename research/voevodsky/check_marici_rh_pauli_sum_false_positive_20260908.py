#!/usr/bin/env python3
"""Exhibit two endpoint Grams with equal Pauli sums but unequal faithful lifts."""
import argparse,json
from pathlib import Path
import sympy as s

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_pauli_sum_false_positive_certificate_20260908.json');args=p.parse_args();I=s.I;checks=0
 X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,I],[-I,0]]);R=X.row_join(Y)
 G1=s.Matrix([[2,1+I/2],[1-I/2,3]])
 G2=s.Matrix([[2,-s.Rational(1,2)-I],[-s.Rational(1,2)+I,3]])
 assert G1.is_positive_definite and G2.is_positive_definite;checks+=1
 sum1=s.simplify(X*G1*X+Y*G1*Y);sum2=s.simplify(X*G2*X+Y*G2*Y)
 assert sum1==sum2==s.diag(6,4);checks+=1
 lift1=s.simplify(R.conjugate().T*G1*R);lift2=s.simplify(R.conjugate().T*G2*R)
 assert lift1!=lift2;checks+=1
 assert s.simplify(X*(lift1[:2,:2]-lift2[:2,:2])*X-(G1-G2))==s.zeros(2);checks+=1
 out={'schema':'marici.rh.pauli-sum-false-positive.v1','status':'summed_pauli_comparison_insufficient','checks':checks,'G1':[[str(G1[i,j]) for j in range(2)] for i in range(2)],'G2':[[str(G2[i,j]) for j in range(2)] for i in range(2)],'common_pauli_sum':'diag(6,4)','faithful_lifts_equal':False,'claim':'positive endpoint Grams with different real correlation and reciprocal orientation can have identical summed Pauli frame operators','consequence':'uniform Pauli observability cannot replace the four-block quadratic identity; equality must be checked before output summation','boundary':'the full Pauli lift is faithful but does not make the original representation theorem easier, since lifted equality is equivalent to endpoint Gram equality'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'common_sum':'diag(6,4)'}))
if __name__=='__main__':main()
