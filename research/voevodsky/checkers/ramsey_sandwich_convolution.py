"""Exact signed-projection control. Each conjugate-angle pair of rotor actions
sums to 2 cos(theta) I. No path absent, no neutral responder used.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def sheet(pair_cosines):
    # A pair represents rotations by +theta and -theta, even at theta=0.
    # Read e1 along the forward route, e2 along its inverse on the same frame.
    # Terminal signed projections onto their original axes both equal cos(theta).
    c=[v for v in pair_cosines for _ in range(2)]
    r,b=(min(c)>=0,max(c)<=0)
    return dict(sum_operator_scalar=str(sum(c)),forward_e1=list(map(str,c)),no_red_minus=r,no_blue_plus=b,final_OR=r or b)

def run():
    a,b=sheet((F(1,4),F(1,4))),sheet((F(1),F(-1,2)))
    assert a['sum_operator_scalar']==b['sum_operator_scalar']=='1' and a['final_OR']!=b['final_OR']
    # For diagonal +/-1 actions, each entry of the full sum fixes that
    # channel's negative count when the number of present routes is known.
    checked=0
    for pairs in product(list(product((-1,1),repeat=2)),repeat=4):
        x,y=zip(*pairs);assert (min(x)>=0,max(y)<=0)==(sum(x)==4,sum(y)==-4);checked+=1
    out=dict(scope='Trial signed extrema at resolution; fixed four routes, unit sandwiches, same marked axes; not derivation of the Ramsey computeds',first=a,second=b,diagonal_control_assignments=checked);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_sandwich_convolution.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':run()
