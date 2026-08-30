# 1994 — All 480 Maximal C9 Orbits Have No New First-Order Horizontal Fold

## Frozen falsifier

Entry 1961 found 480 cyclic orbits tied at the maximal source-complexity score

\[
(8,7,0,9).
\]

No orbit was permitted to stand for the family.  The predeclared test therefore computed, for every orbit, the same routing-visibility and universal-cover Jacobian after removing only the already frozen Gram, soft, and lower-support factors.

The tested signature was

\[
(\text{routing visibility},\ \text{fold rank/type},\
\text{stabilizer},\ \text{physical-support incidence}).
\]

Literal occurrence labels were retained as provenance but excluded from signature equality.  Reflection-related oriented classes were not identified.

## Complete exact census

Every one of the 480 orbits has

\[
\operatorname{rank}(\text{wall normals})=8,
\qquad
\dim(\text{free routing})=1,
\]

and a universal-cover Jacobian of shape

\[
5\times1.
\]

For all 480 orbits, at least one first minor is nonzero.  After the frozen Gram, soft, and lower-support saturation, the common divisor is always a nonzero rational unit:

\[
\begin{array}{c|c}
\text{raw unit}&\text{orbit count}\\
\hline
-\tfrac12&64\\
1&409\\
\tfrac17&7.
\end{array}
\]

These units are normalization data, not distinct fold types.  No declared lower-support factor remains to be removed.

The invariant partition therefore has exactly two classes:

\[
128=\text{complement sector},
\qquad
352=\text{all-region sector}.
\]

They differ only in physical-support incidence.  Their routing and first-order fold types coincide.

## Existing Gram specialization

At the frozen Gram specialization \(k=0\), the ideal has Cartier length one.  At

\[
k=-\frac67,
\]

the corresponding Cartier length is zero.  This is existing Gram support and does not define a new horizontal fold divisor.

## Narrow result

\[
\boxed{
\text{No maximal }C_9\text{ source orbit carries a new generic
first-order horizontal companion fold.}
}
\]

Thus neither maximal source complexity nor first-order routing/fold geometry selects one of the 480 coherent candidates.  The endpoint seams remain relation/coherence cells rather than carrier rays or ordinary period classes.

Any later physical activation must be derived from a separately constructed coefficient mixed-relation defect, for example

\[
\Theta_i
=
\nabla_E d(s_i)-d\nabla_S(s_i),
\]

or a typed homotopy analogue.  This result does not construct such a coefficient object and does not authorize a seam-period pairing.

## Execution repair

The initial all-at-once run spent more than fifteen CPU-hours because evidence serialization refactored already-computed cover equations.  Stage tracing proved that the exact algebraic calculation itself completed rapidly.  Removing that redundant presentation-only factorization reduced the formerly pathological orbit to about 1.5 seconds.

The repaired executable writes one atomic checkpoint per orbit.  The complete packet has 480 consecutive indices and 480 unique canonical keys.

## Verification

- `research/benincasa/marici-gm/src/bin/eight_site_universal_jacobian.rs`
- `research/benincasa/checkers/nine_site_maximal_orbit_linear_signatures.py`
- `research/benincasa/checkers/nine_site_maximal_orbit_fold_partition.py`
- `research/benincasa/results/nine-site-maximal-orbit-universal-jacobians.json`
- `research/benincasa/results/nine-site-maximal-orbit-fold-partition.json`

Universal-Jacobian packet SHA-256:

`f93ba3d19ce8ee0fad510a6af3ef0b40d550877e25802366a4092902c20586e5`

Invariant-partition packet SHA-256:

`3f6397ed93387061be4e21fb842fd60e6763ff69e2b54acd0c16c70ac9caff51`

Allocator claim: `seqclaim-e6bb105b5413fef1c56386af`.

Epistemic graph event: `ev-000000002697-a37d88ad-4804-4743-a78a-2b761739925c`.
