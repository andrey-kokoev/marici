# Implications of the supplied braid-to-effective-operator note

## Provenance and status

The operator-supplied note is preserved verbatim in
`braid-composition-effective-shape-interaction-operators.md`.
It describes a constructive investigation; saving it does not independently
verify all its calculations or experimental correspondences. No checker receipt
for its complete 35-section chain has been produced in this session. The comments
below distinguish connections to our checked packets from new conditional
mathematical implications.

Follow-up: `shape-interaction-finite-operator-audit.md` now supplies an independent
exact checker for the central finite-operator identities (iteration 1). It does
not certify the entire 35-section investigation or its physical correspondence.

## 1. The missing layer is an interaction, not another shape count

Our current packets supply geometric carriers, labelled boundary occurrences,
source symmetries, native phase data and some explicit interfaces. The new note
proposes a grammar for changing the number and identity of carriers, and then
adds amplitude dynamics. This separates three obligations that must not be
collapsed:

- a permitted shape correspondence;
- a coherent linear realization respecting the retained metric and records;
- a physical dynamics and normalized observable probability law.

The electron skeleton's two rotational edge seeds do not establish a two-state
Frobenius algebra. Nor do the neutron's three symmetry seeds establish three
observable scattering channels. Counts alone do not identify state spaces.

## 2. The annulus supplies a through-interface, not a merge by itself

The neutron outer belt is an annulus with two boundary circles. With one circle
designated incoming and the other outgoing it is a 1-to-1 cobordism. In an
ordinary undecorated oriented 2D TQFT, the cylinder realizes the identity.

A merge or split is instead a pair-of-pants surface with three boundary circles.
Thus the annulus can organize port-to-port transport but is not already a 2-to-1
merge, a 1-to-2 split or a proof of recombination. Nontrivial phase transport can
be supplied by additional decorations/operators; it is not forced by annulus
topology alone.

This use of cobordisms concerns histories or correspondences between port loops.
Identifying those loops with complete particle-state boundaries requires a
separate dictionary, especially for the electron's four-dimensional carrier.
A spatial annulus's fundamental group is also not the configuration-space braid
group of the moving carriers.

## 3. Retained intermediate information is the strongest common principle

Our rim-port trial established that matching geometric edges does not identify
independent phase states. Retaining both (x+y)/2 and (x-y)/2 gives a reversible
comparison; deleting the difference is lossy.

The supplied Frobenius multiplication likewise annihilates unequal basis-label
inputs. It is not invertible on the full tensor product. The note's direct-sum
survival/conversion isometry retains that information in other channels. Its
basis-copying comultiplication does not clone arbitrary quantum superpositions.

Similarly, removing the connected state C from the four-state Hamiltonian is
legitimate at the resolvent level only because its contribution remains in the
self-energy. This is the dynamical counterpart of retaining interface mismatch
or history records, not permission to erase them.

For a general observable/hidden decomposition, the relevant formula is

    H_eff(z) = H_PP + H_PQ (zI - H_QQ)^(-1) H_QP.

Our actual hidden record space could contain many modes. Reduction to one C
state and zero internal energy is an additional model choice, not a result of
having exactly two holes or three arrow seeds. A projected effective resolvent
is not automatically a closed, time-local Hermitian Hamiltonian on the visible
channels; hidden occupation and memory remain relevant.

## 4. The existing native interface obstructions still apply

`neutron-rim-port-transport.md` checked the viewer's lower-rim/proton-ABC and
upper-rim/electron-ABC matching. An explicit length scale sqrt(8/3) is needed.
After this match, the native incident-triangle mode norms still differ:

    scaled belt: 4198/675; target ABC face: 20/3.

A Frobenius multiplication or scalar coupling a cannot simply be declared the
missing adapter without specifying its action on those actual modes and its
metric/auxiliary channels.

The proton group contains the required fixed-face rotation. The electron's
supplied five-cycle moves ABC and ABCD. A fixed interaction diagram must either
accommodate this moving port or supply an additional justified operation.
The note does not by itself resolve either obstruction, or establish an electron
indication function.

## 5. What happens to the resolvent ratio when channels are opened

The note correctly distinguishes a finite-system resolvent entry from an
observable scattering probability. An illustrative next model makes this
qualification explicit.

Assume each visible state E,2,3 couples to its own single-channel continuum,
with diagonal retarded self-energies Sigma_j(E), no direct alternative paths,
and flux-normalized widths Gamma_j(E)=-2 Im Sigma_j(E). Keep the note's real
coupling c and zero bare diagonal energy on state 3. Then the last row gives

    [E - Sigma_3(E)] G^r_3E(E) = c G^r_2E(E).

For distinct output and input channels in this declared lead model,

    T_jE(E) = Gamma_j(E) Gamma_E(E) |G^r_jE(E)|^2.

Where the ratio is defined, it follows that

    T_2E/T_3E = [Gamma_2/Gamma_3] |E-Sigma_3(E)|^2 / c^2.

Thus independence from a and b can survive in this restricted architecture,
while the bare |z|^2/c^2 expression acquires output-coupling and self-energy
factors. Additional paths, non-diagonal self-energies, thresholds, multiple modes
or energy averaging require further analysis. This algebraic lead-model example
has not been implemented as a source-bound scattering checker here.

A photon interpretation requires actual multi-output asymptotic spaces and
phase-space/flux normalization; the three finite labels do not supply them.

## 6. Qualification of the empirical target

Retain 372 as the supplied working constraint, not a universal branching ratio.
The empirical comparison must name preparation/spin conditions, collision energy,
resolution and acceptance, and the definitions of two- and three-output events.
Exclusive photon multiplicities especially require a resolution/infrared-safe
measurement specification.

Setting a coupling, interaction time or tolerance from 372 and reproducing 372
is calibration. A prediction requires fixing those quantities independently and
then testing the resulting ratio, preferably across more than one condition.
This does not require adopting a conventional particle ontology; it requires a
well-defined observable.

## 7. A geometric correction to audit before adopting the whole note

Section 17 calls the initial two-tetrahedron complex a three-dimensional ball.
That is true for ordinary face-gluing of two tetrahedra, but not for two
non-overlapping tetrahedra identified only along an edge. In the edge-glued
complex, the shared edge's link is two disjoint intervals rather than a circle
or interval; this fails the local manifold condition.

If section 17 changes from the earlier edge-contact setup to face gluing, that
change needs to be explicit. If it does not, an interaction correspondence can
still be investigated, but manifold/cobordism hypotheses cannot be assumed for
that singular input without a specified replacement. The supplied text is left
unchanged; this qualification is recorded separately.

The separate subdivision warning is directly relevant: our centroid admission
also failed arbitrary-refinement invariance. A topological composition algebra
may remove dependence on a pants decomposition, but it does not automatically
repair metric, centroid or phase data under triangulation changes.

## 8. Recommended continuation

1. Audit the supplied finite matrices, short-time series and Schur complement
   with an exact checker; retain the experimental target separately.
2. Define the interaction on our actual port/mode records, including an explicit
   native phase adapter and the electron's moving-port policy.
3. Keep the connected/mismatch sector and construct a metric-compatible joint
   operator, rather than identifying unequal records by fiat.
4. If a small collective subspace really closes, derive its reduced interaction
   and self-energy; otherwise retain the larger space.
5. Add specified asymptotic channels, prove flux conservation and derive the
   observable ratio without a separately fitted branching parameter.

This is a concrete path from static reconstructible shapes toward interactions.
The key gain is a compositional architecture and a precise elimination method,
not yet a universal interaction law, photon construction or numerical prediction.
