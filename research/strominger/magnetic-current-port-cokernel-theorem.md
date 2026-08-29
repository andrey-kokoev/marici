# The magnetic current port is an intrinsic cokernel coordinate

Fix grade \(g\ge2\) and a source component \(q\ge1\). The branchwise
raising constructor lands in component

\[
Q=q+2.
\]

Define the two-row functional

\[
\lambda_{g,q}
=(q+3-g)e_{q+2}^{\ast}-(q+3)e_{q+3}^{\ast}.
\]

Then, for every finite pole-depth cutoff, \(\lambda_{g,q}\) annihilates
every ordinary column of the target component \(Q\).

## Proof

A minus-branch column of pole depth \(a\) is supported from \(-a-g\)
through \(1-a\). Since \(q\ge1\), it never reaches rows \(q+2,q+3\).

A plus-branch column in component \(Q\) ends at

\[
Q+1-a=q+3-a.
\]

Every admitted positive pole depth \(a\ge2\) therefore ends at or below
\(q+1\). Only the \(a=0\) plus column reaches the two rows detected by
\(\lambda_{g,q}\).

For \(a=0\), all source coefficients vanish except

\[
c_g=4^{\overline g}.
\]

The final two path coefficients of the target plus column, including its
canonical branch sign, are

\[
-(q+3)c_g,
\qquad
-(q+3-g)c_g.
\]

Their pairing with \(\lambda_{g,q}\) vanishes identically. Hence
\(\lambda_{g,q}\) annihilates the entire ordinary target image for arbitrary
cutoff.

## Detection of the current

The plus part of the \(a=0\) inter-component current has equal final
coefficients

\[
2c_g,qquad2c_g.
\]

The minus part does not reach the two observation rows. Therefore

\[
\lambda_{g,q}(K_{g,0,q})
=-2g\,4^{\overline g},
\]

which is nonzero for every \(g\ge2\).

It follows that the universal current defect is not contained in the ordinary
target image at any finite cutoff. No addition of deeper pole columns can
remove it.

## Interpretation

The current port is not a truncation artifact or a delayed magnetic column. It
is an intrinsic cokernel coordinate exposed by inter-component raising.

This settles one part of the sewing problem negatively: ordinary magnetic
transport cannot absorb the current. Any sewing law must add a genuinely new
source-authorized observation or relation.

The theorem detects the \(a=0\) current and is already sufficient to prove
that the full current family cannot be eliminated. Classifying independent
cokernel coordinates for every \(a\) is a stronger remaining problem.

Replay with: python research/strominger/checkers/magnetic_current_port_cokernel_checks.py