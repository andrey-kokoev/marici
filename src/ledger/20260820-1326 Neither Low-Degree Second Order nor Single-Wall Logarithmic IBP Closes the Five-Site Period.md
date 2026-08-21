# 1326 — Neither Low-Degree Second Order nor Single-Wall Logarithmic IBP Closes the Five-Site Period

## Hard comparison

After Entry 1320 excluded first-order polynomial primitives through degree five, two predeclared extensions were tested on the complete 32-sheet Kummer cover.

### Polynomial second order

\[
\partial_z^2\Omega
+a_1(z)\partial_z\Omega
+a_0(z)\Omega
=
\sum_{i=1}^3\partial_{u_i}(V_i\Omega),
\qquad \deg V_i\le d.
\]

Every wall is linear in \(z\), while the five Kummer roots are independent of \(z\). Hence \(\partial_z^2\Omega\) was evaluated exactly term by term.

Across

\[
p=1009,1013,
\qquad z=7,11,
\]

the full-deck systems are inconsistent for every

\[
d=0,1,2,3,4,5.
\]

At degree five each test has 170 unknowns and 6208 equations from 194 independent base points.

### Frozen single-wall logarithmic first order

For each of the 26 labelled walls \(L\) already present in the projective alphabet, test

\[
\partial_z\Omega+a(z)\Omega
=
\sum_i\partial_{u_i}\!\left(\frac{P_i}{L}\Omega\right),
\qquad \deg P_i\le2.
\]

No new denominator is fitted. Every labelled wall is tested separately.

At both independent fibers

\[
(p,z)=(1009,7),\qquad(1013,11),
\]

all 26 systems are inconsistent.

## Surviving statement

\[
\boxed{
\begin{aligned}
&\text{second-order polynomial IBP fails through degree five},\\
&\text{first-order one-wall logarithmic IBP fails through numerator degree two}.
\end{aligned}
}
\]

This excludes two simple explanations for the five-site period:

- that only the scalar differential order was underestimated;
- that one omitted logarithmic wall denominator supplies the certificate.

It does not exclude multidivisor logarithmic primitives, higher degrees, or a vector-valued Gauss--Manin system.

## Updated frontier

The lowest-complexity surviving candidate is no longer a scalar certificate built from one primitive family. The next finite object should be the Kummer-character-resolved de Rham module itself:

\[
\mathcal H_{\rm dR}
=
\frac{\langle\Omega,\partial_z\Omega,\ldots\rangle}
{d_u(\text{frozen logarithmic forms})}.
\]

Compute its rank growth under successive \(z\)-derivatives before choosing a scalar order. A stable rank predicts the minimal vector Gauss--Manin system; failure to stabilize gives a finite obstruction to the present basis.

## Artifacts

- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_second_order_ibp_pilot.rs`
- `research/benincasa/results/five-site-asymmetric-second-order-ibp-pilot.json`
- `research/benincasa/marici-gm/src/bin/five_site_asymmetric_logarithmic_ibp_pilot.rs`
- `research/benincasa/results/five-site-asymmetric-logarithmic-ibp-pilot.json`

Allocator claim: `seqclaim-f8bf1f0a8a5787544b9a806b`.
