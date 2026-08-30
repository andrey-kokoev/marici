# Finite context data cannot certify complete Hankel rank

## Bounded question

When does an observed finite Hankel-rank plateau certify a finite-dimensional
ordered realization, and what source theorem is required to exclude new hidden
directions at longer constructor words?

## Finite-data impossibility theorem

Let \(E\) contain two constructor letters \(0\) and \(1\). Let \(W\subset E^*\)
be any finite set of tested words, and choose \(L\) larger than every word
length in \(W\).

Define the zero scalar process

\[
f_0(w)=0
\]

for every word. Now define another process \(f_\infty\) by

\[
f_\infty(0^i110^j)
=
\begin{cases}
1,&i=j>L,\\
0,&i\neq j,
\end{cases}
\]

and set it to zero on all other words.

The two processes agree on every tested word because every nonzero word of
\(f_\infty\) has length greater than \(L\).

For each \(i>L\), take the Hankel row prefix

\[
u_i=0^i1
\]

and column suffix

\[
v_j=10^j.
\]

Then

\[
H_{f_\infty}(u_i,v_j)
=
f_\infty(0^i110^j)
=
\delta_{ij}.
\]

The complete Hankel matrix contains an infinite identity submatrix. Hence

\[
\operatorname{rank}H_{f_\infty}=\infty,
\]

while

\[
\operatorname{rank}H_{f_0}=0.
\]

No finite collection of scalar word observations can distinguish these two
rank possibilities.

## Consequence for finite plateaux

A rank plateau across all words tested up to length \(L\) proves only the rank
of that finite submatrix. It does not prove that longer prefixes or suffixes add
no new residual direction.

The hostile continuation can be delayed beyond any chosen cutoff. Therefore
arbitrarily many successful finite stages do not imply complete finite rank.

The same construction can add a delayed finite identity block of any prescribed
size. Thus finite data alone provide no upper bound on eventual finite rank
either.

## Why one-step sampled closure is insufficient

Suppose a finite row basis appears closed under appending each constructor when
tested against a finite suffix set. A delayed continuation can agree with all
those sampled equations and violate the same recurrence on a longer suffix.

The required shift law is an identity of residual functions:

\[
f_{ue}(v)
=
\sum_{b\in B}c_{u,e,b}f_b(v)
\]

for every continuation \(v\), not merely for the suffixes already sampled.

Finite numerical agreement with shift closure is evidence for a recurrence. It
is not the recurrence theorem.

## First sufficient gate: a source dimension bound

Suppose a source-derived theorem proves that the complete process has a linear
realization of dimension at most \(r\). If one observed Hankel submatrix has rank
\(r\), then

\[
r
\leq
\operatorname{rank}H_f
\leq
r.
\]

Hence the complete Hankel rank is exactly \(r\).

The finite matrix supplies the lower bound. The source theorem supplies the
upper bound. Neither part can replace the other.

This is the cleanest finite certification route when the constructor algebra
already gives a bounded state module.

## Second sufficient gate: global residual closure

Let \(B=\{b_1,\ldots,b_r\}\) be prefixes whose residual functions are linearly
independent. Suppose the source equations prove that, for every \(b_i\) and
constructor \(e\), the shifted residual \(f_{b_ie}\) lies in the span of
\(\{f_{b_j}\}\) as a function on all suffixes.

Suppose also that the empty residual lies in this span. Induction on word length
then places every residual in the same \(r\)-dimensional space. Therefore

\[
\operatorname{rank}H_f=r.
\]

The shift coefficients define the transition matrices of the realization.
This is a finite basis with an infinite-domain closure proof.

The certificate is finite in generators but not merely empirical. Its force
comes from a symbolic law extending the generator checks to every word.

## Third sufficient gate: a global recurrence

In a unary process, a source-proven linear recurrence of order \(r\) bounds the
Hankel rank by \(r\). In a multi-constructor process, the analogue is a finite
system of residual relations stable under every constructor shift.

Again, fitting a recurrence to finitely many terms does not prove it. The
recurrence must follow from the source dynamics, an algebraic identity, or an
independently established model class.

## Complexity priors are claim-bearing

Model selection often prefers the smallest realization consistent with finite
data. That is a useful inductive policy, but it is not deductive identification.

The statement that the world uses a realization of dimension at most \(r\) is a
substantive complexity hypothesis. It must be exposed to criticism rather than
smuggled in through a rank-truncation algorithm.

Minimum-description or Bayesian preferences can rank continuations. They do not
exclude a delayed new residual direction unless their prior is promoted to an
assumption.

## Completion gate

Suppose each cutoff process \(f_X\) has rank at most \(r_X\). Several distinct
questions remain:

- Is \(\sup_X r_X\) finite?
- Do the transition matrices admit a common coordinate frame?
- Do their norms remain controlled?
- Do the scalar word responses converge for every fixed word?
- Does the limiting process have finite Hankel rank?
- Do reachability and observability survive the limit?

Uniform rank alone is not enough if the realizations have no compatible limit.
Pointwise convergence of scalar responses can also lose observability when
distinguishing singular values collapse.

The completion theorem must control both algebraic dimension and the topology
of the realization maps.

## Smallest delayed finite-rank witness

For a chosen cutoff \(L\), define

Set

\[
f_1(0^{L+1})=1.
\]

For every other word \(w\), set \(f_1(w)=0\).

It agrees with the zero process on every word of length at most \(L\), yet its
Hankel matrix is nonzero. Thus even the distinction between rank zero and
positive finite rank can be postponed beyond an arbitrary finite experiment.

The infinite identity construction strengthens this from delayed nonzero rank
to delayed infinite rank.

## Relation to finite invertibility

Every finite Euler stage can be coherent, invertible, and zero-free while the
completion loses a uniform inverse bound. The Hankel obstruction has the same
logical form:

- every finite context stage may have stabilized rank;
- every tested shift equation may close;
- yet a later or limiting context may expose a new direction.

Finite certification becomes global only through a uniform source law. More
finite checks without such a law extend the verified interval; they do not
change the quantifier.

## Toric-code contrast

The smallest toric-code lattice has a source-derived finite chain complex. Its
dimensions are frozen before syndrome and loop matrices are computed. Once a
finite tester matrix reaches the known state-space dimension, injectivity is a
complete theorem for that frozen packet.

This is why finite toric-code certification closes while an unrestricted
infinite constructor completion does not. The finite source module supplies the
upper bound that raw observations cannot.

## Software instance

A service may match a finite test suite and then enter a new state after an
untested command sequence. No finite suite proves a state bound for arbitrary
software.

A finite-state specification, type invariant, or verified transition relation
can supply the missing upper bound. Tests then establish that the specified
states are actually distinguishable. Without the specification, inferred
minimal state count is a model-selection result.

## Theta/Tate hostile instance

Finite-cutoff context matrices can suggest a stable operator lift. They cannot
exclude new tail residuals at longer constructor words or larger cutoffs.

The required source theorem must provide at least one of:

- a uniform finite module carrying every authorized constructor;
- global residual relations stable under all constructor shifts;
- a recurrence derived from the doubled-tail equations;
- or a completion theorem bounding and identifying the limiting realization.

Absent such a theorem, Hankel reconstruction remains a finite model, not the
completed source operator.

## DPC: finite rank needs a source upper bound

The conjecture is:

> No finite context plateau should be reported as a complete realization theorem
> unless an independent source law bounds the full residual dimension or proves
> global shift closure. Finite data supply lower bounds and falsifiers; the
> explanatory upper bound must come from the constructor theory.

This identifies the exact non-empirical content of a finite-dimensional
explanation.

## Critics

### Real experiments are always finite

Correct. Deductive global conclusions then depend on structural assumptions.
The packet makes those assumptions visible instead of denying their necessity.

### Simplicity justifies choosing the minimal continuation

It justifies a preference, not uniqueness. A delayed higher-rank continuation
remains observationally possible until a complexity law excludes it.

### Analyticity may determine the continuation

Yes, when analyticity and the relevant domain are source-derived and the
identity theorem applies. That is precisely an additional global law, not a
consequence of finite rank data.

### Numerical rank tolerance handles the problem

Tolerance handles noise in a fixed matrix. It does not rule out exact new
directions beyond the sampled word set or singular directions emerging at
completion.

### A known implementation supplies a dimension bound

Yes, if the implementation and its accessible state module are independently
frozen. Then the bound is source authority rather than an inference from the
same output samples.

## Exact falsifiers

- A finite Hankel plateau presented as complete finite rank without a global
  upper bound.
- Shift closure checked only on sampled suffixes and promoted to all words.
- A fitted recurrence treated as source-derived law.
- Uniform finite ranks used to infer convergence of realization matrices.
- A minimal empirical model presented as the unique possible mechanism.
- A delayed higher-rank continuation excluded solely because no current test
  reaches it.
- A completion theorem stated without controlling observability loss.

## Machine-readable rank boundary

```json
{
  "code": "finite_hankel_plateau_not_global",
  "tested_word_bound": "L",
  "observed_submatrix_rank": "r",
  "source_dimension_upper_bound": null,
  "global_shift_closure": false,
  "delayed_infinite_rank_extension_exists": true,
  "complete_rank_certified": false,
  "required_theorem": "source dimension bound or global residual recurrence"
}
```

## Deutschian explanation

A finite rank plateau says that the histories tried so far generate only a
finite space of scalar futures. It does not explain why an untried history
cannot create a new future.

The missing explanation is a constructor law: a bounded state module, a
recurrence, or a shift-closure identity that forces every longer history back
into the known span. Observation finds the basis; theory closes it.

## Claim boundary

This packet proves that arbitrary finite word data admit both zero-rank and
infinite-rank continuations and states two sufficient source-law gates for a
complete rank certificate. It does not prove such a gate for an infinite
physical sector.

## Process calibration

Pre-objective ratings were excitement 10/10, confidence 10/10, and expected
information gain 10/10. The target was the exact completion obstruction for
finite contextual realization.

Post-objective ratings are excitement 10/10, confidence 10/10, and realized
information gain 10/10. Finite context data provide lower bounds; complete
finite rank requires an independently authorized upper-bound or recurrence
theorem.
