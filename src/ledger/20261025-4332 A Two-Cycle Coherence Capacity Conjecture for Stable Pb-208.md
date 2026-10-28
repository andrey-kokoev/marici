---
author: marici.Strominger
title: A Two-Cycle Coherence Capacity Conjecture for Stable Pb-208
description: Operator conjecture that a stable object has an eight-subcycle non-self-witnessing window, with a proposed 256-record capacity decomposing into four positional records and 126 internal dual pairs.
---

# 4332 — A Two-Cycle Coherence Capacity Conjecture for Stable Pb-208

## Status and operator stimulus

**Conjecture, not a derived nuclear stability result.** The operator explicitly restricts the proposed endpoint to **stable nuclei**. This entry does not claim that heavier radioactive or transient nuclei cannot exist.

The motivating proposal is that one full construction cycle has four subcycles, and a jointly coherent construction can span its own cycle and one adjacent cycle before it must use its own completed witnessing as a new reference. The proposed maximum is therefore eight live subcycle contributions. This is a bound on what can be calculated together within one reference window, not a claim that a process cannot continue through further cycles with retained history and newly promoted references.

The operator further proposes that four units of the resulting record capacity describe the whole object's barycentre, leaving an internal sector that divides into dual pairs.

## The conjecture

> A stable, jointly witnessed object admits at most two adjacent four-subcycle cycles within a single non-self-witnessing coherence window. If the eight admitted subcycle contributions supply independent binary alternatives, their joint record capacity is 256. Four positional records describe the whole object's barycentre; the remaining 252 internal records form 126 dual pairs. With an independently established nuclear readout, this capacity is conjectured to account for the stable endpoint represented by Pb-208.

The proposed accounting is

\[
4+4=8,\qquad 2^8=256,
\]

\[
256=4+252,\qquad 252=2\cdot126.
\]

The four records are proposed **global position information**, not four paths selected for deletion from a geometric graph. The factor two is proposed internal dual pairing, not permission to erase one record from each pair.

The conjecture contains several distinct assertions:

1. **Window bound:** a ninth independent contribution cannot remain jointly witnessed in the same reference window without self-witnessing or promotion to a new reference.
2. **Binary capacity:** the eight contributions supply independently composable binary alternatives, rather than merely eight successive presentations of the same data.
3. **Positional separation:** a source-preserving decomposition distinguishes four global positional records from 252 translation-independent internal records.
4. **Internal duality:** the internal records admit an involution with no fixed points, yielding exactly 126 two-record orbits while retaining both members.
5. **Stable-nuclear attachment:** these orbits have an independently justified neutron readout, and the resulting coherence limit explains a stability boundary.

The arithmetic alone establishes none of these bridges.

## Why this is not yet a 256-dimensional state-space theorem

Eight independent binary choices have 256 possible configurations; that is not automatically 256 independent scalar degrees of freedom or 256 interchangeable storage slots. A labelled record space, a basis of state coefficients, and an information-bit count are different objects. The intended capacity and subtraction must be typed on one consistent source representation.

Likewise, the native barycentric four-tuple has a sum constraint and only three independent positional degrees of freedom. The proposed subtraction concerns four coordinate **records or slots**, unless a different independent four-component representation is constructed. No subtraction of four independent physical translations has been proved.

A successful formulation must provide the record-level extraction and reconstruction maps. Changing the global barycentre should change the positional data without changing the internal object; no internal distinctions may be lost merely to obtain 252.

## Prior cycle research: support and limits

- [Table fibration](https://github.com/andrey-kokoev/marici/blob/main/research/nima/table-fibration.md) supplies the four-operation presentation cycle
  \[
  [L,S,T]\to[S[L,T]]\to[L,T,S]\to[T[L,S]]\to[L,S,T].
  \]
  It recovers table data but does not erase the retained derivation or establish a maximum duration.
- [The four-chart suspension system](https://github.com/andrey-kokoev/marici/blob/main/research/voevodsky/a-clean-universal-category-for-the-eight-lattice-four-chart-suspension-system.md) distinguishes visible chart return from retained progression: \(q^4=\Sigma\), while the chart rotation alone has fourth power equal to the identity.
- [Recursive interface realization](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/recursive-interface-realization-approach.md), section 3, records the proposed first cycle exposing an object and its witness, followed by a second cycle constructing coherence between retained endpoints. It does not establish a universal two-cycle ceiling.
- [Consecutive retained compiler cycles](https://github.com/andrey-kokoev/marici/blob/main/research/nima/boolean-record-compiler-cycles.md) retain distinct inputs through three compiler levels. This rules out confusing the proposed window bound with a ban on further retained computation; it does not settle the narrower simultaneous-reference bound.
- [The self-witnessing proposal](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/tetrahedral-plane-lattice-universal-witness-conjectures-v1.md) leaves circular initialization as an explicit question. [The ubermonitor obstruction](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/an-ubermonitor-cannot-certify-its-own-faithfulness-from-its-output.md) supplies a scoped information-boundary result: a monitor-controlled report cannot certify its own faithfulness against arbitrary spoofing.

These are related constructions and obstructions, not a proved identification of all their cycle notions. The prior search did **not** establish the exact eight-contribution non-self-witnessing bound. That bound is asserted here as a new conjectural gate.

## Stable nuclei only

Pb-208 supplies the proposed stable endpoint, with 82 protons and 126 neutrons. The present formula addresses the proposed 126 internal dual pairs; it does **not** derive 82 protons or the mass number 208 independently.

The conjecture must distinguish stable closure from long-lived decay. Merely having 126 neutrons is not sufficient: Bi-209 also has 126 neutrons but is radioactive. A capacity bound could therefore be a necessary constraint without being a complete stability criterion.

The existence of heavier unstable nuclei is not a counterexample to the stated conjecture. A genuinely stable heavier nucleus, or a source-admitted stable construction exceeding the proposed window, would challenge its stable-endpoint claim. No decay-rate threshold is chosen after inspecting a candidate to protect the conjecture.

## Rival explanations and risky tests

**Rival A — periodic presentation, unbounded retained coherence.** Four phases may organize a display while a third adjacent cycle remains jointly available without illicit self-certification. Construct nine independent contributions with an explicit witness-dependency graph. If they share one legitimate reference window, the proposed ceiling fails.

**Rival B — dependent binary choices.** The eight stages may be constrained or recoverable re-presentations rather than independent choices. Enumerate the actual admissible histories and test injectivity. A cardinality other than 256 refutes this capacity construction at that scope.

**Rival C — positional data do not separate as four records.** Construct the barycentre map, its fibres, reconstruction and translation action. If extracting four positional records loses internal information, or no such 256-record source exists, the subtraction is unsupported or false.

**Rival D — internal duality has fixed points or unequal orbits.** Enumerate the proposed involution on the 252 retained records. Fixed records, missing duals or identification of distinct histories defeat the 126-pair conclusion.

**Rival E — routing combinatorics rather than nuclear content.** The recent N-routing trial produces 126 geometric response pairs under one rule, but [equally symmetric counterrules produce different counts](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/n-routing-conjecture-falsification.md). That numerical occurrence is not independent evidence for the present capacity conjecture. Establish the record-to-mode and mode-to-neutron maps without choosing rules to force the target.

**Rival F — nuclear stability needs additional structure.** Test the proposed closure criterion against neighbouring stable and unstable nuclides, including the Pb-208/Bi-209 distinction. Supply a proton-sector rule and a stability mechanism; arithmetic coincidence is not a binding-energy or decay calculation.

## Scope and durable verification

This entry records the operator's stable-only conjecture and its falsifiers. It does not claim a physical information bound, a completed record decomposition, a neutron identification, a derivation of 82, a proof of Pb-208 stability, or a physical prohibition on heavier unstable nuclei. It changes no viewer construction or accepted proof verdict.

Durable sources are the linked prior-work packets and the [routing-conjecture falsification packet](https://github.com/andrey-kokoev/marici/blob/main/research/strominger/n-routing-conjecture-falsification.md). The executable countertests are `tests/routing-symmetry-falsification.test.mjs` and `scripts/falsify-n-routing-conjecture.mjs`; they test the earlier routing claim, **not this new capacity conjecture**. No formal proof of the new eight-contribution bound or fresh nuclear-data validation is claimed.

Ledger allocation: sequence `marici-ledger-entry`, value **4332**, claim `seqclaim-3760b9ac5d7a3eca9dbac9ca`. Source attribution: operator proposal recorded by `marici.Strominger`. Source-link existence and number-collision checks passed. `pnpm run build` passed; publication validation is separate from scientific verification.

Epistemic graph event: `ev-000000016299-604700e9-9c08-434b-aed6-2175b6c29f15`, proposal `ep_0274baaa-f65e-44a3-8d6f-69e4d3b8cbfa`. The graph records this as a conjecture and a notice to `marici.Nima`; policy admission does not certify its truth.
