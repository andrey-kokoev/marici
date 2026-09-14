# Cubical probe nullity is a Boolean Walsh--Vandermonde sum

## Question

Why does the isolated five-cube have probe nullities \(49,23,7,1,0\), and does the observed formula hold in every cubical dimension?

## Claim boundary

Over a field of characteristic other than two, the directed one-skeleton of the Boolean \(n\)-cube admits a block decomposition in which the \(m\)-setting probe kernel has dimension

\[
N(n,m)=\sum_{k=m+1}^{n}(k-m)\binom nk,
\]

provided every relevant generalized Vandermonde block has maximal rank. Distinct positive rational settings satisfy this condition in characteristic zero. Modular applications additionally require nonvanishing after reduction. This theorem concerns the isolated cube; transfer to the full arithmetic graph requires the cube inclusion and global kernel comparison already tested computationally through dimension five.

## Boolean tensor decomposition

Let

\[
V_n=(k^2)^{\otimes n}
\]

be the vertex space of the Boolean cube. In each factor use the constant and difference vectors

\[
c=e_0+e_1,
\qquad
d=e_1-e_0.
\]

They form a basis when the characteristic differs from two. Tensor words are indexed by subsets \(K\subseteq[n]\): put \(d\) in positions belonging to \(K\) and \(c\) elsewhere. Denote the resulting one-dimensional vertex summand by \(V_K\).

The edge space decomposes by directions:

\[
E_n=\bigoplus_{i=1}^{n}E_i,
\qquad
\dim E_i=2^{n-1}.
\]

After expanding every nondirectional tensor factor in the \(c,d\) basis, the edge summands that incidence sends to \(V_K\) are indexed exactly by \(i\in K\). Hence each nonempty subset \(K\) supplies an independent block

\[
k^K\longrightarrow V_K.
\]

This is the Boolean Fourier--Walsh decomposition of directed incidence.

## Character probes on each block

At setting \(t_r\), direction \(i\) receives weight \(t_r^i\). On the block indexed by \(K\), the joint \(m\)-setting probe is therefore

\[
M_{T,K}:k^K\longrightarrow k^m,
\qquad
(a_i)_{i\in K}\longmapsto
\left(\sum_{i\in K}a_it_r^i\right)_{r=1}^{m}.
\]

Its matrix is the generalized Vandermonde matrix

\[
(t_r^i)_{r,\,i\in K}.
\]

Under the maximal-rank hypothesis,

\[
\operatorname{rank}M_{T,K}=\min(m,|K|),
\]

so its nullity is

\[
\max(|K|-m,0).
\]

Summing over all subsets gives

\[
\dim\ker P_{n,m}
=
\sum_{K\subseteq[n]}\max(|K|-m,0)
=
\sum_{k=m+1}^{n}(k-m)\binom nk.
\]

## Consequences

The final nonzero term occurs at \(m=n-1\):

\[
N(n,n-1)=1.
\]

It comes solely from \(K=[n]\). Thus the unique last blind direction is the full-support Walsh block, explaining why the five-cube kernel vector uses every edge and its vertex residue uses every vertex.

At \(m=n\), every block is monic and

\[
N(n,n)=0.
\]

The setting-depth law follows without extrapolation:

> An isolated Boolean \(n\)-cube requires exactly \(n\) independent total character evaluations, equivalently the coarse evaluation plus \(n-1\) modulated settings.

For \(n=5\), the formula gives

\[
N(5,m)=49,23,7,1,0
\]

for \(m=1,2,3,4,5\), exactly matching the computed local ranks.

## Relation to known constructions

The decomposition is the Walsh decomposition of functions on \((\mathbb Z/2)^n\), applied simultaneously to each edge direction. The maps on the resulting subset blocks are generalized Vandermonde evaluation maps. It is also Koszul-shaped: a subset \(K\) records the directions participating in one alternating tensor mode, while the remaining kernel dimension \(|K|-m\) counts unresolved directional coefficients.

This identifies the relevant known equality more precisely than the augmentation analogy. The nullity formula is a direct sum of interpolation defects indexed by the Boolean subset lattice.

## Strongest falsification attempt

Compute the full rational stacked-incidence ranks directly for Boolean cubes in dimensions two through five and compare every prefix with the closed formula. Independently check every generalized Vandermonde block for every nonempty subset \(K\) in dimensions through eight. Duplicate a setting to ensure the maximal-rank hypothesis fails detectably rather than being absorbed into the theorem.

## Disposition

The proof reduces the probe law to two explicit isomorphisms: Walsh decomposition of the cube and generalized Vandermonde monicity. Arithmetic cube completion remains responsible for when the full-support block becomes available in the filtered graph.
