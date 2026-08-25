# Spectral conditional expectation: mathematical selector, physical failure (WP54)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Candidate

On the nondegenerate Yukawa-Gram domain, let (P_i^u) be the spectral
projectors of (H_u=Y_uY_u^\dagger). The canonical pinching map is

\[
E_u(H_d)=\sum_i P_i^uH_dP_i^u.
\]

It is built only from the source-declared Gram geometry. It is unital,
positive, idempotent, and its image is the commutant of (H_u).

## Descent

Under a full common-left weak-basis transformation (Q),

\[
P_i^u\mapsto QP_i^uQ^\dagger,
\qquad
E_{QH_uQ^\dagger}(QH_dQ^\dagger)=QE_{H_u}(H_d)Q^\dagger.
\]

Right-handed basis transformations have already disappeared in Gram
formation. The operation therefore descends to the physical quotient. Unlike
the RG flow of WP53, it is noninvertible and has a proper image.

## What it selects

Its fixed locus is

\[
[H_u,H_d]=0.
\]

For nondegenerate spectra this means the up and down eigenbases agree up to
permutation and phases: CKM mixing is trivial in the physical sense and
(J=0). Thus the map is a genuine **mathematical selector** of a proper
`physical16` subfamily.

It is not a physical flavor selector. The source supplies (H_u,H_d) and
their spectral projectors, but no action, dissipative channel, threshold
process, measurement intervention, or other flavor dynamics applies this
pinching. Declaring its fixed locus preferred would insert the desired
selection rule by hand. Worse, the selected locus is excluded by observed
nonzero CKM mixing and CP violation.

## Context and instrument

The operation collapses generic mixing points onto the commuting locus; it
does not merely rigidify chart presentations. No reference port is involved.
There is no admitted instrument for performing (E_u). Ordinary CKM
measurements instead instrument the operation's failure as a proposed physical
fixed-point law.

The smallest exact falsifier is one nonzero off-diagonal entry of (H_d) in
the (H_u) spectral frame, equivalently one nontrivial CKM mixing modulus.
Signed (J\ne0) is a stronger experimental falsifier.

This is the flavor version of the hostile distinction supplied by the other
sectors: a mathematically distinguished channel need not be executable or
dynamically authorized. Benincasa's contact-normal channel is independently
derived before its score tower; here the channel itself has no source dynamics.

## Verification

`uv run --with sympy python research/flavor/checkers/wp54_spectral_conditional_expectation.py`
writes `research/flavor/results/wp54_spectral_conditional_expectation.json`.
