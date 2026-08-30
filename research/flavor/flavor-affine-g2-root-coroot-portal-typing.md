# Affine G2 Root--Coroot Portal Typing

## Question

Does the asymmetric triple bond of \(G_2\) derive the required flavor portal,
rather than merely offering another integer that can be assigned to it?

## Exact root datum

Use the Cartan convention

\[
A_{ij}=\frac{2(\alpha_i,\alpha_j)}{(\alpha_j,\alpha_j)}.
\]

For finite \(G_2\), with node one short and node two long,

\[
A_{G_2}=\begin{pmatrix}2&-1\\-3&2\end{pmatrix},
\qquad \det A_{G_2}=1.
\]

The finite matrix is full rank. It supplies an intrinsic long--short
orientation but no clockwork-like zero mode.

For the untwisted affine extension, order the nodes as
\(\alpha_0=-\theta,\alpha_1,\alpha_2\), where
\(\theta=3\alpha_1+2\alpha_2\). Then

\[
A=\begin{pmatrix}
2&0&-1\\
0&2&-1\\
-1&-3&2
\end{pmatrix}.
\]

Its primitive Kac marks \(a=(1,3,2)^{\mathsf T}\) and comarks
\(a^\vee=(1,1,2)^{\mathsf T}\) obey

\[
a^{\mathsf T}A=0,
\qquad
Aa^\vee=0.
\]

Thus the triple is genuine root-incidence data, but left and right null data
are not interchangeable.

## The executable-pairing gate

Two canonical positive symmetric forms are available from the same Cartan
packet. The root Gram form is

\[
G_{\mathrm{root}}=A\operatorname{diag}(3,1,3)
=\begin{pmatrix}6&0&-3\\0&2&-3\\-3&-3&6\end{pmatrix},
\]

with kernel \(a=(1,3,2)^{\mathsf T}\) and spectrum

\[
0,\qquad 7-\sqrt7,\qquad 7+\sqrt7.
\]

The dual or coroot form is

\[
G_{\mathrm{coroot}}=\operatorname{diag}(1,3,1)A
=\begin{pmatrix}2&0&-1\\0&6&-3\\-1&-3&2\end{pmatrix},
\]

with kernel \(a^\vee=(1,1,2)^{\mathsf T}\) and spectrum

\[
0,\qquad 5-\sqrt7,\qquad 5+\sqrt7.
\]

Both are exact, positive-semidefinite, and gapped away from their null ray.
They define different relative profiles. Algebraic availability therefore does
not authorize either profile as a physical coupling. A source action must say
which representation and pairing the flavor fields execute.

## Sign, magnitude, RG, and threshold audit

The labelled \(G_2\) datum distinguishes long from short roots and has no
diagram automorphism exchanging them. That orientation is not yet the sign of
\(g_n-g_m\): a Gram quadratic form is unchanged under reversal of its kernel
vector, and the map from Dynkin nodes to the two flavor species is absent.

Multiplying either Gram form by a positive coefficient \(\kappa\) preserves
all Cartan and kernel statements. Hence the root datum fixes no absolute
portal magnitude or threshold clock.

The strict nonzero spectral gap is a conditional algebraic basin: it protects
the null ray inside the declared quadratic packet. It is not an RG basin for
an anomaly-complete matter theory. No beta functions, wavefunction factors,
finite matching coefficients, widths, or decoupling limits follow from the
root datum alone.

Finally, no admitted constructor maps a Dynkin-node perturbation into the
faithful `physical16` quotient and then into calibrated detector units.
Calling a mark an observable would confuse a mathematical discriminator with
a physical instrument.

## Classification

- Finite \(G_2\): orientation rigidifier, not a profile selector.
- Affine \(G_2\) plus a declared root pairing: relative mark-ray selector and
  gapped rigidifier.
- Affine \(G_2\) plus a declared coroot pairing: a different relative
  comark-ray selector and gapped rigidifier.
- Bare affine \(G_2\): neither chooses the executable pairing nor supplies the
  flavor embedding, sign, absolute scale, RG completion, thresholds, or
  instrument.

This is not yet a Deutschian explanation of the portal. It makes the triple
bond hard to vary but leaves the route from that bond to flavor easy to vary.

## Smallest exact falsifier

The same affine Cartan matrix produces two canonical symmetric positive forms:
one has kernel \((1,3,2)\), the other \((1,1,2)\). Both have strict gaps. Without
a source-derived root-versus-coroot coupling functor, the triple profile is not
the uniquely executable consequence of the source.

## Successor

Seek a source action whose matter representation itself chooses the root mark
ray, assigns its oriented nodes to the physical flavor species, and fixes the
coefficient \(\kappa\). Only that completed action can legitimately determine
the anomaly-free beta functions, finite thresholds, and a calibrated
`physical16` response Jacobian.

Verification:

- checker:
  research/flavor/checkers/wp797_affine_g2_root_coroot_portal_typing.py
- generated result:
  research/flavor/results/wp797_affine_g2_root_coroot_portal_typing.json
- exact invocation:
  uv run --with sympy python research/flavor/checkers/wp797_affine_g2_root_coroot_portal_typing.py
- non-simply-laced gauge construction:
  [Cecotti and Del Zotto](https://arxiv.org/abs/1207.7205)
- \(G_2\) symmetrizer convention:
  [Tsymbaliuk](https://arxiv.org/abs/2305.00810)
