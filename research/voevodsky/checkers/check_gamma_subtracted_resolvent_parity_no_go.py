#!/usr/bin/env python3
"""Parity no-go for subtracting the raw gamma sector before paired resolvent realization."""
import json,math
from pathlib import Path

def main():
 euler_gamma=0.5772156649015329
 psi_quarter=-euler_gamma-math.pi/2-3*math.log(2)
 gamma_center=.5*(psi_quarter-math.log(math.pi))
 # Centered completed Xi is even, hence its logarithmic derivative vanishes at zero.
 full_center=0.0
 remainder_center=full_center-gamma_center
 assert abs(gamma_center)>1 and abs(remainder_center)>1
 # Every regular paired resolvent 2z/(z^2+A^2) is odd and vanishes at z=0.
 result={'schema':'marici.voevodsky.gamma-subtracted-resolvent-parity-no-go.v1','psi_one_quarter':psi_quarter,'raw_gamma_log_derivative_at_center':gamma_center,'completed_log_derivative_at_center':full_center,'gamma_subtracted_remainder_at_center':remainder_center,'paired_resolvent_at_center':0,'parity_compatible':False,'first_repair_as_naively_stated':False,'reason':'The raw gamma sector is not odd under centered functional-equation reversal; endpoint, gamma, and prime sectors acquire oddness only after coupled summation.','surviving_repair':'Any reference subtraction must itself be odd and must preserve the coupled pole cancellations before a paired self-adjoint resolvent can be proposed.'}
 out=Path(__file__).parents[1]/'results'/'gamma_subtracted_resolvent_parity_no_go.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
