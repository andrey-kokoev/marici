# Inaccessible record carriers generate a reversal cost

## Question

When reversible source dynamics has distributed relational information across
many carriers, what prevents a local controller from undoing the apparent
decoherence?

## Claim boundary

After (N) independent conditional collisions, let the single-carrier overlap
be

\[
c=|\langle e_0|e_1\rangle|,
\qquad 0<c<1.
\]

Suppose a controller applies the exact inverse collision to (k) accessible
carriers and has no access to the remaining (N-k). The accessible carriers
return to their source state, but the inaccessible carriers retain conditional
overlap

\[
c^{N-k}.
\]

Consequently, the recovered system coherence is multiplied by (c^{N-k}).
Full source coherence is restored only when every independently coupled carrier
is reversed, unless (c=1).

For a declared recovery threshold (eta), the minimum control count is the
smallest (k) satisfying

\[
c^{N-k}\geq\eta.
\]

This is a control-access theorem for the product collision model. It is not a
claim that all natural environments factorize or that inaccessible information
is fundamentally destroyed.

## Exact finite witness

Take (c=3/5) and (N=10).

- Restoring at least one half of the source coherence requires control of nine
  carriers.
- Restoring at least nine tenths requires control of all ten carriers.
- Reversing five carriers leaves coherence factor ((3/5)^5), despite having
  undone half of the visible collision history.

The control requirement is therefore extensive in the number of independent
record carriers for high-fidelity reversal.

## Causal access gate

Let carrier (i) lie at control distance (d_i), and let (v) be the admitted
maximum propagation speed for the reversal operation. Any protocol requiring a
set (K) of carriers obeys

\[
T_{\rm reverse}\geq\max_{i\in K}\frac{d_i}{v}.
\]

The inequality does not create irreversibility. It turns the spatial spread of
independent records into a lower bound on when reversal can become operationally
available.

## Copy-count hostile

If (N) observer labels all read one common conditional carrier, their visible
copy count is (N), but the control rank is one. One inverse operation can then
erase every nominal copy. Therefore neither observer count nor repeated scalar
agreement measures reversal cost.

The source-derived quantity is the number and geometry of independently
conditioned carrier factors required by the inverse constructor.

## Categorical form

Let (U_i) be the collision for carrier (i). The global recording arrow is

\[
U=U_N\circ\cdots\circ U_1.
\]

For an accessible subset (K), the partial inverse cancels only its own
factors. The residual arrow is supported on the complement:

\[
U_K^{-1}\circ U=U_{K^c}
\]

when the declared collision factors commute. If they do not commute, a partial
inverse additionally requires the source order and its coherence cells; carrier
count alone is insufficient.

## Disposition

The finite product-collision theorem is closed. Apparent irreversibility is
retyped as a failure of available control to cover the support of the global
recording arrow. The next deeper question is whether realistic local dynamics
makes the inverse cost grow only spatially, or also computationally and
thermodynamically.

Verification is provided by
`research/nima/checkers/check_inaccessible_record_reversal_cost.py` and
`research/nima/results/inaccessible-record-reversal-cost.json`.
