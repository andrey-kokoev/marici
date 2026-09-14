#!/usr/bin/env python3
"""Exact finite audit of Fejer scalarization and a signed-measure hostile."""
import json,math
from fractions import Fraction
from pathlib import Path

def fejer_from_moments(k,N,theta):
 return k[0]+2*sum((1-Fraction(m,N))*k[m]*math.cos(m*theta) for m in range(1,N))
def main():
 # Positive atoms 2 delta_0 + delta_pi: k_m=2+(-1)^m.
 k=[Fraction(2)+Fraction((-1)**m) for m in range(17)]
 minima=[]
 for N in range(2,17):
  vals=[fejer_from_moments(k,N,2*math.pi*j/4096) for j in range(4096)]
  mn=min(vals);assert mn>=-1e-12;minima.append({'N':N,'sample_minimum':float(mn)})
 # Signed hostile 2 delta_0-3 delta_pi has negative Fejer values near pi for growing N.
 bad=[Fraction(2)-3*Fraction((-1)**m) for m in range(17)]
 bad_values=[float(fejer_from_moments(bad,N,math.pi)) for N in range(2,17)]
 assert any(v<0 for v in bad_values)
 result={'schema':'marici.voevodsky.fejer-scalarization-of-toeplitz-positivity.v1','positive_atomic_orders_checked':'2..16','positive_sample_minima':minima,'signed_hostile_values_at_pi':bad_values,'theorem':'A circle distribution is positive iff every Fejer convolution is a nonnegative function; equivalently all of its finite Toeplitz moment matrices are PSD.','source_formula':'F_N(theta)=K(0)+2 sum_{m=1}^{N-1}(1-m/N) K(mh) cos(m theta)','computational_use':'Use a scalar approximate-identity hierarchy equivalent in the all-N limit; finite Fejer order is not identical to the same-size Toeplitz PSD test.','rh_boundary':'All N and a spacing sequence tending to zero remain required.'}
 out=Path(__file__).parents[1]/'results'/'fejer_scalarization_of_toeplitz_positivity.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'positive_orders':len(minima),'hostile_minimum':min(bad_values)},indent=2))
if __name__=='__main__':main()
