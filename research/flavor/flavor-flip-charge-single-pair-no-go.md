# Flip-charge single-pair no-go: WP668

## Exact contradiction

Let a vectorlike messenger pair have binary charges \(q_L,q_R\) under the
flip for an odd triplet \(n\). A bare Dirac mass requires

\[
q_L+q_R=0\pmod 2,
\]

while a linear Yukawa \(\overline\Psi_LJ_n\Psi_R\) requires

\[
q_L+q_R+1=0\pmod 2.
\]

No charge assignment satisfies both equations. Therefore WP664's convenient
single-pair mass matrix \(MI+yJ_n\) cannot itself realize the exact flip that
WP667 needs to protect the kinetic interface.

## Minimal repair

Two massive vectorlike pairs \(A,B\) suffice. Give them opposite parity and
use off-diagonal triplet vertices

\[
\overline A_LJ_nB_R,
\qquad
\overline B_LJ_nA_R.
\]

The modulo-two equations have exactly two complementary solutions:
\((q_{A_L},q_{A_R},q_{B_L},q_{B_R})=(0,0,1,1)\) and its global complement.
For the two independent triplet flips, an \(n\)-chain differs only in the
\(n\) charge and an \(m\)-chain only in the \(m\) charge.

## Census consequence

WP651 has two identity coefficients and four odd frame-word coefficients.
Keeping one pair for each identity chain and doubling each frame-word chain
changes the minimal vectorlike-pair census from six to ten. Reuse would be a
different topology and must be declared before matching.

## Disposition

Exact kinetic protection is possible, but it changes the messenger grammar.
The protected theory no longer inherits WP651's one-pair tree matching or
WP664's one-pair supertrace automatically. Tree matching, loop support,
thresholds, and anomaly counting must be recomputed for the doubled chains.

This is a source-construction correction, not a selector.

Reproduce with: uv run python research/flavor/checkers/wp668_flip_charge_single_pair_no_go.py

Generated result: results/wp668_flip_charge_single_pair_no_go.json.
