# J Half-Object Falsification Protocol

## Record

Date: 2026-08-12

Status: historical protocol. Entries 11--15 contain the executed tests and current verdict.

## Active question

Construct

\[
\mathsf J_n
=
(I_n^\flat)^{-1}
\left(\operatorname{gr}_R A_{{\rm scalar},n}\right)
\]

directly from scalar boundary geometry and decide whether it is an intrinsic, factorization-natural
half-object with CHY class

\[
[\mathsf J_n]
=
\left[(\operatorname{Pf}'A_n)^2\right].
\]

This protocol was written before the derivation. The criteria below are retained unchanged as an
audit trail; their later outcomes are summarized in entry 15.

## Stage 0: type the construction

Before computing examples, define:

1. the scalar master amplitude or surface object \(A_{{\rm scalar},n}\);
2. the rank-jump stratum \(R\), its normal filtration, and the grade selected by
   \(\operatorname{gr}_R\);
3. the half-object space \(\mathcal H_n\) and its quotient relations;
4. the scalar pairing map \(I_n^\flat:\mathcal H_n\to\mathcal H_n^*\);
5. the boundary restriction or gluing maps on both \(\mathcal H_n\) and \(\mathcal H_n^*\);
6. the comparison map from scalar boundary data to CHY scattering-equation cohomology.

The stage fails if \(\operatorname{gr}_R A_{{\rm scalar},n}\) is not a covector on the same space
that \(I_n\) pairs, or if inversion requires undeclared choices. A formula with unmatched types is
not repaired by agreeing numerically at low multiplicity.

## Stage 1: low-multiplicity reconstruction

Compute the candidate at \(n=4,6,8\) in at least one explicit scalar boundary basis.

- Four points fixes normalization and sign but is weak evidence because the available structure is
  highly constrained.
- Six points is the first meaningful test of multiple terms, quotient relations, and distinct
  factorization channels.
- Eight points tests whether the construction remains coherent across overlapping channels rather
  than fitting isolated residues.

At every multiplicity, change the scalar ordering basis and verify that the transformed candidate
represents the same element of \(\mathcal H_n\). Track the kernel of the pairing explicitly rather
than silently choosing a pseudoinverse.

## Stage 2: identify the CHY class

For off-diagonal entries

\[
(A_n)_{ab}=\frac{k_a\!\cdot k_b}{\sigma_a-\sigma_b},
\qquad
(A_n)_{aa}=0,
\]

compare the scalar-derived candidate with the square of the reduced Pfaffian. The target statement
is equality in the declared CHY quotient:

\[
\mathsf J_n-(\operatorname{Pf}'A_n)^2
=
\text{scattering-equation, integration-by-parts, or twisted-exact terms},
\]

with the applicable class of exact terms stated precisely. Equality only after pairing with one
Parke–Taylor factor does not pass this stage.

The comparison must also show independence of the rows and columns removed in the reduced
Pfaffian, modulo the same quotient and normalization conventions.

## Stage 3: factorization before pairing

For each allowed physical divisor \(D\):

1. choose a plumbing or degeneration parameter;
2. compute the leading boundary grade of \(\mathsf J_n\);
3. identify the induced lower-point half-object spaces;
4. include the universal boundary weight and internal gluing pairing;
5. compare with the canonical tensor product of \(\mathsf J_L\) and \(\mathsf J_R\).

The decisive diagram asks whether inverse pairing and boundary extraction commute. In shorthand,

\[
\operatorname{gl}_D
\left((I_n^\flat)^{-1}a_{R,n}\right)
\stackrel{?}{=}
\left((I_L^\flat)^{-1}\otimes(I_R^\flat)^{-1}\right)
\operatorname{gl}_D^*(a_{R,n}).
\]

The formula must be refined to the correct bundles and internal-state sum. Its purpose is to
prevent full-amplitude factorization from being mistaken for half-object naturality.

One failed physical channel is sufficient to reject \(\mathsf J\) as a primitive normal symbol in
the proposed category.

## Stage 4: close the pairing row

Only after Stages 0–3 pass, test

\[
\langle\mathsf G,\mathsf J\rangle_I
=
\mathrm{Born\!-\!Infeld}
\]

and

\[
\langle\mathsf J,\mathsf J\rangle_I
=
\mathrm{special\ Galileon}.
\]

The target is not merely equality with known tree amplitudes. Each pairing must use the same
scalar kernel, require no extra polarization or projection data beyond that already belonging to
the two halves, and inherit compatible factorization from the half-objects.

## Stage 5: strictification and surface lift

Determine whether the mixed Kähler/Jordan polarization and QTDS quartic grammar have an intrinsic
action at the half-object level. Three outcomes must remain distinct:

1. strictification is an automorphism or alternate representative of \(\mathsf J\);
2. strictification becomes meaningful only after pairing \(\mathsf J\) with \(\mathsf C\);
3. the quartic grammar is amplitude equivalent but has no natural half-object interpretation.

Then translate \(\operatorname{gr}_R\), \(I^{-1}\), and the candidate gluing law into the
surface-function/Cut Equation formulation. Survival means that the construction is intrinsic to
surface boundaries and compatible with cuts, not merely a genus-zero CHY coincidence.

## Evidence standard

A successful result must provide:

- definitions with matched domains and codomains;
- a basis-independent construction;
- explicit checks at four, six, and preferably eight points;
- equality of cohomology classes, not only paired amplitudes;
- all-channel factorization before pairing;
- cross- and self-pairing with no added theory-specific structure;
- a clear statement of what does and does not lift to surface functions.

Computer algebra may establish finite-multiplicity identities and expose counterexamples. It does
not by itself prove all-multiplicity naturality unless the computation implements a proved
recursive or boundary theorem.

## Immediate falsifiers

Stop and record a negative result if:

- the scalar pairing is degenerate on the proposed space and no canonical quotient removes its
  kernel;
- different scalar bases give inequivalent candidates;
- the CHY difference pairs to zero with \(\operatorname{PT}\) but is a nonzero cohomology class;
- a physical boundary produces an unpaired remainder or requires a partner-dependent correction;
- the Born–Infeld or special-Galileon pairing needs an additional selector not present in the
  three-generator proposal.

## Current status

Stages 0--2 pass at all multiplicities, with exact low-point audits through eight points. Stage 3
passes in genus-zero CHY/twisted cohomology on the correctly oriented nearby-cycle channel
quotient; the stronger scalar-to-surface comparison remains open. Stage 4 passes in the CHY
category. Both questions in Stage 5 remain open.

## Next action

Construct or obstruct Jordan/QTDS strictification on the half-class. In parallel, execute the YM
and Frost six-point boundary tests specified in entry 13.
