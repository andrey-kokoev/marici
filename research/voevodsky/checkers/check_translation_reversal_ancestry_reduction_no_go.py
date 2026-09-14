#!/usr/bin/env python3
"""Exact no-go: translation/reversal preserve finite channel-support cardinality."""
import json
from fractions import Fraction
from pathlib import Path

def normalize(p):return {a:c for a,c in p.items() if c}
def shift(p,k):return normalize({a+k:c for a,c in p.items()})
def reverse(p):return normalize({-a:c for a,c in p.items()})
def main():
 p={Fraction(-2):Fraction(1),Fraction(0):Fraction(-3),Fraction(5):Fraction(2)};n=len(p);orbit=[]
 for k in range(-5,6):
  for reflected in (False,True):
   q=shift(reverse(p) if reflected else p,Fraction(k));assert len(q)==n
   orbit.append({'shift':k,'reflected':reflected,'support':[str(x) for x in sorted(q)],'support_size':len(q)})
 assert all(x['support_size']!=1 for x in orbit)
 result={'schema':'marici.voevodsky.translation-reversal-ancestry-reduction-no-go.v1','initial_support':[str(x) for x in sorted(p)],'initial_support_size':n,'orbit':orbit,'theorem':'Translations and reversal are bijections of channel labels, hence preserve the number of nonzero coefficients of every finite composite primitive.','composite_reaches_one_channel_base':False,'consequence':'Bidirectional time propagation cannot force a negative composite Schwarz square into the independently positive single-translate base class.','required_new_operation':'A support-reducing quotient, fold, or coarse-graining; such an operation needs a separate conservativity theorem because it can erase negativity.'}
 out=Path(__file__).parents[1]/'results'/'translation_reversal_ancestry_reduction_no_go.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'support_size':n,'orbit_cases':len(orbit),'reaches_base':False},indent=2))
if __name__=='__main__':main()
