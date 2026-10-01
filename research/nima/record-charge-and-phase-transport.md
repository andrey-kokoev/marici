# Charge boundary and phase transport on record endpoints

## Charge accounting from path records

Orient each of the six unordered links of the four-state complete graph.
Let B be its vertex-link incidence matrix, with -1 at source and +1 at target.
A directed path record contributes a signed link current j; its boundary Bj
is delta_target-delta_source. Concatenation adds boundaries, so intermediate
endpoint contributions cancel. Summing records within a promoted family gives
B(sum j)=sum Bj. The new family label introduces no extra charge by itself.

Reverse traversals cancel in signed current but retain their two positive-cost
history records. Charge/current and traversal-resource accounting are separate.
This defines a conserved endpoint quantity for a transport interpretation; it
does not establish that the quantity is physical electric charge.

## An explicit phase-covariant transport action

Add complex amplitudes psi_v to endpoint states and unit complex link variables
U_ab on each oriented link. Let positive kappa_ab be declared hopping strengths:

    H = sum_(a,b) kappa_ab |psi_b - U_ab psi_a|^2.

A local phase change psi_v -> exp(i chi_v) psi_v is accompanied by
U_ab -> exp(i chi_b) U_ab exp(-i chi_a). Every squared difference and H are
invariant. Triangle products are invariant holonomy observables.

With canonical complex Hamiltonian dynamics i dot(psi)=dH/d(conjugate psi),
set rho_v=|psi_v|^2 and

    J_ab = 2 kappa_ab Im(conjugate(psi_b) U_ab psi_a).

Then dot(rho)+B J=0. This fixes a sign convention for oriented dynamical current;
a labelled path's boundary separately describes endpoint change on traversal.
Total rho is conserved. Under a time-independent local phase change, velocities
transform covariantly. Time-dependent gauge transformations require a temporal
potential, which is not included in this test.

The action and complex canonical dynamics are trial choices. They provide a
concrete U(1)-covariant matter transport interface using the record endpoints,
not a deduction of all these choices from fibration alone.

## Relation to the137 response

This construction supplies a candidate current observable, an action on endpoint
amplitudes, and gauge-invariant loop data. The137 comparison model acts on a
16-dimensional tensor comparison space plus records. An explicit map connecting
this matter transport to its comparison/readout dynamics remains to be supplied.
The conserved norm rho has not been identified with measured electric charge.

Multiplying all kappa_ab by a positive factor preserves covariance and continuity
while scaling H, J and evolution rates. More generally the relative link weights
also remain inputs. A normalized gauge-field action and a source-derived
matter/field identification are required to fix a dimensionless physical coupling.
Local phase covariance alone does not set alpha.

## Remaining field dynamics

The link variables are supplied backgrounds in this experiment. To close a
feedback loop, equip them with a dynamical action and an equation driven by J,
and test the resulting Gauss constraint and gauge transformations. The temporal
potential and canonical field normalization must be included. Physical spatial
propagation and the Coulomb law require a geometry/continuum interpretation.

## Verification

    python research/nima/checkers/check_record_charge_transport.py

Finite integer path checks cover lengths1..4. The complex-amplitude fixture
checks all256 fourth-root local phase choices, energy/current/holonomy invariance,
covariant velocities, continuity, family aggregation, and response rescaling.
The general phase identities follow directly from the formulas above; the finite
phase checks are regression tests, not an exhaustive proof over U(1).
