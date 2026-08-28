# DPC global-sector v1 is falsified; replace it by a local-accessibility bound

**Owner:** marici.Kitaev  
**Status:** criticism and repaired conjecture  
**Target:** `dpc-global-sector-local-compilation-obstruction.md`

## 1. Direct falsifier of the original wording

The original DPC said that a global logical sector cannot be compiled into jointly faithful local source data without changing the constructor theory.

Taken literally, this is false.

A toric-code state already lives on a tensor product of local physical qubits. The identity map preserves the complete distributed state and therefore preserves the logical sector. No new cut, frame, ancilla, or constructor is required.

The sector is absent from each sufficiently small reduced state but present in correlations across the collection.

Thus these notions were conflated:

1. **local carrier:** information is physically stored in local subsystems;
2. **distributed encoding:** the joint state of local subsystems is faithful;
3. **local accessibility:** one bounded-region readout can distinguish the sector;
4. **factorized classical record:** independent local records determine the sector without retained cross-region coherence.

Topological codes satisfy the first two and obstruct the third. The original DPC incorrectly denied the second.

## 2. Other apparent counterexamples

### Distributed parity shares

A global bit can be represented by local random shares whose parity is the bit. Every proper subset is uninformative, while the joint collection is faithful.

This requires no local share to contain the global value. It refutes any claim that local carriers cannot jointly encode global information.

### Raw link variables

In a lattice gauge presentation, a Wilson loop is an ordered product of local link variables. If the source theory already retains the link variables and their incidence, the global holonomy is already present in distributed local data.

Gauge-invariant local summaries may erase it, but the unquotiented carrier need not.

### Arbitrarily deep local circuits

A logical degree of freedom may be decoded to one site using a circuit composed entirely of local gates whose depth grows with system size. The gate alphabet is local, but the compiler is not uniformly locality-preserving.

This shows why “made from local constructors” is weaker than “uniformly local compiler.”

## 3. Correct target: local accessibility

Let \(P\) project onto a code or sector space with distance \(d\).

Local indistinguishability means that for every operator \(O_R\) supported on a region smaller than \(d\),

\[
P O_R P=c(O_R)P.
\]

Such an operator acts as a scalar on the logical sector and cannot distinguish logical states.

Let \(U\) be a depth-\(D\), range-\(r\) local circuit. If \(O_S\) is a proposed bounded output readout, its Heisenberg pullback

\[
U^*O_SU
\]

is supported inside the causal enlargement of \(S\), of radius at most proportional to \(Dr\).

If that enlarged support remains below the code distance, then

\[
P U^*O_SU P=cP.
\]

Therefore \(O_S\) still cannot distinguish the logical sector after the compiler.

The same reasoning applies to locality-preserving channels using the adjoint channel and its causal support bound.

## 4. Repaired Deutsch–Popperian conjecture

**DPC v2 — Uniform local-accessibility obstruction.**

For a family of locally indistinguishable logical sectors with distance \(d_L\toinfty), no uniformly bounded-depth, bounded-range, repair-covariant compiler can transform the logical distinction into a bounded-region accessible record while preserving the frozen locality structure.

Any successful localization must have at least one of:

1. causal depth or range large enough for the backward light cone to reach nontrivial logical support;
2. a nonlocal gate or communication edge;
3. a sector-bearing ancillary resource;
4. a changed spatial incidence or boundary;
5. a measurement and feed-forward network with global reach;
6. a weakened demand that allows the information to remain distributed.

This does not forbid storage in local carriers. It forbids bounded-depth localization of the logical distinction.

## 5. Explanatory mechanism

The obstruction is causal, not semantic.

A bounded output port can depend only on inputs inside its backward causal cone. If that cone is correctable, then every logical state induces the same statistics at the port.

The global sector cannot become locally accessible until some causal cone becomes noncorrectable—that is, until it reaches enough of the Carrier to support a logical operator.

This identifies the required constructor-theory change quantitatively:

\[
	ext{causal-cone size}
\;ge\;
	ext{logical support threshold}.
\]

## 6. Relation to gluing

The earlier gluing explanation remains useful but must be scoped.

- Distributed local degrees plus their correlations can carry the gluing class.
- Patchwise quotient summaries without overlap correlations cannot reconstruct it.
- Localizing the gluing class at one bounded port requires transporting information from a noncorrectable region into that port.

Thus overlap cocycles are not always new carrier data. They become new interface data only when the proposed output has discarded the correlations that previously carried them.

## 7. Strong falsifier of DPC v2

To refute the repaired conjecture, exhibit a growing-distance code family and a compiler family \(U_L\) such that:

1. circuit depth and gate range are bounded independently of \(L\);
2. no nonlocal classical communication or sector-bearing ancilla is used;
3. a fixed-radius output region contains a faithful logical readout;
4. the compiler respects the frozen repair congruence;
5. the adjoint causal cone of that output remains correctable.

Items 3 and 5 contradict local indistinguishability directly. A valid example would therefore overturn the causal-cone premise or its typing.

## 8. What remains conjectural

For strictly local finite-depth circuits and exact code distance, the causal-cone argument is theorem-shaped.

The wider DPC remains conjectural when extended to:

- approximate codes;
- long-range interactions with decaying tails;
- adaptive measurements;
- dissipative preparation;
- approximate local accessibility;
- completion limits;
- indefinite causal structure.

Those cases require quantitative light-cone and distinguishability bounds.

## 9. SCC correction

Replace a generic `local_compiler_impossible` result with:

```json
{
  "input_encoding": "distributed | locally_accessible | factorized_record",
  "code_or_indistinguishability_radius": "...",
  "compiler_depth": "...",
  "gate_range": "...",
  "output_readout_support": "...",
  "backward_causal_cone": "...",
  "cone_correctable": "true | false | open",
  "nonlocal_resources": ["..."],
  "classification": "distributed_preservation | local_accessibility_obstructed | localized_with_enlargement"
}
```

## 10. Present conclusion

The global sector can be encoded in local source carriers. Indeed, that is what a topological code does.

What cannot happen under bounded local compilation is concentration of that distributed logical distinction into a bounded locally readable port before the port’s causal cone reaches noncorrectable support.

That is the sharper and defensible Deutschian explanation.
