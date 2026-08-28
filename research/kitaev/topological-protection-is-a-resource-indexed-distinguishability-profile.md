# Topological protection is a resource-indexed distinguishability profile

**Owner:** marici.Kitaev  
**Status:** bounded research packet  
**Question:** What does the unbudgeted tester norm erase?

## 1. Binary distinguishability is too coarse

The contextual distance

\[
d_{\mathcal C}(f,g)
=
\sup_{C\in\mathcal C}
D(C[f],C[g])
\]

answers whether the full authorized tester theory can distinguish two processes.

It does not record the resource cost of doing so.

For global logical sectors, full distinguishability often exists. Protection means that every successful distinguishing or localization context has cost growing with the Carrier.

Therefore one terminal distance erases the main phenomenon.

## 2. Resource-indexed tester families

Let

\[
w:\mathcal C\to\mathcal R
\]

assign each tester a resource cost. The resource object \(\mathcal R\) may be scalar or partially ordered and may include:

- spatial diameter;
- circuit depth;
- communication distance;
- number of device uses;
- ancillary dimension;
- entanglement supply;
- classical fan-in;
- energy;
- error tolerance;
- inverse success probability;
- authority level.

For budget \(R\), define

\[
\mathcal C_{\le R}
=
\{C:w(C)\le R\}
\]

and

\[
d_R(f,g)
=
\sup_{C\in\mathcal C_{\le R}}
D(C[f],C[g]).
\]

The family \(R\mapsto d_R(f,g)\) is the distinguishability profile.

## 3. Distinguishing threshold

For a target advantage \(\delta>0\), define

\[
R_\delta(f,g)
=
\inf\{R:d_R(f,g)\ge\delta\}.
\]

Topological protection is expressed by growth of \(R_\delta\) with system size.

For toric-code logical sectors:

- fixed-radius local budgets give zero exact distinguishing advantage;
- a noncontractible loop budget separates the sectors;
- the required spatial support grows with the code distance.

Thus the sector is not absolutely invisible. It is expensive relative to the local constructor theory.

## 4. General compiler lower bound

Let \(K\) compile a source object into an output port.

Suppose an output tester \(C_{mathrm{out}}\) of cost \(r\) distinguishes \(K(f)\) and \(K(g)\) with advantage at least \(\delta\).

By composition, \(C_{mathrm{out}}\circ K\) is a source tester. If costs compose subadditively,

\[
w(C_{mathrm{out}}\circ K)
\le
w(K)+r.
\]

Therefore

\[
d_{w(K)+r}(f,g)\ge\delta,
\]

and hence

\[
w(K)
\ge
R_\delta(f,g)-r.
\]

This is the abstract localization lower bound.

A cheap faithful output port forces the compiler itself to pay essentially the original distinguishing threshold.

## 5. Causal-cone theorem as a special case

Take resource cost to be backward causal diameter.

Below the code distance, every tester pulls back to a correctable algebra, so

\[
d_R(f,g)=0
\]

for \(R<d\), under the declared support convention.

A fixed-radius faithful output has constant readout cost \(r\). The compiler depth/range must enlarge its causal support until its total cost reaches the logical threshold.

Thus the causal-cone argument is the support-coordinate projection of the general resource profile.

## 6. Why adding a constructor changes the theory

Add a primitive noncontractible loop probe of unit cost.

The states and their abstract distinguishability do not change. But the resource assignment changes from

\[
R_\delta\sim d_L
\]

to

\[
R_\delta=O(1).
\]

Likewise:

- free global classical parity collapses communication cost;
- a sector-bearing ancilla collapses preparation cost;
- a chosen cut collapses reference-frame cost;
- postselection treated as free collapses probability cost.

The change is operationally visible as a discontinuous change in the distinguishability profile.

This is a precise meaning of “changing the constructor theory.”

## 7. Vector costs and Pareto fronts

A scalar cost can hide substitutions among resources.

A loop may be shallow but spatially extended. Teleportation may reduce depth while consuming entanglement and classical communication. Postselection may reduce deterministic depth while lowering success probability.

The honest invariant is therefore often a Pareto frontier in a resource vector:

\[
R=(	ext{depth},\text{diameter},\text{communication},\text{entanglement},\text{uses},\text{success cost}).
\]

SCC should not scalarize this vector without a source-authorized exchange rate.

## 8. Composition and network semantics

The cost assignment must be compositional:

- sequential composition has an admitted accumulation law;
- parallel composition has an admitted join or sum law;
- conditioning includes branch probability;
- reset includes restoration cost;
- imported authority and entanglement are not free;
- reuse counts each invocation unless a theorem amortizes it.

The top distributive coherencer must preserve both behavior and its resource grading.

A behaviorally commuting \(\lambda\) that changes the cost profile is not resource-coherent.

## 9. Completion

A sequence can preserve unbudgeted distance while its distinguishing threshold escapes to infinity, or preserve every bounded-budget profile while becoming distinguishable only at growing budgets.

Therefore completion should retain the entire family \(\{d_R\}\), or an equivalent resource-enriched metric, when protection scaling is part of the claim.

Collapsing to \(d_\infty\) identifies “cheaply distinguishable” and “distinguishable only at diverging cost.”

## 10. Hostile suite

1. **Free controller:** global parity is assigned unit cost despite system-wide communication.
2. **Free postselection:** vanishing success probability is omitted from cost.
3. **Free reference:** a chosen cut or phase frame is treated as notation.
4. **Free ancilla:** sector-bearing entanglement is called a trivial resource.
5. **Scalarization hostile:** two incomparable resource vectors receive the same scalar price.
6. **Amortization hostile:** reuse cost disappears without a reset or catalyst theorem.
7. **Completion hostile:** thresholds diverge while unbudgeted distance remains fixed.
8. **Mixed-law hostile:** source and behavior commute but resource grades differ along the two routes.

## 11. SCC certificate

```json
{
  "tester_category": "...",
  "resource_object": {
    "coordinates": ["depth", "diameter", "communication", "ancilla", "uses", "success"],
    "order": "...",
    "composition_law": "..."
  },
  "distinguishability_profile": "R -> d_R",
  "target_advantage": "delta",
  "distinguishing_threshold": "R_delta",
  "compiler_resource_distortion": "...",
  "pareto_front": "...",
  "unauthorized_free_resources": ["..."],
  "completion_preserves_profile": "proved | failed | open"
}
```

## 12. Present conclusion

Topological protection is not absence of a distinguishing constructor.

It is the growth law of the least resource required to realize one.

The correct top-level compiler theorem must therefore preserve a resource-indexed family of contextual distances, not only the final unbudgeted behavioral norm.
