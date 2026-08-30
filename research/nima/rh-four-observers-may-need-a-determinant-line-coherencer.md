# Four RH Observers May Need a Determinant-Line Coherencer

## Observer count is not the whole object

Suppose the seam genuinely supplies value and flux data \((M,J)\). A cutoff or
label-extension map then transports this pair by some matrix \(S_{X,Y}\). The
boundary form transforms as

\[
\omega(S_{X,Y}u,S_{X,Y}v)
=\det(S_{X,Y})\omega(u,v).
\]

In two dimensions this identity is exact. Therefore the four-port state
\((P,Q,M,J)\) is closed under cutoff transport only if the source maps preserve
the boundary form:

\[
\det(S_{X,Y})=1.
\]

Reciprocal reflection is different: it reverses interface orientation and has
determinant \(-1\). That sign is typed by reflection rather than treated as a
cutoff anomaly.

## The additional datum

If \(\det(S_{X,Y})\neq1\), the missing object is not automatically a fifth
observer of system state. It is a one-dimensional coherence record attached to
the transport arrow. Under composition,

\[
\det(S_{X,Z})
=\det(S_{Y,Z})\det(S_{X,Y}).
\]

Thus it lives naturally in a determinant line or multiplicative route effect.
It records the failure of cutoff transport to preserve boundary area.

This yields a sharper Ubersector type:

```text
BoundaryUbersector
  left_tail_instrument
  right_tail_instrument
  seam_value_instrument
  seam_flux_instrument
  cutoff_transport
  determinant_line_coherence
  reciprocal_orientation
```

The distinction matters. Adding more observers cannot repair a defective
transport law. Conversely, a nontrivial determinant-line coherencer should not
be miscounted as another state channel.

## DPC

Candidate principle: four source-derived observers form a complete transported
boundary object.

Required consequence: every admitted cutoff extension preserves the alternating
boundary form, after accounting for the declared reciprocal orientation.

Finite falsifier: compute the two-by-two transport matrix between successive
finite seam spaces. If its determinant differs from one, exhibit two boundary
states whose pairing changes by that factor.

Possible verdicts:

- determinant one: the boundary pair transports strictly;
- a source-derived multiplicative factor: retain its determinant-line record;
- presentation-dependent factor: the proposed transport is not coherent;
- unbounded or vanishing factor at completion: boundary information escapes at
  infinity.

## Relation to the existing arithmetic currents

The primitive, prime-square, and archimedean currents may be precisely the
components of this arrow-level anomaly. That possibility is stronger than
treating them as extra positive state ports. Their role would be to make the
full cutoff transport symplectic after the determinant-line contribution is
included.

The immediate theta calculation is therefore paired:

1. test whether \((M,J)\) is a nondegenerate source boundary pair;
2. compute how its alternating form changes when one labelled arithmetic block
   is added.

Only after both tests can we say whether RH has three observers, four observers,
or four observers plus an essential coherence line.
