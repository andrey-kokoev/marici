# What adding the candidate excitation does to the barycenter

## Source and observable

Freshly inspected the twelve-triangle geometry implementation. Reconstruct its twelve local vectors v_i, each of squared norm 20/3, and their assembled mode u of squared norm 80.

For this test, associate each triangle block with the centroid of its existing cone tetrahedron and use squared mode norm as positive weight. This is an explicit spatial/intensity reader, not a derivation of mass or energy density. The source provides the affine geometry and mode norm but does not physically identify their combination with center of mass.

The uniform-volume centroid and unperturbed intensity center are both O=(0,0,0). They remain different observables. A barycenter is also not the categorical identity map, even if it is chosen as a convenient marked reference.

## The two cells at OAB

Their cone centroids are

    r_AB=(7/12, 1/12,-1/12),
    r_BA=(7/12,-1/12, 1/12).

The previously tested opposite-phase contrast d occupies these two blocks with coefficients +1,-1. Its squared norm is 40/3. Its own positive-weight center is

    r_d=(7/12,0,0).

The negative amplitude does not make its intensity contribution negative.

## Three different meanings of addition

### Retain a possibility or dual effect

If the represented positions and weights do not change, adding a retained description, function or provenance record does not move this barycenter. Giving that record a physical energy would require an additional law. Storage in a mathematical package alone supplies no such energy assignment.

### Add an independently weighted excitation

For trial amplitude epsilon, add its intensity to the original distribution without interference. The total weight and center are

    W=80+(40/3)epsilon^2,
    B_ind=(7 epsilon^2/[12(6+epsilon^2)], 0, 0).

At epsilon=1 this gives B_ind=(1/12,0,0). It is movement of the composite's defined center toward the added weight, not motion of the original core or a derived recoil trajectory.

The candidate/core weight ratio is epsilon^2/6, not a predicted electron/proton mass ratio. Neither epsilon nor the identification of this norm with physical energy is selected.

### Coherently perturb the existing mode

For the preparation u+epsilon*d with real epsilon, the two selected block amplitudes become 1+epsilon and 1-epsilon. The total norm is the same as in the independent case because d is globally orthogonal to u. Nevertheless the first moment includes interference:

    B_coh=(7 epsilon^2/[12(6+epsilon^2)],
           epsilon/[6(6+epsilon^2)],
          -epsilon/[6(6+epsilon^2)]).

At epsilon=1 this is (1/12,1/42,-1/42). At epsilon=-1 the transverse components reverse while the longitudinal component stays unchanged.

Thus equal total weights do not determine equal centers. A relative phase can redistribute intensity even when its cross-term in the total norm vanishes. This coherent trial is a perturbation in the same modeled mode space; it is not automatically the addition of a distinct electron in a separate physical sector.

## Charge and reference controls

Global complex conjugation preserves each block's positive intensity. Negative electric charge must not be inserted as a negative mass weight. Relative sign changes in one component are also not the same transformation as conjugating the complete state.

If one hypothetically assigns charges +1 to the core and -1 to the added candidate, the total charge is zero. A normalized charge barycenter is then undefined; a charge dipole remains meaningful. This charge assignment is illustrative, not derived from the mode weights or continuation character.

Translating all cell positions translates the weighted center by exactly the same amount. Recentring coordinates at the new center therefore changes the reference description; it does not prove that matter was dynamically moved.

The geometric body and uniform-volume centroid remain unchanged throughout these amplitude tests.

## Existing dynamics check

The coherent preparation has mean coefficient one for every epsilon. The existing collective projector consequently maps u+epsilon*d back to u after one pass. Its active intensity center returns to O. This is projection of the contrast out of the active mode, not a computed conservative recoil. Retained histories can still contain the contrast.

The independent-addition case would require its own composite-state dynamics; it is not silently subjected to a newly invented electron/proton interaction.

## Outcome

The initial question now has a calculable distinction:

- Added reference/potential description only: no center shift without a weight-changing law.
- Added positive-weight excitation: the composite center shifts toward it.
- Coherent same-field perturbation: interference adds a phase-sensitive transverse shift.

None establishes the barycenter as WG identity or an electron creation mechanism. The current projector does not sustain the candidate's active displacement.

## Verification

`python research/nima/checkers/check_inner_excitation_barycenter.py` passes exact rational geometry, norm, first-moment, amplitude, conjugation, translation and one-pass projector controls. Receipt: `results/inner-excitation-barycenter.json`. Source geometry and existing dynamics were not modified; no physical mass, force law, new formal proof or ledger entry is claimed.
