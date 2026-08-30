# Heavy-pole spectral residues and conditional width sum rules

## Admitted domain

WP509 uses the canonically normalized WP508 heavy gauge blocks on the positive
source domain.  For each entrance coordinate

\[
r\in\{a^2,a^2+b^2,b^2\},
\]

restrict to the open simple-spectrum locus where the cubic \(C_r\) has three
distinct positive roots and \(C_r(Q)\ne0\), with

\[
Q=3g_F^2\mu^2.
\]

The width statement additionally assumes six effectively massless quarks.  It
does not assume that scalar, messenger, or other vector channels are closed.

## Exact root-functional residues

Write the two-current resolvent of one four-generator block as

\[
G_r(z)={N_r(z)\over (z-Q)C_r(z)}.
\]

The embedded quintet residue is

\[
R_{r,Q}={N_r(Q)\over C_r(Q)}.
\]

For every cubic root \(\rho\), its residue is the exact algebraic functional

\[
R_{r,\rho}={N_r(\rho)\over(\rho-Q)C_r'(\rho)}.
\]

The checker proves that \(R_{r,Q}\) is a rank-one \(g_F^2\)-scaled projector
and that \(C_r\) divides \(\det N_r\).  Hence every simple cubic-root residue
has rank at most one.  Self-adjoint spectral positivity makes these matrices
positive semidefinite on the admitted positive simple-spectrum domain; an
independent rational source point verifies three positive rank-one residues in
each sector.

## Completeness and partial widths

The large-frequency coefficient fixes the exact matrix sum rule

\[
R_{r,Q}+\sum_{C_r(\rho)=0}R_{r,\rho}=g_F^2I_2.
\]

Thus the individual residues are independently frozen functions of the source
parameters; no detector fit or desired pole value enters their definition.

With only the declared six-quark channel counted, a pole has conditional
fractional partial width

\[
{\Gamma_q(\rho)\over M_\rho}={\operatorname{tr}R_{r,\rho}\over4\pi}.
\]

Completeness gives the sector sum rule

\[
{\Gamma_q(Q)\over M_Q}
+\sum_{C_r(\rho)=0}{\Gamma_q(\rho)\over M_\rho}
={g_F^2\over2\pi}.
\]

This freezes quark partial widths, not total widths.  Equality with a total
width requires a common-source threshold proof for the enlarged WP506–WP508
scalar, messenger, and vector spectrum.

## Classification and falsifiers

The operation is a source-derived spectral rigidifier, not a numerical
selector.  It descends from the gauge-covariant current resolvent and does not
depend on the Gell-Mann presentation used to compute it.  There is still no
calibrated instrument that prepares two flavor currents, resolves all heavy
poles, and measures their matrix residues in one common frame.

The smallest exact boundary is \(C_r(Q)=0\) or a zero cubic discriminant: the
simple-pole formula then fails and a degenerate spectral projector is required.
The smallest width falsifier is one kinematically open nonquark channel with a
nonzero source vertex.  Numerical prediction additionally fails under any
allowed change of the still-unselected dimensionless source coefficients.
