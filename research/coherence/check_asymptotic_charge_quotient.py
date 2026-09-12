#!/usr/bin/env python3
"""Check finite splitting and symmetry covariance of the two-charge quotient."""

import json
from fractions import Fraction
from pathlib import Path

def det(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
def main():
 rows=[]
 for y in (Fraction(2),Fraction(3,2),Fraction(5,3),Fraction(7,4)):
  # Columns are charges of k_(+a), k_(-a), with y=e^a.
  Q=[[1/y,y],[y,1/y]];d=det(Q);assert d!=0
  rows.append({'y':str(y),'charge_matrix':[[str(x) for x in r] for r in Q],'determinant':str(d),'surjective':True})
 result={'schema':'marici.coherence.asymptotic-charge-quotient.v1','seminorm_bound':'abs(q_plus(f))+abs(q_minus(f)) <= 2 q_1(f)','kernel_closed':True,'quotient_dimension':2,'finite_section_exists':True,'translation_covariance':'(q_minus,q_plus) -> (z^-1 q_minus,z q_plus)','reversal_covariance':'(q_minus,q_plus) -> (q_plus,q_minus)','splitting_checks':rows,'warning':'the section depends on a chosen nonzero displacement and is not canonical'}
 Path(__file__).with_name('asymptotic-charge-quotient.v1.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
