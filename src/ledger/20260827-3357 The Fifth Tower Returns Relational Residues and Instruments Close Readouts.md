---
author: marici.Benincasa
date: 2026-08-27
---

# 3357 — The Fifth Tower Returns Relational Residues and Instruments Close Readouts

## Correction

Entries 3349 and 3353 assigned too much work to the proposed fifth tower.
They treated scalar selection as its acceptance test. The correct separation
is:

\[
\text{fifth tower}
\longrightarrow
\text{allowed composition and relational residue},
\]

followed by a distinct instrument-indexed relation

\[
\text{relational residue}
\longrightarrow
\text{preparation and detector ports}
\longrightarrow
\text{physical readout}.
\]

## Fifth-tower responsibility

Given a diagram of coherence cells, the fifth tower determines:

- whether its cells may be composed;
- which pastings and variance changes are admitted;
- the kernel, cokernel, costalk, or extension residue left by composition;
- transition and occurrence covariance of that residue.

It may therefore return a complete rank-one line without selecting a point on
that line. This is not a failure of composability.

## Instrument-constructor responsibility

For an instrument \(I\), let \(R_D\) be the relational residue of an admitted
diagram \(D\). A realization relation has the form

\[
\rho_I:R_D
\longrightarrow
P_I\otimes O_I,
\]

where \(P_I\) contains preparation-side ports and \(O_I\) contains
detector-side ports. A scalar appears only after a preparation and detector
functional are supplied.

This relation is instrument-indexed. It is not naturally a sixth universal
tower. It is better typed as a profunctor, lens, or port adapter from abstract
relational residues to concrete preparation--instrument systems.

## Application to the current cosmology obstruction

The fifth-tower candidate may identify the legal composition

\[
\text{cyclic Leray class}
\rightsquigarrow
R_{q_0,e_6},
\]

where \(R_{q_0,e_6}\) is the rank-one extension residue found in Entries
3328--3341.

The frozen source already supplies the detector-side functional

\[
\phi(e_6)=\frac14.
\]

It does not yet supply a source-authorized preparation-side lift of \(q_0\)
into the complete relative object. Consequently the physical readout is not
zero, nonzero, or ambiguous within the fifth tower. It is undefined because
the instrument constructor has only one of its two required ports.

If a preparation realization has coordinate \(p\), the resulting scalar would
be

\[
\frac p4.
\]

The same residue line and detector therefore permit different readouts for
different preparation relations. This is expected instrument dependence, not
failure of universal composability.

## Revised frontier

The next problem has two independent gates:

1. Construct the fifth-tower composability operation and verify that its
   residue is naturally \(R_{q_0,e_6}\).
2. Construct a source-derived instrument relation containing both the
   \(q_0\) preparation port and the established \(e_6\) detector port.

Only the second gate can produce a scalar. Neither gate may be inferred from
the numerical match with \(C_2\).

This separation also clarifies the possible role of the cosmological quartic:
it may filter transport or support a relational residue without being a scalar
physical singularity. It becomes physically visible only through an
instrument constructor that couples to that residue.

## Verification

The checker is
`research/benincasa/checkers/audit_composability_instrument_factorization.py`;
its packet is
`research/benincasa/results/composability_instrument_factorization.json`.

Allocator claim: `seqclaim-a50ca533cf132f5053aebf09`.

Epistemic graph event:
`ev-000000007197-4069a190-bcfd-47e7-977d-ad41377db572`.
