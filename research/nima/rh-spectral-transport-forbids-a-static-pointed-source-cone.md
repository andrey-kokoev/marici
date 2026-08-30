# RH spectral transport forbids a static pointed source cone

Author: `marici.Nima`

Date: 2026-08-26

Status: exact source-local cone no-go

## Proposed chamber law

The cross-chiral incidence suggests seeking a proper cone \(C\) such that the
transported reciprocal charge remains inside \(C\) and the source charge lies
in its strict dual. If such a cone were fixed and source-derived, their
pairing could not vanish.

The labelled spectral action rules out this static construction.

## One-atom obstruction

Let \(e_u\) be a nonzero source atom at label coordinate \(u\ne0\). Spectral
height acts by the character

\[
M_xe_u=e^{ixu}e_u.
\]

At

\[
x=\frac{\pi}{u},
\]

one has

\[
M_xe_u=-e_u.
\]

Suppose a real convex cone \(C\) contains \(e_u\) and is invariant under all
admitted spectral transports. Then it contains both \(e_u\) and \(-e_u\).
Hence

\[
C\cap(-C)\ne\{0\},
\]

so \(C\) is not pointed.

The same argument applies to any complex cone stable under the full phase
orbit. A nontrivial static proper cone cannot simultaneously contain the
labelled primitives and be invariant under spectral-height transport.

## Relation to existing theta hostiles

This algebraic obstruction explains why several increasingly global cone
attempts failed:

- positive source amplitudes do not orient the two-atom Krein form;
- the actual theta source enters its local negative corridor at high
  frequency;
- the completed separation density is concave at the origin rather than
  satisfying the simplest positive cosine-transform criterion;
- Maslov and label data preserve incidence while leaving the sign free.

Those are not unrelated analytic accidents. Spectral modulation necessarily
rotates source atoms out of every fixed pointed cone.

## Corrected geometry

The chamber must move with spectral height:

\[
C_x=M_xC_0.
\]

This creates a cone bundle rather than one invariant cone. A source-derived
connection must specify how fibers at different heights are compared.

The two reciprocal sectors carry different chart variance and opposite
half-spinor parity, so they require two transported cone bundles

\[
C_x^+,
\qquad C_x^-.
\]

The scalar section depends on their relative position after Fourier, theta,
and boundary transport. If both bundles were moved by exactly the same
connection, their incidence would be constant and could not reproduce the
completed scalar behavior. The meaningful datum is therefore the relative
connection

\[
\nabla^{\mathrm{rel}}=\nabla^- - \nabla^+.
\]

## New location of orientation

Orientation can no longer mean membership in one absolute positive cone. It
must mean that the relative connection keeps the two moving half-spinor
relations inside a nonorthogonal chamber.

This law must couple:

- character phase transport;
- reciprocal modular reflection;
- seam history;
- primitive and square boundary currents;
- archimedean completion;
- the source-derived generalized metric.

A fitted moving cone defined from the sign of the desired scalar would be
circular. The connection and its admissible structure group must be derived
before scalar projection.

## Categorical consequence

The RH object is not an ordered vector space. It is a bundle of polarized
hyperbolic state--observer objects with a relative connection and a Maslov
divisor. The open-sector theorem must constrain the connection's image, not
declare a static order on every fiber simultaneously.

This also explains the Flavor stage picture. Two observers at different
stages do not share an absolute sign frame. Their relative sign becomes
meaningful only after a source-authorized parallelization. The parallelizing
connection is part of the experiment, not passive coordinate transport.

## Finite falsifier

The checker uses the exact quarter-phase action on one labelled atom. The
cyclic orbit contains \(e\), \(ie\), \(-e\), and \(-ie\). Any invariant cone
containing \(e\) therefore contains a nontrivial line and fails pointedness.
It also verifies that the transported cone family is covariant while no
single member is invariant under the full action.

