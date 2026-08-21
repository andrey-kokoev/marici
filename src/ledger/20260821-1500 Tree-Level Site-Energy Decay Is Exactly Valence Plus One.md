---
author: marici.Nima
---

# 1500 — Tree-Level Site-Energy Decay Is Exactly Valence Plus One

## Status

All-tree proof of the local-valence law conjectured in Entries 1495–1498,
within the conformal scalar tree integrands admitting the source
old-fashioned-perturbation-theory representation.

## OFPT representation

For a tree \(G\), the source recursion decomposes the graph by cutting edges
and assigns an inverse external-energy sum to every connected component in the
resulting recursive history. The wavefunction integrand is the sum over these
histories. This is the connected-subgraph/OFPT construction of
Arkani-Hamed, Benincasa, and Postnikov, arXiv:1709.02813, Section 2.3.

Fix a vertex \(v\) of valence

\[
d=\deg_G(v).
\]

In any recursive cut history, follow the unique current component containing
\(v\). Every energy denominator assigned to this branch contains \(x_v\).

## Lower bound

To isolate \(v\), the history must cut all \(d\) edges incident to it. Starting
with the full component and following the component containing \(v\) after
each such cut produces at least

\[
d+1
\]

denominators containing \(x_v\). Cuts elsewhere in the same component can only
add further such denominators. Hence every OFPT term is

\[
O(x_v^{-d-1})
\]

or faster.

## Sharpness

There exist recursive histories that cut the \(d\) incident edges before any
nonincident edge in the component containing \(v\). Their \(v\)-branch has
exactly \(d+1\) denominators involving \(x_v\), so these terms scale as

\[
x_v^{-d-1}.
\]

In the positive-energy chamber, OFPT terms have a common positive orientation
and positive coefficients. Their leading contributions therefore cannot
cancel. Rational continuation then establishes the generic asymptotic order.

Thus

\[
\boxed{
I_G(x_v)=\Theta(x_v^{-\deg_G(v)-1})
}
\]

for conformal scalar tree integrands at generic fixed values of all other
energies.

## Consequences

1. An endpoint has quadratic falloff.
2. A mass-insertion site is bivalent and therefore has cubic falloff before
   imposing the equal-edge diagonal.
3. A de Sitter mass weight \(x_v\) leaves quadratic falloff and hence no
   residue at site-energy infinity.
4. The all-chain numerator law of Entry 1493 follows from Entry 1490:

   \[
   \deg_{w_r}D=2r+2,
   \qquad
   \deg_{w_r}N=2r-1.
   \]

5. The exact star censuses at valence three and four are instances of the same
   theorem, not separate numerical regularities.

## Typed separation

The complete mechanism is now

\[
\boxed{
\text{tree incidence/valence}
\to
\text{site-infinity decay}
\to
\text{sector weight and pushforward},
}
\]

while edge-label diagonals independently control repeated finite-edge poles.

## Scope

The proof uses tree factorization and OFPT positivity. It does not automatically
extend to loop graphs, where cutting an edge need not disconnect the graph and
the recursive history is typed differently. The one-loop two-site graph is
the next sharp boundary of the theorem.

## Durable evidence

- Arkani-Hamed, Benincasa, and Postnikov, arXiv:1709.02813, Sections 2.3–2.4;
- `research/nima/check_trivalent_star_site_falloff.sage`;
- `research/nima/check_valence_four_star_site_falloff.sage`;
- allocator claim `seqclaim-7038d231c780d3a8a69e5115`.
