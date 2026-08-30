# Gauge, conservation, and antipodal matching are three different reductions

## 1. Gauge is a target quotient

Let `A_P` be the reconstructed one-form space and

\[
 \mathcal G=d\mathcal D'(S^2)
\]

the real exact-shift subspace. The physical curl/period target begins with

\[
 0\longrightarrow\mathcal G\longrightarrow\mathcal A_P
 \longrightarrow\mathcal A_P/\mathcal G\longrightarrow0.
\]

This is a quotient of presentations of the same observable. Its kernel is
the exact subspace. On meromorphic genus-zero data it removes every
zero-residue higher-pole derivative, while leaving the residue cohomology.

## 2. Conservation is a source restriction

Let `S_P` be the labelled hard-source packet and let

\[
 \mathcal C_P:S_P\longrightarrow\mathfrak q^*
\]

collect the independently derived global charges. Admissible radiative data
lie in

\[
 S_P^{\rm cons}=\ker\mathcal C_P.
\]

For the scalar energy packet, the four-momentum columns may be written

\[
 q^\mu(\xi,\bar\xi)=
 (1+\xi\bar\xi,\ \xi+\bar\xi,\
 -i(\xi-\bar\xi),\ 1-\xi\bar\xi),
\]

with the incoming/outgoing signs included in the source coefficients. The
condition is `sum_i e_i q_i^mu=0`. Global conformal or angular-momentum
constraints are additional rows of `C_P`; they must be derived from the hard
charge action rather than fitted from a desired kernel.

Restriction cannot create a new kernel in a previously injective local map:

\[
 R\text{ injective on }S_P
 \quad\Longrightarrow\quad
 R|_{\ker\mathcal C_P}\text{ injective}.
\]

It reduces the set of constructible packets instead.

## 3. Antipodal matching is a graph condition

Let `A` be the already-proved invertible antipodal transport, including its
spin-two chart factor, Lah jet matrix, label permutation, and helicity rule.
Matching past and future records means

\[
 \mathcal H_{\rm match}
 =\{(h^+,h^-):h^+=Ah^-\}
 =\operatorname{Graph}(A).
\]

Projection from this graph to either boundary copy is an isomorphism. Thus
antipodal matching does not itself discard a physical degree of freedom; it
identifies two descriptions by an invertible transport law. The mismatch map

\[
 d_A(h^+,h^-)=h^+-Ah^-
\]

has the exact sequence

\[
 0\longrightarrow\operatorname{Graph}(A)
 \longrightarrow\mathcal H^+\oplus\mathcal H^-
 \xrightarrow{d_A}\mathcal H^+\longrightarrow0.
\]

Treating matching as the projection `(h+,h-) -> h+ + h-` would manufacture a
spurious interference kernel and forget the authority-bearing transport `A`.

## 4. Order of operations

The typed physical reduction is

\[
 \ker\mathcal C_P
 \xrightarrow{R}\mathcal A_P
 \longrightarrow\mathcal A_P/\mathcal G
 \xrightarrow{\rm periods}H^1(S^2-P),
\]

with the source packet first restricted to the antipodal graph when two null
boundaries are present. Gauge quotient, conservation restriction, and matching
graph generally do not commute as untyped matrix deletions; they do commute
as the displayed source-derived maps when their domains and codomains are
retained.

## First-nonfaithful arrows

- Gauge: the quotient arrow, with typed witness `dX`.
- Conservation: no alias; inadmissible packets are excluded at construction.
- Antipodal matching: no alias on the graph; forgetting the matching adapter
  is a presentation error.
- Periods: exact forms and higher local derivatives, as classified previously.

## Evidence

`checkers/completed_gauge_conservation_antipodal_quotient_checks.py` verifies
generic four-momentum rank, persistence of injectivity under conservation
restriction, the gauge exact sequence, antipodal graph exactness for hostile
dimensions, and failure of an untyped sum projection.
