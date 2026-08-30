# Entry 1600 — Boundary Completion Lowers the Anomalous Hard Grade by One

## Claim

For one labelled internal Bogoliubov variation, the complete source-normalized
bulk--bulk, mixed, and boundary--boundary endpoint assembly does not vanish.
It does lower the surviving hard coefficient by exactly one power relative to
the bulk sector.

## Frozen assembly

The calculation retains the source boundary kernel

\[
C(K,\eta_0)=\frac1K\left(\frac1{K\eta_0}-i\right),
\qquad K=p+q+k,
\]

the two mixed placements, the boundary--boundary corner, all contour signs,
and the labelled anomalous \(q\)-occurrence.  Coefficients are compared by
their endpoint grade and frequency label before evaluation at \(\eta_0\).

## Result

The bulk map, mixed map, and boundary corner each occupy the same nine
labelled endpoint classes.  Their sum retains all nine.  On hard rays

\[
q=Q,\qquad k=Q-c
\]

with three generic fixed values of \(c\), the ratio

\[
\frac{\|BB+BS+SB+SS\|_1}{\|BB\|_1}
\]

scales as \(Q^{-1}\) under every doubling from \(Q=40\) through \(320\).
Since the bulk coefficient scales as \(Q\), the complete endpoint residual is
of order \(Q^0\).

## Narrow conclusion

\[
\boxed{
\text{source boundary completion gives one extra hard power but not closure}
}
\]

After the radial measure and the Hadamard condition,

\[
Q^2\beta_Q\,O(1)=o(1).
\]

This is pointwise hard decay, not a proof of absolute radial integrability.
The remaining class is still occurrence-labelled and oscillatory.

## Next falsifier

Project the residual onto the frozen local counterterm response space.  Local
counterterms have only external frequency support \(0,\pm2p\); the test must
decide whether the internal-frequency labels cancel after angular integration
or define a genuinely nonlocal state-dependent residual.

## Artifact

`research/benincasa/marici-gm/src/bin/gaussian_anomalous_endpoint_recurrence.rs`

Allocator claim: `seqclaim-926d4760f435edea6397858f`.
