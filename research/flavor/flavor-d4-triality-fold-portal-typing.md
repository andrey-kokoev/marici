# D4 Triality-Fold Portal Typing

## Question

Can the order-three triality of \(D_4\) derive the asymmetric integer in the
flavor portal and remove WP797's root-versus-coroot choice?

## Source construction

Take the affine \(D_4^{(1)}\) Gram form in node order
\((a,c,o_1,o_2,o_3)\), where \(c\) is central:

\[
H=
\begin{pmatrix}
2&-1&0&0&0\\
-1&2&-1&-1&-1\\
0&-1&2&0&0\\
0&-1&0&2&0\\
0&-1&0&0&2
\end{pmatrix}.
\]

Its primitive null vector is

\[
d=(1,2,1,1,1)^{\mathsf T}.
\]

The triality automorphism cyclically permutes \(o_1,o_2,o_3\), fixes \(a,c\),
has order three, and preserves \(H\). This makes a three-element orbit genuine
source data rather than a fitted charge.

## Three bases for one invariant vector

Let \(s=o_1+o_2+o_3\). In the integral invariant basis \((a,c,s)\), the folded
Gram form is

\[
G_{\mathrm{sum}}=
\begin{pmatrix}
2&-1&0\\
-1&2&-3\\
0&-3&6
\end{pmatrix},
\]

with kernel \((1,2,1)^{\mathsf T}\) and spectrum

\[
0,\qquad 5-\sqrt7,\qquad 5+\sqrt7.
\]

This is the twisted affine fold \(D_4^{(3)}\). It is not the untwisted
\(G_2^{(1)}\) packet whose marks were tested in WP797.

In the orbit-average basis \((a,c,s/3)\), the same source vector has coordinates
\((1,2,3)^{\mathsf T}\). In the canonically normalized basis
\((a,c,s/\sqrt3)\), it has coordinates
\((1,2,\sqrt3)^{\mathsf T}\). Exactly,

\[
\begin{aligned}
d
&=a+2c+s\\
&=a+2c+3(s/3)\\
&=a+2c+\sqrt3(s/\sqrt3).
\end{aligned}
\]

Thus the displayed coefficient three is not itself a basis-independent
physical coupling. Triality makes the orbit size three invariant; it does not
make every coordinate coefficient of that orbit equal to three.

## Physical typing

If the source declares the integral charge lattice, the orbit sum is
privileged arithmetically. If it declares canonically normalized propagating
fields, the normalized basis is privileged dynamically. If it declares a
quotient or averaged observable, the average basis is privileged
observationally. These are different interfaces and cannot be identified
without an action and an instrument.

Triality fixes the central-versus-orbit incidence, but it does not:

- map the folded nodes to the two physical flavor species;
- select the sign of \(g_n-g_m\);
- fix the gauge, compactification, or kinetic normalization;
- supply anomaly-complete matter beta functions;
- derive finite thresholds, widths, and decoupling;
- map the folded mode into calibrated physical16 detector response.

The spectral gap protects each declared folded quadratic packet. It is not a
proof of an RG basin for the flavor theory.

## Classification

- \(D_4\) triality is a source-derived orbit-three and long--short
  rigidifier.
- The integral invariant lattice conditionally selects an orbit-sum
  representation.
- The coefficient three in the averaged coordinates is presentation data.
- No complete flavor selector or physical instrument is obtained.

Triality therefore explains the triple bond better than bare affine \(G_2\),
but it still does not explain the portal. The construction is hard to vary at
the orbit-incidence arrow and easy to vary at every physical interface after
that arrow.

## Smallest exact falsifier

The same \(D_4\) null vector has folded coordinates \((1,2,1)\),
\((1,2,3)\), and \((1,2,\sqrt3)\) in the integral-sum, orbit-average, and
canonically normalized bases. Any portal prediction that reads one of those
coordinate entries without naming the source action and calibrated pairing
fails descent.

## Successor

The positive successor must construct a chiral electric matter action from the
triality-twisted source. That one action must choose the invariant charge
lattice and kinetic pairing, attach its oriented nodes to flavor species, fix
the overall coefficient, determine the beta functions and finite thresholds,
and generate a calibrated physical16 response Jacobian.

Verification:

- checker:
  research/flavor/checkers/wp798_d4_triality_fold_portal_typing.py
- generated result:
  research/flavor/results/wp798_d4_triality_fold_portal_typing.json
- exact invocation:
  uv run --with sympy python research/flavor/checkers/wp798_d4_triality_fold_portal_typing.py
- triality and \(D_4/G_2\) singularities:
  [Mikosz and Weber](https://arxiv.org/abs/1311.0507)
- physical \(Z_3\)-twisted \(D_4\) construction:
  [Chacaltana, Distler, and Trimm](https://arxiv.org/abs/1601.02077)
- non-simply-laced gauge construction:
  [Cecotti and Del Zotto](https://arxiv.org/abs/1207.7205)
