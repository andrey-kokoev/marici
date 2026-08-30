# Diagnostic ports form a partition-refinement lattice

## Bounded question

Given a finite family of candidate fault realizations, how should authorized
ports be combined to localize the fault, and where does an additional port have
the highest diagnostic value?

## Frozen candidate packet

Let

\[
\mathcal M=\{m_1,\ldots,m_n\}
\]

be the frozen finite set of candidate mechanisms. A deterministic diagnostic
test \(t\) has an outcome map

\[
o_t:\mathcal M\longrightarrow O_t.
\]

Two mechanisms remain equivalent under \(t\) when

\[
o_t(m)=o_t(m').
\]

The fibres of \(o_t\) form a partition \(\Pi_t\) of \(\mathcal M\). Each block
is an unresolved fault region relative to that test.

## Joint diagnostic theorem

For a test family \(F\), define the joint signature

\[
\sigma_F(m)=(o_t(m))_{t\in F}.
\]

The unresolved regions are the fibres of \(\sigma_F\). Their partition is the
common refinement

\[
\Pi_F=\bigwedge_{t\in F}\Pi_t.
\]

The family gives exact localization precisely when \(\sigma_F\) is injective.
Equivalently, every distinct pair \(m,m'\) is separated by at least one test:

\[
m\neq m'
\quad\Longrightarrow\quad
o_t(m)\neq o_t(m')
\]

for some \(t\in F\).

Thus diagnostic faithfulness is a joint property. No individual port need be
faithful.

## Monotone refinement

If \(F\subseteq G\), then

\[
\Pi_G\preceq\Pi_F.
\]

Adding a test can only split existing unresolved regions. It cannot merge
regions unless an earlier test or trust assumption is removed.

A new test has zero exact information gain relative to \(F\) when its outcome
is constant on every block of \(\Pi_F\). It may produce another scalar, but it
does not refine the current diagnosis.

This supplies a structural definition of redundant observation: redundancy is
relative to the existing joint tester packet, not to superficial similarity of
the instruments.

## Pair-cover formulation

Let the universe of distinctions be

\[
U=\{\{m,m'\}:m,m'\in\mathcal M,\ m\neq m'\}.
\]

Each test covers the pairs it separates:

\[
S_t
=
\{\{m,m'\}\in U:o_t(m)\neq o_t(m')\}.
\]

A test family is faithful exactly when

\[
\bigcup_{t\in F}S_t=U.
\]

Consequently, synthesizing the smallest nonadaptive diagnostic interface is
the minimum set-cover problem on candidate pairs. If tests have implementation
costs, risks, or authority costs, the appropriate problem is weighted pair
cover.

The compiler may optimize only over authorized tests. An imagined probe that
separates every pair has no standing unless its source constructor and physical
port are admitted.

## Smallest four-mechanism witness

Let

\[
\mathcal M=\{m_{00},m_{01},m_{10},m_{11}\}.
\]

Test \(a\) reads the first index and test \(b\) reads the second. Their
partitions are

\[
\Pi_a
=
\{\{m_{00},m_{01}\},\{m_{10},m_{11}\}\},
\]

and

\[
\Pi_b
=
\{\{m_{00},m_{10}\},\{m_{01},m_{11}\}\}.
\]

Neither test localizes the mechanism. Their joint signatures are

\[
00,\ 01,\ 10,\ 11,
\]

so their common refinement is discrete. Two partial ports are jointly faithful.

A third test that repeats \(a\) has zero exact refinement gain, even if it
improves statistical confidence about the first index.

## Exact resolution versus statistical confidence

Partition refinement concerns distinct predicted outcome laws. Repeating a
noisy test may reduce estimation error without changing which candidate laws
are identical.

For a probabilistic test, replace \(o_t(m)\) by the full outcome distribution

\[
P_t(\cdot|m).
\]

Two candidates occupy the same block exactly when these distributions agree.
Finite samples do not alter the exact partition; they change the confidence
with which one infers its block.

Therefore the programme must keep two quantities separate:

- structural resolution, determined by equality of predicted laws;
- statistical resolution, determined by sample size and separation between
  unequal laws.

## Highest information gain

Without a prior, a conservative next test minimizes the size of the largest
new block inside the current unresolved region. With a declared prior \(\pi\),
one may maximize expected entropy reduction:

\[
H_\pi(M)-\mathbb E[H_\pi(M|O_t)].
\]

Neither criterion replaces pair coverage. A test can have high expected gain
while leaving one theorem-critical pair indistinguishable. When the objective
is falsification of a specific explanation, the highest-value test is the
cheapest authorized test that separates that explanation from its strongest
surviving rival.

The choice rule must therefore freeze:

1. the candidate family;
2. the target distinction or prior;
3. the test costs;
4. the authority boundary;
5. and whether the goal is worst-case, expected, or theorem-critical
   resolution.

There is no context-free scalar called information gain.

## Adaptive diagnostic trees

A nonadaptive packet executes every selected test. An adaptive strategy chooses
the next test from earlier outcomes. It is a decision tree whose nodes are
current partition blocks.

At a node containing candidate set \(C\), a useful test must split \(C\). Exact
adaptive localization is possible precisely when every non-singleton reachable
block has some authorized continuation that separates its remaining candidates.

Adaptive testing can lower expected cost because expensive ports are used only
on branches that need them. It does not overcome an inseparable pair. If two
candidates have identical laws under every executable continuation, no decision
tree distinguishes them.

## Causal-cut constraint

The preceding packet showed that a port must cross the causal cut separating
competing fault loci. The partition theorem now makes that requirement finite.

For every unresolved candidate pair, at least one selected test must both:

- cross a cut on which their realizations differ;
- and produce different predicted outcomes under the frozen model.

A terminal duplicate that never crosses the competing cut covers no such pair.
It may improve confidence about an already exposed distinction while leaving
causal localization unchanged.

## First-failure localization

Suppose each candidate \(m\) marks a possible first failed constructor or an
incomparable set of first failures. The current first-failure report is the
block of \(\Pi_F\) containing the true candidate.

If that block contains several causal locations, a point report is not
authorized. The next diagnostic port should be chosen by the candidate pairs
inside that block, not by distinctions already resolved elsewhere.

This prevents global test counts from masking a local blind region. A large
tester tower may still have zero gain on the one pair that changes the theorem.

## Toric-code instance

Candidate faults may include data error, ancilla preparation fault, extraction
gate fault, measurement fault, shared syndrome-memory fault, and independent
controller-copy fault.

One syndrome readout partitions these mechanisms coarsely. Repeated extraction,
flag ancillas, intermediate ancilla checks, and replica comparison induce
different refinements. A minimal fault-tolerant packet must separate every pair
whose required recovery actions differ.

It need not identify mechanisms that lead to the same authorized recovery and
future behavior. The candidate quotient should therefore be frozen at the
level of control-relevant equivalence, not microscopic storytelling.

## Optical instance

Candidate explanations for a dark output may include source extinction,
polarizer orientation, absorption, detector inefficiency, and display failure.
Intensity at the terminal detector leaves several mechanisms in one block.

An optical tap, polarization-resolved port, detector self-test, and display
loopback cover different candidate pairs. The best next port depends on which
unresolved pair matters and which intervention is physically available.

## Software instance

Candidate faults in an event pipeline may lie in production, serialization,
broker storage, fanout, consumer parsing, or presentation. Logs at several
consumers can be duplicates of one shared broker record and therefore cover few
upstream pairs.

Checksums, source-side captures, broker inspection, replay fixtures, and
consumer loopbacks form a partition-refining test family. Observability count is
irrelevant unless their joint signatures separate the control-relevant faults.

## DPC: diagnostic sufficiency is pair separation

The conjecture is:

> A finite diagnostic explanation is adequate only when its authorized test
> family separates every surviving pair of control-relevant mechanisms, or
> explicitly reports the unresolved equivalence blocks. The next experiment
> should target an unresolved theorem-critical pair rather than maximize the
> number of additional scalar outputs.

This turns criticism into construction. A critic supplies a rival in the same
current block; a productive experiment is one whose predicted outcomes split
that pair.

## Critics

### The true mechanism may be absent from the candidate set

Correct. Pair separation is conditional on candidate completeness. Residual
tests and open-set anomaly channels are needed to challenge the frozen model
itself.

### Exact outcome equality is unrealistic

Then each test needs a statistical distance, tolerance, and sample budget.
The exact partition remains the zero-distance skeleton of that quantitative
problem.

### Minimal set cover ignores test order

Correct. It solves nonadaptive interface synthesis. Adaptive diagnosis requires
a decision tree and may have a lower expected cost.

### Microscopic mechanisms are too numerous

Then quotient candidates by predictive or control equivalence first. The
diagnostic target is the smallest distinction needed for future action, not an
unbounded list of hidden stories.

### Entropy gives an objective ranking

Only after a prior and cost model are frozen. Worst-case and theorem-critical
objectives may select a different test.

## Exact falsifiers

- A diagnostic packet called faithful while one candidate pair has identical
  joint signatures.
- A new output counted as information gain although it is constant on every
  current partition block.
- Repeated samples claimed to separate candidates with identical outcome laws.
- An unauthorized ideal probe included in the minimum port set.
- A high-entropy test preferred while it leaves the theorem-critical rival
  untouched.
- A point fault reported when the observed signature corresponds to a
  multi-candidate block.
- Microscopic candidates separated even though every authorized continuation
  treats them identically.

## Machine-readable diagnostic packet

```json
{
  "code": "diagnostic_partition_refinement",
  "candidate_count": 4,
  "authorized_tests": ["a", "b"],
  "joint_signature_injective": true,
  "unresolved_blocks": [],
  "pair_cover_complete": true,
  "zero_gain_tests": ["duplicate_a"],
  "selection_objective": "theorem_critical_pair",
  "unauthorized_tests_used": false
}
```

## Deutschian explanation

A diagnostic port is useful because rival mechanisms predict different things
there. Each port cuts the space of explanations into blocks. Combining ports
intersects those blocks until either one explanation remains or an equivalence
class survives.

The right next experiment is therefore not the one that produces the most
data. It is the one that breaks the most important surviving imitation at an
authorized causal cut.

## Claim boundary

This packet proves the finite partition-refinement and pair-cover formulation.
It does not solve large minimum-cover instances, validate candidate completeness,
or provide statistical sample-complexity bounds.

## Process calibration

Pre-objective ratings were excitement 10/10, confidence 9.5/10, and expected
information gain 10/10. The target was an exact criterion for diagnostic port
selection.

Post-objective ratings are excitement 10/10, confidence 10/10, and realized
information gain 10/10. Diagnostic sufficiency is now pair separation, and the
highest-value next test is relative to a frozen unresolved pair, authority
boundary, and cost objective.
