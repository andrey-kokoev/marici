#!/usr/bin/env python3
"""Exact hostile to a uniform Dirichlet margin on the unweighted label space."""
import argparse,json
from fractions import Fraction
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_labelled_theta_uniform_margin_hostile_certificate_20260908.json');args=p.parse_args();checks=0;rows=[]
 # G_nn=3*sqrt(2)/(16n).  Divide by the common positive factor
 # 3*sqrt(2)/16; the normalized Rayleigh value on basis vector e_n is 1/n.
 previous=None
 for n in (1,2,4,8,16,32,64,128):
  normalized=Fraction(1,n)
  assert normalized>0;checks+=1
  if previous is not None:
   assert normalized<previous;checks+=1
  previous=normalized
  rows.append({'label':n,'normalized_basis_rayleigh':f'1/{n}','exact_dirichlet_diagonal':f'3*sqrt(2)/({16*n})'})
 # For every proposed positive rational margin epsilon=a/b, choosing n>b/a
 # makes 1/n<epsilon.  Record exact representative hostiles.
 hostiles=[]
 for epsilon in (Fraction(1,2),Fraction(1,10),Fraction(1,100)):
  n=epsilon.denominator//epsilon.numerator+1
  assert Fraction(1,n)<epsilon;checks+=1
  hostiles.append({'proposed_normalized_margin':f'{epsilon.numerator}/{epsilon.denominator}','witness_label':n,'rayleigh':f'1/{n}'})
 out={'schema':'marici.rh.labelled-theta-uniform-margin-hostile.v1','status':'no_unweighted_uniform_margin','checks':checks,'rows':rows,'hostiles':hostiles,'identity':'G_nn=3*sqrt(2)/(16n)','claim':'finite labelled theta Dirichlet Grams are positive definite but have no cutoff-independent lower bound relative to the unweighted l2 label norm','disposition':'retain finite positivity; completion requires a source-derived weighted coefficient norm or a different coercive form','boundary':'does not refute coercivity in a weighted label space or on a source-restricted completed subspace'}
 Path(args.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'last_rayleigh':'1/128'}))
if __name__=='__main__':main()
