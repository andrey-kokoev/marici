#!/usr/bin/env python3
"""Compare the endpoint grade-two current with P2 of the primitive interval operator."""
import argparse,json
from fractions import Fraction
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_endpoint_square_common_operator_hostile_certificate_20260908.json');a=p.parse_args();rows=[];checks=0
 for prime in (2,3,5,7,11,13):
  primitive_increment=Fraction(1,prime)-1
  operator_p2=primitive_increment*primitive_increment/2
  # Existing weighted endpoint filtration at grade k=2:
  # ((p^-2)-1) p^-1 / 2.
  endpoint_square=(Fraction(1,prime**2)-1)*Fraction(1,prime)/2
  residual=operator_p2-endpoint_square
  assert residual!=0;checks+=1
  assert operator_p2>0 and endpoint_square<0;checks+=2
  rows.append({'prime':prime,'primitive_increment':str(primitive_increment),'operator_P2':str(operator_p2),'endpoint_grade_two_current':str(endpoint_square),'residual':str(residual)})
 out={'schema':'marici.rh.endpoint-square-common-operator-hostile.v1','status':'primitive_interval_operator_falsified_for_square_grade','checks':checks,'rows':rows,'claim':'P2(A_logp) is not the independently derived weighted grade-two endpoint current','residual_formula':'(p^-1-1)^2/2 - ((p^-2-1)p^-1/2)','disposition':'withdraw the claim that the diagonal primitive interval operator supplies both endpoint low grades; retain its star-composition theorem only','next_test':'construct the transported two-step operator on the action groupoid and compare its trace with the grade-two endpoint current'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'primes':[r['prime'] for r in rows]}))
if __name__=='__main__':main()
