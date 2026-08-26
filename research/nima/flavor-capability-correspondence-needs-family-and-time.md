# Flavor Capability Correspondence Needs Family and Time

## Result

Two independent coordinates are missing from a static scalar Flavor portal:

1. a typed bipartite family coordinate that retains reversal-odd orientation;
2. a temporal coherence process that determines reliability under continued
   use.

Neither coordinate reconstructs the other. Their joined correspondence is the
smallest object that separates the exact four-class hostile below.

## Spatial family obstruction

Let \(P\) be the clockwise cyclic permutation on three labels:

\[
P=
\begin{pmatrix}
0&1&0\\
0&0&1\\
1&0&0
\end{pmatrix}.
\]

Counterclockwise transport is \(P^T\). In one operator family, reciprocal
elimination retains the symmetric combination

\[
P+P^T,
\]

which is unchanged when clockwise and counterclockwise are exchanged. The
orientation is erased.

With two inequivalent families \(A,B\), a directed cross-block \(K\) can live
inside the reciprocal full kernel

\[
\begin{pmatrix}
0&K\\
K^T&0
\end{pmatrix}.
\]

The full kernel is symmetric for either \(K=P\) or \(K=P^T\), but the two
kernels are distinct. Reciprocity therefore does not forbid orientation once
the source supplies two typed families. It forbids smuggling the orientation
into a single undifferentiated family.

## Temporal obstruction

Now compare two four-record coherence processes. Both have outage marginal

\[
q=\frac{1}{10}
\]

at every time.

For independent outages, the probability that all four records lose coherence
is

\[
q^4=\frac{1}{10000}.
\]

For the stationary persistent Markov process with

\[
\Pr(O_{t+1}\mid O_t)=\frac{91}{100},
\qquad
\Pr(O_{t+1}\mid C_t)=\frac{1}{100},
\]

the same one-time marginal is stationary, but the four-outage probability is

\[
\frac{1}{10}
\left(\frac{91}{100}\right)^3
=
\frac{753571}{10000000}.
\]

A static visibility value therefore cannot determine continuation reliability.

## Exact obstruction square

Let \(C_+\) and \(C_-\) denote the two cyclic orientations, and let \(T_0\)
and \(T_1\) denote the independent and persistent temporal laws. The finite
source has four classes:

\[
\{C_+,C_-\}
\times
\{T_0,T_1\}.
\]

The static one-family record maps all four classes to one value. Retaining only
the bipartite cross-block leaves two classes distinguished. Retaining only the
temporal failure law also leaves two. Joining the two records separates all
four.

Thus family typing and temporal typing are transverse refinements. The source
has four classes. Projection to either the family coordinate or the process
coordinate leaves two classes. Static projection leaves one.

The diagram is a lattice of distinguishability quotients, not a sequence in
which one repair subsumes the other.

## Capability correspondence

Sontag's terminology is exact here:

- the Task graph contains the abstract typed cyclic and continuation
  transformations;
- the Carrier graph contains the realized cross-family channels, phase-monitor
  transitions, and detector records;
- their closed compatibility locus is the capability correspondence.

The Flavor mediator must land in this correspondence. A static portal number,
a single two-port interference result, or a one-family reciprocal kernel is a
projection of it.

## Finite falsifiers

Any candidate mediator fails if either of these occurs:

- its clockwise and counterclockwise cross-family matrices coincide;
- two admitted coherence processes with the same marginal visibility produce
  different multi-record failure probabilities while the mediator records
  only that marginal.

The exact checker realizes both failures and verifies that the joined record is
faithful on the four-class hostile.

## Status

The architectural target is now sharper than a generic mediator grammar. The
source must derive two inequivalent cyclic families, their ordered reciprocal
cross-block, and a temporal coherence or phase-monitor process in the same
Carrier graph. The remaining question is whether a microscopic Flavor model
constructs that capability correspondence and whether physical16 receives a
calibrated projection of it.
