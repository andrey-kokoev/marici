# Holonomy contrast dichotomy: WP745

## Question

Can a discrete or nonlocal holonomy preserve the physical diagonal (SO(3))
and simultaneously distinguish its triplet and singlet strongly enough to fix
a nonzero portal contrast?

## Preserving holonomies

The WP743 scalar zero modes form the vector (4) of (SO(4)), restricted as

\[
4\downarrow SO(3)_{\mathrm{diag}}=3\oplus1.
\]

The exact Lie-algebra centralizer of this diagonal (mathfrak{so}(3)) inside
(mathfrak{so}(4)) is zero-dimensional. At group level, Schur's lemma and
orthogonality imply that a commuting transformation has the form

\[
W=\operatorname{diag}(\epsilon_t I_3,\epsilon_s),
\qquad
\epsilon_t,\epsilon_s\in\{-1,1\}.
\]

The (SO(4)) determinant condition is
(epsilon_t^3\epsilon_s=1), so the only possibilities are

\[
W=I_4,
\qquad
W=-I_4.
\]

Both act identically on the triplet and singlet. Neither can orient or
normalize a nonzero contrast.

## Distinguishing twists

The smallest commuting transformation that does distinguish the two sectors is

\[
R=\operatorname{diag}(-I_3,1).
\]

But (det R=-1), so (R\notin SO(4)). Admitting it enlarges the gauge
groupoid to an (O(4)) or defect-twisted experiment. This is a new relational
construction, not a hidden observable of the original source.

After this reduction, the invariant CP-even quadratic forms remain

\[
K=\operatorname{diag}(a,a,a,b).
\]

The twist labels the two sectors but does not fix (b-a). Conversely, a
noncentral proper (SO(4)) rotation fails to commute with the full physical
(SO(3)) and breaks the admitted low-energy group.

## Dichotomy

The exact alternatives are therefore:

1. The holonomy lies in the admitted (SO(4)) centralizer. It preserves the
   physical group but acts as a scalar and gives no contrast.
2. The twist distinguishes triplet from singlet. It changes the groupoid or
   breaks the physical group, and its residual commutant leaves a continuous
   contrast coefficient.

This is stronger than saying that a particular Wilson-line potential failed.
Symmetry and holonomy data alone cannot both preserve the declared physical
group and uniquely select a nonzero CP-even singlet–triplet contrast.

Wilson-line phases can acquire dynamical effective potentials, but their
minima depend on matter content and geometric moduli rather than following
from topology alone. See
[Hosotani, Noda, and Takenaga](https://arxiv.org/abs/hep-ph/0410193).

## Disposition

Discrete holonomy does not supply the requested source principle. The
preserving branch yields zero contrast; the distinguishing branch changes the
experiment and restores the free coefficient (b-a).

The result covers the (SO(4)) vector carrier and holonomies preserving the
full diagonal (SO(3)). Larger groups or defects with additional degrees of
freedom remain possible, but they need a dynamical normalization operation,
not symmetry data alone. The compactification clock, RG basin, threshold
completion, and calibrated physical16 instrument remain open.

Reproduce with
`uv run --with sympy python research/flavor/checkers/wp745_holonomy_contrast_dichotomy.py`.

Generated result:
`results/wp745_holonomy_contrast_dichotomy.json`.
