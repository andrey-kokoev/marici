# Full behavior is a dependent bundle, not a flat product

**Owner:** marici.Kitaev  
**Status:** bounded research packet  
**Question:** What behavior object must the top distributive coherencer preserve?

## 1. Flat products admit impossible states

A tempting signature is

\[
B_{mathrm{flat}}
=
B_{mathrm{out}}
\times B_{mathrm{authority}}
\times B_{mathrm{resource}}
\times B_{mathrm{fault}}
\times B_{mathrm{reset}}.
\]

This records all named coordinates, but it also admits arbitrary combinations of them.

Many such combinations are not source-admissible:

- an executable action with no current authority;
- a successful output after the required resource was consumed elsewhere;
- a reset successor incompatible with the reported waste;
- a nominal result whose fault branch has no common underlying transition;
- a completion state whose coordinate limits come from incompatible subsequences.

The missing information is incidence between coordinates.

## 2. Minimal finite hostile

Let a behavior packet contain two bits:

- authority \(a\in\{0,1\}\);
- executable action \(u\in\{0,1\}\).

Admissibility requires

\[
u\le a.
\]

Thus

\[
E=\{(0,0),(1,0),(1,1)\}
\subsetneq
\{0,1\}\times\{0,1\}.
\]

Suppose a binary source constructor combines authority by exclusive-or and executable action by inclusive-or:

\[
a_{mathrm{out}}=a_1\oplus a_2,
\qquad
u_{mathrm{out}}=u_1\lor u_2.
\]

Each coordinate operation is a perfectly typed Boolean map.

But two admissible inputs

\[
(a_1,u_1)=(1,1),
\qquad
(a_2,u_2)=(1,0)
\]

produce

\[
(a_{mathrm{out}},u_{mathrm{out}})=(0,1),
\]

which is outside \(E\).

Therefore componentwise coherence does not imply joint behavioral coherence.

The first failed law is preservation of the incidence predicate.

## 3. Dependent behavior signature

Let \(Q\) carry authority, resource, domain, and other indexing data. For each \(q\in Q\), let \(B_q(X)\) be the behaviors admissible under that index.

The total behavior object is a dependent sum

\[
B(X)=\sum_{q\in Q}B_q(X),
\]

or equivalently the total category of a fibration over \(Q\).

Outputs, faults, resets, and successor states live in fibers determined by the current resource and authority index. A constructor may move between fibers, but that movement must be explicit.

The mixed coherencer must therefore preserve:

1. the base index transition;
2. the fiber behavior;
3. the incidence law relating them;
4. reindexing under context transport.

## 4. Joint distributive law

A component family

\[
\lambda_i:T B_i\to B_i T
\]

is insufficient.

The required cell is a lift

\[
\lambda_E:T E\to E T
\]

on the admissible total object \(E\), whose projections recover the component laws.

Equivalently, if \(E\) is defined as a subobject or pullback of the flat product, the componentwise map must land in \(E\). This is a preservation theorem, not an additional scalar equality.

For an admissibility predicate \(P\), the gate is

\[
P(x_1),\ldots,P(x_n)
\quad\Longrightarrow\quad
P(\lambda(x_1,ldots,x_n)).
\]

If source construction changes the index, the theorem must also identify the authorized target fiber.

## 5. Reindexing coherence

Contexts can change the base index through:

- authority delegation;
- resource expenditure;
- fault occurrence;
- reset;
- domain restriction;
- completion transport.

Let \(f:q\to q'\) be such a base transition. Behavior has a corresponding reindexing or transport map.

The mixed law must commute with this transport. Depending on variance and structure, the certificate may take the form of a naturality, cartesianity, or Beck–Chevalley condition.

The exact categorical name must be derived from the frozen fibration. SCC should request the square and its typing rather than presume one variance convention.

## 6. Final behavior must be final in the constrained category

A final coalgebra for the flat product can contain behavior streams that violate the joint incidence law.

The relevant final object, when it exists, is final among coalgebras in the constrained or indexed behavior category.

Only then does the earlier theorem induce source composition on semantically admissible final behaviors.

Finality in each coordinate separately does not imply joint finality.

## 7. Relation to current cross-sector work

Nima’s successor-authority, waste, fault, and domain-transport hostiles are exactly joint-incidence tests.

Strominger’s source-content versus final snake-index distinction shows how a coarse behavior projection can forget incidence needed by later construction.

Figueiredo’s shared preparation correlations likewise show that marginal behavior channels do not determine their joint source occurrence.

Kitaev’s quantum coefficient lens gives the same warning: central, block, and executable descriptions may share projections while differing in admitted joint operations.

## 8. SCC certificate extension

The behavior side should report:

```json
{
  "behavior_base": {
    "indices": ["authority", "resource", "domain", "fault_state"],
    "base_transitions": ["..."]
  },
  "behavior_fibers": {
    "signature": "...",
    "admissibility_predicate": "...",
    "total_object": "dependent_sum | pullback | subobject | other"
  },
  "component_laws": ["..."],
  "joint_incidence_preservation": "proved | failed | open",
  "reindexing_coherence": "proved | failed | open",
  "target_fiber_transport": "...",
  "joint_finality_scope": "...",
  "first_invalid_joint_packet": "..."
}
```

SCC must reject promotion from componentwise distributive laws to a joint law without the incidence-preservation certificate.

## 9. Hostile suite

1. Every projection is well typed, but the combined output violates admissibility.
2. Each coordinate law is natural, but their shared pullback square is not preserved.
3. Authority transport changes the fiber while behavior remains in the old fiber.
4. Reset repairs output but does not restore the required resource index.
5. Fault and nominal branches use incompatible underlying transitions.
6. Coordinatewise completion converges, but no joint limiting packet exists.
7. Each coordinate has a final coalgebra, but the product final object contains forbidden packets.
8. A joint repair succeeds only by adding an unauthorized index or transport.

## 10. Present conclusion

The top distributive law can self-close, but only after the behavior object has been typed correctly.

The correct target is not “all observable columns placed side by side.” It is the space of jointly admissible behavior packets together with their allowed index changes.

Thus the next explanatory principle is:

> Coherence of projections is weaker than coherence of incidence.
