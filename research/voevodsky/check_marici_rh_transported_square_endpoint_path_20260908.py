#!/usr/bin/env python3
"""Exact transported two-step decomposition of the weighted square endpoint current."""
import argparse,json
from fractions import Fraction
from pathlib import Path

def main():
 p=argparse.ArgumentParser();p.add_argument('--output',default='research/voevodsky/marici_rh_transported_square_endpoint_path_certificate_20260908.json');a=p.parse_args();rows=[];checks=0
 for prime in (2,3,5,7,11,13):
  x=Fraction(1,prime)
  first=x-1
  transported_second=x*(x-1)
  total=first+transported_second
  assert total==x*x-1;checks+=1
  endpoint_square=x*total/2
  declared=(x*x-1)*x/2
  assert endpoint_square==declared;checks+=1
  fixed_state=x*(first+first)/2
  residual=fixed_state-declared
  assert residual!=0;checks+=1
  rows.append({'prime':prime,'first_segment':str(first),'transported_second_segment':str(transported_second),'total_increment':str(total),'weighted_square_current':str(endpoint_square),'fixed_state_two_copy_residual':str(residual)})
 out={'schema':'marici.rh.transported-square-endpoint-path.v1','status':'transported_two_step_exact','checks':checks,'rows':rows,'identity':'x(x^2-1)/2 = (x/2)((x-1)+x(x-1)), x=p^-1','claim':'the endpoint square current is the weighted complete two-step path with a transported second coefficient state','hostile':'replacing the transported second segment x(x-1) by a second fixed-state copy x-1 gives a nonzero residual','boundary':'this constructs the grade-two path current but not a single operator whose P1 and P2 traces equal the independently derived endpoint grades'}
 Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':out['status'],'checks':checks,'primes':[r['prime'] for r in rows]}))
if __name__=='__main__':main()
