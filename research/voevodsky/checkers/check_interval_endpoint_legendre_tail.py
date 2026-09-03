from __future__ import annotations
import json
from pathlib import Path
import flint
from flint import arb

flint.ctx.prec=192
N=160;L=arb('0.35');ZNORM=arb('11.031')

def odd_double_factorial(n):
    v=1
    for k in range(1,n+1,2): v*=k
    return v

def main():
    x=L/2;df=odd_double_factorial(2*N+1)
    ibound=x**N/df*(x*x/(2*(2*N+3))).exp()
    moment=2*L*((2*N+1)/(2*L)).sqrt()*ibound
    exp_norm=(2*L.sinh()).sqrt()
    per_column=2*moment*exp_norm*ZNORM
    ratio=x/(2*N+3)
    matrix_tail=arb(5)*per_column/(1-ratio*ratio).sqrt()
    passed=matrix_tail.upper()<arb('1e-400').lower()
    result={'schema':'marici.voevodsky.interval-endpoint-legendre-tail.v1',
      'starting_degree':N,'z_norm_bound':str(ZNORM),
      'modified_spherical_bessel_majorant':str(ibound),
      'normalized_legendre_moment_majorant':str(moment),
      'successive_ratio_upper':str(ratio),
      'twenty_five_column_frobenius_tail_upper':str(matrix_tail.upper()),
      'tail_below_1e_minus_400':bool(passed),'passed':bool(passed)}
    rendered=json.dumps(result,indent=2,sort_keys=True)
    Path('research/voevodsky/results/interval_endpoint_legendre_tail.json').write_text(rendered+'\n',encoding='utf-8')
    print(rendered)
if __name__=='__main__':main()
