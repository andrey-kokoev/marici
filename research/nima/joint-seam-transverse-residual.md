# Retaining the parent-face ambiguity as a transverse seam record

## Result

**105 exact checks pass.** The two candidate parent-face modes that the AB edge
reader could not distinguish differ by precisely

    v_C - v_D = (C-D)/3.

The complementary edge C-D, already present in the supplied tetrahedral geometry,
provides a diagnostic: its readings on the candidates are +4/3 and -4/3.
It is orthogonal to AB, explaining why the earlier edge reader missed it.
This does not supply a physical instrument or choose a preferred parent face.

## Retain both possibilities in their actual raw span

The earlier completion chose either v_C or v_D as the missing seam mode.
Instead retain their span. For surviving common amplitude a and residual r,
write the missing raw vector as

    w = -a (v_C+v_D)/2 + r (v_C-v_D)/2.

The original edge equality is satisfied for every r. The two earlier candidate
branches are r=-a and r=+a. Neither is discarded; no default r=0 is selected.
The three surviving amplitudes remain (a,a,a), giving a two-dimensional joint
compatible space rather than either prior one-dimensional branch.

This is an explicit enlargement of the previous conditional completion, not a
claim that the incomplete primitive constructor already authorized arbitrary
superpositions of the two orphan modes.

## Metric and recovery

The candidate vectors are not independent orthogonal registers:

    ||v_C||^2 = ||v_D||^2 = 20/3,
    <v_C,v_D> = 56/9.

Using the actual raw-vector pairing gives the exact joint norm

    ||joint(a,r)||^2 = (238/9)|a|^2 + (2/9)|r|^2.

The checker constructs the 12-by-2 encoding E, its induced metric G=E*E,
its decoder G^-1 E*, and the joint projector E G^-1 E*. Encoding and decoding
recover both coordinates exactly. The orthogonal complement remains a separate
retained channel; two coordinates do not reconstruct arbitrary twelve-component
raw inputs.

The new projector's compression to the old nine raw coordinates is 90/119 of
the old collective projector. This differs from the previous 3/4 because the
admitted joint space has changed. It is not a retuned recovery coefficient.

## What the new reader establishes

The pair of geometric readers AB and C-D has an invertible restriction to the
two candidate-mode span, so it recovers both coefficients there. It still has
a kernel on arbitrary three-component raw inputs. Its sufficiency is explicitly
relative to the candidate span, not general spatial tomography.

Swapping C and D changes the residual coordinate's sign and the encoding's
residual column together, leaving the represented state unchanged. The geometric
reader is checked covariant under all tetrahedral orthogonal relabellings; those
coordinate changes are not thereby asserted to be admitted physical dynamics.

## What is now resolved

The prior ambiguity is localized rather than hidden: it is a concrete transverse
component, with an exact metric, recovery map and discriminating geometric probe.
The edge-only observer can forget it for the static edge equality, but cannot
claim to recover the full candidate completion.

Still unprovided are the preparation and update law for r, source selection of
the edge-matching interface, and an instrument realizing either reader. No new
exchange kernel, mediator interpretation, physical force or energy scale is
inferred from this representation.

## Reproduction

    uv run --with sympy python research/nima/checkers/check_joint_seam_transverse_residual.py

Receipt: `results/joint-seam-transverse-residual.json`.
All four single-edge deletions are rebuilt using the unchanged constructor.
No original source or owner receipt is modified.
