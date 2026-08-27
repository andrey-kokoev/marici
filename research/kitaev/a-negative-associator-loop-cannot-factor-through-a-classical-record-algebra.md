# A negative associator loop cannot factor through a classical record algebra

Owner: `marici.Kitaev`

## Question

Which resource is unavoidable in every realization of the electric
associator loop, independently of whether one uses a four-copy cyclic shift,
weak sequential measurements, or another interferometer?

The exact loop value is negative:

\[
\operatorname{Tr}(P_AQ_AP_BQ_C)=-\frac18.
\]

A product of commuting positive record events has nonnegative expectation.
Therefore no positive commutative record algebra can preserve this ordered
loop. Every successful realization must retain a noncommutative coherent path
across at least one phase-bearing cycle until that cycle is closed.

This gives a precise constructor--record complementarity. A perfect
which-route record made on an edge before loop closure deletes that edge from
the coherent support graph. Recording a cut set that intersects every cycle
removes all associator phase information even though every edge probability
may remain available.

## Claim boundary

The theorem excludes positive multiplicative factorization of the ordered
loop through a commutative event algebra. It does not exclude classical
simulation with signed or complex quasiprobabilities, nor does it claim a
computational separation.

The graph cut theorem uses an explicit edge-local dephasing model. A physical
record that acts jointly on several edges requires its own incidence map and
may have a different minimum cost.

## Frozen electric witness

On the total-`C` multiplicity space, the left and right fusion-tree projectors
obey

\[
\Omega
=
\operatorname{Tr}(P_AQ_AP_BQ_C)
=
-\frac18.
\]

Every factor is a positive rank-one projector. The negative number arises from
their noncommutative ordered composition, not from a negative state or a
negative measurement effect.

The four pairwise edge readouts remain ordinary probabilities:

\[
\operatorname{Tr}(P_AQ_A)=\frac14,
\]

\[
\operatorname{Tr}(P_BQ_C)=\frac12,
\]

\[
\operatorname{Tr}(P_AQ_C)=\frac12,
\]

\[
\operatorname{Tr}(P_BQ_A)=\frac14.
\]

Their product is positive and determines only

\[
|\Omega|^2=\frac1{64}.
\]

Thus the obstruction appears only when the four positive local contacts are
retained as one ordered coherent word.

## Commutative positive-factorization theorem

Let `A` be a commutative unital C-star algebra, let

\[
p_1,p_2,p_3,p_4\in A
\]

be projections, and let `tau` be a positive linear functional. Since the
projections commute,

\[
p=p_1p_2p_3p_4
\]

is again a projection. Hence

\[
\tau(p)\geq0.
\]

More generally, a product of commuting positive elements is positive in a
commutative C-star algebra and has nonnegative value under every positive
functional.

Suppose a proposed classical record realization provides a positive
multiplicative map sending

\[
P_A,Q_A,P_B,Q_C
\]

to positive events

\[
p_A,q_A,p_B,q_C
\]

and preserves the accepted evaluation functional. It would imply

\[
-\frac18
=
\tau(p_Aq_Ap_Bq_C)
\geq0,
\]

which is impossible.

Therefore the ordered electric loop has no positive commutative event-algebra
realization preserving multiplication and evaluation.

## What the theorem does not prohibit

A classical calculation may store the number `-1/8` directly or reproduce it
using signed weights. Such a model abandons at least one required arrow:

- the weights are not positive event probabilities;
- multiplication does not represent conjunction of commuting records;
- the scalar is inserted rather than generated from admitted event incidence;
- or the evaluation does not preserve the physical state--effect pairing.

The theorem is consequently about explanatory realization, not numerical
simulatability.

## Record overlap law

Consider two coherent route histories with normalized environment records:

\[
|\Psi\rangle
=
a|h_0\rangle|r_0\rangle
+
b|h_1\rangle|r_1\rangle.
\]

After discarding the record system, the route coherence is multiplied by

\[
\gamma=\langle r_1|r_0\rangle.
\]

Every phase-sensitive cross term is therefore attenuated by `gamma`. If
independent record fragments are produced,

\[
|r_j\rangle
=
\bigotimes_{k=1}^n|r_j^{(k)}\rangle,
\]

then

\[
\gamma_n
=
\prod_{k=1}^n
\langle r_1^{(k)}|r_0^{(k)}\rangle.
\]

One perfectly distinguishing fragment has zero overlap and kills the complete
cross term. Redundant imperfect fragments suppress it multiplicatively.

Under an ideal equal-amplitude two-route model, define normalized visibility
and optimal pure-record distinguishability by

\[
V=|\gamma|,
\qquad
D=
\frac12
\left\|
|r_0\rangle\langle r_0|
-
|r_1\rangle\langle r_1|
\right\|_1.
\]

For pure record states,

\[
D=\sqrt{1-|\gamma|^2},
\qquad
V^2+D^2=1.
\]

This is the exact local tradeoff: improving the objective which-route record
reduces the coherent loop resource. It is not a statement that all records are
forbidden.

## Record timing matters

A pointer record produced after the two alternatives have coherently closed
may record the final control quadrature without revealing which internal route
was taken. Such a record need not reduce the already formed interference
signal.

A pointer record produced before closure and correlated with the route label
changes the future Carrier. If it is perfectly distinguishing, it removes the
cross-route term required by the loop.

Thus the relevant distinction is not measurement versus no measurement. It is

- an invariant final record of the closed loop;
- versus a route-resolving record inserted across the open loop.

The first reports the holonomy. The second destroys the capability whose
holonomy was to be reported.

## Coherent support graph

Let the nonzero left--right overlap graph be

\[
G=(L\sqcup R,E).
\]

An edge belongs to the coherent support when its complex overlap remains
available for ordered composition. Its probability may remain measurable even
after its phase coherence is lost.

Let `D` be a set of edges on which an ideal local record performs complete
which-route dephasing. The surviving coherent graph is

\[
G_{\mathrm{coh}}=G\setminus D.
\]

Its cycle-space dimension over the two-element field is

\[
\dim Z_1(G_{\mathrm{coh}})
=
|E\setminus D|-|V|+c(G\setminus D),
\]

where isolated vertices are included in the component count.

Phase-bearing overlap monomials survive only on cycles of this coherent graph.
All cycle phases are destroyed exactly when `D` meets every cycle, equivalently
when

\[
G\setminus D
\]

is a forest. Such a set `D` is a feedback edge set.

For a graph with `E` edges, `V` vertices, and `c` components, a minimum
feedback edge set has size

\[
E-V+c.
\]

This is the exact edge-local record cost for deleting every coherent cycle.
It is also the number of independent non-tree phase links that must remain
controlled if every cycle coordinate is to remain potentially accessible.

## Electric support specialization

The frozen electric overlap graph has

\[
|V|=6,
\qquad
|E|=8,
\qquad
c=1.
\]

Its coherent cycle rank is therefore

\[
8-6+1=3.
\]

Under the edge-local model, three suitably chosen perfect record edges can
reduce the coherent graph to a spanning tree and erase all cycle phases while
leaving eight scalar transition probabilities available as classical data.

For the particular four-edge loop

\[
A_L-Q_A-B_L-Q_C-A_L,
\]

perfectly recording any one of its four coherent edges destroys that loop.
Other electric cycles may survive unless the recorded edges form a feedback
set for the full graph.

## Constructor lower bound

The four-copy controlled-shift circuit is only one sufficient realization.
The present theorem yields the implementation-independent lower bound:

> Every faithful realization of the negative loop must contain a stage whose
> accepted algebra has not factored through commuting positive route records,
> and coherent memory must cross every record cut intersecting the target
> cycle until the cycle is closed.

This does not require a literal control qubit, Fredkin gate, or four parallel
copies. It requires an operational equivalent of noncommutative ordered
coherence.

Any alternative compiler may lower copy count or fanout, but it must identify
where this coherence lives, how it crosses the route cuts, and why its error
model does not silently replace the ordered word by positive scalar edges.

## Relation to objective record formation

The associator experiment and the objective-record programme are not separate
problems. They occupy opposite sides of the same cut.

- Before closure, broadcastable route information is an environment-induced
  dephasing channel on the phase-bearing support.
- At closure, noncommutative ordered composition converts route coherence into
  a gauge-invariant loop value.
- After closure, a commuting pointer may redundantly record that final value.

The physically important design problem is therefore to localize the record
boundary: protect the open cycle from route-resolving fanout, then deliberately
classicalize the invariant closed-loop quadrature.

## Hostile fixtures

### Positive Boolean path model

Assign nonnegative weights to the four record events and multiply them around
the cycle. The result is nonnegative and cannot equal `-1/8`.

### Signed classical repair

Insert one negative path weight to recover the desired scalar. The numerical
answer is reproduced, but the weight is not a positive event probability and
the model no longer realizes a commutative record algebra.

### Perfect early route record

Attach orthogonal environment states to the two interfering histories. Their
overlap is zero, so the phase-sensitive term vanishes although the route label
becomes perfectly broadcastable.

### Final invariant pointer

Close the interferometer first and then copy its `X`-quadrature result into a
commuting pointer. This does not contradict the theorem because the record is
of the closed invariant, not of the open route.

### Scalar edge archive

Retain all eight electric transition probabilities after dephasing a feedback
edge set. The archive is complete for the edge table and incomplete for all
three cycle phases.

## Falsifiers

- Four commuting positive projections are assigned negative product
  expectation under a positive state.
- Signed quasiprobability is called an ordinary positive classical record.
- A perfect which-route record is claimed to preserve the corresponding
  interference term after the record is discarded.
- Every measurement is claimed to destroy the loop regardless of timing and
  measured algebra.
- Edge probabilities are counted as surviving coherent edges after complete
  phase dephasing.
- The feedback-edge count is applied to a joint record constructor without
  first deriving its edge incidence.
- A single recorded edge outside the target cycle is claimed to destroy that
  cycle.
- The noncommutative lower bound is promoted to a Fredkin-gate lower bound.
- The negative electric loop is promoted to a complete contextuality or
  computational-advantage theorem.

## Disposition

The implementation-independent resource boundary is now exact. The negative
electric associator loop cannot pass through a positive commutative record
algebra while preserving ordered multiplication and evaluation. A perfect
route record before closure deletes coherent cycle information; a final record
of the closed invariant is admissible.

In the edge-local model, phase survival is governed by the cycle space of the
coherent support graph. The electric graph has three independent cycle
coordinates, and a feedback edge set of size three removes all of them. The
next constructor question is no longer whether a particular four-copy circuit
is mandatory. It is where any proposed compiler stores the noncommutative
coherence that crosses the cycle until closure.

No checker, build, or Git operation was run for this research-only packet.
