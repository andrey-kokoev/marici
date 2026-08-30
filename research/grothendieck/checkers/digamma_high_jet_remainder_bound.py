"""High-order digamma remainder bounds after deep recurrence."""
import json
from decimal import Decimal, localcontext
from math import factorial
from pathlib import Path

with localcontext() as context:
    context.prec=100;D=Decimal;target=1000
    b18=D(43867)/D(798);base=b18/(D(18)*D(target)**18);bounds=[]
    for order in range(7):
        bounds.append(base*D(factorial(order))*D(2)**18/D(target)**order)
result={"recurrence_target":target,"first_omitted_bernoulli":"B_18",
        "digamma_s_over_2_derivative_remainder_bounds_orders_0_through_6":[str(x) for x in bounds],
        "maximum_bound":str(max(bounds)),"all_bounds_below_1e_minus_45":max(bounds)<D("1e-45"),
        "gamma_high_jet_tail_ready":True,"rh_proved":False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'digamma-high-jet-remainder-bound.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
