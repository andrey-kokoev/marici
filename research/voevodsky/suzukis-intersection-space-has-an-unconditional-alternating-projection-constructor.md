# Suzuki's intersection space has an unconditional alternating-projection constructor

## A genuine ambient contraction

Suzuki defines unconditionally the conjugate-linear isometric involution

\[
K=\mathcal F^{-1}M_\Theta J\mathcal F,
\qquad
K^2=I,
\]

using the boundary-unimodular function `Theta=E#/E`. Let

\[
H_+=L^2(0,\infty)
\]

in the time-side Hardy realization, and define

\[
V=H_+\cap K H_+.
\]

Unlike a finite-rung Douglas map, the orthogonal projection onto `V` is an ambient source-defined contraction available before any positivity assertion.

## Explicit construction by alternating projections

Let

\[
P=P_{H_+},
\qquad
Q=P_{KH_+}=KPK.
\]

Both are orthogonal projections; the second identity follows because `K` is an isometric involution. Von Neumann's alternating-projection theorem gives

\[
\boxed{
P_V=s\!\!\lim_{n\to\infty}(PQ)^nP.
}
\]

Equivalently, one may use the symmetric positive contractions

\[
(PQP)^n
\]

on `H_+`. Their strong limit is `P_V`. Consequently

\[
P_V^2=P_V=P_V^*,
\qquad
\|P_V\|\le1.
\]

This is a non-tautological contraction theorem: its norm bound follows solely from orthogonal projection geometry and not from Weil positivity.

## Exact leakage characterization

For `f in H_+`, membership in `V` means

\[
Kf\in H_+.
\]

Thus

\[
V=\ker(P_-K|_{H_+}).
\]

The projection `P_V` is therefore the maximal positive-carrier projection that kills Suzuki's Hardy leakage:

\[
P_-KP_V=0.
\]

This gives an exact abstract realization of the previously requested operation:

\[
\text{ambient source state}
\xrightarrow{P_V}
\text{leakage-free state}.
\]

No zero list, Blaschke product, or finite Gram diagonalization is needed to define it.

## Why this does not yet prove the Weil identity

Projection removes every component outside the intersection. To factor the original Weil form, one would need a source-faithfulness identity of the form

\[
Q_W(f,g)
=
\langle P_VA_{src}f,P_VA_{src}g\rangle
\]

or at least a positive decomposition of the discarded norm. Suzuki proves the corresponding identification with his Weil Hilbert space under RH, using model-space/de Branges structure. He does not prove it unconditionally.

The unconditional projection only gives

\[
\|A_{src}f\|^2
=
\|P_VA_{src}f\|^2
+
\|(I-P_V)A_{src}f\|^2.
\]

There is no source identity assigning the second term the sign or arithmetic role needed to reconstruct `Q_W`. Declaring it null would change the terminal polarization.

## Collapse risk is real

Suzuki explicitly notes that determining whether

\[
V(0)=\{0\}
\]

unconditionally is extremely difficult. If `V=0`, then `P_V=0`; the construction remains a perfectly valid contraction but produces the zero carrier. Therefore positivity and contractivity alone do not provide faithfulness.

This parallels the semilocal analytic-cokernel collapse:

- the quotient/projection exists canonically;
- it kills the obstruction by construction;
- but it may also kill the arithmetic signal;
- proving nontriviality and exact source identification carries the missing spectral content.

## Finite alternating approximants

The operators

\[
R_n=(PQP)^n
\]

are explicit positive contractions on `H_+` and converge strongly to `P_V`. They provide a canonical hierarchy independent of Gaussian Gram positivity. For every source vector `f`,

\[
\|R_nf\|\le\|f\|.
\]

However, finite `n` only suppresses leakage; it does not eliminate it. Moreover, strong convergence supplies no uniform lower bound

\[
\|P_Vf\|\ge c\|f\|
\]

on a dense translation-invariant Gaussian family unless `V=H_+`. Such a bound would make the projection injective with closed range on that family and would again approach the full innerness gate.

## Precise missing comparison

The best possible source theorem around this projection would be

\[
\boxed{
Q_W(f,g)
=
\langle P_VA_{src}f,P_VA_{src}g\rangle
+
Q_{\partial}(f,g),
}
\]

where `Q_partial` is derived from endpoint--gamma completion and independently positive. This would retain, rather than silently discard, the orthogonal complement.

But an off-axis zero makes `Q_W` negative on a localized test while both displayed terms would be nonnegative. Therefore universal positivity of `Q_partial` is equivalent to eliminating the off-axis defect. The identity is a valid target, not a consequence of alternating projections.

## Disposition

Suzuki does contain a genuine unconditional ambient contraction:

\[
\boxed{
P_V=s\!\!\lim(PKPKP)^n
\quad\text{(up to the chosen placement of }P\text{)},
}
\]

namely projection onto `H_+ intersect K H_+`. It canonically kills Hardy leakage and avoids finite-dimensional Douglas circularity.

Its obstruction is faithfulness, not contractivity. No unconditional theorem identifies the projected norm with the complete endpoint--gamma--prime Weil form, and the intersection may collapse. The next exact gate is therefore an arithmetic Green identity for the discarded complement, not construction of another contraction.
