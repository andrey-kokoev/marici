# Five residual types for the RH meta-observer

## Question

Which residuals should be quotiented, annihilated, trivialized, bounded, or preserved?

## 1. Presentation residual

Packet repetitions, permutations, and declared gauge relations generate a presentation subspace

\[
P_I\subseteq V_I.
\]

These directions are removed by the canonical quotient `V_I/P_I`. A duplicate-label null vector belongs here. Its vanishing is not evidence for spectral degeneracy.

Disposition: **quotient**.

## 2. Observer-invisibility residual

On the presentation quotient, define

\[
N_I=
\ker\!\left(\prod_{p\in\mathcal O_I}O_p\right).
\]

Joint faithfulness requires `N_I=0` after refinement through the full observer family. A nonzero class here means the observers fail to distinguish a source degree of freedom.

Disposition: **annihilate by proved joint faithfulness**, not by adding a presentation relation after observation.

## 3. Local transition anomaly

Before global descent, local representatives may differ by transition residuals `Omega_f`. They must obey the cocycle law and be trivialized by one endpoint--gamma completion datum. Once one global completed kernel exists, this modality is discharged and `Omega=delta K` is tautologically exact.

Disposition: **trivialize before descent**.

## 4. Arithmetic approximation residual

For a prime cutoff,

\[
E_{I,N}=G_I-G_{I,N}.
\]

This residual is neither quotiented nor set formally to zero. It receives a cell-specific norm bound, including derivative order, and converges to zero as the cutoff enlarges.

Disposition: **bound and converge**.

## 5. Substantive positive residual

The completed Weil form is

\[
R_I=A_I^*A_I-B_I^*B_I.
\]

The desired constructor gives

\[
R_I=D_I^*D_I\ge0.
\]

These forms must be natural under observer restriction. Their nonzero values contain the mathematical signal being tested.

Disposition: **preserve and prove positive**.

## Forbidden coercions

The following identifications are invalid:

- treating a presentation null as a zero of the positive spectral form;
- declaring an invisible source class to be gauge merely because no current observer detects it;
- treating a finite cutoff error as a completion anomaly;
- forcing the substantive positive residual to zero in the name of coherence;
- assigning cohomology to `delta K` after a global `K` has already been constructed.

## Meta-observer output type

Each record should carry

\[
(\text{residual kind},\text{source object},
\text{observer/cell},\text{typed value},
\text{bound or witness},\text{required disposition}).
\]

A record is malformed if its action does not match its residual kind.

## Disposition

The operator's expected residual is not one undifferentiated defect. The meta-observer must preserve this five-way type distinction. Only observer invisibility and genuine completed commutator curvature have a zero target; the positive residual is the final object of interest.
