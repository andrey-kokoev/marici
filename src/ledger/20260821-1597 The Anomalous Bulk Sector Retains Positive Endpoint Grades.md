# Entry 1597 — The Anomalous Bulk Sector Retains Positive Endpoint Grades

## Hard-to-vary claim

For the source bulk--bulk nested commutator with one labelled internal
Bogoliubov variation, the full endpoint recurrence retains positive powers of
the initial-time endpoint.  The Schwinger--Keldysh sector sum cancels the
generic zero-frequency logarithms but does not by itself supply enough hard
suppression to prove ultraviolet convergence under the Hadamard bound.

## Frozen inputs

- the source-checked four-branch to ordered-commutator reduction;
- vertex weight \(t_1^{-2}t_2^{-2}\);
- labelled internal momenta \(q\) and \(k=|p-q|\);
- the coefficient of \(\beta_q\) in the anomalous \(q\)-Wightman function;
- the ordinary Bunch--Davies \(k\)-Wightman function;
- the endpoint primitive recurrence, with no fitted cancellation.

## Result

The anomalous product has frequencies

\[
q-k,\qquad q+k.
\]

After recurrence and the complete nested-commutator sum, the surviving lower
endpoint grades are

\[
0,1,2,
\]

while the observation endpoint has grades \(0,1\).  All generic
zero-frequency logarithmic classes cancel.

Along \(q=Q\), \(k=Q-0.8\), the lower-endpoint coefficients scale as \(Q\)
before multiplying by the radial measure and \(\beta_Q\).  Therefore

\[
Q^2\,\beta_Q\,(Q)=o(Q)
\]

under only \(\beta_Q=o(Q^{-2})\).  This does not establish absolute
convergence.

## Classification

\[
\boxed{
\text{one hard primitive survives, but bulk-sector endpoint closure fails}
}
\]

This is a coefficient/endpoint-filtration result over the existing sourced
time carrier.  It introduces no new carrier incidence.

## Prohibited inference

The surviving superficial grade is not yet a physical divergence.  Boundary
sectors and the frozen local counterterm response space have not been applied
to this anomalous coefficient.

## Next falsifier

Transport the anomalous lower-endpoint grades through the source boundary
sectors and counterterm response matrix.  Determine whether their labelled
sum closes, leaves a local renormalizable class, or leaves a genuinely
nonlocal state-dependent residual.

## Artifacts

- `research/benincasa/marici-gm/src/bin/gaussian_anomalous_endpoint_recurrence.rs`
- `research/benincasa/results/gaussian-anomalous-endpoint-recurrence.json`
- `research/benincasa/anomalous-middle-endpoint-recurrence.md`

Allocator claim: `seqclaim-4d1345dbd7486af47eaef066`.
