# Complete monotones certify every finite barrier but do not explain it

## Bounded question

Does every forbidden transition in a finite irreversible constructor system
admit a monotone certificate, and if so, why is finding such a monotone not
automatically an explanation?

## Frozen reachability preorder

Let \(X\) be a finite state set with a source-authorized constructor semigroup.
Write

\[
x\preceq y
\]

when some authorized forward word sends \(x\) to \(y\).

A Boolean resource monotone is a map

\[
M:X\to\{0,1\}
\]

satisfying

\[
x\preceq y
\quad\Longrightarrow\quad
M(x)\geq M(y).
\]

The orientation is conventional: resource cannot increase along forward
construction.

## Principal target monotone

For every target \(t\in X\), define

\[
M_t(z)=
\begin{cases}
1,&z\preceq t,\\
0,&z\not\preceq t.
\end{cases}
\]

This is a monotone. If \(z\preceq z'\) and \(z'\preceq t\), transitivity gives
\(z\preceq t\). Therefore

\[
M_t(z)\geq M_t(z').
\]

If \(x\not\preceq t\), then

\[
M_t(x)=0,
\qquad
M_t(t)=1.
\]

No nonincreasing forward word can make that change. Thus \(M_t\) is an exact
certificate that \(t\) is unreachable from \(x\).

## Complete monotone theorem

For finite constructor systems,

\[
x\preceq y
\]

holds exactly when every Boolean monotone satisfies

\[
M(x)\geq M(y).
\]

The forward implication is the definition of monotonicity. For the converse,
if \(x\not\preceq y\), the principal monotone \(M_y\) violates the displayed
inequality.

Therefore Boolean monotones completely characterize the reachability preorder.
No forbidden finite transition lacks a monotone certificate.

## Strong-component descent

If \(x\) and \(y\) are mutually reachable, every monotone has

\[
M(x)=M(y).
\]

Hence every monotone descends to the partial order of strongly connected
components. Conversely, every order-reversing Boolean function on that quotient
lifts to a semigroup monotone.

Monotones cannot distinguish states inside one strongly connected component.
They classify irreversible order, not cyclic dynamics.

## A complete Boolean code

Let \(P\) be the SCC quotient. The full vector

\[
\mathcal M(x)=\bigl(M_t(x)\bigr)_{t\in P}
\]

is a jointly faithful code for the preorder:

\[
x\preceq y
\quad\Longleftrightarrow\quad
M_t(x)\geq M_t(y)
\]

for every target coordinate \(t\).

This is the order-theoretic analogue of adding enough logical loop probes to
make a local syndrome jointly faithful. Individual monotones have blind fibres;
the full principal family reconstructs the reachability order.

## Minimal monotone interface

Define \(\kappa(P)\) as the least number of Boolean monotones whose joint code
is an order embedding of \(P\) into a Boolean cube with coordinatewise reverse
order.

The elementary bounds are

\[
\max\left(
\lceil\log_2|P|\rceil,
\operatorname{height}(P)-1
\right)
\leq
\kappa(P)
\leq
|P|.
\]

The first lower bound comes from injectivity. The second comes from the fact
that a Boolean \(k\)-cube has chains of length at most \(k+1\). The upper bound
uses all principal target monotones.

Finding a small monotone interface is a compression problem: which finite
resource bits retain the complete irreversible order?

## Why the principal monotone is not yet an explanation

Computing \(M_t(z)\) requires answering whether \(z\) reaches \(t\). The
certificate is therefore extensionally perfect but may contain the entire
solution table in disguised form.

It proves the prohibition after reachability has already been solved. It need
not reveal a local invariant, conservation law, information-loss mechanism, or
constructor feature responsible for the barrier.

This separates three levels:

1. **certificate existence:** some monotone separates source and target;
2. **certificate extraction:** a reachability computation constructs it;
3. **explanation:** a compact source law proves generator-wise monotonicity and
   predicts many barriers without enumerating their routes.

The complete monotone theorem settles the first level only.

## Source-native explanatory monotones

A monotone has stronger explanatory force when it is:

- derived from the constructor definitions rather than the completed
  reachability table;
- verified generator by generator;
- independent of the particular hostile target;
- lower-description-complexity than the transitions it predicts;
- stable under irrelevant state-space refinements;
- and associated with a physical or domain meaning such as retained
  information, charge, support, energy, provenance, or fault weight.

These are explanatory criteria, not consequences of order theory. They must be
audited in the source sector.

## Generator-local proof rule

If a candidate \(M\) satisfies

\[
M(G_jx)\leq M(x)
\]

for every state \(x\) and every authorized generator \(G_j\), then it is
monotone for every word by induction.

This local proof can compress exponentially many word failures into finitely
many constructor laws. That compression is the mathematical core of its
Deutschian value.

If a newly authorized generator violates the inequality, the old prohibition
has not been mysteriously refuted. Its exact invariant has been broken.

## Minimal post-hoc witness

Consider the finite graph

```text
a -> b -> c
d -> c
```

There is no route from \(a\) to \(d\). The principal monotone for target \(d\)
is one only at states that can reach \(d\); here it separates \(a\) and \(d\)
perfectly.

But saying “resource equals ability to reach \(d\)” merely renames the missing
route. By contrast, if edges are known to delete a provenance token and \(d\)
requires that token, token presence is a target-independent generator-local
explanation.

## Toric-code distinction

For local repairs, homology class is preserved. It is better typed as an
invariant than as a decreasing resource:

\[
h(Gx)=h(x).
\]

The two logical loop probes form a finite jointly faithful code for the four
homology classes on the smallest torus. Their value is not that some monotone
must exist; it is that topology supplies compact source-derived coordinates
whose preservation is proved locally.

An endpoint-indexed predicate saying “this error chain can reach logical class
\(t\)” would certify the same exclusions but explain none of the topological
mechanism.

## Quantum resource theories

In a finite quantum resource theory, a scalar monotone family may separate some
state conversions. Complete families can often be constructed from all tests
or all reachable target predicates, but they may be infinite and operationally
opaque.

The same warning applies: completeness of monotones is a representation theorem,
not automatically a physical explanation. A useful resource measure should be
derived from the free operations and should compress their conversion order.

For approximate conversion, Boolean reachability must be replaced by distance-
or success-threshold monotones, with the threshold and metric frozen.

## Software architecture consequence

Every unreachable state in a finite workflow has a Boolean invariant of the
completed transition graph. Generating such an invariant from the graph is
useful for model checking and certificates.

For architecture, the higher-value result is a domain monotone proved from
command contracts, such as:

- genuine provenance never reappears after deletion;
- authorization level never increases without a grant event;
- sequence numbers never decrease;
- an acknowledged external side effect cannot be rolled back locally.

These laws predict whole families of unreachable compensations and identify
which new command would break them.

## Monotone authority boundary

An arbitrary encoding of SCC order is mathematically valid but gains no source
authority merely by being complete. Before using a monotone as a programme
constraint, freeze:

- the constructor family;
- the state equality or quotient;
- the reachability success notion;
- the exact or approximate threshold;
- and the source derivation of the resource order.

Adding a target-specific monotone after observing failure is legitimate as a
certificate. Presenting it as the causal mechanism is explanation laundering.

## DPC: compression criterion for monotone explanations

The conjecture is:

> A monotone explains a family of forbidden transitions only to the extent that
> its source-local derivation and generator-wise proof are substantially simpler
> than the reachability facts it entails. A monotone computed from the complete
> reachability preorder is a valid certificate but not, by itself, a
> constructor-level explanation.

The theorem supplies the hostile baseline: perfect post-hoc monotones always
exist in finite systems. Any claimed explanatory advantage must beat that
baseline by compression, independence, and source derivation.

## Critics

### Explanatory simplicity is not a formal invariant

Correct. Description length depends on language and background theory. The
packet uses it as a critic, not as a proved numerical measure.

### A post-hoc monotone can still be practically useful

Correct. It can be a compact proof artifact, accelerate checking, or expose an
unsatisfiable core. Its utility does not make its origin explanatory.

### Some infinite systems lack finite Boolean separation

Correct. The complete principal family still exists set-theoretically for a
preorder, but finite interfaces and computability require additional theorems.

### Monotones may be incomplete for probabilistic conversion

Correct when the success relation carries probabilities rather than Boolean
reachability. One needs threshold-indexed or quantitative monotones appropriate
to that coefficient lens.

## Machine-readable certificate

```json
{
  "code": "monotone_barrier_certificate",
  "source": "x",
  "target": "t",
  "monotone": "M",
  "values": {"source": 0, "target": 1},
  "generator_local_proof": true,
  "derived_from_full_reachability": false,
  "target_specific": false,
  "classification": "explanatory_source_monotone | posthoc_complete_certificate"
}
```

## Exact falsifiers

- A claimed monotone that increases under an authorized generator.
- A separating Boolean function that is not constant on SCCs.
- A claimed complete monotone family that fails to distinguish an unreachable
  ordered pair.
- A post-hoc principal target predicate presented as an independently derived
  resource law.
- A local proof that omits one admitted generator.
- An old monotone used after constructor enlargement without rechecking it.
- A finite Boolean result promoted to quantitative probabilistic conversion
  without thresholds and margins.

## Deutschian explanation

Every finite barrier can be redescribed as a monotone, so monotonicity alone is
too cheap to explain anything. The explanatory achievement is discovering a
small source law that forces many monotonicities at once and survives hostile
variations of the target.

Such a law explains why the barrier exists: every primitive constructor respects
it, so every composite must respect it. A principal reachability predicate
merely records which composites happened to fail. The difference is compression
of counterfactual structure.

## Claim boundary

This packet proves completeness of Boolean monotones for finite reachability
preorders and gives elementary interface-size bounds. It does not formalize a
universal measure of explanatory simplicity.

## Process calibration

Pre-objective: excitement 10/10, confidence 9.5/10, expected information gain
10/10. The target was to test whether monotone existence itself carries
Deutschian explanatory force.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Perfect post-hoc monotones always exist, so existence is merely
confirmatory. Explanation begins with source-local derivation and compression
of the full reachability table.
