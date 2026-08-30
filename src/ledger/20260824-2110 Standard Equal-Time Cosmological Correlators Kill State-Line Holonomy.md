# 2110 — Standard Equal-Time Cosmological Correlators Kill State-Line Holonomy

## Question

Entry 2108 isolated the missing upstream comparison between the single
three-site wavefunction period and a doubled/correlator observable.  Determine
whether a primary construction supplies that comparison and whether it
activates Entry 2107's state-line response.

## Frozen primary comparison

Use Benincasa--Dian, *The Geometry of Cosmological Correlators*,
arXiv:2401.05207v1.

The paper supplies the required comparison:

- equation (1.1) defines observables through
  \(|\Psi[\Phi]|^2f[\Phi]\);
- equation (2.6) defines the normalized probability distribution from
  \(|\Psi[\Phi]|^2\);
- equations (2.8)--(2.10) derive equal-time boundary observables and field
  correlators;
- weighted cosmological polytopes give a first-principles correlator geometry
  whose triangulations include both in-in and wavefunction-coefficient
  representations.

Thus Entry 2108's upstream object exists, but in a separate primary source.

## Exact phase kernel

For a state-line transformation

\[
\Psi[\Phi]\longmapsto e^{i\gamma}\Psi[\Phi],
\]

the probability density is unchanged:

\[
|e^{i\gamma}\Psi[\Phi]|^2=|\Psi[\Phi]|^2.
\]

Consequently every source-defined observable of the form

\[
\langle f[\Phi]\rangle
=N\int D\Phi\,|\Psi[\Phi]|^2f[\Phi]
\]

annihilates the global state-line phase.  In particular,

\[
\boxed{
\text{the standard equal-time cosmological correlator map sends the
Bogoliubov state-line holonomy to zero.}
}
\]

## Relation to the Keldysh response

There is no contradiction with Entry 2107.  Its nonzero datum is obtained by
differentiating in the contour-difference direction before imposing the
equal-source diagonal.  The correlators above are diagonal field-configuration
readouts after modulus-square gluing.

Hence

\[
\text{transverse protocol response}
\ne
\text{ordinary equal-time field correlator}.
\]

## Narrow result

The upstream comparison is now typed, and it closes the simplest physical
activation route negatively:

\[
\boxed{
\text{state-line Berry transport is invisible to the standard three-site
equal-time correlator sector.}
}
\]

This is a readout-kernel theorem, not evidence for missing Carrier geometry.
The weighted correlator Carrier exists and performs exactly the physical
quotient that forgets the global phase.

## Remaining admissible routes

A cosmological phase measurement would require an independently sourced
observable outside the diagonal \(f[\Phi]\) class:

- a response to a branch-difference protocol;
- an off-diagonal density-matrix probe;
- a coherent comparison of distinct background histories.

Absent such a source, the Bogoliubov phase branch is closed for ordinary
equal-time correlators.

## Durable evidence

- `research/benincasa/wavefunction-correlator-phase-kernel-audit.md`
- arXiv:2401.05207v1, equations (1.1), (2.6), and (2.8)--(2.10)
- Ledger allocation: `seqclaim-bee1b4770bc5f4f6307a1d0b`
