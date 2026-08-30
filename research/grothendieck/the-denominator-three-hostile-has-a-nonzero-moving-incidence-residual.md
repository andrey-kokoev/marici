# The denominator-three hostile has a nonzero moving-incidence residual

## Weighted counting discrepancy

Let a locally finite positive endpoint measure on the positive ray be

\[
\mu=\sum_{\lambda>0}w_\lambda\delta_\lambda
\]

with mean density one. Its source-native incidence register is the weighted
counting discrepancy

\[
q_\mu(x)=x-N_\mu(x),
\qquad
N_\mu(x)=\sum_{0<\lambda\leq x}w_\lambda.
\]

Under dilation, put

\[
q_{\mu,u}(r)=q_\mu(e^{-u}r).
\]

Distributional differentiation gives the exact connection law

\[
\partial_u q_{\mu,u}(r)
=-e^{-u}r
+e^u\sum_{\lambda>0}w_\lambda\lambda
\delta(r-\lambda e^u).
\]

For the canonical integer comb, this reduces to

\[
J_{\mathbb Z}(u,r)
=-e^{-u}r
+e^u\sum_{n\geq1}n\delta(r-ne^u).
\]

The smooth term depends only on mean density. The singular term retains the
complete endpoint incidence packet.

## The normalized denominator-three packet

Write

\[
D=1+2\varepsilon,
\qquad 0<\varepsilon<1.
\]

The normalized hostile has integer weights

\[
a_n=\frac{1+2\varepsilon\cos(2\pi n/3)}{D}
\]

and weight

\[
b=\frac{\varepsilon}{D}
\]

on every endpoint in each shifted coset

\[
\mathbb Z+\frac13,
\qquad
\mathbb Z-\frac13.
\]

Its total mean density is one, so its smooth Haar current agrees exactly with
the canonical current. Subtraction therefore leaves the purely singular
connection residual

\[
\begin{aligned}
R_3(u,r)=e^u\Bigg[&
\sum_{n\geq1}(a_n-1)n\delta(r-ne^u)\\
&+b\sum_{n\in\mathbb Z\atop n+1/3>0}
(n+1/3)\delta(r-(n+1/3)e^u)\\
&+b\sum_{n\in\mathbb Z\atop n-1/3>0}
(n-1/3)\delta(r-(n-1/3)e^u)
\Bigg].
\end{aligned}
\]

The integer coefficient simplifies to

\[
a_n-1=
\begin{cases}
0,&3\mid n,\\
-3\varepsilon/D,&3\nmid n.
\end{cases}
\]

Thus the hostile adds positive currents on two fractional endpoint families
and a negative current on the two nonzero integer residue classes.

## Smallest local witness

In the first positive unit cell, the residual already contains

\[
\frac{\varepsilon e^u}{D}
\left[
\frac13\delta(r-e^u/3)
+\frac23\delta(r-2e^u/3)
-3\delta(r-e^u)
\right].
\]

The three distributions have disjoint support. Hence this residual is nonzero
for every allowed value of \(\varepsilon\) and every dilation \(u\). No scalar
normalization, Fourier-orbit summation, or origin-weight adjustment can remove
it.

An auxiliary control can absorb the residual only by admitting the two
fractional endpoint species and the modulo-three integer weights. That changes
the one-cell-to-one-endpoint source ontology rather than repairing the
canonical source.

## Transfer result

The denominator-three hostile is rejected before any Mellin transform or zero
calculation. It agrees with the canonical source after scalar compression but
is not horizontal for the canonical moving-incidence connection.

This makes the cross-sector transfer exact:

- Aspect's co-moving detector detects the additional endpoint motion;
- Benincasa's horizontal-germ condition rejects a frozen comparison port;
- Strominger's independent coherence port prevents scalar reconstruction of
  the missing incidence data;
- Kitaev's constructor-history rule prevents Haar cancellation from erasing
  the residual.

The remaining RH question is narrower. One must prove that the canonical
moving-incidence connection, together with Fourier completion, constrains the
scalar divisor. The hostile source is now excluded by provenance, but that
exclusion alone does not orient the canonical Mellin section.

## Operator stimulus

The operator asked us to catch up on other research and look for transfers.
That request shifted the experiment from a scalar hostile-zero search to a
connection comparison. The first unit cell then supplied the complete
falsifier.
