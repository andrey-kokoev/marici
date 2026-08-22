"""Construct the cancellation-free t-series of ell'(t) from the odd Xi log jet."""
import json
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

import central_source_fourth_order_jet as J

with localcontext() as context:
    context.prec=100;J.ORDER=13;J.DEPTH=300;D=Decimal
    q=[D(0),D(1)]+[D(0)]*(J.ORDER-1);s=J.add(J.const(Fraction(1,2)),q)
    eta,eta_s=J.eta_pair_jets(s);log2=D(2).ln();r=J.expj(J.scale(J.sub(J.const(1),s),log2))
    zlog=J.sub(J.div(eta_s,eta),J.div(J.scale(r,log2),J.sub(J.const(1),r)))
    endpoint=J.add(J.inv(s),J.inv(J.sub(s,J.const(1))))
    xi_log_derivative=J.add(endpoint,J.const(-D('0.5')*J.PI.ln()),
                            J.scale(J.digamma_jet(J.scale(s,Fraction(1,2))),Fraction(1,2)),zlog)
    even_residual=max(abs(xi_log_derivative[n]) for n in range(0,J.ORDER+1,2))
    ell_prime=[xi_log_derivative[2*n+1]/2 for n in range(6)]

    # Form F=(4t-1)ell' and H=(F')^-1/2 as ordinary t-series.
    J.ORDER=5
    ep=ell_prime
    t=[D(0),D(1)]+[D(0)]*4
    f=J.mul(J.sub(J.scale(t,4),J.const(1)),ep)
    g=[D(n+1)*f[n+1] for n in range(5)]+[D(0)]
    h=J.powj(g,Fraction(-1,2))
    h2_at_zero=2*h[2];h3_at_zero=6*h[3]

result={"centered_q_order":13,"eta_euler_depth":300,
        "maximum_even_coefficient_residual_in_Xi_log_derivative":str(even_residual),
        "ell_prime_t_coefficients_through_degree_five":[str(x) for x in ell_prime],
        "H_double_prime_at_t_zero_from_even_series":str(h2_at_zero),
        "H_triple_prime_at_t_zero_from_even_series":str(h3_at_zero),
        "reflection_oddness_residual_below_gamma_truncation_scale":even_residual<Decimal('1e-30'),
        "square_root_cancellation_removed_before_t_series":True,
        "interval_certified":False,"rh_proved":False}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'central-xi-log-even-series.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items():print(f'{key}={value}')
