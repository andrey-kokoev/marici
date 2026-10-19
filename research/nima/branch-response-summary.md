# A branch-readable outer interface without selecting endpoint wiring

## Fresh constructive result

Implemented an additive two-branch outer summary. It preserves branch-resolved matrix means without requiring the eventual reader to reopen original leaves or requiring every final family to be branch-uniform.

The supplied branch selector, original member masses and fixed reference remain explicit inputs. No context keys or comparison domains are changed.

Reusable module: `checkers/branch_response_summary.py`.

## Summaries transported during promotion

For each branch retain

    mass = sum member masses,
    response sum = sum mass*member matrix.

These statistics combine by addition. A first family reads its members once; higher families combine their CHILD SUMMARIES, not branch-blind child means. The final reader divides by the appropriate branch masses.

This is a declared observation-interface extension. It does not claim missing statistics can be reconstructed from old means alone.

The exact checker verifies staged/direct equality for inherited32-family, common1-family and endpoint-only16-family policies, as well as source/target presentation routes and a nonuniform positive-mass control.

## Minimal linear completion of J4

Let m_a,m_s be branch masses, M=m_a+m_s, and keep the original aggregate J4. Add the contrast

    D=mean_arrow(C)-mean_state(C).

The common fixed reference cancels from this contrast. Then

    J_arrow=J4+(m_s/M)*D,
    J_state=J4-(m_a/M)*D.

Thus the observed interface is J4, D and the retained branch masses. The original J4 is unchanged, not renamed or recalibrated.

For the declared full2x2 matrix branch-mean task there are8 linear coordinates. J4 has rank4; the J4/contrast map has rank8 and determinant1 in the displayed block basis. Consequently one extra4-coordinate matrix is a minimal LINEAR completion of that task. This is not a claim about minimal physical instruments, finite precision encodings or restricted response submodels.

## Earlier shared-leg hostile is now detected

The prior finite shared-leg preparations had identical16 outer means and identical J4, while their branch means differed.

Their new contrast differs by

    delta D=(137/440)*I.

The checker recovers both branch means from the new outer interface. The distinction is carried by statistics actually propagated from source members, not a postprocessing function of the unchanged old means.

These remain mathematical preparation controls, not independently writable137-record memory or a claimed physical pulse.

## Consequence for T9

This closes the OUTER branch-readout gap for the tested policies. All three candidate endpoint policies now support the same declared branch-response observation without reopening histories.

Therefore even an outer branch-mean task need not force inherited-key T9: one may retain its sufficient statistics instead. Requiring DIRECT tagged endpoint contexts is a different, stronger task, which still conditionally selects inherited keys within the endpoint-preserving partition class.

The decisions must remain separate:

- **observation task:** what response must be accessible at the outer boundary;
- **context task:** which pairs must be admitted or forbidden;
- **physical interpretation:** what instruments implement those operations and observations.

The new observer is NOT identified with J4 alone or a physical detector. Its successful square does not authorize cross-target connectors, alter source leg coefficients, or choose intended T9.

## Verification

    uv run research/nima/checkers/check_branch_response_summary.py

24 exact summary/recovery checks pass. Dependencies freshly rerun the branch-task hostile and earlier endpoint-role chains. Checks cover original J4 and masses, both original branch readers, all three staged summary squares, presentation invariance, hostile recovery, nonuniform weights, linear rank/minimality and rejection of undefined empty-branch means.

No fresh Agda closure is claimed.

Artifacts:

- `checkers/branch_response_summary.py`
- `checkers/check_branch_response_summary.py`
- `results/branch-response-summary.json`

The missing source selection is now restricted to CONTEXT WIRING if this extended branch observation is the desired declared task. It remains an explicit operational requirement, not something inferred from scalar agreement.
