# Normalized fixed-dimensional memory factorizations are compact

## Correction target

The preceding causal-Hankel packet left open the possibility that every finite
table might have a normalized realization in one fixed memory dimension while
all factor gauges escape in completion. That possibility is false at the bare
probability-factorization level.

Once states and effects are normalized inside a fixed finite carrier, their
parameter spaces are compact. Exact finite satisfiability then forces a global
factorization.

## Frozen infinite table

Let \(\mathcal P\) be any set of past labels and \(\mathcal F\) any set of
future-test labels. Let

\[
H:\mathcal F\times\mathcal P\to[0,1]
\]

be one fixed probability table. Finite restrictions use finite subsets
\(P\subset\mathcal P\) and \(F\subset\mathcal F\).

The table itself must be consistent: overlapping finite restrictions are
restrictions of the same \(H\). A sequence of independently fitted tables is a
different problem.

## Classical compactness theorem

Fix a classical memory cardinality \(r\). Suppose that for every finite
\(P,F\), there exist probability vectors

\[
s_p\in\Delta_r
\]

and bounded response vectors

\[
e_f\in[0,1]^r
\]

such that

\[
H_{f,p}=e_f\cdot s_p
\]

for every \(p\in P\) and \(f\in F\).

Then one global family \(\{s_p\}_{p\in\mathcal P}\) and
\(\{e_f\}_{f\in\mathcal F}\) with the same dimension realizes all of \(H\).

### Proof

Consider the product space

\[
X=
\prod_{p\in\mathcal P}\Delta_r
\times
\prod_{f\in\mathcal F}[0,1]^r.
\]

Every factor is compact, so \(X\) is compact. For each pair \((f,p)\), the
constraint

\[
e_f\cdot s_p=H_{f,p}
\]

defines a closed subset of \(X\). The finite-realizability assumption says
that every finite collection of these closed sets has nonempty intersection.
Compactness gives a point in their total intersection.

## Quantum compactness theorem

Fix a Hilbert-space dimension \(d\). Let \(\mathcal D_d\) be the compact set of
density operators and let

\[
\mathcal E_d=\{E:0\leq E\leq I\}
\]

be the compact effect interval.

Suppose every finite restriction of \(H\) has a normalized quantum
factorization

\[
H_{f,p}=\operatorname{Tr}(E_f\rho_p),
\qquad
\rho_p\in\mathcal D_d,
\quad
E_f\in\mathcal E_d.
\]

Then a single global dimension-\(d\) factorization realizes all of \(H\).

The proof is identical in

\[
X=
\prod_{p\in\mathcal P}\mathcal D_d
\times
\prod_{f\in\mathcal F}\mathcal E_d,
\]

because the trace-pairing constraints are closed.

## Countable constructive form

When past and future labels are countable and presented in nested finite
prefixes, the theorem can be seen by diagonal subsequences. Choose a normalized
factorization at every cutoff. Compactness gives a subsequence on which the
first state and effect converge, then a further subsequence for the second, and
so on. The diagonal subsequence converges coordinatewise, and continuity of the
trace pairing preserves every fixed table entry.

This constructs existence but need not supply an effective convergence rate.

## Vanishing-error form

Suppose the \(N\)-th normalized dimension-\(d\) factorization approximates the
first \(N\) past and future labels with uniform error \(\varepsilon_N\), where

\[
\varepsilon_N\to0.
\]

The same diagonal compactness argument produces an exact global factorization:
for each fixed pair, the approximation error eventually tends to zero and the
pairing is continuous.

A fixed positive error tolerance yields only an approximate global model at
that tolerance.

## What compactness does not prove

The theorem establishes existence of a global probability factorization. It
does not establish:

- uniqueness or identifiable coordinates;
- a uniform inverse tester-frame bound;
- continuity of \(p\mapsto\rho_p\) in an external label topology;
- continuity of \(f\mapsto E_f\);
- compatibility with a constructor monoid acting on labels;
- a common dynamical update law between multiple temporal cuts;
- locality, energy, or implementation bounds;
- or computability of the selected global factorization.

These conditions can define nonclosed or noncompact subclasses. Escape can
reappear there without contradicting the theorem.

## Why unnormalized gauges can escape

An abstract bilinear factorization is invariant under

\[
x_p\mapsto Gx_p,
\qquad
y_f\mapsto G^{-*}y_f.
\]

A sequence of poorly chosen \(G\) can make one factor family diverge while the
products remain fixed. Density normalization and the order interval
\(0\leq E\leq I\) eliminate this artificial gauge escape by placing all
coordinates in compact sets.

Therefore an escaping unnormalized factorization is not evidence that no
normalized memory exists. One must first test whether a source-authorized
normalization is available.

## Rank versus normalized realization

Bounded ordinary rank alone is insufficient. It neither bounds nonnegative
rank nor PSD rank in general. The compactness theorem assumes the stronger
fact that every finite restriction already has a normalized factorization in
one fixed classical cardinality or quantum dimension.

Likewise, an arbitrary PSD factorization need not arrive with density traces
and effect upper bounds. Including the normalization experiment and causal unit
rows in the table is one way to make the physical constraints part of finite
satisfiability rather than an afterthought.

## Relation to completion loss

There are now three distinct completion questions.

### Bare representation existence

Fixed-dimensional normalized finite realizability implies a global
factorization. No inverse bound is required.

### Stable inference

Reconstructing factor coordinates from noisy probabilities requires a uniform
tester-frame or condition-number bound. This may fail even though a global
factorization exists.

### Constructor-compatible completion

If label operations, dynamics, topology, or source currents must act
continuously on the factors, those additional laws need their own closedness
and compactness theorem. Bare table compactness does not supply it.

The earlier “inverse norms escape” phenomenon belongs to stable inference or
constructor continuity, not automatically to existence of a finite normalized
memory carrier.

## Finite falsifiers

The fixed-dimension compactness conclusion can fail only if at least one
hypothesis fails. The first obstruction must identify one of:

- a finite subtable having no normalized dimension-\(d\) factorization;
- carrier dimension increasing with cutoff;
- inconsistent values on overlapping finite tables;
- states not confined to a compact normalized set;
- effects not confined to a compact bounded interval;
- approximation errors not tending to zero;
- or an extra constructor/topology law whose admissible realization set is not
  closed under the compact limit.

“Every finite stage works but no global normalized factorization exists” is
not an admissible hostile fixture under the frozen theorem hypotheses.

## Consequence for the finite-Euler analogy

Finite zero-freeness of scalar Euler stages does not meet these hypotheses for
an inverse operator. Nonzero scalars can approach zero because the inverse
norms live in a noncompact space. By contrast, normalized memory states and
bounded effects live in compact spaces before inversion.

The analogy is therefore conditional:

- finite invertibility needs a uniform inverse bound;
- finite normalized probability factorability needs only fixed dimension and
  exact consistency for global existence;
- stable recovery of the factors again needs a uniform inverse bound.

Conflating these questions manufactures a completion obstruction where none
exists.

## Deutschian explanation

The global memory exists because every finite demand can be satisfied inside
one compact normalized carrier, and closed probability laws survive limits.
There is nowhere for the carrier coordinates to escape.

When completion still fails, the explanation must name the noncompact datum:
inverse sensitivity, growing dimension, discontinuous label action, incompatible
cutoffs, or an unbounded current. “The limit is infinite” is not enough.

## Claim boundary

This is an existence theorem for normalized classical and quantum
past-future factorizations. It does not construct a unique process tensor or a
continuous dynamical realization across all temporal cuts.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The target was to determine whether fixed-rank finite memory models can
genuinely disappear in completion.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Full normalization changes the answer: fixed-dimensional finite
realizability is compact and globalizes. The hard completion problem survives
only in inference, constructor continuity, dynamics, or growing capacity.
