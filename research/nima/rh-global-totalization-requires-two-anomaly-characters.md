# Factorized global totalization would require two anomaly characters

## Source-typing correction

The argument below classifies a factorized scalar totalization. Later source
inspection shows that the primitive and square currents do not possess
separate completed scalar readouts at the critical boundary. The primitive
current requires an exponential/Laplace rigging, and the undamped spectral
readout is not an admissible test for either completed current separately.

Therefore the product of two scalar characters below is a conditional
factorization test, not the native theta constructor. The source-compatible
object is a joint relative character defined only after primitive, square,
archimedean, and zero-frequency boundary data are sewn together.

## Constructor signature

The three analytic strata do not enter one undifferentiated completion. Their
natural completed carriers have different modalities:

- a primitive-current boundary carrier;
- a square-current Hilbert or tempered carrier;
- a Schatten-three tail carrier.

If the scalar determinant constructor factorized through the two anomaly
carriers, it would have the schematic form

\[
\operatorname{Tot}(P,Q,T)=
\chi_1(P)\chi_2(Q)\det_3(I-T)^{-1}.
\]

Here \(\chi_1\) and \(\chi_2\) could not be arbitrary regularization choices.
They would have to be source-derived characters on their respective boundary
carriers.

## Monoidal laws

For independent labelled blocks, direct sum is the source composition law.
The anomaly characters must therefore satisfy

\[
\chi_r(A\oplus B)=\chi_r(A)\chi_r(B),
\qquad
r\in\{1,2\}.
\]

In logarithmic coordinates, their boundary functionals must be additive. The
totalization must also be natural under cutoff refinement: refining a labelled
packet and then totalizing must agree with first transporting its three typed
components and then applying the completed constructor.

These conditions identify the missing coherencer. It is a pair of monoidal
natural boundary characters, together with their compatibility cell against
the order-three determinant and reciprocal dagger sewing.

## Why a single scalar counterterm is insufficient

A scalar prescription can match every tested packet while violating source
composition. For example, adding a mixed term proportional to \(PQ\) changes
the logarithmic totalization by

\[
\alpha PQ.
\]

It vanishes on packets carrying only one anomaly type, so separate primitive
and square tests do not see it. On a direct sum it produces cross-block terms
and fails additivity. It therefore has no character interpretation.

A second hostile prescription attaches a cutoff-dependent multiple to an
otherwise valid anomaly functional. It may be additive at each fixed cutoff
while failing refinement naturality. Cutoffwise multiplicativity is not enough.

## Reciprocal compatibility

Reciprocal dagger sewing acts on the two boundary carriers before scalar
projection. The characters must intertwine that action with the declared
determinant-line involution. Equality of final scalar values is weaker: two
nonintertwining characters can cancel after multiplication.

Thus the source calculation must derive four pieces together:

1. the primitive boundary carrier and its character;
2. the square boundary carrier and its character;
3. cutoff-refinement naturality;
4. reciprocal compatibility with the Schatten-three determinant.

## Finite falsifier

Given two independently supported packets \(A\) and \(B\), compare

\[
\log\operatorname{Tot}(A\oplus B)
\]

with

\[
\log\operatorname{Tot}(A)+
\log\operatorname{Tot}(B).
\]

Any nonzero residual rejects the proposed anomaly characters. A second test
compares the same packet before and after an authorized cutoff refinement.
These two squares are the smallest finite gates for the global constructor.

## DPC verdict

The order-three determinant supplies only the tail leg of global
totalization. Separate typed characters would be necessary for a factorized
scalar constructor, but the native source riggings obstruct their individual
critical-boundary readouts. The surviving target is a joint relative
character. The tests here remain valid against any proposal claiming the
stronger factorization.

## Verification

`check_rh_anomaly_character_totalization.py` verifies direct-sum and refinement
naturality for a typed character fixture, then rejects a mixed anomaly term
and a cutoff-dependent additive prescription.
