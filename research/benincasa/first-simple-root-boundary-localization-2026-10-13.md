# First simple root: an actual source boundary and the missing target square

## Result — 2026-10-13

The coefficient-valued successor now has a concrete source-boundary test, not just a formal Laurent model. The target/physical boundary extraction remains absent. Eleven exact checks pass.

## Source chart and boundary

Use the sourced F positive chart with six nonzero columns embedded at {1,2,3,4,5,8}; columns 6 and 7 are zero. Its ordered orientation is dlog alpha1 wedge ... wedge dlog alpha8.

At alpha1=0, Delta23=alpha1*alpha5 vanishes and all other supported minors remain positive on the open positive boundary. The new parallel class is {2,3}; the other nonzero columns {1},{4},{5},{8} stay distinct. Zero columns remain {6,7}.

Delta12=1 fixes the determinant scaling in the Plucker patch. Exact Jacobian samples give top rank eight and boundary rank seven. Nonzero minors witness nonempty algebraic rank opens; the boundary has only seven coordinates. Thus this is a genuine codimension-one source chart boundary, not merely a matching label or a contracted coordinate face.

The residue orientation is +1:

    Res_alpha1=0 omega_F = dlog alpha2 wedge ... wedge dlog alpha8.

External kinematics is held fixed for this source-chart calculation. Consequently c is independent of alpha and is regular at the selected external fixtures. The two successor residues are c times and (1-c) times this same boundary generator. They recombine to its unit residue. Deliberately reversing the K0 residue orientation changes it by -2c, nonzero at every tested fixture. Replacing c by unit normalization gives the nonzero defect 1-c.

This is splitting/recombination of one parent form, not cancellation between distinct histories or weighted codimension-two descent.

## Typed extraction available at the top generator

The source table identifies the named F-chart canonical invariant with its five-bracket superfunction. The previous exact seed-admission controls match this superfunction to the transported generalized-R history, with full ratio one at three rational fixtures.

That supplies a restricted map on a rank-one external-coefficient module:

    E_top: R omega_F -> R F_t,
    E_top(f omega_F)=f F_t.

The existing component selector has a different, explicit type:

    S23: R F_t -> R K,
    S23(f F_t)=f K.

Their composite sends the named top-level candidates to K0=cK and B11=(1-c)K. This is a restricted generator map plus coefficient linearity. It is not a definition on arbitrary differential forms, nor a construction of the target bosonized eight-form pushforward. Positive seed admission at finite fixtures does not replace a global target map.

## The remaining square cannot be manufactured by scalar extraction

The source residue lives in a seven-form module on a positroid boundary. E_top lands in a superfunction module. The current selector does not accept seven-forms as input, and no target boundary normal or seven-form-to-superfunction boundary extraction was supplied.

Hence the desired square

    E_boundary o Res_source = Res_target o E_top

is not yet typed/constructed. Multiplying a boundary generator by the top scalar K would invent the bottom map, not test its commutativity. Likewise calling alpha1=0 a particular physical target divisor requires the missing target incidence/pushforward witness.

The current test makes c's role precise: external-fixed for this source boundary. Its interpretation as a varying target coefficient, including its extra pole corrections, still requires a target pullback map. The symbolic kinematic-slice poles are not promoted to physical facets.

## Next recommendation

The simple-root branch has reached a precise missing-target-square gate. Recover the source bundle and obtain the actual target boundary generator, normal, extraction and normalization before physical residue replay. Do not repeat the source split or fit a target coefficient to force agreement.

Meanwhile `composite-normalization-definition` is independently actionable. It is now the recommended next local task: specify the top component/form extraction and target pushforward for history 5/[1,2], without conflating the source dlog form, its superfunction and the eventual seven-form residues. This can clarify the same target-interface gap without pretending it has already been filled.

## Reproduction

    python research/benincasa/checkers/check_first_simple_root_boundary_localization.py

Receipt: `research/benincasa/results/first_simple_root_boundary_localization.json`.

Prior receipt source/checker hashes are verified. No owner producer, missing historical receipt or physical target atlas was regenerated. Fresh verification comprises exact source minors/Jacobian controls, external coefficient linearity and an orientation-failure control, not a kernel proof or full target boundary theorem.
