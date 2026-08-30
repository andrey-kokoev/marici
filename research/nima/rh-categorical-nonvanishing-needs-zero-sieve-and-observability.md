# Categorical Nonvanishing Needs a Zero Sieve and Observability

## Pointed functor

The source transport functor is not yet the RH-bearing object. It must be
pointed by a distinguished source state \(\Omega_s\) and equipped with a scalar
readout \(r_s\). The completed function is the present observation

\[
\Xi(s)=r_s(\Omega_s)
\]

up to an independently controlled nonzero normalization.

Every admitted source word \(w\) generates a future probe

\[
r_s\circ F_s(w).
\]

The collection of all such probes is the behavioral or Yoneda-style image of
the state. It contains strictly more information than the present scalar
readout.

## Two independent gates

An off-seam nonvanishing theorem follows from two properties.

First, zero propagation: if the present readout vanishes, then every
source-authorized future probe vanishes:

\[
r_s(x)=0
\quad\Longrightarrow\quad
r_s(F_s(w)x)=0
\]

for every admitted word \(w\).

Second, joint faithfulness: if every future probe vanishes, then the state is
zero:

If \(r_s(F_s(w)x)=0\) for every \(w\), then \(x=0\).

Combined with an independently nonzero distinguished state, these properties
force \(r_s(\Omega_s)\neq0\).

## Why both are necessary

Observability alone is insufficient. Let the update swap two coordinates, let
the readout select the first coordinate, and let the state be the second basis
vector. The present output is zero, the next output is nonzero, and the two
future probes are jointly faithful. A present zero did not propagate.

Zero propagation alone is also insufficient. Let the update be the identity
with the same readout and hidden state. Every future output is zero, but the
state remains nonzero. The probes are not jointly faithful.

These are the smallest finite falsifiers for either one-gate proposal.

## Categorical statement

For a fixed \(s\), let \(Z_s\) be the subobject defined by the present kernel of
the readout. Zero propagation says that the distinguished zero belongs to a
source-stable zero sieve: every admissible continuation remains inside the
corresponding readout kernel. Joint faithfulness says that the intersection of
all kernels in that sieve is the zero subobject.

Equivalently, the behavioral map

\[
\mathcal O_s:x\longmapsto
\bigl(r_s(F_s(w)x)\bigr)_w
\]

must be monic, and a present zero must map to the zero behavioral record.

This is the categorical form of the control-theory observability mechanism that
kept reappearing in the programme.

## RH-strength DPC

Candidate law: the source-derived four-port functor forces its distinguished
scalar readout to be nonzero in each open half-plane.

Required derivation:

1. construct the pointed state without dividing by the completed scalar;
2. prove that a scalar zero propagates through every generating source arrow;
3. prove joint faithfulness of the resulting future-probe family in the source
   completion;
4. prove that the distinguished state remains nonzero after completion;
5. show that reciprocal sewing is the only locus where zero propagation or
   joint faithfulness may fail.

Failure at any finite generator supplies a falsifier. Failure only in the
completion limit is the previously identified escape-at-infinity obstruction.

## Hostile multiplier test

A hostile scalar multiplier can preserve the abstract transport category while
inserting a new present zero. The repaired category rejects it only if that zero
fails to propagate through the source-generated probe family or if the altered
distinguished state is not admitted by the source pointing.

Therefore the true additional structure is neither another observer nor another
coherence cell. It is the pointed behavioral orbit and a theorem relating one
scalar zero to its entire zero sieve.
