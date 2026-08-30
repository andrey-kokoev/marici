# Bell base/fiber factorization audit

Entry 1580 proves that a positive momentum selection preserves the photon Bell
packet when it acts as

\[
S_{\rm base}\boxtimes 1_{\rm helicity}.
\]

The present exact audit verifies the corresponding algebraic naturality.  On a
two-bin momentum base and a two-dimensional helicity fiber,

\[
[S\otimes I,I\otimes T]=0
\]

for an arbitrary fiber operator \(T\).  The correctly typed Cut tensor is the
mixed-variance coevaluation \(\omega\in V\otimes V^*\), and it is invariant
under \(U\otimes U^{-T}\).

This does **not** complete the Marici realization.  Entry 45's word “support”
denotes signed derivative support in polarization-type scaffold variables.  It
does not provide a positive accepted-event support or relative pushforward on
the momentum base.  Thus the existing transmutation/Cut theorem is compatible
with a Bell-safe support lens, but does not construct that lens.

The next source-level datum must be a positive momentum-base chain or measure
and its pushforward.  Only then can one test that its action is helicity-blind.

Reproduce with:

```text
uv run --with sympy python research/nima/check_bell_base_fiber_factorization.py
```
