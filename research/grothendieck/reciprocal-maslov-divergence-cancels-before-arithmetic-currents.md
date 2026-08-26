# Reciprocal Maslov Divergence Cancels Before Arithmetic Currents

## Signed reciprocal areas

Fourier–Tate reciprocity reverses the orientation of the phase-space cell. In normalized units, the two sectors therefore carry areas (t) and (-t), where

\[
t=\frac{\mathcal A}{2\pi}.
\]

Using the standard integer grade (m(t)=\lfloor t\rfloor), one has for every noninteger (t)

\[
m(t)+m(-t)=-1.
\]

At an exact crossing (t\in\mathbb Z), the sum is zero because the centered Fourier minor itself vanishes.

Thus the grades of the two reciprocal sectors may diverge separately, but their sum is bounded before any prime, square, or archimedean subtraction is introduced.

## Half-boundary normalization

Away from crossings, define the centered grade

\[
\mu(t)=\lfloor t\rfloor+\frac12.
\]

Then

\[
\mu(-t)=-\mu(t).
\]

The half-unit is not fitted to the theta zeros. It is forced by reciprocal oddness of the two standard floor decompositions. It is the familiar endpoint convention for an oriented crossing count.

At an exact crossing, the oriented minor is zero and the grade requires a one-sided or relative convention. The jump is real data and may not be smoothed away.

## Consequence

The extensive Maslov divergence does not require primitive or prime-square currents for cancellation. Reciprocity already cancels it. Therefore identifying those arithmetic currents with Maslov counterterms merely because both appear near completion would be a typing error.

What survives is only:

- the half-boundary convention;
- the discrete jump at each aliasing surface;
- and any source-labelled incidence between those jumps and the physical boundary readout.

## Why this weakens the metaplectic RH route

Fourier aliasing surfaces occur universally and abundantly. Their reciprocal crossing grade is coherent and finitely normalized without arithmetic input. Hence the Maslov lift by itself cannot orient the de Branges/Krein form or distinguish the theta source from hostile sources.

The route remains relevant only if labelled theta transport proves a nontrivial incidence theorem: the crossings contributing to the physical boundary line must carry a source signature unavailable to generic Fourier cells. Without that extra law, the metaplectic grade is explanatory geometry but no RH force.

## Next falsifier

Construct a hostile reciprocal source with the same centered minor and reciprocal half-grade law but an off-seam scalar zero. Such a source would show decisively that Maslov coherence plus seam typing is insufficient. Existing symmetric multiplier and compact-source hostiles are likely candidates; the test must preserve the complete declared boundary metadata.

## Verification

The dependency-free exact-rational checker `research/grothendieck/checkers/reciprocal_maslov_half_boundary.py` verifies bounded raw grade sums, reciprocal oddness after the half-boundary normalization, exact-crossing behavior, and cancellation at arbitrarily large rational area.
