#!/usr/bin/env python3
"""Exact hostile to uniform domination of atomic evaluations by a continuous L2 square norm."""
import json,math
from fractions import Fraction
from pathlib import Path

def main():
 # p_n(z)=(4z(1-z))^n has p_n(1/2)=1.
 # Integral_0^1 |p_n|^2 dz = 16^n (2n)!^2/(4n+1)!.
 rows=[]
 for n in (1,2,4,8,16,32,64):
  integral=Fraction(16**n*math.factorial(2*n)**2,math.factorial(4*n+1));ratio=Fraction(1,1)/integral
  rows.append({'degree':2*n,'continuous_square_norm':float(integral),'atomic_to_continuous_ratio':float(ratio)})
 assert all(rows[i+1]['atomic_to_continuous_ratio']>rows[i]['atomic_to_continuous_ratio'] for i in range(len(rows)-1))
 result={'schema':'marici.voevodsky.atomic-prime-continuous-square-domination-no-go.v1','polynomial':'p_n(z)=(4z(1-z))^n','atomic_value_at_one_half':1,'continuous_reference':'Lebesgue measure on [0,1]','exact_square_integral':'16^n (2n)!^2/(4n+1)!','rows':rows,'uniform_domination_exists':False,'general_obstruction':'Point evaluation at an atom is unbounded in the L2 norm of a non-atomic measure on a polynomial-dense closure.','source_consequence':'A degree-uniform absolute bound of the discrete prime functional by a purely continuous gamma measure cannot hold without a stronger topology, matching atoms, or cancellation retained in the coupled form.'}
 out=Path(__file__).parents[1]/'results'/'atomic_prime_continuous_square_domination_no_go.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'first_ratio':rows[0]['atomic_to_continuous_ratio'],'last_ratio':rows[-1]['atomic_to_continuous_ratio']},indent=2))
if __name__=='__main__':main()
