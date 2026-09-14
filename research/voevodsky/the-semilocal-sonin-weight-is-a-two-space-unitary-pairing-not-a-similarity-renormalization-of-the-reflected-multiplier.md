# The semilocal Sonin weight is a two-space unitary pairing, not a similarity renormalization of the reflected multiplier

## Exact source formulas

In Connes--Consani--Moscovici, arXiv:2310.18423, the finite-stage canonical spectral measure is

\[
dm_S(s)
=
\left|
\prod_{v\in S}
L_v(1/2-is)
\right|^2ds.
\]

Their unitary canonical transform is

\[
V_S:L^2(X_S)^{K_S}
\longrightarrow
L^2(\mathbb R,dm_S).
\]

The dual Hardy--Titchmarsh transform lands instead in

\[
L^2
\left(
\mathbb R,
|E_S(s)|^2ds
\right),
\qquad
E_S(s)=
\prod_{p\in S}
L_p(1/2+is).
\]

Proposition 4.4 pairs these two different weighted spaces by the unweighted integral

\[
\langle\xi,\eta\rangle_R
=
\int_\mathbb R
\xi(s)\eta(s)ds,
\]

and proves that this pairing corresponds to the original Hilbert product on the semilocal space.

## Semilocal amplification

For the Sonin amplification `Sigma_S`, Proposition 4.6(ii) gives

\[
\mathcal F_\mu w_S(\Sigma_Sf)(s)
=
\mathcal F_\mu w(f)(s)
\prod_{p\in S\setminus\{\infty\}}
L_p(1/2+is)^{-1}.
\]

Proposition 4.7 then uses the two opposite local factors

\[
L_p(1/2+is)^{-1}
\]

and

\[
L_p(1/2-is)
=
\overline{L_p(1/2+is)}
\]

inside the dual/canonical pairing. Their product cancels against the weighted measures, yielding

\[
\boxed{
\langle\Sigma_Sf,\Sigma_Sg\rangle
=
\langle f,g\rangle.
}
\]

Theorem 4.6 concludes that

\[
\Sigma_S:
\mathcal S(\mathbb R,e^\lambda)
\overset{\sim}{\longrightarrow}
\mathcal S(X_S,\lambda)
\]

is a Hilbertian isomorphism.

## Why this is not a scalar similarity

A previous target proposed a scalar multiplication weight `W_S` and the conjugated operator

\[
\widetilde T_S
=W_SM_{\Theta_S}^*W_S^{-1}.
\]

If `W_S` and `M_Theta` are scalar multiplication operators on the same spectral representation, they commute. Hence, on their common domain,

\[
\boxed{
W_SM_{\Theta_S}W_S^{-1}
=M_{\Theta_S}.
}
\]

A scalar similarity cannot change the reflected multiplier, its essential modulus, or its expansive boundary channels.

Likewise, changing from `L2(w ds)` to another scalar-weighted `L2` space does not reduce the norm of a multiplier acting within one space:

\[
\|M_\Theta\|_{L^2(wds)\to L^2(wds)}
=
\operatorname*{esssup}|\Theta|
\]

for every positive weight `w` with the usual support assumptions.

Therefore the semilocal Sonin construction cannot validate the proposed similarity-renormalization inequality.

## Correct two-space structure

The source instead provides a pair of spaces

\[
H_S^+
=
L^2
\left(
\mathbb R,
|E_S(s)|^2ds
\right),
\]

\[
H_S^-
=
L^2(\mathbb R,dm_S),
\]

with a bilinear duality

\[
H_S^+
\times
H_S^-
\longrightarrow
\mathbb C.
\]

The inverse Euler multiplier acts in one direction and the conjugate Euler multiplier acts in the other. Positivity occurs only after pairing the two directions through their common semilocal origin.

Thus the correct architecture is not

\[
H_S
\xrightarrow{W_SM_\Theta W_S^{-1}}
H_S,
\]

but

\[
\boxed{
H_S^+
\xleftrightarrow[\text{canonical transform}]
{\text{dual transform}}
H_S^-.
}
\]

This is a genuine contratower.

## Two-space Euler cancellation

At one prime, write

\[
a_p(s)=L_p(1/2+is)^{-1},
\qquad
b_p(s)=L_p(1/2-is).
\]

For real `s`,

\[
b_p(s)=
\overline{a_p(s)^{-1}}.
\]

Therefore the bilinear pairing satisfies the pointwise cancellation

\[
a_p(s)b_p(s)
=
\frac{
L_p(1/2-is)
}{
L_p(1/2+is)
}.
\]

This ratio is unimodular on the critical line. Its phase derivative is exactly the real prime-power current. Hence:

- its modulus disappears in the two-space norm pairing;
- its phase remains in the differentiated/trace pairing.

This is the source mechanism behind simultaneous Hilbert stability and nontrivial Weil prime terms.

## What must replace complementary contractivity

Since no one-space scalar similarity works, the correct target is a two-space observation operator

\[
J_S:H_S^+	o(H_S^-)^*
\]

induced by the source pairing. The completed Weil form should arise from a differentiated pairing

\[
Q_S(f,g)
=
\langle
\nabla_S^+f,
g
\rangle_R
-
\langle
f,
\nabla_S^-g
\rangle_R
+
Q_{end}(f,g),
\]

where the difference of the two connections extracts

\[
\partial_s\log
\frac{L_p(1/2-is)}
     {L_p(1/2+is)}.
\]

A positive realization must then factor this **paired derivative**, not make either one-space multiplier contractive.

## Prime transition

Adjoining `q` changes the dual transform by the inverse factor

\[
L_q(1/2+is)^{-1}
\]

and changes the canonical weighted realization by the conjugate local factor encoded in `dm_(S union {q})`. Proposition 4.7 proves preservation of the original Hilbert product after these two changes are made together.

The transition should therefore be retained as the source commutative square between the dual and canonical transforms, rather than rewritten prematurely as two endomorphisms of one `L2` space. Its invariant statement is

\[
\boxed{
\langle \Sigma_{S\cup\{q\}}f,
\Sigma_{S\cup\{q\}}g
angle
=
\langle \Sigma_Sf,\Sigma_Sg
angle.
}
\]

The exact bilinear-versus-sesquilinear placement of the conjugation matters when differentiating this square; it must be inherited from Proposition 4.4 rather than guessed from scalar multiplier notation.

## Remaining trace identity

The source formulas establish Hilbertian and Fourier stability, but the cited section does not state that the differentiated cross pairing equals the finite-place Weil quadratic form or that it is positive on convolution squares.

The missing theorem remains

\[
\boxed{
W_S(g*g^*)
=
\text{paired connection trace on }
H_S^+\times H_S^-
+
E_{end}(g),
}
\]

followed by a positive factorization of that paired trace.

## Disposition

The proposed scalar essential-norm renormalization is impossible and is not what the semilocal Sonin theorem does. The primary text supplies a stronger but differently typed fact:

\[
\boxed{
\text{inverse Euler factors in the dual tower}
+
\text{conjugate Euler factors in the canonical contratower}
=
\text{an isometric cross pairing}.
}
\]

The next construction must differentiate this preserved two-space pairing and compare the result directly with the finite-place Weil trace formula. One-space contraction theory is the wrong category for this step.
