# Effects Do Not Determine Instruments

## Attack on the evaluation-square candidate

The evaluation square is necessary but insufficient for a continuation-closed
Marici object. An effect assigns a present record value or probability. It does
not determine the Carrier state produced when that record occurs.

A physical observation is therefore not merely an effect \(e\). It is an
instrument branch with two outputs:

\[
\mathcal I_r:x\longmapsto (r,x_r'),
\]

where \(r\) is the stable record and \(x_r'\) is the post-record Carrier state.
In stochastic or quantum settings the branch is subnormalized and its total
weight supplies the effect value.

## Minimal deterministic hostile

Take one preparation \(x\), two post-record states \(a,b\), and two
instruments \(I,J\). Both produce the same current record zero:

\[
I(x)=(0,a),
\qquad
J(x)=(0,b).
\]

Their present effect is identical. Now admit a continuation probe \(p\) with

\[
p(a)=0,
\qquad
p(b)=1.
\]

The two instruments are present-readout equivalent and effect-equivalent, but
not predictively equivalent. The one-step continuation separates them.

No evaluation pairing \(\operatorname{ev}(e,x)\) can recover which update
occurred because both instruments induce the same \(e\) at \(x\). The missing
datum is the record-conditioned update.

## Strengthened operational square

For an intervention \(G\), an instrument \(I\), and a later probe \(p\), a
closed object must type both routes:

1. act by \(G\), execute instrument branch \(I_r\), then continue from the
   resulting state;
2. compose the instrument with \(G\) as a record-labelled state transformer,
   then evaluate the pulled-back future tester.

The required equality concerns joint sequential records, not only the first
effect value. Schematically,

\[
\Pr(r,s\mid I,G,x)
=
\Pr(s\mid p, x_r')\Pr(r\mid I,G,x).
\]

In a deterministic fixture both factors are zero or one. In quantum theory
the instrument branches are completely positive maps; the POVM effect is only
their probability shadow. In control language, the observation channel and
state-update map jointly form the observer dynamics.

## Consequence for the Marici object

Replace the earlier effect-only clause with an instrumented transition clause:

- effects describe current record statistics;
- instruments lift effects to record-labelled Carrier transitions;
- later Task operations act on the post-record Carrier state;
- lineage binds the later record to the particular earlier instrument branch;
- sequential evaluation assigns joint records to the resulting history.

The capability witness must therefore range over transformations that can
produce both Carrier updates and records. A Boolean compatibility relation, an
effect presheaf, or a POVM alone is insufficient.

## Equivalence ladder

This gives a strict implication ladder. Physical-realization identity implies
instrument identity; instrument identity implies effect identity; and effect
identity implies equality of the present record statistics. Reverse
implications require a future-completeness theorem. Predictive equivalence of
instruments means equality of every joint record under every admitted later
continuation, not merely equality of their first-record effects.

## Deutschian pressure

An explanation of observation must say what physical transformation produces
the record and what capabilities remain afterward. A rule that gives only the
record probability leaves the post-record counterfactuals unexplained.

Thus the evaluation square was not the final missing primitive. It was the
probability/readout shadow of the stronger object: a record-labelled update
whose sequential compositions remain instrumented and lineage-correct.

## Verification boundary

The dependency-free checker verifies that the two instruments have identical
present records and effects, but different post-record states, distinct
one-step future records, and distinct joint record words.

This is a finite deterministic criticism. It does not select a unique
categorical packaging or prove quantum instrument completeness.
