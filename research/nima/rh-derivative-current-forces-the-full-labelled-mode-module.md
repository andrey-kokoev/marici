# The derivative current forces the full labelled mode module

## Starting point

The naive reverse arrow for the triangular tail operator leaves the exact
commutator

\[
[\partial_q,M_f]=M_{f'}.
\]

Adjoining one port for \(f'\) is useful only if repeated composition closes on
a fixed finite source module.  The closure question can be answered exactly
for every finite exponential source packet.

Let

\[
f_X(q)=\sum_{j=1}^{N_X} c_j e^{-\lambda_j q},
\]

where every \(c_j\) is nonzero and the labelled rates \(\lambda_j\) are
distinct.  Then

\[
\partial_q^k f_X(q)
=\sum_{j=1}^{N_X}c_j(-\lambda_j)^k e^{-\lambda_j q}.
\]

The coefficient matrix of the first \(N_X\) derivative iterates is a
Vandermonde matrix.  Its determinant is

\[
\left(\prod_j c_j\right)
\prod_{i<j}(\lambda_i-\lambda_j),
\]

up to the harmless sign fixed by the ordering convention.  It is nonzero.
Therefore

\[
\dim\operatorname{span}
\{f_X,f_X',\ldots,f_X^{(N_X-1)}\}=N_X.
\]

## Consequence

The commutator closure of differentiation with the aggregate forcing port is
not a one-port repair.  At cutoff \(X\), it recovers the entire labelled
exponential mode space.  If the number of distinct source rates grows with the
cutoff, no cutoff-independent finite-dimensional derivative-current extension
can close the reverse-arrow algebra.

This is not a failure of source closure.  It identifies the correct source
object: the label-resolved mode module, with differentiation acting diagonally
by \(-\lambda_j\).  Aggregating the labels into one scalar forcing function
before constructing the reverse arrow hides precisely the state needed to
absorb the commutator.

## DPC classification

Finite-port Cartan repair is rejected for a source packet with unboundedly many
distinct rates.  The surviving possibilities are:

1. retain the full labelled mode module and construct the reverse incidence
   before scalar synthesis;
2. derive a source relation that genuinely identifies the derivative orbit;
3. use an infinite rigged correspondence and prove its completion continuity.

A fitted finite recurrence is not admissible.  It must follow from the source
grammar and remain uniform under cutoff inclusion.

The finite falsifier is immediate: at any proposed port dimension \(r\), choose
a cutoff containing \(r+1\) distinct rates.  The first \(r+1\) derivative
currents have nonzero Vandermonde determinant, so the claimed closure fails.

## Relation to the RH frontier

This result aligns the reverse-arrow problem with the earlier prime-transport
closure theorem.  Both scalar transport and differential commutator closure
force the same architectural correction: arithmetic labels must remain typed
until after the operator-level coherence is constructed.  Neither theorem
supplies the missing orientation, but both rule out recovering it from a fixed
small scalar block.

## Verification

`check_rh_derivative_mode_closure.py` verifies exact ranks and determinants for
several rational labelled packets and exercises the dimension-overrun
falsifier.

