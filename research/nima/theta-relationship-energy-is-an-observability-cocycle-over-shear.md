# Theta relationship energy is an observability cocycle over shear transport

Owner: marici.Nima

## Question

Can the positive reciprocal tail–seam energy be reconstructed from the
endpoint unipotent shear whose off-diagonal coefficient is the scalar
transform?

## Endpoint holonomy is not energy-faithful

For a source path on \([a,b]\), the integrating-factor transport is

\[
S_{a,b}=
\begin{pmatrix}
1&F_{a,b}\\
0&1
\end{pmatrix},
\qquad
F_{a,b}=\int_a^b f(v)e^{sv}\,dv.
\]

There exist nonzero compactly supported source paths for which

\[
F_{a,b}=0.
\]

Such a path has the same endpoint shear as the zero source:

\[
S_{a,b}=I.
\]

Nevertheless, its internal tail path and any faithful positive path energy are
nonzero. Therefore no function of the endpoint shear alone can recover that
energy.

More formally, let \(E(f)\ge0\) be faithful on source paths. If a map
\(\Phi\) satisfied

\[
E(f)=\Phi(S_{a,b}(f)),
\]

then every nonzero cancelling source with \(S_{a,b}(f)=I=S_{a,b}(0)\) would
give

\[
E(f)=\Phi(I)=E(0)=0,
\]

contradicting faithfulness.

The positive energy does not descend through the endpoint-holonomy quotient.

## Minimal higher-rung state

Let a state \(x_a\) propagate across an interval by

\[
x_b=S_{a,b}x_a.
\]

Suppose the interval carries a source-derived output or energy density
represented by an observation operator \(C(q)\). Define the interval
observability Gramian

\[
W_{a,b}
=
\int_a^b
U(q,a)^*C(q)^*C(q)U(q,a)\,dq,
\]

where \(U(q,a)\) is the internal transport from \(a\) to \(q\). Then

\[
E_{a,b}(x_a)=x_a^*W_{a,b}x_a.
\]

The minimal relationship object that retains both endpoint transport and
internal energy is therefore the pair

\[
(S_{a,b},W_{a,b}),
\]

not the shear \(S_{a,b}\) alone.

## Exact cascade law

For \(a<b<c\),

\[
S_{a,c}=S_{b,c}S_{a,b}.
\]

The energy on the second interval is evaluated on
\(x_b=S_{a,b}x_a\). Consequently,

\[
W_{a,c}
=
W_{a,b}
+
S_{a,b}^*W_{b,c}S_{a,b}.
\]

Thus the Gramian is a positive cocycle over the transport semigroup.

The corresponding composition law is

\[
(S_2,W_2)\circ(S_1,W_1)
=
\left(
S_2S_1,\,
W_1+S_1^*W_2S_1
\right).
\]

Associativity follows from associativity of matrix multiplication:

\[
\begin{aligned}
W_{123}
&=W_1+S_1^*W_2S_1
  +S_1^*S_2^*W_3S_2S_1\\
&=W_1+S_1^*(W_2+S_2^*W_3S_2)S_1.
\end{aligned}
\]

This is the exact systems form of relationship-energy accumulation.

## Zero versus energy

At a scalar transform zero, the total transport may satisfy

\[
S_{a,c}=I.
\]

The Gramian need not vanish:

\[
W_{a,c}>0.
\]

Hence identity holonomy means zero net transfer coefficient, not zero internal
activity. The pair \((I,W)\) distinguishes a nontrivial cancelling
relationship from the empty relationship \((I,0)\).

This removes the topological puncture error and the endpoint-energy erasure in
one construction.

## Relation to the reciprocal seam

The homogeneous doubled transport supplies a seam-selective metric statement:
its directional condition number is uniformly bounded on the half-line only
when \(\operatorname{Re}(s)=1/2\). The shear endpoint, by contrast, exists and
is invertible everywhere.

The required global object should therefore be a completed cocycle pair

\[
(S_s,W_s),
\]

where:

1. \(S_s\) is the boundary-bearing restricted-product transport;
2. \(W_s\) is constructed from the reciprocal tail, seam, primitive,
   prime-square, connected-tail and archimedean observation channels;
3. the cascade law survives cutoff completion;
4. \(W_s\) is faithful on every admissible zero-dynamics state; and
5. its source graph norm is not fitted from the completed scalar section.

## What this does not prove

The abstract Gramian cocycle is automatically positive once an observation
operator is supplied. That positivity is not an RH theorem. The unresolved
content is deriving the correct \(C(q)\), state topology and boundary rows
from the theta/Tate source and proving completion stability.

The construction becomes circular if \(C(q)\) or \(W_s\) is selected merely
to make the completed scalar zero-free.

## Finite falsifiers

- two nonzero source paths with the same endpoint shear but different proposed
  energies;
- failure of the Gramian cascade identity on adjacent intervals;
- an observation row not derived from a typed source or boundary port;
- cutoffwise positive Gramians whose least observable direction collapses;
- a completed zero-dynamics state lying in the kernel of the full Gramian;
- erasure of primitive or prime-square channels during scalar compression.

## Outcome

Relationship energy lives one categorical rung above endpoint transport. It
is a positive cocycle over the shear, not a scalar function of the shear.
This is the minimal architecture capable of retaining both destructive
interference and the internal energy of the cancelling path.
