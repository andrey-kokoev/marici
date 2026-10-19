# Composite [1,2]: fixed top normalization and local pushforward — 2026-10-13

## Net task and progress

Started `composite-normalization-definition` at history 5/root [1,2], using the existing component selector and sourced canonical seed, without choosing a normalization from the desired scalar or target residue.

Constructed a first-composite top-level normalization convention and local target-branch controls. The three-composite specification and target boundary/component comparison remain open.

## Source identification

History 5 has outer pair (2,6), inner pair (3,5), prefix (6,2), and no endpoint update. Thus K=K0 for this composite; the simple-root correction factor is not imported.

Three rational momentum-conserving supertwistor fixtures match the source H seed on support {1,2,3,4,5,6,8}, cyclic rotation 2, with full superfunction ratio exactly 1. Every matching comparison checks all 70 one-SU(4) quotient numerator coefficients and bosonic prefactors. The cell has parallel classes {1},{2},{3,4},{5},{6,8}, with zero column 7.

The scalar extraction is fixed as

    prefactor_outer * prefactor_inner
      * (q_outer[2]q_inner[3]-q_outer[3]q_inner[2])^4 / <23>^4.

It is extraction from the superfunction, not direct application of a scalar selector to an arbitrary eight- or seven-form.

## Frozen differential-form and target conventions

- Source: the H positive chart from the source table, with ordered orientation dlog alpha1 wedge ... wedge dlog alpha8.
- Embedding: matched support and rotation, with the rank-two positive cyclic twist. Wrapped columns are multiplied by (-1)^(2-1)=-1.
- Target map: Phi_Z(C)=CZ for positive rank-six bosonized external Z.
- Target chart: normalize columns 1,2 of Y to the identity; list the remaining eight matrix entries in row-major order.
- Local regular branch density: reciprocal determinant of d(target coordinates)/d(log alpha), including the declared intrinsic source orientation. No free per-term scale is supplied.
- Residue extension: retain deletion parity and transition Jacobian, and specify the target normal and boundary extraction before testing a residue equality. This convention is fixed; its complete physical implementation is absent.

## Local target tests

Two exact positive source parameter sets and two positive moment-curve external-Z samples produce nonzero eight-dimensional log Jacobians. All ordered six-by-six Z minors are checked positive. Source Plucker minors are checked nonnegative at the selected parameters.

An alternate target pivot (columns 1,3) supplies an independently differentiated target transition. Its Jacobian carries the first branch Jacobian to the second, and the two reciprocal densities transform correctly. This validates local coordinate normalization, not global covering degree or the five physical facet incidences attributed to this history.

The intrinsic alpha orientation is explicit. Its comparison with the completed BCFW chain's global orientation anchor is still an external witness, not inferred from local determinant signs.

## Positive-embedding failure retained as a control

The first target execution rejected plain cyclic relabeling: its source minors were not all nonnegative. Cell keys alone had concealed this distinction. The source positive cyclic convention requires sign reversal on wrapped columns for rank two. Applying that fixed convention restored the positive samples; the checker now retains the count of negative minors under the untwisted embedding as a hostile regression.

A subsequent implementation-only failure in counting SymPy Boolean values was corrected with explicit Python bool conversion. Neither failure was repaired by fitting a target density or changing the normalization requirement.

## Type and scope boundary

The superfunction fixtures use four-dimensional momentum supertwistors. The target differential tests use six-dimensional bosonized external Z and an eight-dimensional Grassmannian target chart. These are distinct domains.

Successful seed matching plus a regular CZ local branch does not by itself construct the commuting bosonization/component extraction square. No independent closed target superform, global degree witness, complete facet atlas, physical boundary normal or target seven-form extraction was supplied. The absent source bundle remains absent.

## Next step

Extend these same intrinsic conventions to histories 8/[1,3] and 9/[2,3], with no fitted scales and positive cyclic embeddings checked explicitly. Keep the bosonized-target/component square and boundary extraction as separate missing witnesses. A top-level local branch is not the normalized nine-to-twenty-sector map.

## Reproduction

    python research/benincasa/checkers/check_composite_root_normalization.py

Receipt: `research/benincasa/results/composite_root_normalization.json`.

Eight grouped exact controls pass. The source matcher producer was not executed; only its literal seed definitions and pure constructors were reused. Evidence level is fresh finite superfunction matching and local differential algebra, not a kernel proof, complete atlas recovery or weighted-descent theorem.
