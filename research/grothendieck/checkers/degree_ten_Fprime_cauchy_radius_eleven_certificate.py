"""Directed Cauchy-tail certificate for Re F'(t)>0 on |t|<=9."""
import json
from decimal import Context, Decimal as D, ROUND_CEILING, ROUND_FLOOR
from pathlib import Path
ROOT=Path(__file__).parents[1]; down=Context(prec=90,rounding=ROUND_FLOOR);up=Context(prec=90,rounding=ROUND_CEILING)
sharp=json.loads((ROOT/'results'/'F-prime-unit-disk-theta-sharp-certificate.json').read_text())
jet=json.loads((ROOT/'results'/'central-xi-log-even-series-interval.json').read_text())
c=[tuple(map(D,b)) for b in sharp['normalized_Y_coefficients_c0_through_c6']]
q=[tuple(map(D,b)) for b in jet['normalized_boundary_margin_coefficients_through_degree_ten']]
A=D('12.2291447802683980216431793240891324860028232975681928967813222103417342289462238562065712')
anchor=D(81); R=D(16); target=D(11)
def deriv_upper(k):
 total=D(0)
 for n in range(k,7):
  fall=D(1)
  for j in range(k): fall=up.multiply(fall,D(n-j))
  total=up.add(total,up.multiply(c[n][1],up.multiply(fall,up.power(R,n-k))))
 fall=D(1)
 for j in range(k): fall=up.multiply(fall,D(7-j))
 tail=up.divide(up.multiply(A,up.multiply(fall,up.power(R,7-k))),up.power(anchor,7))
 return up.add(total,tail),tail
C,Ctail=deriv_upper(0);Cp,Cptail=deriv_upper(1);Cpp,Cpptail=deriv_upper(2)
den=down.subtract(D(2),C)
p=up.divide(Cp,den); qlog=up.add(up.divide(Cpp,den),up.multiply(p,p))
M=up.add(up.multiply(D(4),p),up.multiply(up.add(up.multiply(D(4),R),D(1)),qlog))
r=up.divide(target,R)
remainder=up.divide(up.multiply(M,up.power(r,11)),down.subtract(D(1),r))
poly0=down.divide(q[0][0],D(4)); variation=D(0)
for n in range(1,11): variation=up.add(variation,up.multiply(max(abs(q[n][0]),abs(q[n][1]))/D(4),up.power(target,n)))
poly_lower=down.subtract(poly0,variation); final=down.subtract(poly_lower,remainder)
assert den>0 and final>0
out={'source_cauchy_radius':str(R),'target_disk_radius':str(target),'normalized_source_upper_on_cauchy_radius':str(C),'normalized_source_modulus_lower_on_cauchy_radius':str(den),'Fprime_modulus_upper_on_cauchy_radius':str(M),'degree_ten_polynomial_real_lower_on_target_disk':str(poly_lower),'degree_eleven_and_higher_remainder_upper':str(remainder),'Fprime_real_lower_on_radius_eleven':str(final),'Im_F_strictly_positive_on_upper_radius_eleven_disk':True,'directed_decimal_rounding':True,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
 pth=ROOT/'results'/'degree-ten-Fprime-cauchy-radius-eleven-certificate.json';pth.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
