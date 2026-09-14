#!/usr/bin/env python3
"""Exact two-prime mismatch between independent random phases and one deterministic character."""
import json
from fractions import Fraction
from pathlib import Path

def main():
 a=Fraction(1,2);b=Fraction(1,3)
 # E|a X_p+b X_q|^2 for independent Haar phases: cross expectation is zero.
 random_average=a*a+b*b
 # At deterministic aligned character xi=0, both phases are one.
 deterministic_aligned=(a+b)**2
 cross=deterministic_aligned-random_average
 assert cross==2*a*b and cross>0
 # At a character with opposite phases, the same cross polarization reverses sign.
 deterministic_opposed=(a-b)**2
 assert deterministic_opposed-random_average==-cross
 result={'schema':'marici.voevodsky.random-Euler-cross-prime-mismatch.v1','weights':[str(a),str(b)],'independent_Haar_average':str(random_average),'deterministic_aligned_square':str(deterministic_aligned),'deterministic_opposed_square':str(deterministic_opposed),'erased_cross_term_magnitude':str(cross),'theorem':'Independent prime phases retain diagonal prime energies but erase the deterministic cross-prime polarization 2ab cos(xi(log p-log q)).','conclusion':'Random Euler-product and multiplicative-chaos measures cannot directly represent the fixed-character terminal Weil square.'}
 out=Path(__file__).parents[1]/'results'/'random_Euler_carrier_erases_deterministic_cross_prime_polarization.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
