# Broader prior-research search after the normalization stop

## Scope and correction

Fresh searches covered Nima's gravity, response, reference and normalization work, Voevodsky's gravitational realization/frame work, Flavor's clock-normalization work, and cross-program physical-realization pointers. This is a bounded search, not a repository-wide absence theorem.

The last stop was valid only for the current exchange model. Prior research contains concrete physical frame selectors and source-to-observer maps. Saying that the programme must invent a physical coupling/readout from scratch would be too strong. The missing task is to connect the retained WG source and selected bank port to an existing physical realization without silently importing its assumptions.

## 1. Actual relational physical-frame selectors already exist

`marici-machian-gravity-direction.md` contains substantially more than the early memory conjecture:

- Timelike total momentum selects a rest direction.
- X^mu=J^{mu nu}P_nu/P^2 selects the transverse center-of-momentum origin.
- Nonzero Pauli--Lubanski data selects a spin axis.
- Nonzero radiated momentum selects a time origin through u*=2 DeltaK.dot(DeltaP)/|DeltaP|^2.
- A local tidal tensor with simple spectrum selects a spatial triad up to discrete signs. Repeated eigenvalues retain continuous stabilizers.

These are conditional selectors from gravitational state, not a selection of that state by the Boolean seed. The note explicitly replaces the overly strong claim that an exterior reference is always necessary: generic localized curvature already fixes the continuous frame freedom.

## 2. A full-history physical frame transport is available

`../voevodsky/two-polarization-shear-selects-area-and-parallel-frame.md` constructs, in a declared vacuum Einstein plane-wave sector,

    gamma=r^2 C, det C=1,
    r''+[tr((C^-1 C')^2)/8]r=0,
    F'=-(1/2)gamma^-1 gamma' F.

Supplied shape history, corner area/expansion and initial frame determine the area and parallel frame. The explicit rotating-shape loop has comparison angle -121*pi/1800. It therefore retains a nonzero history-dependent frame response beyond an instantaneous eigenvalue or sign reading.

This is a promising prior physical realization to compare against the retained-memory architecture. It does not derive the Einstein law, choose the source shape history or fix G; vacuum equations cannot fix the matter-coupling coefficient. Its two-dimensional frame also must not simply be identified with the Clifford bank's internal frame by matching matrix sizes.

Historical verification: the source reports 45 exact rational checks in `../voevodsky/check_two_polarization_characteristic_selection.py`. The source and implementation were inspected; this search did not rerun that result-writing checker.

## 3. Retained orientation data predates the latest bank construction

`reference-context-descent-and-orientation.md` already retains a rank-two orientation representation of the primitive sphere classes. Independent stabilizer swaps act by diag(+/-1,+/-1); the common fixed subspace is zero, but the representation is retained rather than erased. Transition witnesses and invariant scalar readouts are explicitly distinguished.

This is directly relevant to the new determinant-character hidden sector. The next concrete structural question is whether the ACTUAL retained source package provides an equivariant map from these orientation records to the required endpoint-relative orientation line. That would test a source attachment other than taking det(V) from the same edge being observed.

No such map is established here. The primitive relation and a filled tetrahedral witness need not have the same homology; their cell sets, endpoint roles and admitted transport groups must be compared first. Identical sign formulas alone are not a typed identification or a new physical reference.

## 4. Source-derived nonlinear response composition already exists

`mean-fluctuation-transport-and-context-policy.md` derives, for a declared same-slot source composition,

    (B diamond A)_i=A_i+B_i+B_i r A_i,
    K(B,A)=sum_i w_i b_i r a_i.

The covariance correction is computed from retained records, not fitted. `full-cycle-prior-work-reconciliation.md` records the later promoted-context discriminator: 977 versus 18769 supported leaf pairs distinguish policies with the same first mean. It also records the failed linear identification with conservative exchange feedback.

This branch should not be replaced by another generic averaging or scheduling experiment. Its outstanding choice is which actual source operation is performed and which ports it composes. It is not yet a selected gravitational coupling.

## 5. Normalization has sharper prior boundaries than our latest test

- `comparison-update-dynamics-and-energy-normalization.md` already gives a Hamiltonian embedding with H=(S/(2T)) x^T K x and Poisson tensor J/S. Changing S cancels out of the trajectory. This is a stronger explicit physical-identification boundary than simply observing that an orthogonal map preserves scaled norms.
- `comparison-tensor-sewing-logarithm.md` selects A(e)=-log(1-2e)/2 from tensor sewing plus A'(0)=1. The leading normalization is a stated requirement, and independent tensor sewing is not sequential shared-edge composition.
- `comparison-kinetic-readout.md` retains undetermined positive scales F and U and a supplied spacetime interpretation.
- `../flavor/flavor-radius-stabilized-common-clock-cofiber.md` reduces a clock-calibration question to B/A=6 n^2, but neither the flux sector nor the gauge/gravity ratio is selected.
- `../voevodsky/linearized-einstein-to-poisson-and-scalar-state-gate.md` derives Poisson normalization and geodesic acceleration from supplied Einstein dynamics and the dust limit. G is still an input. It is a real conditional unification, not merely an assumed Poisson kernel.

No inspected source closes gravitational normalization for the current WG model. These are precise reusable interfaces and obstructions, not evidence that no physical-source work exists.

## 6. One tempting earlier metric claim fails a fresh control

`machian-metric.md` claims an intrinsic stabilizer metric and a Lorentzian extension. Inspection of `checkers/check_machian_metric.py` shows that its Gram is instead the Euclidean dot product of numerical permutation-label vectors. It does not implement the asserted Lorentzian construction or Einstein compatibility law.

A fresh exact root-preserving relabelling control gives:

    e=(0,1,2,3), p=(0,2,1,3), a=(0,1,3,2),
    dot(e,p)=13,
    dot(a e a^-1, a p a^-1)=10.

Thus that implemented pairing is not intrinsic under its declared S4 carrier symmetry. This falsifies that particular source-free metric claim, not all stabilizer-based metrics. No historical artifact was overwritten.

## Broader physical-realization pointer

`../voevodsky/project-compatibility/prior-physical-realizations.md` already corrects a similar programme-wide missing-readout diagnosis. It points to Benincasa's fixed-source spectral Gaussian observer and positive-energy graph readouts, while retaining their continuation and normalization boundaries. Those are different source sectors and should not be imported as a WG/gravity bridge without a comparison.

## Recommended continuation

Do not repeat the scalar calibration audit. First inspect the full retained orientation package and its actual transition maps against the determinant-character bank port. In parallel, use the existing tidal/characteristic physical-frame sector as an explicit comparison target, retaining its boundary data and Einstein assumptions. A source-to-source intertwiner or a precise type obstruction would be new progress; simply declaring their matrices to be the same would not.

Search and source inspection only, except for the freshly executed label-Gram counterexample above. No new gravitational derivation, rerun of historical physical checkers, publication or owner adoption is claimed.
