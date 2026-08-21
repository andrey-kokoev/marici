# Deck Readout Variance Correction

## The typing issue

For a finite deck quotient \(q:G\to H\), the coefficient and Betti factors
in Entry 1225 do not have the same functorial variance.

Let \(\operatorname{Fun}(H,\mathbb Q)\) be the coefficient sheet space and
\(\mathbb Q[G]\) the Betti sheet-orbit space, paired by evaluation.  The
canonical maps are

\[
q^*: \operatorname{Fun}(H)\longrightarrow\operatorname{Fun}(G)
\]

and

\[
q_*:\mathbb Q[G]\longrightarrow\mathbb Q[H],
\qquad
q_*\Gamma_g=\Gamma_{q(g)}.
\]

They satisfy the exact adjunction

\[
\boxed{
\langle q^*c,\Gamma\rangle_G
=
\langle c,q_*\Gamma\rangle_H.
}
\]

The unnormalized fiber sum \(q_!\) on coefficient functions is the linear
dual of pullback, but it is not the same typed operation as Betti
specialization.  Applying transfer to both factors is not the physical
comparison supplied by the coefficient--Betti pairing.

## Consequence for the identity selection

Under coefficient pullback,

\[
q^*\delta_{0,H}=\mathbf 1_{\ker q},
\]

not \(\delta_{0,G}\) unless \(q\) is injective.  This is not automatically
a defect: every sheet in \(\ker q\) specializes to the same branch sheet.
The paired Betti pushforward accounts for that coalescence through the
adjunction.

Thus the earlier statement that fiber-sum transfer “repairs physical
selection variance” was too coarse.  It repairs a covariant algebraic
selection law on functions.  The cosmological source instead demands a
two-sided coefficient--Betti calculus with pullback on coefficients,
pushforward on cycles, and a pairing between them.

## Revised architectural claim

\[
\boxed{
\text{physical readout is a paired mixed-variance correspondence, not a
single functorial invariant algebra.}
}
\]

The finite Mackey/Beck--Chevalley calculus remains valid algebraically.  Its
physical admission must be tested on the paired coefficient and relative
Betti objects, including orientation, support, boundaries, and normalization.

For the five-site branch strata, the remaining source test is precisely
whether the set-level quotient in Entry 1224 lifts to the Betti chain map
\(q_*\) above and satisfies the adjunction with the Kummer coefficient
pullback.
