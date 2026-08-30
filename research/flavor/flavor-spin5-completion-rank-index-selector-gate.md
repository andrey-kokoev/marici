# Spin(5) Completion Rank-Index Selector Gate

Work package: WP920

## Question

Does any existing source principle select Completion A or B, or do current
invariants merely distinguish two already prepared completions?

## Admitted completion domain

WP879 supplies two minimal anomaly-compatible per-family packets:

\[
A=4_{+1/2}\oplus5_{-1},
\]

\[
B=4_{-3/2}\oplus1_0\oplus1_{+1}\oplus1_{+2}.
\]

After combination with the shared portal matter, both cancel the same local
anomaly vector and both give even global Spin(5) spinor parity. Consequently
the complete currently admitted consistency record places them in one
contextual class.

## Transfer from the rank-index theorem

WP762 proved that a chiral index forgets anomaly-neutral vectorlike content.
Adding a total-rank coordinate can make the packet identifiable, but the
source must generate that total; measuring it after preparation does not
select the preparation.

The exact analogue here is the extended record

\[
(T,S)=
(\text{added representation dimension},
  \text{Spin(5) Dynkin-index sum}).
\]

For the two completions,

\[
(T_A,S_A)=(9,3/2),
\qquad
(T_B,S_B)=(7,1/2).
\]

This pair separates A from B on the admitted two-point domain. Their one-loop
coefficients likewise differ, (b_0^A=9/2) and (b_0^B=13/2).

None of these distinguishing coordinates is a selector. Anomaly consistency
admits both. Choosing smaller dimension, lower Dynkin cost, immediate bare
massability, or a favorable beta coefficient after inspecting the downstream
answer is an added optimization principle, not a consequence of the declared
source.

## Contextual partition

- Anomaly plus global parity: one class ({A,B}).
- Extended rank-index record: singleton classes ({A}) and ({B}).
- Present source preparation: no arrow selecting either singleton.

The refinement therefore supplies identification and typing, with zero
selection reduction. This is the same distinction as a detector that reads a
state faithfully but does not prepare it.

## Smallest exact falsifier

A and B share the cancelled anomaly vector and even global parity, while their
added dimensions are (9) and (7) and their gauge coefficients differ by
(2). Any claim that anomaly consistency uniquely selects one completion is
falsified by this two-point pair.

## Verdict

No existing flavor constructor independently selects Completion A or B. The
current operation is a consistency rigidifier and, after adding the extended
record, a completion identifier. It is neither a completion selector nor a
physical16 selector.

The next admissible source must generate exactly one labelled matter packet:
for example a parent representation with a singleton branching image, an
endpoint-resolved rank-index or K-theory class fixing both net chirality and
total content, or a locality/normalizability theorem. Its branching rule must
be frozen before beta functions are inspected.

No physical instrument is missing at this discrete stage. Instrument design
begins only after the source prepares one completion and its thresholds are
derived.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp920_spin5_completion_rank_index_selector_gate.py
~~~
