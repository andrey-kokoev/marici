# 1846 — The Polar Double-Morse Coefficient Is a Legendre Variation

## Frozen branch data

Entry 1845 gives the ordered branch points

\[
0,\quad 1,\quad
a=-\frac{h_2}{h_1-h_2},\quad
b=-\frac{\delta_2}{\delta_1-\delta_2}.
\]

Use the uniquely normalized Möbius coordinate

\[
T(x)=\frac{x(1-b)}{x-b},
\]

which sends \((0,1,b)\) to \((0,1,\infty)\).  The fourth branch point is

\[
\boxed{
m=T(a)=\frac{h_2\delta_1}{h_2\delta_1-h_1\delta_2}.
}
\]

Thus the polar double-Morse coefficient is the pullback of the universal
Legendre Gauss--Manin variation by this Hessian-weighted normal modulus,
up to the Kummer factor already typed by the physical current in Entry 1843.

## Labelled cusps

The three nodal degenerations are

\[
\begin{array}{c|c}
\delta_1=0&m=0\\
\delta_2=0&m=1\\
h_2\delta_1-h_1\delta_2=0&m=\infty.
\end{array}
\]

The first two are the existing labelled wall normals.  The third is Entry
1845's internal coefficient collision.  Standard Legendre nearby cycles at
all three cusps are Tate/Kummer; no additional carrier incidence is needed.

Exchanging the two labelled walls gives

\[
(1\leftrightarrow2):\qquad m\longmapsto1-m,
\]

so occurrence covariance is retained rather than erased by an unlabelled
cross-ratio.

## Narrow result

The five-site polar sector repeats, at a new local geometry, the architecture
previously found in the homogeneous three-site loop:

\[
\boxed{
\text{labelled wall normals}
\longrightarrow
\text{source-weighted modular coordinate}
\longrightarrow
\text{Legendre coefficient variation}.
}
\]

This supports H2: the carrier supplies the labelled walls and their incidence,
while the elliptic period system is a sector-specific coefficient object.

## Scope

This is a local coefficient theorem near the polar double-Morse point.  It
does not construct the global physical relative-chain pairing, and it does
not prove that the complete five-site observable is exhausted by this block.

## Next falsifier

Compute the coarse modular parameter near each labelled cusp.  Test whether
each linear resolved normal is a square-root coordinate over the coarse
modular degeneration, as at the three-site total-energy boundary.

## Evidence

- `research/benincasa/checkers/five_site_region_pair_polar_legendre_modulus.py`
- `research/benincasa/results/five-site-region-pair-polar-legendre-modulus.json`
- Entries 1843--1845
- allocator claim: `seqclaim-0aca92678db7f957d2438692`
