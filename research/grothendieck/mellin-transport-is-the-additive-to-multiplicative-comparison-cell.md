# Mellin Transport Is the Additive-to-Multiplicative Comparison Cell

## The two construction paths

For a positive integer \(n\), its prime-valuation packet determines

\[
\log n=\sum_p v_p(n)\log p.
\]

The additive theta path assigns the heat weight

\[
h_t(n)=e^{-\pi t n^2}
=
\exp\left(
-\pi t\exp\left(2\sum_pv_p(n)\log p\right)
\right).
\]

This is globally coupled in the prime coordinates. It does not factor into
one-place weights.

The multiplicative Euler path assigns

\[
n^{-s}
=
\exp\left(-s\sum_pv_p(n)\log p\right)
=
\prod_p p^{-s v_p(n)}.
\]

This factors exactly over the prime coordinates.

## Mellin monoidalizes the heat weight

For \(\operatorname{Re}s>0\), the labelwise Mellin integral is

\[
\int_0^\infty
e^{-\pi n^2t}t^{s/2-1}\,dt
=
\pi^{-s/2}\Gamma(s/2)n^{-s}.
\]

Thus Mellin transport converts the globally coupled additive heat
construction into the separable multiplicative character, with the
archimedean gamma factor retained.

For \(\operatorname{Re}s>1\), absolute convergence permits interchange of
the integer sum and the Mellin integral:

\[
\int_0^\infty
\sum_{n\ge1}e^{-\pi n^2t}t^{s/2-1}\,dt
=
\pi^{-s/2}\Gamma(s/2)\zeta(s).
\]

This is the exact comparison cell between:

1. diagonal integer formation followed by heat transport and Mellin
   observation;
2. prime-valuation formation followed by Euler-character aggregation.

It exists before analytic continuation and before any zero is inspected.

## Completion of the cell

Poisson reflection extends the additive path beyond its initial convergence
sector. Splitting at the self-dual scale exposes the two polar boundary
currents. Retaining those currents gives the relative completed comparison.

The continuation is therefore not a new equality imposed on the scalar
answer. It is completion of an already commuting source square:

- labelwise Mellin transport supplies the interior comparison;
- Poisson reflection supplies the reciprocal chart;
- the two polar currents supply the boundary of the completed square.

This explains why additive theta formation and multiplicative Euler formation
produce the same completed section.

## What the cell does not explain

The comparison cell is faithful to source provenance, but it is
divisor-neutral. After the integer labels have been summed, evaluation at one
complex \(s\) is still a scalar compression. Distinct label contributions can
cancel while the comparison square remains perfectly coherent.

Equivalently, Mellin transform is faithful when retained as a transform, but
point evaluation of its output is not faithful to the source packet.

Therefore adding the comparison cell closes the question of why the two
constructions agree. It does not answer why their common scalar section should
avoid zero away from the reciprocal seam.

## Revised missing rung

The programme no longer lacks:

- an angular state port;
- a radial--angular identification;
- or an additive--multiplicative comparison.

All three are present.

The missing rung is a law on the comparison cell itself: a source-derived
orientation, conservation, or exactness statement that survives scalar
evaluation and forbids off-seam cancellation.

That law must distinguish the completed Gaussian--integer source from a
hostile source whose Mellin comparison square also commutes but whose scalar
transform has off-seam zeros.

## Falsifier

Any proposed higher coherence is nonexplanatory if it follows solely from:

- the labelwise gamma integral;
- absolute Fubini interchange in the Euler chamber;
- Poisson functional-equation sewing;
- or equality of the final completed scalar sections.

Those properties establish the comparison cell derived here and are
compatible with scalar cancellation.
