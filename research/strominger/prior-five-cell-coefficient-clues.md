# Recovered prior five-cell spin machinery

## Correction

The recent interface audit stopped at `geometric-phase-energy-bridge.md` and missed constructive successors. A repository-wide claim that five-cell spin transport is absent is incorrect. The copied-fiber 720/rank-ten control is not the strongest existing candidate.

## Strongest existing chain

1. `research/voevodsky/cell-interface-assembly-contract.md`: typed local spaces, interface restrictions, compatibility kernel and metric-dependent orthogonal return. Distinguishes exact constraint assembly from ordered products of projections. Gives a conditional flat rank-two extension with explicit sqrt(5) attachment recovery.
2. `research/voevodsky/pentachoron-geometric-spin-interfaces.md`, checker `check_pentachoron_spin_interfaces.py`: derives chiral projectors for every oriented triangular face and intrinsic facet-fold spin transports from the 4D regular simplex. Recovers the old tetrahedral encoding exactly. Inherited-face matching and full-spinor parallel matching both have zero-dimensional kernels. The declared equally weighted seam-mismatch operator has lowest rank four and energy 4-sqrt(6).
3. `research/voevodsky/pentachoron-cycle-spin-energy-transport.md`, checker `check_pentachoron_cycle_transport.py`: binds the actual relative-electron generator to the regular simplex, constructs a spin lift, verifies covariance of all face projectors and folds, and reversible transport on the low space. Bare cell permutation fails the face-covariance control.

The third packet supplies two invariant doublets extending the old attachment. Adding the separately declared operation defect (T-I)* (T-I) to the seam mismatch selects one. Reversing the spin lift selects the other. Geometry does not uniquely choose the lift or justify the additional physical coupling.

## Actual reusable exports

`check_pentachoron_cycle_transport.py:export_attachment` exports, for both doublets and chiralities:

- a 10-by-2 cell isometry;
- a 40-by-2 face isometry and ordered face keys;
- exact isometry checks.

They occur in `results/pentachoron_cycle_transport.json` under `chirality_results[*].conditional_cycle_defect_extension.{attachment_encoding,opposite_lift_attachment_encoding}`.

Arithmetic already exists in `check_pentachoron_spin_interfaces.py`: Q(sqrt(2),sqrt(3),sqrt(5),i). Our new Q(sqrt(3),i) network core cannot directly represent it; generalize its field interface rather than round these exports or reconstruct them in floating point.

## Important label bridge

The prior transport code explicitly maps the source attachment pole to geometric E, with source affine basis columns A-E,B-E,C-E,D-E. Thus its geometric ABCD attachment corresponds to the facet opposite the source pole. Raw label matching across these conventions is wrong; use the existing affine intertwiner.

## Next concrete experiment

- Reuse the exact exported cell/face isometries and intrinsic projectors rather than identical copies of a single cell's frame.
- Extend the checked source five-cycle lift construction to the five retained triangle generators, with reflection-word signs explicit.
- Test covariance, reverse histories and preservation of the rank-four space and each candidate doublet under the full generated action. A doublet selected by one cycle cannot simply be presumed compatible with added generators.
- Declare the global L/G/N factorization and its execution schedule before counting its transfer supports. A return projector or an isometry alone is not a uniquely specified staged protocol.
- Keep chirality, lift, mismatch/selection rule and attachment normalization in the retained input.

This replaces the broad missing-transport diagnosis with narrower work: adapting existing spin machinery to the added generators and specifying the coefficient protocol on the admitted global carrier.

## Evidence checked in this search

Read the three notes and actual export code. The stored cycle receipt reports verification passed, and all four recorded hashes match current files: source seed, cycle checker, spin-interface checker and predecessor receipt. The predecessor receipt also reports verification passed. No fresh full algebraic replay was executed during this search; hash agreement is not claimed as one. Shared stores were not rewritten.
