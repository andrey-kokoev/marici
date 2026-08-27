# Cutoffwise anomaly triviality can fail at the derived limit

## Two different descent gates

The finite anomaly-frame calculation has a spatial gate. On every fixed cutoff
cover, each degree-resolved transition cocycle must be a coboundary. Passing
that gate does not produce a completed frame.

The cutoff tower adds a second, longitudinal gate. If \(u_X\) is a finite
potential trivializing the anomaly transitions at cutoff \(X\), then the
potentials must be compatible with the bonding maps:

\[
r_{Y,X}u_Y=u_X,
\qquad
Y\ge X.
\]

They must also remain in the topology of the completed boundary carrier. A
sequence of valid finite potentials that escapes every bounded set does not
define a completed trivialization.

## Minimal escape model

Take one new labelled anomaly increment at every cutoff:

\[
d_X=1.
\]

Every finite prefix is exact. Fixing \(u_0=0\), its unique potentials are

\[
u_X=X.
\]

Thus every finite determinant line is trivialized, and every finite transition
is reproduced exactly, but there is no bounded potential in the completed
supremum-norm carrier.

This is the anomaly-frame version of partner escape at infinity. Nothing
fails at a finite chart cycle. The failure appears only when the finite
null-homotopies are totalized through completion.

## Derived-limit typing

The completed obstruction has the form of a derived inverse-limit class. The
ordinary inverse limit asks for a compatible family of finite frames. The
next derived layer records the failure to choose such a family after every
finite stage has been solved.

Calling the theta obstruction a specific nonzero derived-limit class requires
the actual cutoff bonding system and its topology. The finite escape model
does not establish that theta has such a class. It proves that cutoffwise
coboundary tests alone cannot exclude one.

There are therefore two independent hostile witnesses:

1. a nonzero cycle sum at one cutoff, which defeats local descent;
2. boundedness or compatibility failure of finite potentials, which defeats
   completion descent.

There is also a typed cancellation trap. Degree-one potentials may grow as
\(X\) while degree-two potentials grow as \(-X\). Their scalar sum is zero at
every cutoff, although neither anomaly frame exists in its own completed
carrier. Since the two degrees have different source meanings, scalar
cancellation cannot replace their separate completion laws.

## Source-compatible repair

A successful boundary law must provide more than transition cancellation. It
must construct the potentials naturally across cutoffs and control their
completed graph norm. Equivalently, the endpoint, seam, primitive, square,
and archimedean maps must supply a compatible contracting homotopy for the
anomaly-frame tower.

This identifies the role of the operative coherencer. It is not the scalar
regularized determinant and not a static equality certificate. It is the
cutoff-natural operation transporting finite anomaly contractions into the
completed boundary object.

## DPC verdict

Finite order-three totalization plus finite cocycle triviality does not imply a
global scalar determinant frame. Completion stability of the trivializing
potentials is a separate gate. The smallest falsifier is a tower whose anomaly
increments are exact at every finite prefix while every normalized potential
diverges.

## Verification

`check_rh_anomaly_derived_limit_escape.py` verifies a uniformly bounded
trivialization, the exact-but-unbounded escape tower, gauge invariance of the
escape after fixing one base frame, an incompatible bonding fixture, and the
opposite-divergence cancellation trap.
