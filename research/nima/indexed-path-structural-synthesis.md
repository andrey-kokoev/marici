# Indexed paths as a common object for three presentations

## Clarified intended operation

The operator identifies the base triple as disaggregated path records,
source-indexed path records, and target-indexed path records. Grouping retains
all paths; it does not choose one member per fiber. This selects the existing
dependent-fiber construction rather than section-field-promotion-cycle.md.
The latter is a separate experiment and is not the intended rung rule.

A labelled span is the common object:

\[
A\xleftarrow{s}E\xrightarrow{t}B,\qquad \ell:E\to L.
\]

Its three presentations are E, the family

\[
F(a)=\sum_{e:E}(s(e)=a),
\]

and the family

\[
G(b)=\sum_{e:E}(t(e)=b).
\]

All retain labels and the other endpoint. The existing fibration kernel gives
field-preserving equivalences Sigma_a F(a) equivalent to E equivalent to
Sigma_b G(b). A family is typed A->Type or B->Type; it is not a section of itself.
In HoTT, endpoint indexing can be packaged as the joint family

\[
K(a,b)=\sum_{e:E}((s(e)=a)\times(t(e)=b)),
\]

with label readout inherited from e. Successively summing over a and b recovers
E. Source-first and target-first sum order give the two indexed presentations.

## Cycle law

Group by source, reconstruct, group by target, reconstruct. With field roles
and membership witnesses retained, the resulting table is equivalent to the
starting one. A separate operation history can record the traversal of these
presentations. The cycle alone adds neither new path records nor path length.
This is a presentation cycle, distinct from Gram rank-reducing restriction.

## A compositional successor candidate

A labelled span can compose with a second span B<-D->C. The composite row type
is the homotopy pullback

\[
E\times_B D=\sum_{e:E}\sum_{d:D}(t(e)=s_D(d)).
\]

Its external endpoints are s(e) and t_D(d); its label can retain the pair of
original labels. In the finite set implementation, records retain the entire
ordered path word and composition matches the common endpoint.

For a self-span on X, self-composition defines a successor E_(2m)=E_m times_X E_m.
Each E_m again has disaggregated, source-indexed and target-indexed presentations.
The three presentations at m=1,2,4 therefore give a concrete nine-cell diagram.
The exponent here is path length; identifying it with gauge-group powers would
be a separate physical claim. Self-composition is an additional successor rule,
not a consequence of regrouping by an endpoint.

## Candidate nine-cell diagram

| Rung label | Presentation | Path length in this candidate |
|---:|---|---:|
| 12 | E1 | 1 |
| 11 | source fibers of E1 | 1 |
| 10 | target fibers of E1 | 1 |
| 9 | E2=E1 times_X E1 | 2 |
| 8 | source fibers of E2 | 2 |
| 7 | target fibers of E2 | 2 |
| 6 | E4=E2 times_X E2 | 4 |
| 5 | source fibers of E4 | 4 |
| 4 | target fibers of E4 | 4 |

This is a testable compositional proposal, not a recovered prior theorem about
the user's tower. In particular it does not equate row counts with rung labels.

## Four-state test

For the complete directed four-state graph without self edges, there are
12 length-one, 36 length-two, and 324 length-four paths. Per source the counts
are 3,9,81. Counts of closed paths are 0,12,84 respectively. Source and target
reindexing preserve every path word. Composition is associative in the finite
word model. A reversed two-edge traversal retains both edges and positive
length even though its endpoints agree.

Length-two paths already have 36 histories but only 16 endpoint pairs; dropping
history changes the object. A gain/readout calculation must state whether it
acts on individual histories, amplitudes, probabilities, or weighted resources.

## Verification

    python research/nima/checkers/check_indexed_path_synthesis.py

Finite checks enumerate all paths at lengths1,2,4, reconstruct every endpoint
fiber presentation, verify the cycle, and compare both association orders.
The set checks do not prove new higher homotopy coherence theorems. The generic
fiber reconstruction is supplied by the existing TableFibrationCycle kernel.
