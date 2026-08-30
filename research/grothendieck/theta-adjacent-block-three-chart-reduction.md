# Three fixed charts remove every folded-label cusp from the adjacent block

Let `L=pi/b`. The whole adjacent block is not intrinsically a transported
difference: by changing variables in its second term,

\[
 \int_0^L[H(D)+H(D+L)]\,dD
 =\int_0^{2L}H(d)\,dd.                                 \tag{1}
\]

Return to `u=U`, `v=V`, so `d=u-v` and `S=u+v`. The Jacobian cancellation
between `(S,D)` and `(u,v)` gives the labelled block

\[
 \mathcal B_{nm}=
 \int_{0\le u-v\le2L}
 e^{a(u+v)}f_n(u)f_m(v)
 [\beta(u+v)\cos(b(u-v))+\alpha(u-v)\sin(b(u-v))]
 \,du\,dv,                                             \tag{2}
\]

where `f_n(u)=phi_n(|u|)`.

Put `d=u-v`. The two moving cusps are `v=0` and `v=-d`. Split the strip into
three source-defined sign charts.

## Chart A: both variables nonnegative

Set `v=x`, `u=x+d`, with `x>=0`:

\[
 f_n(u)f_m(v)=\phi_n(x+d)\phi_m(x),\qquad S=2x+d.       \tag{3}
\]

## Chart B: both variables nonpositive

Set `u=-x`, `v=-x-d`, with `x>=0`:

\[
 f_n(u)f_m(v)=\phi_n(x)\phi_m(x+d),\qquad S=-2x-d.      \tag{4}
\]

## Chart C: the variables straddle zero

Set `v=-x`, `u=d-x`, with `0<=x<=d`:

\[
 f_n(u)f_m(v)=\phi_n(d-x)\phi_m(x),\qquad S=d-2x.       \tag{5}
\]

Every chart has positive orientation and unit absolute Jacobian in `(x,d)`.
All theta-label arguments are nonnegative and smooth on the chart interior.
The only boundaries are the fixed faces `x=0`, `x=d`, `d=0`, and `d=2L`.

## Certification consequence

The hostile exchange-orbit integral at `(a,b)=(1,8)` can now be enclosed
without interval absolute values or boxes crossing moving cusps:

1. integrate charts A and B on `[0,infinity) x [0,pi/4]`;
2. integrate chart C on the triangle `0<=x<=d<=pi/4`;
3. sum only the source exchange orbit `(1,2)+(2,1)`;
4. bound the `x` tails of A and B by the explicit super-exponential label
   formula; and
5. retain directed sine and cosine bounds on the fixed `d` interval.

This is a reduction to a rigorous interval certificate, not the certificate
itself. It introduces no regrouping chosen from the observed sign.

## Durable verification

- Checker: `checkers/theta_adjacent_block_three_chart_reduction.py`
- Result: `results/theta-adjacent-block-three-chart-reduction.json`
