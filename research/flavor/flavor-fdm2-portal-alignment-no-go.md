# Scalar CP breaking does not universally transmit through FDM-2: WP1018

## Question

Does selecting a complex FDM-2 singlet vacuum select physical quark CP
violation over the full admitted mediator-coefficient family?

## Admitted state domain

Use the complete real-coefficient WP90 tree grammar at either CP-conjugate
singlet vacuum:

\[
Y_d=Y_0+zab,qquad z=4/5\mathord\pm3i/5.
\]

The source coefficients (Y_0,a,b) are allowed real parameters. The faithful
output is the weak-basis orbit of the Hermitian Gram pair in physical16.

## Exact hostile portal

Choose

\[
Y_0=\operatorname{diag}(1,2,4),\qquad a=e_1,qquad b=e_1^T.
\]

Although \(\operatorname{Im}z=\mathord\pm3/5\ne0\), the induced down Gram is

\[
H_d=\operatorname{diag}(18/5,4,16).
\]

It is nondegenerate and commutes with
\(H_u=\operatorname{diag}(1,4,9)\). Hence

\[
\det[H_u,H_d]=0.
\]

The singlet source is CP broken, but the portal does not transmit that
breaking into physical flavor CP violation.

## Local coefficient image

At the original WP90 witness, varying the nine real entries of (Y_0) with
the portal direction frozen gives an eight-dimensional Gram response. Allow
only one additional already-admitted portal coefficient, (a_1), and the
exact response rank becomes nine. A pivot minor is

\[
663552/25\ne0.
\]

Thus the full mediator grammar has locally open image in the nine-dimensional
down-Gram representative. Its freely adjustable coefficients do not impose a
proper local physical relation. The rank statement is capacity, not source
authority.

## Contextual partition and descent

The CP-broken singlet vacuum family splits into aligned portals with physical
(J=0) and generic portals with (J\ne0). Both statements use the
weak-basis-invariant commutator determinant; the Jacobian uses only a local
representative and is not treated as an invariant coordinate.

All 1,210 fitted sheets have (J\ne0). The fixed WP90 witness therefore
demonstrates capacity, but the full admitted coefficient family does not
select the fitted CP-violating class.

## Instrument and smallest falsifier

The signed Jarlskog/CKM readout is sufficient to detect the failure. The
smallest exact falsifier is the single-generation aligned portal above:
nonzero singlet imaginary part, nondegenerate spectra, and exactly zero
physical CP invariant.

## Claim boundary

This does not invalidate the fixed WP90 nonzero-CP witness or the scalar
vacuum selector. It corrects the stronger inference that scalar CP breaking
alone selects physical quark CP violation throughout the allowed mediator
grammar. No implicit time or causal ordering is assigned.

## Disposition

Reclassify FDM-2 as a singlet-vacuum selector and a conditional physical CP
transmitter. A genuine flavor selector additionally requires a source law
restricting the portal coefficients to a proper CP-transmitting locus, plus
physical coefficient calibration and numerical survival on the fitted
ensemble.

Verification: uv run --with sympy python
research/flavor/checkers/wp1018_fdm2_portal_alignment_no_go.py.
