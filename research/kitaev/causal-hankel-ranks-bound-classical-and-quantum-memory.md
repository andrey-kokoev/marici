# Causal Hankel ranks bound classical and quantum memory

## Bounded question

Given only probabilities obtained by joining authorized past experiments to
authorized future tests, what minimum memory must cross the cut, and which
parts of that conclusion are realization-independent?

## Frozen past-future table

Choose a finite family of authorized past interventions \(p\in\mathcal P\) and
future success tests \(f\in\mathcal F\). Cut the ordered process between them
and define

\[
H_{f,p}=\Pr(f\text{ succeeds after }p).
\]

This nonnegative matrix is the finite causal Hankel table. Rows are future
functionals; columns are past-induced states at the cut.

The term “Hankel” refers to the past-future factorization, not necessarily to a
time-translation-invariant scalar sequence.

## Classical memory factorization

Suppose an accessible classical memory with \(r\) latent values carries all
relevant influence across the cut. Let \(s_p(m)\geq0\) be the subnormalized
weight of memory value \(m\) after past \(p\), and let \(e_f(m)\geq0\) be the
future success probability conditioned on \(m\). Then

\[
H_{f,p}=\sum_{m=1}^r e_f(m)s_p(m).
\]

Therefore

\[
\operatorname{rank}_+(H)\leq r,
\]

where \(\operatorname{rank}_+\) is nonnegative rank.

Conversely, a nonnegative factorization supplies an algebraic latent-state
interface. To promote it to a normalized physical stochastic realization, one
must also enforce the preparation normalization, effect bounds, and causal
compatibility rows. Nonnegative rank is therefore an exact factorization
invariant and a lower bound on any typed classical realization.

## Quantum memory factorization

Suppose instead that a \(d\)-dimensional quantum memory crosses the cut. Every
past induces a positive semidefinite operator \(\rho_p\), and every future test
pulls back to a positive effect \(E_f\). Then

\[
H_{f,p}=\operatorname{Tr}(E_f\rho_p).
\]

Hence the positive-semidefinite rank obeys

\[
\operatorname{rank}_{\rm psd}(H)\leq d.
\]

As in the classical case, an abstract PSD factorization becomes a physical
memory realization only after the trace, effect, and causal constraints are
typed. It nevertheless gives an exact algebraic lower bound on quantum memory
dimension.

Since the real vector space of Hermitian \(d\)-by-\(d\) matrices has dimension
\(d^2\),

\[
\operatorname{rank}(H)\leq d^2.
\]

Thus every quantum realization satisfies

\[
d\geq\left\lceil\sqrt{\operatorname{rank}(H)}\right\rceil.
\]

Every classical realization also satisfies

\[
r\geq\operatorname{rank}_+(H)\geq\operatorname{rank}(H).
\]

## What each rank means

- Ordinary rank measures the dimension of the observable linear
  past-future correlation space.
- Nonnegative rank measures the smallest algebraic commutative latent carrier.
- PSD rank measures the smallest algebraic positive noncommutative carrier.

These are coefficient-lens invariants on the same carrier cut. They do not
encode the temporal order by themselves; the row and column labels retain the
past-future typing.

## Four-by-four qubit witness

Let \(r_1,\ldots,r_4\) be the vertices of a regular tetrahedron on the Bloch
sphere, so

\[
r_i\cdot r_j=
\begin{cases}
1,&i=j,\\
-1/3,&i\neq j.
\end{cases}
\]

Define pure qubit states and effects

\[
\rho_i=E_i=\frac12(I+r_i\cdot\sigma).
\]

Their probability table is

\[
H_{j,i}=\operatorname{Tr}(E_j\rho_i)
=
\begin{cases}
1,&i=j,\\
1/3,&i\neq j.
\end{cases}
\]

Equivalently,

\[
H=\frac23I_4+\frac13J_4.
\]

Its eigenvalues are \(2\) once and \(2/3\) three times, so

\[
\operatorname{rank}(H)=4.
\]

The displayed qubit factorization proves

\[
\operatorname{rank}_{\rm psd}(H)\leq2.
\]

Rank forbids PSD factor size one, hence its PSD rank is exactly two. Ordinary
rank also forces nonnegative rank at least four, while the four-column trivial
factorization gives at most four. Therefore

\[
\operatorname{rank}_+(H)=4,
\qquad
\operatorname{rank}_{\rm psd}(H)=2.
\]

The same finite probability table thus requires at least four classical latent
values but only a two-dimensional quantum carrier. This is a carrier-dimension
separation, not a claim that one qubit contains more unrestricted classical
information than two bits.

## Finite memory-obstruction certificate

Given a claimed memory dimension, the smallest algebraic rejection data are:

- a finite past list and future list;
- the exact probability matrix \(H\);
- a rank or factorization lower-bound witness;
- the claimed classical cardinality or quantum Hilbert dimension;
- and the frozen cut through which memory must pass.

For quantum dimension \(d\), any nonzero minor of order \(d^2+1\) immediately
rejects the claim. For classical cardinality \(r\), ordinary rank greater than
\(r\) rejects it, while stronger cases require a nonnegative-rank certificate.

## Tester completeness and memory dimension

An underspecified tester family can only lower the observed ranks. Adding past
preparations or future tests appends columns or rows and can reveal a larger
memory requirement.

Therefore a low observed Hankel rank has two explanations:

1. the process truly factors through a small memory;
2. the authorized tester packet is blind to additional memory directions.

Only a jointly faithful tester theorem on the declared process class turns the
observed factorization into a complete memory classification.

This repeats the toric-code lesson: local syndrome may reveal a quotient while
noncontractible probes expose the missing logical directions. Here the missing
directions are past-future correlations rather than homology classes.

## Completion stability

For a growing, exactly consistent family \(H_N\), an important compactness
distinction applies. If one fixed memory dimension works at every finite stage
with normalized states and bounded effects, then a global factorization exists.
The finite-dimensional density-operator and effect spaces are compact, and the
probability equations are closed. Finite satisfiability therefore has the
finite-intersection property.

Factor gauges can escape only when normalization is omitted, dimension grows,
the cutoff tables are inconsistent, or extra noncompact constructor/topology
requirements are imposed. A uniform tester-frame bound is needed for stable
inference and reconstruction, but not for bare existence of a normalized
global factorization.

Conversely, unbounded ordinary rank proves that no fixed finite-dimensional
classical or quantum memory can realize the full completed table.

Bounded ordinary rank alone still does not bound nonnegative or PSD rank. The
compactness theorem applies after one fixed normalized factor dimension has
been established at every finite stage.

## First failed cut

For a multi-time process, form the Hankel table at every causally ordered cut.
Relative to a frozen refinement order, the first failed cut is the earliest cut
whose certified rank exceeds the declared carrier capacity or whose uniform
factorization bound collapses.

“First” is therefore not absolute. It is defined by:

- the temporal cut order;
- the nested past and future tester families;
- the chosen coefficient lens;
- and the declared memory capacity.

Changing any of these changes the diagnostic question and must be reported as
a new audit, not as a refinement of the same first-failure claim.

## DPC: minimal causal memory

The conjecture is:

> The explanatory memory of a finite process is the smallest source-authorized
> carrier through which all admitted past-future correlations factor while
> preserving causal composition. Apparent additional memory unsupported by a
> rank increase is either tester-invisible, gauge, or encoded in untested
> interventions.

This becomes a proper explanation only when paired with a completeness claim
for the authorized tester family. Otherwise it is a minimal model relative to
present questions, not a claim about every counterfactual experiment.

## Critics

### Factor rank does not identify the realization

Correct. Many inequivalent state and effect families produce the same table.
Ranks bound carrier size; they do not reconstruct dynamics or constructor
authority.

### Quantum and classical dimensions use different units

Correct. Classical cardinality \(r\) and quantum Hilbert dimension \(d\) should
also be compared through storage costs such as \(\log_2r\) and \(\log_2d\),
plus preparation and readout restrictions. The factorization separation is
still exact.

### A larger hidden memory can remain invisible forever

Correct relative to an incomplete tester family. The theorem reports the
minimal memory needed for admitted correlations, not the ontic size of an
uncontrolled environment.

## Exact falsifiers

- A claimed classical memory size below a certified nonnegative-rank bound.
- A claimed quantum dimension \(d\) when \(\operatorname{rank}(H)>d^2\).
- An abstract factorization promoted to a physical realization without
  normalization and causal constraints.
- A low-rank table called complete without joint tester faithfulness.
- A cutoffwise bounded rank promoted to stable completion despite divergent
  factor gauges or vanishing frame bounds.
- Past and future labels mixed so that the alleged Hankel factorization crosses
  no fixed causal cut.
- Comparison of classical cardinality and Hilbert dimension as if they were the
  same resource unit.

## Deutschian explanation

Memory is what mediates counterfactual dependence of future outcomes on past
interventions across a frozen causal cut. The Hankel table exposes this
dependence, and its factorization rank measures the smallest carrier algebra
capable of transmitting it.

The explanation predicts how to refute an undersized memory model: add an
authorized past or future probe that raises the relevant rank. It also explains
why one endpoint trace is insufficient: a single row cannot reveal the
dimension of the space of counterfactual future responses.

## Claim boundary

This packet proves finite algebraic lower bounds and the tetrahedral separation.
It does not solve general nonnegative-rank or PSD-rank computation, certify a
unique physical realization, or impose continuity of a global factorization in
an additional source topology.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The target was a quantitative, falsifiable answer to how much accessible
memory an ordered process requires.

Post-objective: excitement 10/10, confidence 9.5/10, realized information gain
10/10. Causal Hankel factorization separates commutative and noncommutative
memory costs exactly. A subsequent compactness audit corrected the completion
boundary: fixed-dimensional normalized finite factorizations do yield a global
factorization; instability remains in identification, growing dimension, or
additional noncompact constructor topology.
