"""Uniform Cauchy bound for eta Euler tails through derivative order six."""
import json
from decimal import Decimal, localcontext
from math import factorial
from pathlib import Path

with localcontext() as context:
    context.prec=90;D=Decimal;depth=300;radius=D("0.1");gamma_reciprocal_bound=D(4)
    bounds=[]
    for order in range(7):
        bound=gamma_reciprocal_bound*D(factorial(order))*(1/radius)**order/(D(depth)+D("0.4"))*D(2)**(-depth)
        bounds.append(bound)
result={"s_real_interval":["0.5","0.6"],"cauchy_radius":str(radius),
        "cauchy_rectangle_real_range":["0.4","0.7"],"cauchy_rectangle_imaginary_radius":"0.1",
        "reciprocal_gamma_bound":str(gamma_reciprocal_bound),"euler_depth":depth,
        "eta_derivative_tail_bounds_orders_0_through_6":[str(x) for x in bounds],
        "maximum_tail_bound":str(max(bounds)),"all_bounds_below_1e_minus_80":max(bounds)<D("1e-80"),
        "interval_jet_tail_ready":True,"rh_proved":False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'eta-high-jet-cauchy-tail.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
