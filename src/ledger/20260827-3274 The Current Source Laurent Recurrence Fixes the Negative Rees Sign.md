---
id: 20260827-3274
date: 2026-08-27
status: replicated-source-direct-modular-theorem
---

# 3274 — The Current Source Laurent Recurrence Fixes the Negative Rees Sign

## Result

Entry 3269 isolated a sign conflict at the unique total-energy double pole.
The reconstructed rank-twelve candidate gave

\[
\operatorname{Lead}^{(-2)}_{u=0}(B_u)_{e_6,q_0}=-\frac18,
\]

whereas Entry 292 recorded (+1/8) in its raw two-wall calculation.

The present test bypasses the reconstructed (B)-block.  It computes the
same coordinate directly from the complete cleared source presentation, with

\[
e_6=-\frac{K_1}{2K^{3/2}},
\qquad q_0=[\Omega_{111}],
\qquad \nabla=d+A.
\]

The source-direct result is

\[
\operatorname{Lead}^{(-2)}_{u=0}(B_u)_{e_6,q_0}=-\frac18.
\]

It agrees with the reconstructed candidate and disagrees with Entry 292's
recorded sign in the presently declared frame.

## Construction

At fixed generic (v), write the 132 cleared source identities as

\[
M(u)x(u)=r(u),
\]

where (x) retains all 372 class and primitive coordinates.  The calculation
does not substitute any candidate connection entry.

The polynomial matrices were reconstructed over the field prime from exact
source evaluations at (u=0,1,\ldots,16).  Evaluation at (u=17), excluded
from reconstruction, verifies every reconstructed source coefficient.

Insert the Laurent ansatz

\[
x(u)=\sum_{j=-2}^{3}x_j u^j
\]

and equate orders (u^{-2},\ldots,u^3).  This gives 792 equations in 2232
Laurent coordinates.  The reduced rank is 655.

An important truncation effect is visible.  Through order (u^1), the
(u^{-2}e_6) coordinate is not fixed.  Through order (u^3), the complete
recurrence fixes it to (-1/8).  Thus neither the leading symbol nor a short
normal jet is sufficient to determine the source normalization.

## Independent replications

The result was repeated at

\[
v=5, 7
\]

and at the two field primes

\[
2305843009213693921,
\qquad
2305843009213693951.
\]

Every run has rank 655 and rationally reconstructs the same fixed coordinate
(-1/8).  This is a replicated modular source theorem.  A universal cleared
identity over \(\mathbb Q(v)\) remains stronger than what is claimed here.

## Effect on the earlier result

Entry 292's structural result survives:

- the primitive marked top class requires second normal order;
- the correction lands only on the established algebraic line
  \(\langle e_6\rangle\subset\mathcal T_7\);
- the elliptic Gysin image is zero;
- no new carrier stratum is required.

Its displayed (+1/8) coefficient is not transportable into the current
source frame without an explicit sign bridge.  No such bridge is present in
the frozen Entry 292 packet, and its original generator is not tracked.
Accordingly, the current source-normalized rank-twelve calculation uses
(-1/8); the older sign is retained only as an unresolved historical
normalization claim.

## Interpretation

The unique double pole is now source-authorized at the tested generic fibers.
It is an existing-coefficient Rees correction, not an interpolation artifact
and not a new carrier divisor.  The pole-lattice audit has therefore passed
its highest-order total-energy gate.

The next source-authorization problem concerns the simple-pole residues:
first at (u=0), then factor by factor across the remaining eleven existing
support divisors.  Those tests must compare residues or costalk maps, not just
denominator occurrence.

## Durable artifacts

- source recurrence checker:
  `research/benincasa/checkers/audit_marked_extension_source_laurent_lead.py`;
- replication checker:
  `research/benincasa/checkers/audit_marked_extension_source_laurent_replication.py`;
- aggregate packet:
  `research/benincasa/results/marked_extension_source_laurent_lead.json`;
- three replication packets in the same results directory;
- allocator claim: `seqclaim-9e0df4cdfb8f9da6d5f45913`.
