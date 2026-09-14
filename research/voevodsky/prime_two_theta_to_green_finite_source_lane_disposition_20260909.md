# Prime-two theta-to-Green finite source lane disposition

Date: 2026-09-09

## Question

How far can the first source-authorized theta-pair-to-Green comparison test be constructed before the canonical G4 witness is exposed?

## Claim boundary

At prime two and jet cutoff two, the source lane is complete through the ordered theta-pair density, radial Stokes graph, Adams grade, bordered Schur readout, pole-cancelling source range, boundary Green form, reciprocal odd sewing, contragredient action, and maximal-isotropic sewing graph. None of these constructions identifies the source object with G4 or supplies the missing arithmetic loading.

## Constructed finite lane

The ordered pair `(1,2)` on the shell with exponential endpoint coordinates `(1,2)` supplies

\[
\rho(t)=\int_a^b\Phi_1(u)\Phi_2(u+t)\,du,
\qquad
D_t\rho=e-\frac12w.
\]

The retained finite feature consists of Adams grade two, two wall coordinates, and endpoint/Wronskian jets through order two on both orientations. Its ambient feature matrix has shape \(24\times15\) and rank \(15\).

The bordered response is

\[
R(z)+2E(z)=\frac{\rho(0)+E(z)-\frac12W(z)}{z}+2E(z).
\]

On the source-generated range the apparent pole cancels:

\[
\rho(0)+E(0)-\frac12W(0)=0.
\]

This constraint is retained separately on the two reciprocal orientations.

The finite boundary coordinates

\[
q_\pm=\rho_\pm(0),
\qquad
p_\pm=E_{\pm,0}-\frac12W_{\pm,0}
\]

carry the nondegenerate Green matrix

\[
J=
\begin{pmatrix}
0&-1&0&0\\
1&0&0&0\\
0&0&0&1\\
0&0&-1&0
\end{pmatrix}.
\]

The unique common-sign sheet swap preserving this matrix is

\[
q_+\leftrightarrow q_-,
\qquad
p_+\leftrightarrow-p_-.
\]

Its matrix \(W\) is an orthogonal involution and preserves \(J\). The graph of \(W\) is maximal isotropic in the doubled form \((-J)\oplus J\), and the finite contragredient equals \(W\).

## Falsification results

Exact hostile checks reject:

- erasure of pair ordering;
- deletion of either shell endpoint;
- replacement of the Wronskian coefficient \(-1/2\) by zero;
- retention of only the zeroth response jet;
- replacement of shell history by the Adams scalar \(1/16\);
- deletion of either pole-cancellation equation;
- equal orientation on the two half-lines;
- collapse of Hermitian adjoint into analytic transpose;
- use of \(J\oplus J\) for the doubled sewing graph.

## First missing typed datum

The canonical G4 carrier, metric, differential, boundary traces, sewing matrix, arithmetic loading, and response readout are still not exposed. Consequently there is no source map

\[
C_{\mathrm{FP}}:X_{\mathrm{FP}}^{\mathrm{ret}}\longrightarrow X_{G4}
\]

whose pullback can be compared with the finite matrices above.

The first executable test after exposure is the Wronskian row:

\[
D_t\rho-e+\frac12w=0.
\]

The canonical G4 row must pull back to coefficient \(-1/2\); coefficient zero is the preregistered deliberate failure. Passing that row does not authorize the remaining nine interface comparisons.

## Disposition

The finite source lane survives all preregistered internal hostiles and is ready as a conformance target. Further construction inside this lane would duplicate already retained coordinates or invent the missing G4 arrows. Work stops at the source-identification boundary until an owner-reviewed G4 witness is materialized.

## Verification

- `research/voevodsky/results/prime_two_theta_history_transfer_fixture.json`
- `research/voevodsky/results/prime_two_theta_history_partial_transfer.json`
- `research/voevodsky/results/prime_two_radial_boundary_form_candidate.json`
- `research/voevodsky/results/prime_two_reciprocal_boundary_sewing_candidate.json`
- `research/voevodsky/results/prime_two_maximal_isotropic_sewing_graph_candidate.json`
- `research/voevodsky/results/g4_green_interface_conformance_manifest.json`
