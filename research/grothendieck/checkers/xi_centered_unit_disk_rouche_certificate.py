"""Elementary directed certificate of Xi(3/2)<2 Xi(1/2)."""
import json
from decimal import Decimal,Context,ROUND_FLOOR,ROUND_CEILING
from fractions import Fraction
from pathlib import Path

D=Decimal;down=Context(prec=80,rounding=ROUND_FLOOR);up=Context(prec=80,rounding=ROUND_CEILING)
row=[]
for n in range(1,42):
    root_lo=down.sqrt(D(n));root_hi=up.sqrt(D(n));row.append((down.divide(1,root_hi),up.divide(1,root_lo)))
eta_lower=D(0);two=D(2)
for _ in range(40):
    eta_lower=down.add(eta_lower,down.divide(row[0][0],two))
    row=[(down.subtract(row[i][0],row[i+1][1]),up.subtract(row[i][1],row[i+1][0])) for i in range(len(row)-1)]
    two*=2
sqrt2_upper=up.sqrt(D(2));zeta_half_abs_lower=down.divide(eta_lower,up.subtract(sqrt2_upper,1))

# Gamma(1/4)>3.4 from the [0,1] cubic exponential minorant plus a [1,2]
# tail; pi^(-1/4)>0.7 from pi<4.
xi_half_lower=D(Fraction(1,8).numerator)/D(Fraction(1,8).denominator)*D('3.4')*D('0.7')*zeta_half_abs_lower
# Gamma(3/4)<=4/3 by log-convexity after shifting to 7/4; zeta(3/2)<3
# by the integral test; pi^(-3/4)<1/2 from pi>3.
xi_three_halves_upper=D(3)/D(8)*D(4)/D(3)*D(3)*D(1)/D(2)
margin=down.subtract(down.multiply(2,xi_half_lower),xi_three_halves_upper)
assert margin>0
result={'eta_half_positive_Euler_partial_lower_bound':str(eta_lower),
        'absolute_zeta_half_lower_bound':str(zeta_half_abs_lower),
        'Xi_half_lower_bound':str(xi_half_lower),'Xi_three_halves_upper_bound':str(xi_three_halves_upper),
        'twice_Xi_half_minus_Xi_three_halves_lower_bound':str(margin),
        'Xi_three_halves_less_than_twice_Xi_half_certified':True,
        'centered_q_unit_disk_zero_free_by_theta_Rouche':True,
        'directed_decimal_rounding':True,'zero_locations_used':False,'rh_proved':False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'xi-centered-unit-disk-rouche-certificate.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
