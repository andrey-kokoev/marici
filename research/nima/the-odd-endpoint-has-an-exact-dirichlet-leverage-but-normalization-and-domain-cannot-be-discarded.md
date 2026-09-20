# The odd endpoint has an exact Dirichlet leverage, but normalization and domain cannot be discarded

## Question and conjecture

Can the shifted-Laplacian route suggested by prior Sonin research supply the odd endpoint range factorization without fitting a positive metric?

The source-known endpoint vectors are exp(x/2) and exp(-x/2). Test their odd combination against the independently specified shifted differential expression P=partial_x^2-1/4 on (-L,L), L>0. The candidate comparison energy is its Dirichlet Green energy. Rivals are the unconditioned residual norm ||P f||^2 and a normalization that silently sets the physical endpoint coefficient to one.

Active obligation: a source-domain and range-factorization test, not another presentation-coherence calculation. The Dirichlet boundary condition is a declared comparison choice, not yet derived from the semilocal canonical/dual carrier.

## Immediate domain hostile

Let h(x)=sinh(x/2). Then Ph=0, while

\[
\langle h,h\rangle=\sinh L-L>0.
\]

Thus on an unrestricted H2 interval domain containing h, no inequality

\[
a|\langle h,f\rangle|^2\le\|Pf\|^2
\]

can hold for any a>0. Taking f=h is the exact counterexample. The bare differential residual cannot control this endpoint functional while retaining its harmonic kernel. Whether the actual source domain excludes that vector is a separate source question.

Here the endpoint functional is the L2 pairing with the source-known exponential vector (the Paley–Wiener evaluation functional), not the point trace f(L)-f(-L). Those two notions of endpoint must not be interchanged.

## Dirichlet Green constructor

Take the positive operator

\[
H_D=-\partial_x^2+\tfrac14,
\qquad D(H_D)=H^2(-L,L)\cap H_0^1(-L,L).
\]

Its closed form is

\[
q_D(f)=\int_{-L}^{L}(|f'|^2+\tfrac14|f|^2)\,dx,
\qquad D(q_D)=H_0^1(-L,L).
\]

This changes both the energy and the domain relative to the bare residual-norm rival; it is not a repair obtained by adding an arbitrary fitted matrix.

Put delta_L=sinh L-L and v_L=h/sqrt(delta_L). Solving the resonant boundary-value problem H_D w=h gives the explicit source-expression solution

\[
w_L(x)=L\coth(L/2)\sinh(x/2)-x\cosh(x/2),
\qquad w_L(\pm L)=0.
\]

Therefore H_D^-1 v_L=w_L/sqrt(delta_L). The rank-one leverage is

\[
\ell_D(L)=\langle v_L,H_D^{-1}v_L\rangle
=L\coth(L/2)-\frac{L\cosh L-\sinh L}{\sinh L-L}
=1-\frac{L(L\coth(L/2)-2)}{\sinh L-L}.
\]

Positivity of H_D gives ell_D>0. For t>0, t cosh t-sinh t has derivative t sinh t>0 and vanishes at zero, so t coth t>1. Hence ell_D<1 for every finite L>0.

The exact limits are

\[
\ell_D(L)\sim L^2/15\quad(L\downarrow0),\qquad
\ell_D(L)\to1\quad(L\to\infty).
\]

There is no cutoff-uniform positive gap below one.

## Explicit Douglas vector and retained source coefficient

For the rank-one term c_L v_L v_L* with c_L>=0, define

\[
d_L=\sqrt{c_L}\,H_D^{-1/2}v_L.
\]

Then

\[
H_D^{1/2}d_L=\sqrt{c_L}\,v_L,\qquad
\|d_L\|^2=c_L\ell_D(L).
\]

Thus the Dirichlet comparison gate is exactly c_L ell_D(L)<=1. The coefficient is not a free normalization.

For the recorded parity vector

\[
e_{odd}(x)=\frac{e^{x/2}-e^{-x/2}}{\sqrt2}
=\sqrt2\sinh(x/2),
\]

one has ||e_odd||^2=2 delta_L. If b=e_odd in this comparison model, then c_L=2 delta_L and its leverage is

\[
2\delta_L\ell_D(L)\longrightarrow\infty.
\]

Consequently the unit-coefficient normalized inequality cannot prove control of the unnormalized endpoint by this fixed Dirichlet energy as L grows. The required bulk coefficient or endpoint transport must come from the actual source pairing.

This also affects successor naturality. Under zero extension from a smaller Dirichlet interval to a larger one, pairing with the unnormalized e_odd is preserved on the old domain. Pairing with v_L changes by the ratio sqrt(delta_old/delta_new). Keeping the normalized vector and discarding c_L would therefore change the source endpoint functional under refinement.

## Relation to the actual Sonin gate

The semilocal target remains C_k>=c_k v_k v_k*, where C_k must be formed from the differentiated canonical/dual two-space pairing. This note has not identified C_k with H_D, nor transported its boundary conditions or c_k.

A sufficient genuine comparison would be a source-derived map T_k into the Dirichlet form domain with

\[
q_D(T_k f)\le q_{C_k}(f)
\]

and an exact intertwining of the endpoint functional, retaining its coefficient. The Dirichlet Cauchy–Schwarz bound would then apply with that coefficient. Neither the existence nor contractivity of T_k is proved here. This is the same source bridge named in prior research, now equipped with an explicit reference solution and a normalization falsifier, rather than an unspecified energy target.

The negative results reject two concrete shortcuts: using ||P f||^2 on a domain containing the odd harmonic mode, and promoting the normalized c=1 estimate to an unnormalized source endpoint inequality. They do not refute the actual Sonin Schur condition.

## Disposition and verification

Constructed: an explicit Dirichlet Green solution, range factorization and sharp leverage formula for the source-shaped odd exponential endpoint. Falsified: the unrestricted residual-norm rival and uniform unnormalized endpoint domination by this fixed comparison energy.

The physical/semilocal positive seam remains unproved. No relation to the earlier -4/5 matrix residual is inferred.

`uv run --with sympy python research/nima/checkers/check_odd_endpoint_shifted_laplacian_range.py` exits 0 with twelve exact symbolic checks. Result: `research/nima/results/odd-endpoint-shifted-laplacian-range.json`. The inequalities for all L are justified by the displayed analytic argument, not finite numerical sampling.
