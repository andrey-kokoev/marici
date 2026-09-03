#!/usr/bin/env python3
"""Factor the residual after the explicit second-normal-residue lift."""
import json
from pathlib import Path
# s=Y-3, Q=s^2 R, R=R0+sR1, b=-3K0 s.
# T-L1_y(b)=3s^2[(K-K0)R-K0*s*R_s].
# K0=9X^4, K1=-216X^2, R0=X^2(X-6), R1=X(X-6).
# Third residue: 3(K1R0-K0R1)=-27X^4(X-6)(X+24).
for x in range(-5,8):
 lhs=3*((-216*x*x)*(x*x*(x-6))-(9*x**4)*(x*(x-6)))
 rhs=-27*x**4*(x-6)*(x+24)
 assert lhs==rhs
out={'schema':'marici.benincasa.cosmology-rees-second-lift-residual.v1','problem':'compute the full residual after matching tau through second normal order','bold_conjecture':'the explicit second-order lift cancels tau exactly','named_rivals':['exact cancellation','a nonzero third normal residue remains'],'risky_consequences':['the factored residual must vanish identically','its third normal coefficient must be zero'],'strongest_falsification_attempt':{'lift':'b=-3K0s','exact_residual':'3s^2[(K-K0)R-K0sR_s]','residual_s_order':3,'K0':'9X^4','K1':'-216X^2','R0':'X^2(X-6)','R1':'X(X-6)','third_normal_residue':'-27X^4(X-6)(X+24)','nonzero':True},'disposition':'the lift is not exact; it raises the residual order from two to three and leaves an explicit nonzero third residue','surviving_scope':'the exact residual factorization supplies the next finite obstruction test','next_test':'compute the constrained third-residue image after enforcing first and second residue cancellation, then test membership of -27X^4(X-6)(X+24)','passed':True};R=Path(__file__).resolve().parents[1]/'results';(R/'cosmology_rees_second_lift_residual.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
