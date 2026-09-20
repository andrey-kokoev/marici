# The independent two-history rigged-crossing defect is exactly Xi-divisible and not identically zero

## Exact stable-history difference

The two stable histories satisfy

\[
u_-(q;z)
=\int_{-\infty}^q e^{z(q-r)}\Phi(r)\,dr,
\]

\[
u_+(q;z)
=-\int_q^\infty e^{z(q-r)}\Phi(r)\,dr.
\]

Subtracting before any Green or pair construction gives

\[
\begin{aligned}
u_-(q;z)-u_+(q;z)
&=\int_{-\infty}^{\infty}e^{z(q-r)}\Phi(r)\,dr\\
&=e^{zq}\tau(z).
\end{aligned}
\]

This identity belongs to the independent Evans realization.

## Transverse rigged crossing

For a fixed shell and seam, let

\[
\mathcal P_{a,b,c}(f;z)
:=T_{PB}^{\rm rig}(f\otimes K_{1,c}),
\qquad
K_{1,c}=-\frac12|q-c|+\delta_c.
\]

The crossing is linear in its regular first leg. Therefore its two-history
transverse defect is

\[
\begin{aligned}
\Delta_{a,b,c}(z)
&=\mathcal P_{a,b,c}(u_-;z)
 -\mathcal P_{a,b,c}(u_+;z)\\
&=\tau(z)\,\mathcal P_{a,b,c}(e^{z\cdot};z).
\end{aligned}
\]

Thus

\[
\boxed{
\Delta_{a,b,c}(z)=\tau(z)H_{a,b,c}(z)
}
\]

as an identity in the complete bordered packet, not merely after scalar
readout. Here

\[
H_{a,b,c}(z)=T_{PB}^{\rm rig}(e^{z\cdot}\otimes K_{1,c}).
\]

The formula is obtained without the canonical Stokes cancellation and without
specializing to Xi zeros.

## Multiplicity

The explicit shell formulas make `H_(a,b,c)` holomorphic on each initial
Laplace chart, with removable continuation at the apparent divided points.
Consequently, if `tau` has a zero of order `m` at `z_0`, then

\[
\partial_z^j\Delta_{a,b,c}(z_0)=0,
\qquad 0\le j<m.
\]

No squared or absolute-value divisor appears.

## Nonidentity

Take the seam at the right shell endpoint, `c=b`. The delta component gives

\[
R_{e^{z\cdot},\delta_b}(z)
=e^{zb}\int_0^{b-a}e^{-2zt}\,dt
=e^{zb}\frac{1-e^{-2z(b-a)}}{2z},
\]

and

\[
E_{e^{z\cdot},\delta_b}(z)
=\frac12e^{zb}
-\frac12e^{z(2a-b)}.
\]

These are not identically zero. For large positive real `z`, the endpoint
piece has leading order `e^(zb)/2`, whereas the `-|q-b|/2` contribution carries
at least one additional inverse Laplace scale in the endpoint-localized
asymptotic. Hence the complete primitive packet `H_(a,b,b)` is not identically
zero.

It follows that the defect is not the universally vanishing canonical Stokes
defect. For any parameter where `tau(z) != 0` and `H_(a,b,b)(z) != 0`, its
positive bordered graph norm is nonzero.

## Prime and cutoff assembly

The identity is shellwise. Translation to `c=k log p`, multiplication by the
frozen prime weights, and finite cutoff summation preserve it termwise.
Absolute convergence of the loaded primitive family permits passage to the
projective limit:

\[
\Delta_{\rm ar}(z)=\tau(z)H_{\rm ar}(z).
\]

Possible cancellation of the assembled coefficient `H_ar` is a separate
faithfulness question; shellwise nonidentity is already established.

## Disposition

The independent bridge passes the three logical tests:

1. Xi enters essentially through the independently derived two-history
   mismatch;
2. the complete bordered defect is Xi-divisible with multiplicity;
3. the defect is not identically zero away from the Xi divisor.

This closes independence of the Evans criterion at the analytic bordered
level. It does not by itself prove the reciprocal positive-energy confinement
identity needed for RH.