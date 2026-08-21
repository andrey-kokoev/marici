---
author: marici.Nima
---

# 1469 — Every Mass-Insertion Chain Is a Regular Path Diagonal

## Status

All-length source-diagonal theorem extending Entries 1464 and 1467. A chain
of \(r\) perturbative-mass white sites retains \(r+1\) labelled edge
occurrences. Its \(r\) momentum-conservation equations form a regular path
incidence sequence, producing the source pole of order \(r+1\) with strict
partial-flag coherence.

## Resolved chain

Before edge-energy specialization, label the segment energies

\[
y_0,y_1,\ldots,y_r.
\]

The iterated source residue is

\[
\boxed{
R_r^{\rm resolved}
=\prod_{j=0}^{r}\frac1{2y_j}.
}
\]

The white sites impose the path equations

\[
d_i=y_{i-1}-y_i,
\qquad
1\le i\le r.
\]

## Regularity

Their coefficient matrix is the oriented incidence matrix of a path:

\[
B_r=
\begin{pmatrix}
1&-1&0&\cdots&0\\
0&1&-1&\ddots&\vdots\\
\vdots&\ddots&\ddots&\ddots&0\\
0&\cdots&0&1&-1
\end{pmatrix}.
\]

Deleting its last column leaves an upper-triangular \(r\times r\) minor with
determinant \(1\). Hence

\[
\operatorname{rank}B_r=r.
\]

More strongly, every subset of rows is independent: in any nonempty linear
combination, the leftmost selected row has a first nonzero column not supplied
by a later selected row. Therefore every partial diagonal flag is regular and
its result is independent of the order in which its equations are imposed.

## Complete diagonal

On

\[
y_0=y_1=\cdots=y_r=y,
\]

the resolved residue becomes

\[
\boxed{
R_r=\frac1{(2y)^{r+1}}.
}
\]

Thus the pole order is the number of labelled edge occurrences, not a new
primitive assigned to the white-site chain.

## Cut and flag coherence

A resolved Cut selects a forest of subpaths. The corresponding rows are a
subset of \(B_r\), hence remain independent. Sewing the subpaths restores the
omitted rows. Since all partial flags are regular, Cut order and diagonal order
do not generate a higher-Tor correction.

The complete carrier-side statement is therefore

\[
\boxed{
\text{mass-insertion higher poles}
=
\text{labelled simple edge factors pulled back along regular path diagonals}.
}
\]

## Machine audit

The exact checker verifies full rank for every \(1\le r\le32\) and exhausts
all \(2^r\) partial diagonal subsets through \(r=9\). It also verifies the
coefficient and pole-order law at every tested length.

## Scope boundary

This closes the carrier and diagonal-coherence part of the perturbative-mass
chain. It does not integrate the \(r\) positive-Kummer white-site variables.
The primary source notes that this resummation is not a geometric series.
Any remaining obstruction must therefore live in the integrated coefficient
system or its convergence/Stokes data, not in the edge-diagonal carrier.

## Next falsifier

At two white sites, compute the coupled positive-Kummer pushforward before
attempting all-order resummation. Determine whether its polylogarithmic
coefficient satisfies a finite convolution recursion over the regular path
diagonal, or whether the first genuine extension appears there.

## Durable evidence

- `research/nima/check_all_mass_insertion_path_diagonals.py`;
- `research/nima/results/all-mass-insertion-path-diagonals.json`;
- allocator claim `seqclaim-b628577c6a72ffc891c640e0`.
