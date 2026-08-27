# Record fanout separates deterministic transport from common-mode noise

## Bounded question

Once a commutative record can be copied, which transformations preserve its
copying structure, and what does failure to preserve that structure say about
fault location?

## Classical record object

Let \(R\) be a finite record alphabet. Define copying and deletion by

\[
\Delta_R(r)=(r,r),
\qquad
\epsilon_R(r)=*.
\]

Copying is coassociative:

\[
(\Delta_R\times\operatorname{id})\Delta_R
=
(\operatorname{id}\times\Delta_R)\Delta_R.
\]

It is cocommutative and deletion is a counit. These equations say that the
number and order of downstream copies do not alter the copied value.

This comonoid structure is the algebra of classical fanout. It is additional
structure on the carrier, not a consequence of having a set of scalar labels.

## Deterministic transport theorem

Every function

\[
f:R\longrightarrow S
\]

preserves copying and deletion:

\[
\Delta_S f=(f\times f)\Delta_R,
\qquad
\epsilon_S f=\epsilon_R.
\]

Therefore deterministic relabelling, coarse-graining, encoding, and routing
commute with fanout.

The information properties of \(f\) remain distinct:

- injectivity preserves every record distinction;
- a many-to-one map performs authorized coarse-graining;
- surjectivity says every target label is reachable;
- bijectivity gives reversible record transport.

Preservation of fanout alone does not imply faithfulness.

## Stochastic rigidity theorem

Let \(K:S\leftarrow R\) be a Markov kernel. For an input \(r\), write

\[
p_s=K(s|r).
\]

There are two composites:

\[
R\xrightarrow{K}S\xrightarrow{\Delta_S}S\times S
\]

and

\[
R\xrightarrow{\Delta_R}R\times R
\xrightarrow{K\times K}S\times S.
\]

The first has joint law

\[
p_s\delta_{st}.
\]

The second has joint law

\[
p_sp_t.
\]

Equality for all \(s,t\) requires

\[
p_s\delta_{st}=p_sp_t.
\]

For distinct \(s,t\), this forbids two positive probabilities. Normalization
then forces one probability to equal one. Hence a stochastic channel preserves
copying exactly if and only if it is deterministic on every input.

Randomness therefore does not commute through fanout. Its position relative to
copying is observable in the correlation pattern.

## Common-mode versus branch-local noise

Let \(R=\{0,1\}\), and let \(N_q\) flip a bit with probability \(q\).

If noise acts before copying,

\[
r\xrightarrow{N_q}\tilde r
\xrightarrow{\Delta}(\tilde r,\tilde r),
\]

the replicas always agree. They are jointly wrong with probability \(q\).

If copying occurs first and independent noise acts on each branch,

\[
r\xrightarrow{\Delta}(r,r)
\xrightarrow{N_q\times N_q}(r_1,r_2),
\]

the replicas disagree with probability

\[
2q(1-q).
\]

Thus an equality comparator detects some branch-local faults but no common-mode
fault inserted before fanout. The difference is not merely a reliability
heuristic. It is the failure of the stochastic channel to be a comonoid
homomorphism.

## Three-copy majority

With three independently corrupted copies, majority decoding fails when at
least two copies flip. Its failure probability is

\[
3q^2(1-q)+q^3
=
3q^2-2q^3.
\]

A single flip is corrected. By contrast, one pre-fanout flip changes all three
copies together and defeats majority with probability \(q\).

Controller redundancy therefore protects the post-fanout branches. It does not
protect the source value, the fanout constructor, or any shared transport
upstream of the replicas.

## Shared randomness is a hidden port

The product channel \(K\times K\) models independent randomness. Correlated
branch noise instead requires a common random variable \(\lambda\):

\[
K_{12}(s,t|r)
=
\sum_\lambda
\mu(\lambda)
K_1(s|r,\lambda)K_2(t|r,\lambda).
\]

Moving a random operation across fanout silently changes whether its random
seed is shared or duplicated. The seed is therefore part of the constructor
interface whenever correlation matters.

This is the record analogue of retaining an environment port. A scalar error
rate does not determine the joint fault process.

## Constructor equivalence consequence

Two pipelines may have identical single-copy marginals and different
multi-copy behavior:

\[
\Delta K
\neq
(K\times K)\Delta.
\]

They are scalar-coincident under one-output tests but not predictively
equivalent once fanout and comparison are admitted constructors.

Hence a record-processing component cannot be specified only by its marginal
input-output law when downstream consumers compare replicas. Its correlation
and seed ports belong to the frozen constructor packet.

## Toric-code controller instance

Suppose a syndrome bit is extracted once and then copied to two classical
decoder components. A wrong extraction or pre-fanout memory flip is common
mode. Both decoders receive the same wrong syndrome, so equality comparison is
silent.

Independent transmission or memory faults after fanout may create disagreement
and are detectable. Neither mechanism repairs a quantum data fault or validates
the syndrome-extraction interaction.

The fault model must therefore type at least four locations:

1. quantum data and actuator;
2. syndrome extraction;
3. classical fanout and shared source memory;
4. independent replica branches.

Collapsing them into one bit-flip probability destroys the algebra needed to
justify redundancy.

## Optical instance

A detector event amplified once and then split into several electrical records
has a shared upstream detection fault. Independent downstream electronics can
be cross-checked; a missed photon or common discriminator error cannot.

The observed agreement of several displays certifies only the post-fanout
transport, conditional on the shared detector event. It does not independently
confirm the optical interaction.

## Software instance

Producing one event and publishing it to several consumers differs from asking
each consumer to rerun a randomized computation. In the first system, an
upstream error is copied consistently. In the second, consumers may disagree.

The systems can have the same per-consumer response distribution while having
different correlation, replay, and fault-containment semantics. A shared
random seed, cached result, or source event identifier is an explicit port, not
an implementation detail.

## DPC: fanout locality of error

The conjecture is:

> Every redundancy claim must identify the fanout constructor and place each
> admitted fault before it, inside it, or after it. Marginal error rates are
> insufficient. Only post-fanout independent faults are exposed by replica
> disagreement; pre-fanout faults remain common mode unless an independent
> source observation is added.

This explains both the power and the limitation of redundancy from one
structural law: stochastic transformations do not commute with copying unless
they are deterministic.

## Critics

### Hardware copies are never perfectly independent

Correct. Independence is an assumption about the joint channel, not a
consequence of drawing separate boxes. Shared power, clock, calibration, code,
or environment introduces a common port.

### Random relabelling can be implemented deterministically with a seed

Correct. On the enlarged carrier \((r,\lambda)\), the constructor may be a
deterministic function. The theorem then identifies the seed as part of the
source state. Copying or hiding that seed determines the output correlations.

### Many-to-one functions lose information despite preserving copying

Correct. Comonoid preservation characterizes compatibility with fanout, not
injectivity. Faithfulness requires a separate kernel or fibre test.

### Quantum records need not be classical bits

Correct. The alphabet may be any finite commutative algebra. The copied
information is classical relative to that algebra even when physically
encoded in quantum hardware.

### Majority improves reliability, so upstream faults may be negligible

That is a quantitative engineering claim requiring an upstream fault bound.
Majority supplies no algebraic suppression of a perfectly correlated flip.

## Exact falsifiers

- A nondeterministic Markov kernel claimed to commute exactly with fanout.
- Replica agreement used to exclude a pre-fanout fault.
- Independent-noise formulas applied when replicas share a seed or environment.
- A many-to-one record map called faithful because it preserves copying.
- Identical single-copy marginals used to infer identical redundant-system
  behavior.
- Three-copy majority claimed to repair a common-mode source flip.
- A duplicated classical syndrome claimed to repair the quantum extraction
  interaction.

## Machine-readable fault boundary

```json
{
  "code": "record_fanout_fault_locality",
  "record_alphabet": "R",
  "fanout": "Delta",
  "transport": "K",
  "commutes_with_fanout": false,
  "deterministic_transport": false,
  "pre_fanout_fault": "common_mode",
  "post_fanout_fault": "branch_local_if_independent",
  "shared_randomness_port_typed": true,
  "marginals_sufficient": false
}
```

## Deutschian explanation

Copies agree because they inherit one history. Redundancy becomes informative
only after their histories separate. A fault before that separation is copied
as faithfully as the intended value; a fault after separation can make the
branches disagree.

The first meaningful question about a redundant system is therefore not how
many copies it has. It is where the copies acquire independent causal histories.
The fanout constructor marks that boundary.

## Claim boundary

This packet proves the finite stochastic rigidity of exact fanout preservation
and derives the binary redundancy formulas. It does not establish independence
for any physical replicas, estimate hardware fault rates, or price the added
interfaces.

## Process calibration

Pre-objective ratings were excitement 10/10, confidence 9.5/10, and expected
information gain 10/10. The target was an exact structural criterion for which
record transformations preserve fanout.

Post-objective ratings are excitement 10/10, confidence 10/10, and realized
information gain 10/10. Deterministic transport is exactly fanout-compatible,
and the placement of randomness relative to fanout determines common-mode
versus detectable branch-local failure.
