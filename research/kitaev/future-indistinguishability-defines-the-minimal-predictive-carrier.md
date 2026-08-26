# Future indistinguishability defines the minimal predictive carrier

## Bounded question

Which distinctions created by past interaction must closure retain as source
data for every authorized future operation, and which distinctions may be
quotiented away without predictive loss?

## Frozen deterministic constructor system

Let \(X\) be a finite state set. Let \(\Sigma\) be a finite alphabet of
source-authorized constructors

\[
G_a:X\to X,
\qquad a\in\Sigma,
\]

and let

\[
r:X\to Y
\]

be the frozen observable readout. A word \(w=a_k\cdots a_1\) acts by the
ordered composite \(G_w\). The empty word is admitted.

The data packet \((X,\Sigma,G,r)\) defines what “future consequence” means.
Changing the constructor alphabet or readout changes the quotient problem.

## Future-indistinguishability relation

Define

\[
x\equiv_r y
\quad\Longleftrightarrow\quad
r(G_wx)=r(G_wy)
\]

for every authorized word \(w\).

Two states are equivalent exactly when no allowed future intervention followed
by the declared readout can distinguish them.

This is stronger than equality of the present readout. States can satisfy

\[
r(x)=r(y)
\]

while a future constructor exposes their difference.

## Constructor-congruence theorem

The relation \(\equiv_r\) is an equivalence relation and a forward constructor
congruence:

\[
x\equiv_r y
\quad\Longrightarrow\quad
G_ax\equiv_r G_ay
\]

for every \(a\in\Sigma\).

Indeed, for every continuation word \(w\),

\[
r(G_wG_ax)=r(G_{wa}x)=r(G_{wa}y)=r(G_wG_ay).
\]

The readout is constant on equivalence classes because the empty word is
included. Therefore both constructors and readout descend to the quotient

\[
X_{\min}=X/{\equiv_r}.
\]

This quotient is a closed predictive carrier: every authorized future word can
be evaluated on it without choosing a representative.

## Minimal predictive-carrier theorem

Suppose another quotient

\[
q:X\to Q
\]

supports descended constructors and readout:

\[
qG_a=\bar G_aq,
\qquad
r=\bar r q.
\]

If \(q(x)=q(y)\), induction on word length gives

\[
r(G_wx)=r(G_wy)
\]

for every \(w\). Hence

\[
q(x)=q(y)
\quad\Longrightarrow\quad
x\equiv_r y.
\]

So every predictive quotient must distinguish at least the classes of
\(X_{\min}\). The future-indistinguishability quotient is the unique minimal
deterministic carrier up to isomorphism.

“Minimal” here means fewest carrier states compatible with every declared
counterfactual readout, not minimal physical energy or implementation cost.

## Finite partition refinement

Define relations \(\equiv_k\) recursively. First,

\[
x\equiv_0y
\quad\Longleftrightarrow\quad
r(x)=r(y).
\]

Then

\[
x\equiv_{k+1}y
\]

when \(x\equiv_0y\) and

\[
G_ax\equiv_kG_ay
\]

for every generator \(a\).

Induction shows

\[
x\equiv_ky
\quad\Longleftrightarrow\quad
r(G_wx)=r(G_wy)
\]

for every word of length at most \(k\).

The partitions refine monotonically and stabilize after at most \(|X|-1\)
strict splits. At stabilization they equal \(\equiv_r\).

## First distinguishing word

If \(x\equiv_{k-1}y\) but

\[
x\not\equiv_ky,
\]

then the shortest authorized word distinguishing them has length \(k\).

Thus “first” is defined by constructor word length and the frozen generator
alphabet. The partition refinement not only finds the minimal carrier; it
produces a shortest contextual witness for every split.

This is the deterministic analogue of the shortest loop-probe or observation
word that resolves a hidden sector.

## Closure criterion for historical distinctions

Suppose an interaction produces two possible post-interaction states \(x\) and
\(y\).

- If \(x\equiv_r y\), closure may merge them without affecting any declared
  future readout.
- If \(x\not\equiv_r y\), erasing their distinction destroys at least one
  authorized counterfactual prediction. The shortest distinguishing word is the
  exact lost capability witness.

Therefore real-world interaction is not automatically retained in full.
Closure retains precisely the distinctions required by the declared future
constructor/readout packet.

Audit, provenance, safety, or later expansion may require additional readouts.
Those requirements refine \(\equiv_r\); they cannot be inferred from present
operational output alone.

## Present shadow versus predictive state

The present-readout quotient identifies states only by \(r(x)\). It can be
strictly coarser than \(X_{\min}\).

The gap consists of latent distinctions that are presently silent but become
observable after some constructor word. This is exactly the crossed-polarizer
pattern in deterministic form: an intermediate context can convert a hidden
state distinction into a visible endpoint difference.

Consequently, a scalar completed section is a sufficient state description
only if its kernel is invariant under every authorized future constructor. If
not, the section is a diagnostic shadow rather than a predictive realization.

## Small deterministic witness

Let

\[
X=\{x,y,u,v},
\qquad
r(x)=r(y)=0,
\qquad
r(u)=0,
\qquad
r(v)=1.
\]

For one constructor \(G\), set

\[
Gx=u,
\qquad
Gy=v.
\]

The states \(x\) and \(y\) have the same present output but are distinguished
by the one-letter word \(G\). Any carrier retaining only present readout merges
them incorrectly. The minimal predictive carrier must retain their latent bit.

## Toric-code instance

Take Pauli error configurations as states, authorized local Pauli repairs as
constructors, and local syndrome as readout. Error configurations differing by
a noncontractible logical loop have the same local syndrome. Applying the same
local repair word preserves that logical difference, so syndrome-only future
readout continues to merge the logical sectors.

Adding two noncontractible loop probes to the readout refines the initial
partition and separates the four logical classes on the smallest torus. The
Carrier geometry supplies the cycles and local repair action; the quantum
coefficient lens supplies Pauli commutation and the operational probe algebra.

The logical data were not created by the extra readouts. They were latent
distinctions in the full state packet that the syndrome quotient erased.

## Software architecture instance

Two service states may return the same REST representation now yet respond
differently to a future command because one retains an authorization grant,
idempotency token, causal predecessor, or unsent event.

If future command behavior differs, those states cannot be merged in a
predictive domain model. A cache or projection containing only the present API
response is a diagnostic shadow.

Conversely, historical fields that affect no admitted future command or readout
may be removed from the operational carrier. If audit later becomes an admitted
readout, the quotient must be refined or the historical port retained
separately.

## Relation to event sourcing

An append-only event history is generally larger than the minimal predictive
carrier. Folding the history into state is sound when every future command and
readout factors through that state.

Two histories may be compacted together exactly when all admitted future words
produce identical outputs from their folded states. If legal audit requires
distinguishing the histories themselves, audit is an additional readout and the
equivalence becomes finer.

Thus event retention and operational state minimization answer different
questions. Closure must not use one as authority for the other.

## Weighted, stochastic, and quantum extensions

For stochastic or quantum processes, equality of one deterministic output is
replaced by equality of every future probability functional:

\[
p(f|w,x)=p(f|w,y)
\]

for all admitted continuations and tests.

The resulting predictive equivalence remains valid, but the minimal realization
need not be a finite set quotient. Its linear dimension is controlled by the
causal Hankel rank; positive classical and quantum realizations are controlled
by nonnegative and PSD factorizations.

This is the coefficient-lens transition:

- deterministic lens: finite congruence classes;
- additive probabilistic lens: linear Hankel state;
- positive quantum lens: operator-valued memory;
- ordered noncommutative lens: comb or process realization.

The shared Carrier question is unchanged: which past distinctions can some
authorized future context expose?

## Minimality is not explanation

The quotient can be computed by exhaustively refining future behavior. Like the
principal monotone, that establishes an exact minimal representation but may
not explain why its classes have a compact source description.

A stronger explanation supplies invariants, charges, homology, types, or domain
contracts whose local constructor laws generate the same partition without
enumerating every word.

Minimal predictive realization and Deutschian explanation are complementary:

- minimization removes distinctions with no admitted consequence;
- explanation compresses the distinctions that remain into source laws.

## DPC: predictive closure conjecture

The conjecture is:

> A closed source carrier should retain exactly those interaction distinctions
> that some source-authorized future constructor and readout can distinguish,
> plus any independently mandated audit or safety coordinates. Retaining less
> loses counterfactual capability; retaining more may be legitimate history but
> is not forced by predictive closure.

The finite deterministic theorem proves the predictive part. The conjectural
boundary is identifying the complete authorized future tester family and the
independent nonpredictive retention obligations.

## Critics

### Future constructor families can change

Correct. Minimality is relative to the frozen alphabet and readout. A later
enlargement can expose distinctions previously safe to merge. Extensibility may
justify a deliberately richer carrier.

### Equal output probabilities do not imply equal post-test states

Correct. The future family must include all later interventions whose state
updates matter. A terminal tester family cannot certify process equivalence for
unopened slots.

### Audit data may be predictively inert but legally mandatory

Correct. Audit is an independently authorized readout/retention purpose and
must be typed separately.

### Minimal finite state can be computationally expensive to find

Correct. The theorem establishes the target quotient and bounded refinement;
large state spaces need symbolic abstraction.

## Machine-readable witness

```json
{
  "code": "predictive_carrier_distinction_required",
  "states": ["x", "y"],
  "present_readout_equal": true,
  "shortest_distinguishing_word": ["a1", "...", "ak"],
  "future_readouts": ["r(G_w x)", "r(G_w y)"],
  "word_length": "k",
  "constructor_family_version": "frozen id",
  "extra_retention_basis": "audit | safety | null"
}
```

## Exact falsifiers

- Two states merged despite an authorized future word distinguishing them.
- A claimed minimal quotient with two distinct classes having identical future
  readouts for every word.
- A descended constructor whose result depends on the chosen representative.
- A shortest distinguishing word contradicted by a shorter one.
- Present readout equality presented as full predictive equivalence.
- A quotient retained after enlarging constructors without rerunning refinement.
- Audit retention presented as forced by operational prediction without typing
  audit as a readout.
- A deterministic quotient theorem applied directly to quantum post-measurement
  states without the probability/process extension.

## Deutschian explanation

A latent state distinction is real for the programme when some authorized
future context can make it matter. The shortest distinguishing word explains
how the distinction becomes visible; constructor congruence explains why every
other merged distinction remains forever silent.

The minimal predictive carrier is therefore neither the full past nor the
current scalar output. It is the quotient of the past by all distinctions that
no admitted future can expose. Source laws such as homology or provenance then
explain the structure of the surviving classes.

## Claim boundary

This packet proves the finite deterministic future-equivalence and minimality
theorems. It sketches, but does not reprove, stochastic Hankel and quantum comb
realization theory.

## Process calibration

Pre-objective: excitement 10/10, confidence 9.5/10, expected information gain
10/10. The target was an exact answer to which interaction records closure must
retain.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Future indistinguishability is the minimal predictive quotient, and
partition refinement supplies shortest contextual witnesses. Closure retains
counterfactually exposable distinctions, while audit and extensibility remain
separate authority layers.
