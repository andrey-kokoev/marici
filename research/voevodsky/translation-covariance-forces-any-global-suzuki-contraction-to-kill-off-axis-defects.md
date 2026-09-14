# Translation covariance forces any global Suzuki contraction to kill off-axis defects

## Proposed global constructor

The previous reduction asks for a common positive source representation and a contraction

\[
A_B=C A_S,
\qquad \|C\|\le1,
\]

where `A_S` is the positive Schur feature and `A_B` is the forbidden-divisor feature. A source-defined construction should respect translation of test functions, because additive translation is the basic symmetry behind the Weil convolution pairing and Suzuki's screw line.

This covariance requirement produces a sharp obstruction.

## Source translations are unitary

Let

\[
(\tau_a f)(x)=f(x-a),
\qquad a\in\mathbb R.
\]

On every positive Fourier/Hardy source carrier, translation is represented by a unitary group

\[
U_a=e^{-iaL},
\qquad \|U_av\|=\|v\|.
\]

Assume the positive feature map is covariant:

\[
A_S\tau_a=U_aA_S.
\]

A natural global comparison must intertwine this action with the divisor feature action:

\[
C U_a=V_a C,
\qquad
A_B\tau_a=V_aA_B.
\]

## Off-axis evaluations are nonunitary characters

A divisor coordinate at a complex spectral point `rho` is an evaluation functional of a Fourier--Laplace transform. Under translation it obeys

\[
\widehat{\tau_af}(\rho)
=e^{-ia\rho}\widehat f(\rho).
\]

Write

\[
\rho=\alpha+i\beta.
\]

Then

\[
|e^{-ia\rho}|=e^{a\beta}.
\]

If `beta != 0`, this character is exponentially unbounded in one time direction. It cannot be a nonzero subrepresentation of a unitary real-translation group on a positive Hilbert space.

## Contractivity contradiction

Take `f` with nonzero `rho`-coordinate in `A_Bf`. Covariance and contractivity give

\[
\begin{aligned}
\|V_aA_Bf\|
&=\|A_B\tau_af\|\\
&=\|C A_S\tau_af\|\\
&=\|C U_aA_Sf\|\\
&\le\|A_Sf\|.
\end{aligned}
\]

The right side is independent of `a`. But the `rho` component on the left grows as

\[
e^{a\beta}|(A_Bf)_\rho|
\]

in one direction. Letting `a` tend to the corresponding infinity forces

\[
(A_Bf)_\rho=0.
\]

Since this holds for every source vector,

\[
\boxed{
\text{a translation-covariant contractive Hilbert comparison annihilates every off-axis divisor coordinate.}
}
\]

Thus a faithful global contraction exists only if the forbidden divisor is absent.

## Paired orbit does not repair the growth

One might retain both `rho` and `bar(rho)`. Their translation matrix is

\[
V_a=
\begin{pmatrix}
e^{-ia\rho}&0\\
0&e^{-ia\bar\rho}
\end{pmatrix}.
\]

Its singular values are

\[
e^{a\beta},
\qquad e^{-a\beta}.
\]

Their product is one, reflecting preservation of the orbit's indefinite Krein form, but the operator norm is

\[
\|V_a\|=e^{|a\beta|}.
\]

Hence conjugate pairing makes the representation Krein-unitary, not Hilbert-unitary. It cannot be contractively intertwined with a positive unitary source representation unless both coordinates vanish.

This is the representation-theoretic version of the `(1,1)` signature obstruction.

## Consequence for endpoint--gamma--prime constructions

Any common source map assembled from translation-covariant positive operations--Fourier transform, multiplication by unimodular real characters, orthogonal projection commuting with translations, or positive spectral calculus of the translation generator--inherits a unitary real-translation action.

Therefore no contraction built solely from such operations can absorb a nonzero off-axis Blaschke defect while preserving its arithmetic evaluation. It must either:

1. annihilate the defect, which proves the forbidden divisor absent;
2. break translation covariance;
3. use an indefinite metric;
4. restrict translations to a bounded semigroup; or
5. alter the terminal Weil polarization.

Options 2 and 5 violate the global source symmetry; option 3 returns to the Pontryagin factorization; option 4 may support a local one-sided estimate but cannot directly prove the bilateral Weil criterion.

## Why semigroup restriction is a genuine remaining aperture

For `a>=0`, one member of an off-axis pair decays while the other grows. Selecting only the decaying member defines a contractive semigroup, but conjugation symmetry exchanges it with the growing member. The completed Weil form requires both members and their cross-polarization. Therefore a one-sided semigroup carrier must acquire a boundary coupling that recovers the conjugate branch without restoring exponential growth.

This is exactly the kind of boundary sewing sought in the relative-trace/co-Poisson route. The present theorem gives its acceptance test: the sewn positive representation must reproduce the paired Krein character while remaining contractive. Ordinary orthogonal doubling cannot do so.

## Disposition

The desired global source contraction is obstructed before any norm estimate:

\[
\boxed{
\text{positive unitary translation covariance}
+
\text{contractive faithful divisor intertwiner}
\Longrightarrow
\operatorname{Im}\rho=0.
}
\]

Hence a translation-covariant Suzuki contraction would itself prove the spectral statement. No formal composition of already-known positive source operations can construct it in the presence of an off-axis orbit. The only nonredundant abstract continuation is a one-sided semigroup plus a genuinely nonorthogonal boundary-sewing mechanism.
