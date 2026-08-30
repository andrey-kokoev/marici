# Spin(5) Completion Massability Does Not Select Threshold Scales

## Question

Does the currently declared matter content provide a completion-specific mass
action that removes WP884's free threshold-mass coordinate?

## Exact bare-mass criterion

In left-handed notation, a gauge-invariant bare bilinear requires two fields
whose Spin(5) representations admit a singlet and whose hypercharges sum to
zero. The relevant representation facts are

\[
4\otimes4\supset1,
\qquad 5\otimes5\supset1.
\]

The shared portal packet is

\[
4_{-1/2}\oplus5_{+1}.
\]

Completion A adds

\[
4_{+1/2}\oplus5_{-1}.
\]

It therefore admits two independent invariant bilinears,

\[
M_4,4_{-1/2}4_{+1/2}
+M_5,5_{+1}5_{-1}.
\]

Gauge invariance permits every pair ((M_4,M_5)). It supplies no equation
relating either mass to the breaking radii (a,b), the portal coefficient,
or the subtraction scale. Completion A is massable but has a
two-dimensional bare-mass fiber per family before flavor matrices are added.

Completion B adds

\[
4_{-3/2}\oplus1_0\oplus1_{+1}\oplus1_{+2}.
\]

No nonzero-charge Spin(5) multiplet in the combined packet has an
opposite-charge partner in the same representation. Its gauge-invariant bare
mass matrix therefore has rank zero for the charged portal multiplets. The
neutral singlet may have a Majorana mass, but that does not mass the charged
Spin(5) fields.

## What scalar breaking could change

Completion B may acquire masses from Yukawa couplings to the declared or new
scalars. That is a different constructor. It requires an explicit invariant
census, vacuum insertion, and full mass-matrix rank calculation. Anomaly
cancellation alone neither guarantees those invariants nor fixes their
Yukawa coefficients.

The present packet deliberately does not infer a Yukawa grammar from desired
massability. It proves only the exact bare-bilinear boundary.

## Consequence for finite thresholds

- Completion A makes the threshold calculation definable, but with freely
  chosen (M_4,M_5); it cannot select WP884's (eta).
- Completion B does not yet define the charged threshold spectrum; a scalar
  and Yukawa mass action must be supplied first.

Thus “prefer the immediately massable completion” is an optional minimality
principle, not a theorem of the declared source. Even if adopted, it selects a
presentation of the spectrum without selecting its numerical threshold.

## Smallest exact falsifiers

1. Completion A with ((M_4,M_5)=(1,1)) and ((2,1)) obeys the same gauge
   and anomaly constraints but gives different thresholds.
2. Completion B's charged list has no representation-matched pair with
   hypercharge sum zero.
3. The neutral (1_0) Majorana mass does not increase the charged-sector
   mass rank.

## Verdict

The mass-action branch splits rather than closes. Completion A has an
executable algebraic mass action with unconstrained scales; Completion B
requires new Yukawa construction. Neither is a source-generated numerical
selector. The next admissible calculation is a complete invariant Yukawa
census using only the already declared scalar packet, followed by a generic
mass-matrix rank test.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp885_spin5_completion_bare_massability_audit.py
~~~
