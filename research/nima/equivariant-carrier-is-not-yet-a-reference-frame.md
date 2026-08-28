# An equivariant carrier is not yet a reference frame

## Question

Does constructing a faithful primitive \(U(1)\) representation already fix the
phase ambiguity?

## Claim boundary

No. It constructs a carrier capable of recording phase. A reference frame
requires an additional source-prepared basepoint or a second correlated system
whose relative phase is observable. This packet proves the distinction in a
finite torsor model and states its categorical form.

## Carrier versus pointed carrier

Let \(W\) carry the primitive weight-one action of \(U(1)\). The representation
specifies how a putative record transforms, but it selects no nonzero vector
\(w_0\in W\). Without \(w_0\), simultaneous phase rotation remains an
automorphism of the complete apparatus description.

A framed reference is therefore a pointed representation

\[
(W,w_0),
\qquad w_0\neq0,
\]

together with source operations that prepare, preserve, and interrogate that
pointing. Forgetting \(w_0\) returns the unframed carrier and restores the
global phase symmetry.

## Relational alternative

Suppose target and reference are two \(U(1)\)-torsors with coordinates \(x\)
and \(y\). Under common rotation,

\[
(x,y)\longmapsto(gx,gy).
\]

Neither absolute coordinate descends, but the relative coordinate

\[
xy^{-1}
\]

is invariant. A second observer therefore does not reveal an absolute phase;
it constructs a relational phase.

If the source prepares \(y=1\) in an independently authorized frame, the same
relative coordinate numerically equals \(x\). That equality depends on the
preparation constructor and must not be attributed to the representation
alone.

## Categorical formulation

An unframed phase carrier is a \(G\)-object. A physical reference is a section
or pointing whose stabilizer is trivial on the intended orbit. The forgetful
functor from pointed \(G\)-objects to \(G\)-objects discards exactly the datum
needed to turn covariance into a coordinate.

Alternatively, two unpointed torsors admit a diagonal quotient. Its invariant
coordinate is relative, not absolute. This is the lawful route when no external
phase standard exists.

The two architectures must remain distinct:

1. external framing: one target plus a source-prepared pointed reference;
2. internal comparison: two co-transforming systems plus a relational readout.

## Cross-sector consequences

- A local oscillator is not merely a two-quadrature mode. Its prepared phase
  and phase-locking protocol are the pointing.
- Flavor interference can determine relative complex phases while leaving a
  common rephasing gauge intact.
- A reciprocal theta boundary pair may support a relative phase comparison
  without supplying an absolute determinant-line phase.
- An endpoint augmentation fixes a frame only if its preparation and transport
  are source-derived; naming the positive unit is insufficient.

## Finite falsifier

In the cyclic torsor \(C_4\), simultaneous shifts

\[
(x,y)\longmapsto(x+g,y+g)
\]

change both absolute coordinates while preserving \(x-y\). Any purported
absolute reconstruction from the unpointed pair is therefore false. Preparing
\(y=0\) makes the relative coordinate equal to \(x\), but deleting that
preparation restores the ambiguity immediately.

## DPC

For every proposed reference:

1. identify its equivariant carrier;
2. identify the pointing or relational partner separately;
3. derive the preparation and transport of that datum from the source;
4. distinguish absolute-coordinate claims from diagonal-quotient claims;
5. delete the pointing constructor and verify that the claimed absolute
   coordinate becomes ambiguous;
6. retain only the relative observable if no external frame survives.

## Disposition

Primitive transport is necessary but insufficient. A reference is a
source-pointed equivariant carrier, or else a relational comparison of two
co-transforming carriers. The latter yields relative phase only.

## Verification

The checker check_equivariant_carrier_pointing.py exhausts the \(C_4\) torsor,
proves invariance and completeness of the relative coordinate under diagonal
rotation, demonstrates absolute ambiguity, and verifies recovery after an
authorized basepoint preparation.
