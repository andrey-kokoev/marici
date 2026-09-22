# The actual old observer has a nine-dimensional source-action presentation

## Result

The old two-seed observer O_2 now has an explicit symbolic presentation reconstructed from its actual source coefficient functionals, rather than from the five-dimensional gain fixture.

Its dimension is **9**. The actual source-ideal filtration has dimensions

`dim(O_2, I O_2, I^2 O_2)=(9,1,0)`.

Left and right ideal images coincide. The export contains the complete contextual basis, source representatives, 128 marked prime-action matrices, the first transition and its section, and the old evaluation of the retained source lift.

This supplies the lower observer needed for the actual O_3-to-O_2 comparison. It does not yet export the full 270-row O_3 or the four-tower faces.

## 1. Freeze the two actual seed functionals

The background-two four-event packet has primes `(2,3,5,7)`. The first seed is the unit vacuum coefficient of the canonical forgotten `(2,3)` path, supported at arithmetic corner `[2,12]`.

The old four-event seed has two supported words, both in canonical event order:

- marks `(1,0,0,0)` with coefficient `-rho`;
- marks `(0,1,0,0)` with coefficient `1`.

Here `rho=A/B` is the fixed actual early/late sector ratio. This presentation divides the entire old residual family by its fixed nonzero late-sector factor, including its common analytical prefactor. It is a whole-family coordinate normalization, not a change of detector recipe.

The source of the initial vacuum summand and these two old sectors is pinned in the owning source-tower and calibration notes:

- `../voevodsky/saturated-observer-transitions-split-first-and-retain-later-filtered-extensions.md`;
- `../voevodsky/the-current-calibration-refinements-fix-one-physical-sector-ratio-not-a-family-of-observers.md`.

No numerical midpoint replaces rho. Computation takes place symbolically over Q(rho), followed by an exact audit of all specialization guards on `[9/20,12/25]`. The owning calibration places the actual ratio inside that interval.

## 2. Compute the saturation on the actual ideal

A nonzero context of either seed must be a prefix and suffix of one of its supported words. The checker enumerates all 33 nonzero contextual candidates before restriction to I, including contexts that later vanish on I.

For every source corner in the four-event packet with at least two events, it independently constructs the terminal recorder on ALL marked paths and computes its exact rational kernel. There are 33 such corners. Zero- and one-event corners contribute no ideal states, by the owning injectivity argument.

Each contextual coefficient is restricted to these kernels. Exact row-span selection removes zero and dependent contextual functionals. The dual evaluation space has nine coordinates. Selected source representatives evaluate to the coordinate basis, proving that the presentation describes the actual evaluation image, not an arbitrary ambient readout space.

Only canonical-chain corners support the contextual seed functionals. Off-chain ideal corners are nevertheless included in the action audit; they are not discarded on the assumption that observed states must come from canonical source paths.

## 3. Source actions, not just scalar evaluations

The exporter computes every forgotten and retained prime-edge action on both sides: 64 marked edges, giving 128 action matrices.

It then checks evaluation compatibility on the entire kernel basis of every composable source corner, not only on the chosen state representatives. There are 544 nontrivially typed source-action checks.

The contextual construction gives completeness of the saturated family. The source-kernel checks ensure that actions descend to its dual evaluation image. All longer path actions are determined by these edge actions.

Two-event forgotten and mixed source relations generate the possible nonzero ideal actions. Their left and right images are the same one-dimensional full-corner subspace. Every positive-length edge action kills that image. Longer ideal factors cannot contribute because an input ideal state already requires two events, while the seed packet contains only four.

This proves the displayed ideal-depth dimensions using the actual recorder ideal, not a joint-action ideal imported from the earlier fixture.

## 4. Initial corner and chosen old lift

At the initial ideal corner let a_0 and a_1 be the forgotten and mixed diamonds. The exported evaluation matrix is exactly

`diag(1,1-rho)`.

It is invertible throughout the admitted fixed-calibration enclosure. Thus the old observer already sees the whole two-dimensional initial ideal corner.

The first transition projects onto the vacuum coordinate. Its source section is Obs_2(a_0). Both are checked against all positive-length actions, and their composite is the identity. This recovers the owning split first transition.

For

`x=path(2_forgotten,3_retained) forgotten(5,7)`,

`v2=mixed(2,3) forgotten(5,7)`,

the exported source evaluations satisfy the exact vector identity

`(1-rho) Obs_2(x)=Obs_2(v2)`.

This is the old endpoint of the actual chosen lift. It does not assert that Obs_3(x) lies in I O_3: the previous source-action audit proves the opposite. Quotient evaluation into O_2 can identify these states even though their filtration behavior differs upstairs.

## 5. The background-two acquisition cannot be appended as a split block

Voevodsky's `../voevodsky/the-background-two-vacuum-acquisition-is-a-nonsplit-observer-enlargement.md` supplies the relevant new boundary. Its checker was freshly rerun successfully.

The fully observed initial corner forces the lift of a_0 under any hypothetical section. But the old observer kills

`a_0 forgotten(5,7) forgotten(11,13)`,

while the new background-two vacuum row evaluates it to one. Right equivariance therefore contradicts such a section.

This is unlike the canonical split 30-dimensional increment from backgrounds three and four. The new background-two saturation overlaps old contextual functionals; its restriction kernel cannot be identified with the full 15-dimensional vacuum block or blindly adjoined as a direct summand.

The acquisition extension's unfiltered nonvanishing is distinct from the adjacent source pushout's filtered nonvanishing and unfiltered vanishing. The old chosen nullhomotopy remains available; it does not split the acquisition restriction.

## 6. Remaining assembly gate

The missing old component is now smaller and more explicit:

- O_2 and its complete source actions are exported;
- its initial forced-lift corner and chosen-lift normalization are checked;
- the split background-three/four blocks are separately available;
- the background-two acquisition must retain its nonsplit coupling;
- the full actual O_3 evaluation and transition must still be assembled and linked to the chosen source lift.

The six tower comparisons and four face witnesses still require that actual assembly. The earlier tetrahedral fixture does not become an identification merely because one endpoint is now known.

## Verification

`uv run --with sympy python research/nima/checkers/export_actual_old_observer.py`

Artifact:

`research/nima/results/actual-old-observer-symbolic.json`

The symbolic export passes: dimension 9, ideal-depth dimensions `(9,1,0)`, 33 source corners, 544 source-action checks, and 128 action matrices. All nonconstant specialization guards reduce to rho and rho-1, which are nonzero on the declared enclosure.

Acquisition boundary:

`python research/voevodsky/checkers/check_background_two_vacuum_coupling.py`

This is an exact symbolic reconstruction with source checks, not yet a separate portable verifier of the exported JSON. Identification of the fixed analytical ratio and source-category hypotheses remains external.
