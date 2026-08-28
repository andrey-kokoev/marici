# Euler cyclic attachment requires primitive feedback loops

## The cut colligation is acyclic

The lossless tail–seam colligation transports source state forward through
successive interval shells. At every finite cutoff its transport graph is
acyclic. After a topological ordering, its state operator is strictly upper
triangular.

Let \(S\) denote such a finite transport. Then

\[
S^N=0,
\qquad
\operatorname{Tr}(S^k)=0
\]

for every \(k\geq1\), and

\[
\det(I-S)=1.
\]

Adding feed-forward boundary outputs or seam states does not change this:
the enlarged operator remains block triangular and has no directed cycle.

Therefore the lossless cut colligation cannot by itself generate any Euler
cyclic grade.

## Trace requires closure

The Euler chart for one prime contains a primitive loop

\[
L_pe_p=q_pe_p.
\]

Its cyclic grades are

\[
\mathfrak c_k(L_p)=\frac{q_p^k}{k}.
\]

Categorically, these grades require a trace: an output must return to the same
typed input through an evaluation–coevaluation closure. A feed-forward source
shift supplies no such return arrow.

The missing Euler attachment is consequently a feedback constructor. It must
close each primitive prime channel before cyclic powers are formed.

## One global return is the wrong grammar

Closing an \(N\)-stage shift into one weighted \(N\)-cycle does create
cyclic traces, but only at lengths divisible by \(N\). If the product of edge
weights is \(q\), then

\[
\operatorname{Tr}(C^k)=0
\]

unless \(N\) divides \(k\), while

\[
\operatorname{Tr}(C^{mN})=Nq^m.
\]

This does not reproduce \(q^k\) at every return depth. A coarse closure of
the whole transport chain therefore creates the wrong arithmetic language.

The minimum correct carrier has one primitive one-cycle for every prime.
Their direct sum satisfies

\[
\operatorname{Tr}(L^k)=\sum_p q_p^k,
\]

which is exactly the prime-power grammar. No primitive cycle exists at a
mixed composite label, so no false \(pq\) primitive is introduced.

## Attachment data

A genuine Euler-to-boundary attachment now requires:

1. the primitive loop object \(E_p\);
2. its source weight \(q_p\);
3. an incidence map from \(E_p\) into the doubled cut boundary;
4. a return map with the same prime type;
5. a coherence cell equating repeated feedback with the corresponding
   moving-seam comparison;
6. locally uniform control after restricted-product completion.

The first two items give arithmetic grammar. They do not authorize the last
four. An arbitrary return map could fit the desired determinant and remains
inadmissible without source derivation.

## DPC verdict

Resolved:

- the lossless cut colligation alone has trivial cyclic determinant;
- cyclic Euler grades require feedback;
- a single global feedback cycle has the wrong return-depth grammar;
- one primitive one-cycle per prime gives the correct prime-power traces.

Withheld:

- the source incidence and return maps between primitive loops and the doubled
  boundary;
- their seam coherence cells;
- restricted-product boundedness;
- the zero-state-to-flux bridge.

The finite falsifier is any proposed feed-forward attachment claiming a
nonzero primitive current: its state matrix is acyclic, so its first trace and
all higher cyclic traces vanish.

## Verification

The checker `check_euler_feedback_loop_necessity.py` verifies nilpotent
acyclic transport, the wrong grammar of one coarse cycle, and the exact cyclic
grades of independent primitive one-cycles.
