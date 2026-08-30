# Seam zeros make the sector index a relative boundary class

## The direct Toeplitz obstruction is not yet defined

A Toeplitz operator with continuous scalar symbol is Fredholm only when the
symbol is invertible on the boundary. The completed Riemann section is expected
to vanish at infinitely many points on the critical seam. Therefore its raw
boundary value cannot directly define the sector Fredholm class required by
the previous proposal.

This is not a technical nuisance. A boundary zero makes the assignment of
index charge to the two adjacent sectors ambiguous.

## Exact circle hostile

Consider the boundary symbol

\[
u_0(z)=z-1
\]

on the unit circle. It has one zero exactly on the boundary, so its Toeplitz
operator is not Fredholm.

Approach it through

\[
u_n^-(z)=z-(1-1/n)
\]

and

\[
u_n^+(z)=z-(1+1/n).
\]

Both coefficient families converge to the same boundary-zero symbol. But
`u_n^-` has its zero inside the disk, while `u_n^+` has its zero outside.
Consequently their winding numbers, and hence Toeplitz indices, differ by one
for every finite `n`.

The limiting boundary data do not determine which sector receives the charge.

## Half-plane version

For a real seam coordinate `t`, the regularizations

\[
t-i\varepsilon
\qquad\text{and}\qquad
t+i\varepsilon
\]

have identical boundary modulus

\[
t^2+\varepsilon^2
\]

but place the zero in opposite half-planes. Their ratio

\[
\frac{t-i\varepsilon}{t+i\varepsilon}
\]

is a unit-modulus Blaschke factor carrying one unit of sector index.

Thus even the full boundary energy and the singular seam limit cannot choose
the sector allocation.

## Required replacement

The correct object is a relative boundary class, not an absolute Toeplitz
index of the raw scalar. It requires a source-authorized treatment of the seam
divisor, such as:

- a spectral section or Calderón projector;
- a two-sided germ specifying how the boundary state approaches the seam;
- a relative Toeplitz pair whose common boundary-zero factor cancels;
- a determinant line with a declared boundary divisor;
- a source complex in which seam zeros are retained as boundary states rather
  than assigned to either bulk sector.

Only after adjoining that seam object can one ask whether the remaining bulk
class has zero sector index.

## C2 interpretation

The seam is not merely the common boundary of two independent index problems.
It carries the extension datum deciding how a boundary kernel is shared. In
categorical terms, the sector index is defined only relative to a seam object
and two incidence maps.

This gives a sharper fifth-tower diagram:

\[
K_{\mathrm{seam}}
\longrightarrow
H_+\oplus H_-
\longrightarrow
H_{\mathrm{completed}}.
\]

The first map prevents a critical-line state from being arbitrarily pushed
into either half-plane. The second records the completed sewing. Off-seam zeros
would then appear as residual bulk index not accounted for by the seam image.

## DPC

The relative-index route requires:

1. a source-derived seam kernel or boundary-state object;
2. incidence maps into both Hardy sectors;
3. a proof that declared critical zeros contribute only through this seam
   object;
4. a relative Fredholm operator after quotienting or adjoining the seam data;
5. invariance under admissible seam regularizations;
6. a sector-resolved residual index;
7. completion control at infinite height.

Reject:

- choosing an indentation direction by convention;
- assigning half of each boundary zero to each sector without a source law;
- deleting the seam divisor before defining its incidence;
- reading the sector index from boundary modulus;
- using a finite-height contour whose horizontal arcs carry an untyped charge;
- inferring the relative class from the desired RH allocation.

## Verdict

The absolute Toeplitz-index proposal is blocked by the allowed seam divisor.
The strengthened route survives only as a relative index theory with the seam
retained as an independent typed carrier. This matches the earlier analytic
result that the seam cannot be reconstructed from the tail.

