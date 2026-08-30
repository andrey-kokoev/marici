# 3933 — The Conductor Bockstein Line Is Not Horizontal

## Hard claim tested

Entry 3916 supplied a fiberwise rank-one exact boundary line. A coefficient-local-system interpretation requires that line to be preserved by the source-derived Gauss–Manin transport.

Because the boundary is already the gamma-normal derivative, the test must retain the mixed grade (epsilon_\gammaepsilon_X). Independently reduced fibers cannot be compared: Entry 3921 found that their normal-form supports change.

## Simultaneous bidual reduction

The complete rank-26 presentation was reduced over

\[
\mathbb F_p[\epsilon_\gamma,\epsilon_X]/
(\epsilon_\gamma^2,\epsilon_X^2).
\]

The two exact relations were lifted in the (X)-direction before extracting their gamma and mixed components. This retains variation of the relation representatives and avoids choosing a connection between separately reduced fibers.

## Result

For both (X=x,y) and both primes (32009,32003):

- quotient dimension: (26);
- lifted exact-relation dimension: (2);
- gamma-Bockstein image rank: (1);
- gamma plus mixed image rank: (2);
- mixed support sizes: (0,27).

Thus the mixed image is not contained in the Bockstein line. The line is not horizontal in the source-normalized quotient frame.

## Narrow conclusion

The fiberwise exactification cone from Entry 3916 does not globalize as the proposed rank-one coefficient sub-local-system. The failure does not require a new Carrier stratum: the source supplies the mixed coherence cell, and that cell transports the boundary out of its line.

The rank-23 fiberwise cone cohomology remains a valid finite calculation, but it cannot be promoted through this rank-one boundary construction.

## Joint first saturation

Exporting the actual gamma and mixed vectors permits a basis-independent joint rank test. At both primes,

\[
\operatorname{rank}\langle\beta\rangle=1,
\qquad
\operatorname{rank}\langle\beta,\nabla_x\beta\rangle
=\operatorname{rank}\langle\beta,\nabla_y\beta\rangle=2,
\]

but

\[
\operatorname{rank}\langle\beta,\nabla_x\beta,\nabla_y\beta\rangle=3.
\]

Thus the two added directions are independent modulo the Bockstein line. The tempting rank-two saturation is already falsified at first order.

## Next falsifier

Derive the Fitting/rank-jump stratification of the Bockstein-plus-mixed map over the kinematic base and audit every proper constant-rank stratum. Only after this support geometry is fixed may one test whether the generic rank-three first saturation is preserved by second mixed derivatives and curvature. Continued growth retires this exactification route globally; finite closure would still require conductor-target and cyclic-atlas compatibility.

## Globalization qualification

Parameterizing the reducer and testing ((x,y,z)=(3,4,5)) exposed a limitation of the relation-discovery algorithm: after removing an invalid rule that treated nilpotent-only residual columns as relations, the sequential pivot solver found no lifted relation there. The original ((2,3,4)) calculation remains unchanged and passes, but this does not establish that the relation bundle disappears at the second point. A genuine dual-kernel lift must solve the nilpotent residual equation using the complete base-kernel freedom.

Therefore Entry 3933 currently proves local nonhorizontality at the audited point and primes. Its global Fitting interpretation is suspended until the kernel-lifting solver is repaired.

## Artifacts

- `research/benincasa/checkers/check_rank26_bidual_coefficient_ring.py`
- `research/benincasa/checkers/check_rank26_bidual_quotient_horizontality.py`
- `research/benincasa/results/rank26-bidual-quotient-horizontality-x.json`
- `research/benincasa/results/rank26-bidual-quotient-horizontality-y.json`
- corresponding `-p32003-` packets
- `research/benincasa/checkers/check_rank26_bockstein_first_saturation.py`
- `research/benincasa/results/rank26-bockstein-first-saturation.json`
- `research/benincasa/results/rank26-bockstein-first-saturation-p32003.json`

Ledger sequence claim: `seqclaim-4cdb57161f0213589d087911`.
