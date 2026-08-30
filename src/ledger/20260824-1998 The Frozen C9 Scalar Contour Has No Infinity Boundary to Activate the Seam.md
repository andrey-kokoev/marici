# 1998 — The Frozen C9 Scalar Contour Has No Infinity Boundary to Activate the Seam

## Question inherited from Entry 1997

Entry 1997 proves that the scalar logarithmic five-circuit seam defect is canonically de Rham exact:

\[
\partial_\mu\partial_{\rm OS}(\alpha_C)
=
d_zH_\mu,
\qquad
H_\mu=-\partial_{\rm OS}T_\mu(\alpha_C).
\]

A closed contour annihilates this term.  The sole remaining scalar activation route is a source-derived relative boundary with a nonzero pairing against \(H_\mu\).

## Frozen source contour

Equations (4.1)--(4.4) of arXiv:2305.19686v2 define the post-localization contour as a real contour in each unfixed variable.  Each real line may be closed in the upper or lower half-plane; the two choices give residue representations of the same canonical function.

The frozen \(C_9\) localization leaves nine variables:

\[
(c_{2,2},c_{3,2},\ldots,c_{9,2},c_{9,3}).
\]

For every variable, the source integrand contains:

1. its own factor \((c-i\epsilon)^{-1}\);
2. exactly three localized linear denominators depending nontrivially on that variable.

Thus the denominator degree is four in every contour direction.

## Projective infinity audit

For one unfixed variable,

\[
\omega(c)\sim\frac{dc}{c^4}.
\]

With \(c=1/s\),

\[
\omega
\sim
-s^2,ds.
\]

Hence the form vanishes to order two at projective infinity.  All nine infinity residues are zero.  The closing arcs contribute nothing, so the source contour defines a closed residue cycle rather than a relative cycle with an infinity boundary current.

The logarithmic transgression does not worsen this conclusion: replacing a parameter derivative of a linear denominator by \(h=\partial_\mu L/L\) adds no positive power of \(c\).  Its pullback to every infinity face still vanishes.

## Narrow result

\[
\boxed{
\text{The frozen scalar }C_9\text{ contour cannot physically activate
the seam transgression.}
}
\]

Finite UHP/LHP poles label residue decompositions of the closed contour; they are not a new relative boundary.  Therefore the scalar logarithmic coefficient lane is closed:

\[
\int_{\Gamma_{C_9}}d_zH_\mu=0.
\]

Any nonzero seam activation must come from additional source-derived coefficient or relative-chain structure, such as a nonsplit higher-rank connection whose mixed defect is not de Rham exact in the relevant supported complex.  This entry does not authorize constructing such an object by fitting.

## Verification

- `research/benincasa/results/nine-site-canonical-contour-packet.json`
- `research/benincasa/checkers/c9_contour_infinity_decay.py`
- `research/benincasa/results/c9-contour-infinity-decay.json`

Result SHA-256:

`30e94d23914f3dca3c80dc5fb0b738b72cdea29c2c5035818e4d85dae31c5df4`

Allocator claim: `seqclaim-ca6d7d89ba9982d12aac959c`.

Epistemic graph event: `ev-000000002712-838bfe08-cf05-4f16-b6e9-5b24fbb5c033`.
