# Self-consistent residual-response feedback at the 420-mode cutoff

Date: 2026-10-12  
Status: **New fixed-grid numerical approximation of the omitted-space feedback. Not a complete omitted-space solution, continuum certificate, or physical electron–positron prediction.**

## 1. Result

A residual-adapted closed-response space has been coupled back to the retained
entrance and downstream equations. On a matched 17-energy packet quadrature,
peak internal transport increases from 1.698655 to
1.729546, in units 10^-3/t0. The relative change is
1.8185%. Both values are expansion-directed internal
transport, not the full mean-strain derivative.

This is **not** obtained by interpreting the prior frozen-source norm bound as a
percentage error or by inserting its inverse-only upper bound as a self-energy.
The positive radial and contact terms remain in the added closed block. Its
response and the retained source are solved together.

The additional space has 64 directions derived from the full raw omitted
internal inverse. It does not contain every omitted direction. A 128-direction
control was solved only at the central stationary energy, not for a new complete
packet. Those limits are material to the result.

## 2. Sources and fixed physical/model choices

The immediate archived source is `pentachoron_omitted_mode_estimate_bundle.zip`.
The unchanged large source is `pentachoron_higher_closed_cutoff_bundle.zip`;
its archive and nested manifests are checked before regeneration. The previous
note supplies the raw residual construction and the fixed-grid Schur bounds.

The strain/radial grid remains 49 by 32, with 25 material-tilt nodes and 32 hinge
intervals. The strain boundary is 2.4, radial support 9.6 ell, and quadratures
64 and 24. The Hamiltonian, geometric comparator and patch, elastic energy,
material connections, pose convention, full-spinor switching rules, output
record interpretation, and incoming ground-mixture preparation are unchanged.

The packet center is K=3.30 epsilon with RMS width 0.035 epsilon. K is radial
energy above the same joint ground, 3.560628202170 epsilon. The original 420
internal eigenmodes include every open incident mode throughout the packet band.
All newly added response modes are closed. No new physical reaction channel is
introduced by the numerical enrichment.

## 3. Construct a response space rather than another uniform energy cutoff

One raw internal body grid has 49*25*10 = 12,250 directions. Let P retain the
420 source eigenmodes; Q=I-P therefore has 11,830 directions. This P is distinct
from the rank-two physical/model entrance matching projector.

At K=3.30 solve the old retained problem and form its complete raw omitted
forcing, including the geometric potential, the diagonal matching term, and
the solved hinge source:

    R = Q H P Psi_420.

Collect all 32 radial-cell, two-body-copy, and four-preparation columns into a
12,250-by-256 matrix. The body records are expressed in their consistent source
frames before combining these numerical snapshots.

Solve the full raw sparse internal system, deflated against P:

    Z = [Q(h_int-E_c)Q]^(-1) R,
    G_response = R^dagger Z.

The inverse acts on the full raw internal matrix, not only the next 28 computed
eigenvectors. Diagonalize the positive response Gram matrix. Transform its
leading directions back to internal coordinates, orthogonalize them against P,
and use an ordinary orthonormal basis for their span Q_r.

For r=64, the selected span captures
99.993508% of this **frozen-source inverse-weighted diagnostic**.
That percentage is not a fraction of physical events, not a proof that the
actual closed-block response is captured to that accuracy, and not a packet
error bar. The inherited radial kinetic and contact terms were omitted only in
constructing the diagnostic basis, not in the subsequent feedback solve.

The central snapshot rank at the numerical construction tolerance is
202. Increasing r to 128 captures
99.99999777% of the same diagnostic. These are tailored
linear combinations across the omitted spectrum, not the next r eigenmodes.

The old 420 eigenvectors remain unchanged. The native internal operator is
Rayleigh–Ritz diagonalized on Q_r, so the projected space has 484 directions per
body for r=64. Its added Ritz energies span approximately 16.693–58.057 epsilon;
this is **not** a claim that all eigenmodes below 58.057 have been retained.
The conservative lower bound for the still-omitted complement is 16 epsilon.

The response space is fixed for the entire energy band. It is not refitted at
each spectral sample or used to change incoming phases between samples.

## 4. Solve the feedback with radial and diagonal contact terms retained

Project the same raw geometric and patch quadratures into P plus Q_r. Copy the
retained-retained blocks from the verified source and independently construct
the cross and response blocks. The same radial square-root resolvent is used
for every added internal Ritz direction. Neither the entrance nor the hinge is
held fixed in this new scattering solution.

At fixed energy, the structure is

    D_r(E) = H_(Q_r Q_r) - E,
    Psi_(Q_r) = -D_r(E)^(-1) H_(Q_r P) Psi_P,
    H_eff,r(E) = H_PP - H_(P Q_r) D_r(E)^(-1) H_(Q_r P).

Here D_r includes the radial kinetic and diagonal interaction terms, and the
retained sector includes the existing downstream records. This is the Schur
form of the enlarged conservative Galerkin problem. It is not a separately
chosen negative potential, imaginary loss term, or fitted branching weight.

Because the added block is closed, its exact form is positive at the tested
energies. The response-subspace Schur quadratic action is a lower approximation
to the full omitted action. Positivity alone does not determine the sign of a
current or product-flux change.

Four prepared source columns are solved together by a batched Frobenius-space
GMRES implementation of the same linear equations. Independent separate-column
applications of the original operator check its true residual. The central
64-direction solution was also obtained with the original separate-column
solver. This is an algebraic implementation choice, not a new Hamiltonian.

## 5. Closed-block audit on the frozen old source

For comparison with the previous bound, keep the old retained source fixed and
solve the added positive closed block independently. Values are actions in
hbar units under the unit-flux convention:

| Quantity at K=3.30 | Value |
|---|---:|
| Previous inverse-internal upper bound beta | 0.0161262380 |
| Solved 64-direction closed-block action | 0.0076273287 |
| Solved 128-direction closed-block action | 0.0076929908 |

The 64-to-128 action increase is
0.8609%. The radial and interaction terms
matter: the solved action is less than half the previous inverse-only upper
bound. The conservative difference beta minus the 128-direction action is
still about 0.008433.
That broad inequality is not a packet-current error estimate.

The closed inverse equations and an independently written closed
Lippmann–Schwinger equation agree. The actually solved feedback tail also
satisfies the closed equation with its **updated** retained source and hinge
trace. The relative change of the retained contact coefficients at the center
is about 0.818%; this is
not a whole-space norm or event probability.

## 6. Coherent packet result and matched baseline

The principal feedback packet uses 17 fresh stationary energy solutions on
3.09 <= K/epsilon <= 3.51, six RMS widths on either side of the center. Complex
amplitudes are summed before currents are formed. The baseline is replayed on
the same 17 energy nodes from the supplied 33-node source kernels.

Rates below are in 10^-3/t0, with t0=hbar/epsilon. Product flux is a percentage
of the full incident preparation.

| Approximation, same 17-node energy rule | Peak internal transport | Whole-packet transport | Product-record flux |
|---|---:|---:|---:|
| 420 eigenmodes, replayed baseline | 1.698655 | 2.620729 | 0.566594% |
| 420 plus 64 response directions | 1.729546 | 2.647664 | 0.565309% |

Peak transport changes by 1.8185%, whole-packet
transport by 1.0277%,
and product flux by -0.001286 percentage
points. The previous quoted 420-mode peak rate, 1.696480, used 33 energy nodes;
its matched 17-node replay is 1.698655. The table does not mix those quadratures.

The peak time changes from 8.783202 to 8.788339 t0.
Positive R_peak means internal transport toward larger axial factors. It is
not the entire conditional mean-length derivative: selective entry and release
remain separate. The direct-sum record model is not a two-particle preparation.

## 7. Response-space and energy-sampling checks

Doubling the response space at the **central stationary energy only** changes
the current-to-residence ratio from
0.003336883314 to
0.003336880724 /t0,
a relative change of -0.0000776%.
The central product fraction changes by
0.00002690 percentage points.
A full 128-direction packet has not been calculated. This central agreement is
not a band-wide or nonlinear peak-observable error certificate.

A paired 17-to-9-node energy-subsampling control changes the **feedback increment**
in peak transport from 3.089073532e-05 to
3.110042476e-05 /t0, about
0.679% of the increment.
However, the absolute rates on 9 nodes are appreciably under-resolved: the
feedback rate is 1.482836 rather than
1.729546. Paired cancellation must not be advertised as
absolute energy-quadrature convergence. No 33-node feedback packet was recomputed.

## 8. Verification actually executed

There are 17 completed feedback energy rows, one additional 128-direction
central row, and one fresh old-basis central reconstruction used to form the
response snapshots. Unchanged source packets are replayed, not counted as new
stationary solutions. No new full scattering matrix is computed.

Independent checks include:

- source hashes, rebuilt ground and cutoff energies, and exact preservation of
  the old retained subspace and its projected interaction blocks;
- raw all-internal inverse residual, response-space orthogonality, and native
  projected diagonalization;
- separate-column source-equation residuals for every prepared solve and the
  actual four-column flux Grams;
- reconstruction of downstream stationary equations at five packet energies;
- direct time-domain wavefunction, interior Schrodinger equation, every
  strain-slice continuity identity, and conditional mean-current balance at
  five times;
- direct energy summation versus energy-space Gram reconstruction;
- independent frozen and self-consistent positive closed-block equations.

The main raw-field verifier passes 40 entries. The largest
prepared-column flux residual is
1.975e-12; the largest retained linear
residual is 1.902e-12. These are
numerical algebra checks, not continuum or experimental error bars. Finite
spatial grids, high response directions outside the chosen space, and the
source's physical interpretation remain unresolved.

## 9. Interpretation and next step

The omitted response has now been fed back **in an explicit numerical response
subspace**, instead of being treated only as a frozen-source upper bound. The
computed packet correction is modest and expansion-directed transport survives.
This does not certify the complete omitted-mode correction or the continuous
model's current. It supplies no physical electron/positron threshold, calibrated
speed, contraction law, independently occupied product, photon, or branching
ratio.

The next response-space test should use the residual of the corrected solution
and repeat the full packet in a larger response space. Spatial and energy-grid
refinement remain separate obligations.

## 10. Reproduction

See README.md. The compact package contains scripts, coherent kernels, prepared
scattering columns, numerical receipts, and source hashes. It omits regenerated
large projection matrices, eigenvectors and raw wavefields. `replay_feedback.py`
audits the saved readout only; `reproduce_feedback.py` rebuilds the fields from
the unchanged earlier source archive and runs the raw audits. No network access
or repository modification is required.
