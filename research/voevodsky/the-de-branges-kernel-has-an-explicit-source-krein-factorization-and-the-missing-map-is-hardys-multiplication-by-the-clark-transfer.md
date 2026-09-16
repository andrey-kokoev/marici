# The de Branges kernel has an explicit source Krein factorization, and the missing map is Hardy multiplication by the Clark transfer

> **Correction.** The positive de Branges--Rovnyak filler uses the co-defect
> `I - M_Theta M_Theta^*`, not the input defect `I - M_Theta^* M_Theta`.
> See `correction-the-de-branges-filler-is-the-co-defect-not-the-input-defect.md`.

## Laplace feature for the Cauchy denominator

For upper-half-plane points \(z,w\),

\[
\frac1{i(\overline w-z)}
=
\int_0^\infty
 e^{izr}
 e^{-i\overline w r}
\,dr.
\]

Define Hardy features

\[
a_z(r)=
\frac1{\sqrt{2\pi}}
E(z)e^{izr},
\]

\[
b_z(r)=
\frac1{\sqrt{2\pi}}
E^*(z)e^{izr}.
\]

Both lie in \(L^2(\mathbb R_+,dr)\) for \(\operatorname{Im}z>0\).

Their Grams satisfy

\[
\langle a_w,a_z\rangle
-
\langle b_w,b_z\rangle
=
\frac{
E(z)\overline{E(w)}
-
E^*(z)\overline{E^*(w)}
}{
2\pi i(
\overline w-z
)
}.
\]

The right side is the de Branges kernel.

Thus the kernel already has a fully explicit source-defined Krein factorization

\[
\mathcal D(z,w)
=
\langle a_w,a_z\rangle
-
\langle b_w,b_z\rangle.
\]

## Candidate contraction

Since

\[
E^*(z)=
\Theta(z)E(z),
\]

we have

\[
b_z(r)=
\Theta(z)a_z(r).
\]

On the Hardy realization, the candidate map is multiplication by the Clark transfer:

\[
C=M_\Theta.
\]

The positive defect feature would be

\[
d_z=
(
I-M_\Theta^*M_\Theta
)^{1/2}a_z.
\]

If \(M_\Theta\) is contractive, then

\[
\mathcal D(z,w)
=
\langle d_w,d_z\rangle.
\]

This is the desired positive Gram construction.

## Theta-source formula for the multiplier

The previous doubled-shift calculation gives

\[
\Theta(z)
=
\frac{
F(s)+F(-s)-F'(s)+F'(-s)
}{
F(s)+F(-s)+F'(s)-F'(-s)
},
\qquad
s=-iz.
\]

Therefore the candidate contraction is explicitly determined by the theta source. No zero list is used.

## Exact remaining condition

Multiplication by \(\Theta\) is contractive on upper-half-plane Hardy space exactly when

\[
\Theta\in H^\infty,
\qquad
\|\Theta\|_\infty\le1.
\]

Equivalently,

\[
|E^*(z)|
\le
|E(z)|
\]

throughout the upper half-plane.

Thus the signed construction is complete, and the positive construction reduces to one operator-norm assertion:

\[
\|M_\Theta\|
\le1.
\]

## Functional interpretation

The missing cross-storage is not an arbitrary operator on the theta-tail space. After Hardy dilation, it is the canonical multiplication operator \(M_\Theta\).

The coherence tetrahedron has the following control realization:

- incoming feature: \(a_z\);
- outgoing feature: \(b_z\);
- feedback map: \(M_\Theta\);
- common storage defect: \(I-M_\Theta^*M_\Theta\);
- positive filler: its square root.

Every coordinate and map is now explicit. The only unresolved question is whether the defect operator is positive.

## Scope

Positivity of the defect is equivalent to the global Schur/Hermite--Biehler property and therefore to RH. The factorization does not prove that property, but it identifies the unique canonical operator whose positivity would complete the construction.
