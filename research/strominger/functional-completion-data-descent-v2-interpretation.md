# Functional completion through data-descent kernel v2

Owner: `marici.Strominger`

## Typed disposition

The compilation separates five objects that a coordinate-only contract would
collapse:

1. `projected_characteristic_locus` is the local scalar cotangent locus
   `p^4-q^4=0`.
2. `localized_characteristic_state_space` has rank zero in compact-support and
   planar finite-energy (`L2`) categories.
3. `finite_atomic_to_weakstar_radon` is a topology-bearing completion in
   `sigma(M,C0)`, not an ordinary flat base change.
4. `completed_magnetic_low_kernel` is the ordinary degree-zero kernel of the
   completed global paired spin operator:
   \[
   \ker\mathcal A_3=\bigoplus_{l=2}^4\mathcal H_l.
   \]
   Its real magnetic rank is 21. It is not `Tor`, and its origin is a global
   spectral zero rather than the local characteristic locus.
5. `low_harmonic_repair_ports` is a finite linear observation fiber. Its 21
   exact coefficient projections form the identity coordinate frame on the
   kernel. It is executable because the source-side harmonic projection is
   independently declared, not because the modes share geometric support.

## Smallest missing constructors

Nima v2 correctly validates derived base change, correspondences, replay, and
finite state-transforming capability fibers. It does not currently interpret
topological completion or linear observation fibers. Silently placing either
object in an ignored JSON field would not compile it.

The conservative sector adapter therefore adds exactly:

- `topological_completion(topology, dense-image evidence, source authority,
  comparison evidence)`;
- `finite_linear_observation_fiber(source kernel, finite ports, execution,
  independent port authority, joint rank)`.

It calls the unmodified Nima v2 validator first. These additions are proposed
constructors, not retroactive changes to Nima's schema.

## Correspondence and support

The hard-flux constructor is typed as a span with
contravariant-left/covariant-right variance. Its left leg pulls flux to the
linear Bondi constraint incidence object; its supported right leg solves and
pushes to spin shear. Compact `u` support covers pulses, while endpoint
transitions carry an explicit finite-news-energy boundary declaration. This
linear source authority does not establish every nonlinear dominant-energy
matter realization.

## Hostile results

The checker rejects all of the following:

- identifying the characteristic locus with the completed kernel;
- omitting the weak-* topology;
- calling completion ordinary base change;
- retyping the kernel as a Tor grade;
- erasing correspondence variance;
- deriving executable ports from support alone;
- deleting any one of the 21 ports;
- promoting the historical cosmology cutoff-five rank-21 plateau to a current
  coincidence or identity.

Deleting one coordinate projection leaves rank 20 on a 21-dimensional blind
space. Thus fewer than 21 scalar ports cannot make the joint readout faithful.

## Cosmology rank correction

The magnetic low kernel still has rank 21. The current cosmological
marked-relative geometric closure has stabilized rank 26; its earlier rank 21
was a cutoff-five plateau. The contract now records
`superseded_cutoff_plateau_not_current_coincidence`. No source-derived
comparison map is known, and the current objects do not even have equal rank.

## Evidence boundary

The bounded replay executes the 91-gate aggregate checker, verifies its three
semantic fields, and compares the exact SHA-256 of its JSON artifact. The
contract and its hostile mutations are then compiled deterministically by
`checkers/functional_completion_data_descent_v2_checks.py`.
