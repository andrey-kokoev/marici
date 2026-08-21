# Finite Deck Norm Obstruction

For a surjective finite deck map \(q:G\twoheadrightarrow H\), let

\[
q^*:\operatorname{Fun}(H)\to\operatorname{Fun}(G)
\]

be pullback and let \(q_!\) be unnormalized fiber sum.  Then

\[
\boxed{
q_!q^*=|\ker q|\,\operatorname{id}.
}
\]

The Betti-side induction and projection satisfy the dual identity

\[
q_*q^!=|\ker q|\,\operatorname{id}.
\]

Therefore a retraction of pullback requires the averaged transfer

\[
\frac1{|\ker q|}q_!.
\]

But the frozen identity selector obeys

\[
q_!\delta_{0,G}=\delta_{0,H},
\]

whereas averaging gives

\[
\frac1{|\ker q|}q_!\delta_{0,G}
=
\frac1{|\ker q|}\delta_{0,H}.
\]

Consequently

\[
\boxed{
\text{strict retraction normalization}
+
\text{frozen identity-selector normalization}
}
\]

are compatible if and only if \(|\ker q|=1\).

The checker verifies every canonical cyclic quotient
\(C_n\twoheadrightarrow C_m\) with \(m\mid n\le30\).

## Interpretation

This is not a failure of the Mackey/Beck--Chevalley calculus.  It is the
expected degree or norm of a finite covering.  The obstruction arises only
when one demands both:

1. categorical splitting/ambidexterity normalized to the identity; and
2. the source's unscaled identity-chamber selector.

The five-site Kummer branches have kernel orders \(2^{|B|}\), so the
conflict is unavoidable at every nontrivial branch.  The earlier
selector-non-descent result is stronger for the frozen physical functional:
it fails even before one chooses a normalization.

Radiative memory avoids this finite-degree conflict.  Its quotient readout
descends through kernel annihilation; it does not require a finite-cover
trace to split the quotient.

Artifacts:

- `research/nima/check_finite_deck_norm_obstruction.py`
- `research/nima/results/finite-deck-norm-obstruction.json`
