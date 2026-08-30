# Complete rational-exact classification of the magnetic kernel

Fix `g>=2`, a finite admitted even-depth set `A`, a finite Laurent source
window, and the full target.  Let `T` be the visible positive-depth tower set.
Let `v_0` indicate visibility of the depth-zero tower, and let `v_1,v_2`
indicate visibility of the two grade-two exceptional circuits.

The combinatorial kernel theorem gives the direct basis

\[
\ker M_g
=\langle D_{g,0}\rangle^{v_0}
\oplus\bigoplus_{a\in T}\mathbb QD_{g,a}
\oplus\langle E_1^-\rangle^{v_1}
\oplus\langle E_2^-\rangle^{v_2}.
\]

Here an exponent means that the summand is present only when its indicator is
one.

## Exact named classes

The depth-zero tower has rational primitive

\[
\Phi_{g,0}
=-\frac{(g+3)!}{6(g-1)(1+u)^{g-1}}.
\]

At grade two,

\[
E_1^-=1-\bar z^{-2}
\]

has primitive

\[
\Phi_1=-\frac{20(z+\bar z)}{1+u}.
\]

The second circuit

\[
E_2^-=\bar z^{-8}-3z^{-4}\bar z^2+2z^{-6}
\]

has primitive

\[
\Phi_2=
-\frac{4(-2\bar z^8z+3\bar z^7+5z^7)}
{\bar z^7z^7(1+u)}+8\bar z^{-7}.
\]

Thus both local parity-collision circuits are rationally contractible.

## Necessary and sufficient criterion

For each `a in T`, put

\[
r_{g,a}=-g(g+1)C_{g+1}a^{\overline{g-1}}.
\]

Every positive-depth tower has the normal form

\[
F_g(D_{g,a})=d\Phi_{g,a}+r_{g,a}\eta,
\qquad
\eta=d\log\frac{u}{1+u}.
\]

Therefore an arbitrary kernel vector

\[
D=c_0D_{g,0}+\sum_{a\in T}c_aD_{g,a}
+e_1E_1^-+e_2E_2^-
\]

is rational-exact if and only if

\[
\boxed{\sum_{a\in T}c_ar_{g,a}=0.}
\]

Sufficiency follows by summing the rational primitives after the logarithmic
coefficient cancels.  Necessity follows because `eta` has nonzero residue at
`u=0`, whereas every rational derivative has zero residue.

Choosing any reference depth `a_0 in T`, a basis of the rational-exact
positive-depth combinations is

\[
R_{g,a}^{(a_0)}
=r_{g,a_0}D_{g,a}-r_{g,a}D_{g,a_0},
\qquad a\in T\setminus\{a_0\}.
\]

These vectors may be divided by the pairwise gcd for a primitive integral
basis element, but rational exactness itself is independent of that
normalization.

## Dimension law

Let `p=|T|`.  Then

\[
\boxed{
\dim K_g^{rat}
=v_0+v_1+v_2+\max(p-1,0),
}
\]

and

\[
\boxed{
\dim(\ker M_g/K_g^{rat})=\mathbf1_{p>0}.
}
\]

Source cutoffs only change the visibility indicators and the set `T`; they do
not change the criterion.  A partially visible exceptional support is not a
class and contributes nothing.

This classification is ordinary rational de Rham exactness.  A depth-labelled
residue associated grade intentionally forbids the cross-depth sum in the
boxed criterion and is a different object.
