# Twelve-arrow blocks are not a selection of physical generations

## Frozen question

Does the strongest existing twelve-label construction select the claimed three
SM generations, or only supply particular mathematical quotients? Does the old
S4^3 numerical Gram actually follow from the declared subgroup and probes?

Active SCC obligation: forward realization and compatibility of group actions,
probes and their Grams. This is ONE source-to-generation comparison, not a new
flavor model or a new carrier-size search.

Use `carrier-gram-restriction-tower.md` and the actual implementation
`check_carrier_probe_adapter.py`: retain all twelve ordered arrows (i,j), i!=j,
of the existing four-point carrier, their diagonal S4 action, probe functions,
and hidden orientation information. The normalized S12 fixed-label Gram is
10I+J by the supplied stabilizer-indicator/counting construction. Do not replace
this richer source by twelve featureless points when testing available quotients.
The already closed source-metric mismatch and physical-probe ambiguity remain
closed; see `carrier-probe-adapter-and-state-reference.md` and
`primitive-comparison-task-and-probe-roles.md`.

Also retain and execute the ACTUAL full 12-by-12 phase implementation and its
subgroup predecessor. Their assumed block labels, input phases and numerical
matrices are evidence to inspect, not physical selection criteria to adopt.

**Conjecture:** the retained arrow action admits a unique invariant partition
into three four-arrow matching blocks, but does not supply three independent
S4 factors or a physical matter interpretation. The old subgroup matrix is not
the result of either of its claimed counting rules.

**Rivals:** the existing source has no intrinsic three-block quotient; merely
finding that quotient proves the claimed SM selection; the subgroup matrix is
already a correct restriction of the completed probe implementation.

**Risky tests:** classify ALL S4-invariant block systems on the actual twelve
arrows, not just a chosen partition. Compare the induced action on matching
blocks with the independently acting S4^3. Enumerate its declared 24^3 elements
and compare both fixed-label Gram counts and point-transfer counts with the
preserved original matrices. Keep the valid supplied-matrix spectra distinct
from a source derivation. Do not test CKM predictions or replace the old matrix
by corrected entries while calling it the same evidence.

**Equivalence:** transport all arrow/end-point labels together. Relabellings
of a three-by-four partition under S12 are presentations, NOT different physical
predictions. On the enriched source the specified diagonal S4 action is retained.

**Closure:** exact quotient classification and a source-bound group/probe
comparison settle this question. A canonical three-block quotient is a positive
conditional result; physical generations additionally require a matter map and
selection criterion. No such conclusion follows just from cardinality, positivity
or input block labels. A future physical model must not reopen this closure.

## What the retained source actually supplies

The existing arrow action is transitive. An invariant partition is determined
by its block containing one fixed arrow; that block's size divides 12. The
checker exhausts all 695 such subsets and checks the block criterion: every
translate is either identical or disjoint. There are exactly six partitions:

| Blocks | Arrows per block | Source map |
|---:|---:|---|
| 12 | 1 | Individual ordered arrows |
| 6 | 2 | Opposite orientations of each edge |
| 4 | 3 | Common source vertex |
| 4 | 3 | Common target vertex |
| 3 | 4 | Two opposite edges and both orientations: a perfect matching |
| 1 | 12 | Entire carrier |

In particular, the three matching blocks are intrinsic to the retained endpoint
structure. There is exactly ONE invariant partition with four arrows per block.
The rival “no intrinsic three-block quotient exists” is false. Its blocks are
unordered; S4 induces the FULL S3 permutation action on them. The quotient
classification does not discard the twelve original records or their orientation
coordinates, and the two star maps are not claims of different physical worlds.

Equivariance alone does not select the four-arrow block condition from this list.
Even after that condition is accepted, identifying the blocks as SM generations
requires a matter map, not a cardinality match. On a bare twelve-label carrier
the 5775 partitions of shape 4+4+4 are all S12-related presentations; that count
must not be misreported as 5775 physical alternatives.

## Three matching blocks do not supply three independent S4 actions

Write rho:S4->S12 for the ACTUAL arrow action. The group H=S4^3 in the old
numerical model fixes each of its three blocks individually. Only four elements
of rho(S4), the Klein four kernel of its action on matchings, do that. Thus rho
does not factor through H with the same arrow action. The source action is
transitive on all twelve arrows; H has three separate four-point orbits.

Both rho and H are legitimate DIFFERENT inclusions into the ambient S12. Neither
the existence of the matching quotient nor covariance of a block-constant Gram
identifies them. In fact the old and corrected block Grams below are both
covariant under rho after explicit relabelling, even though this group-action
factorization fails. Metric covariance cannot replace the missing action map.

A new internal action or symmetry-breaking rule could supply additional data.
This result does not prohibit such a model; it rejects its derivation from the
currently retained arrow action alone.

## The actual subgroup-count defect

The stronger prior already repaired the S12 counting semantics: f_i(sigma)
is the indicator that sigma fixes i. Its Gram counts TWO simultaneous fixed
labels, not permutations transferring i to j. We keep that SAME probe rule when
restricting to the declared H, and enumerate all 24^3=13824 elements.

| Pair of labels | Fixed-label probe Gram on H | Point-transfer count on H | Old numerical entry |
|---|---:|---:|---:|
| Same label | 3456 | 3456 | 3456 |
| Distinct, same block | 1152 | 3456 | 1152 |
| Different blocks | 864 | 0 | 576 |

The first column follows from 6*24^2, 2*24^2 and 6^2*24 respectively.
A blockwise permutation never transfers a point between blocks. The old
3456/1152/576 matrix therefore comes from NEITHER asserted rule.

Let B_ij=1 when i and j lie in the same four-point block. Retaining the entire
original 12-by-12 matrix gives

\[
G_{\rm old}=2304I+576B+576J,\qquad
G_H=2304I+288B+864J.
\]

The residual is exactly 288(J-B), confined to cross-block entries. This is not
an overall normalization discrepancy. Their actual spectra are:

| Matrix | Uniform mode | Block-mean contrasts | Within-block contrasts |
|---|---:|---:|---:|
| Original supplied matrix | 11520 (1) | 4608 (2) | 2304 (9) |
| Correct fixed-label Gram on H | 13824 (1) | 3456 (2) | 2304 (9) |

The original matrix IS positive definite. Its numerical existence is retained;
its advertised full-spectrum and source-count explanations are not.

The original code's selected three-by-three cross-probe matrix is
576I3+576J3, with eigenvalues 576,576,2304. The same selected rows and columns
in the corrected fixed-label Gram give 288I3+864J3, with eigenvalues
288,288,2880. These are spectra of SPECIFIED mathematical submatrices, not
physical mass predictions. The second matrix is not silently substituted for
the first or advertised as a newly predicted hierarchy.

Finally, the completed literal probe restriction along rho has rank SIX because
opposite arrows have equal fixed-endpoint probes, with hidden orientation data
retained separately. Both block matrices above have rank twelve. They cannot be
that same restricted probe Gram under a scalar or invertible basis change. This
preserves the prior adapter's exact conclusion rather than declaring the whole
source to have only six records.

## Disposition and visible repair

**Constructed:** complete invariant-block classification on the strongest
existing arrow source, including its canonical three-block matching quotient.
**Refuted:** identifying that action with independent S4^3 factors, and deriving
the old numerical matrix from either declared counting rule.
**Not selected:** three physical SM generations. The missing datum is a
source-authorized matter/action interpretation and criterion selecting it; no
such datum is computed by the inspected size tables or block model. Repeating
4n examples cannot supply it. The other earlier finite/source closures remain
unchanged.

All six legacy evidence entry points now refuse execution as verification with
exit code 2 and a superseding pointer. Their COMPLETE originals remain in
`quarantine/20261007-generation-evidence/SHA256SUMS`, alongside the pre-correction
index/compendium/session pages. The numerical full implementation was executed
from that archive, not replaced by a smaller realization. Its declared phases
were not fitted again and its CKM readout was not validated by this turn.
The separate successor `twelve-point-phase-readout-descent.md` now resolves that
readout question without reopening this generation/block comparison.

The print-only larger-carrier script also had a missing json import; the
original NameError was reproduced separately. Merely fixing that import would
not turn its printed generation/minimality assertions into tests. The correct
fixed-label factorial calculation already existed in
`carrier-gram-restriction-tower.md` and remains available through its untouched
exact checker.

The hierarchy and completion entries now point to this disposition. This closes
the frozen comparison, not all possible physical interpretations or larger
carrier constructions.

## Verification

The admitted SciPy profile runs `collect_generation_diagnostics.py`, reusing the
existing write-suppression loader. All original numerical statements execute,
but only source-bound matrices and indices are transported as raw data. The
SymPy consumer `check_twelve_arrow_generation_boundary.py` verifies their hashes,
reruns the complete existing tower/adapter, classifies the blocks, compares
both count rules, and tests all six quarantine refusal gates. It rejects the
deliberately false old-count identity. No S12 factorial-size enumeration or
floating-point tolerance establishes the conclusions.

Collection: `e_38524_1791398149898432000_56`. Frozen comparison:
`e_38524_1791398466863949600_58`, against
`scc-freezes/nima-twelve-arrow-generation-boundary.9bbe664fbd6ab938.json`.
Receipt: `results/twelve-arrow-generation-boundary.json`.
Here `survives` refers to the source-comparison conjecture, not SM selection.

Final original-producer replay: `e_38524_1791398881586729400_59`; fresh headless
SCC check: `e_38524_1791398923825845300_60`. Integrity check
`e_38524_1791398989609371000_61` confirms all 22 consumed hashes current, all nine
snapshots intact and all five historical receipts still absent. Graph event:
`ev-000000015822-d0fa445d-ccc1-4474-99c8-e6e9662fa75c`, proposal
`ep_c9188761-161e-4c9d-a3ca-3aa8b07e330b`. Admission records the bounded result,
not physical truth. No commit, push or publication was performed.
