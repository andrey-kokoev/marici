# One-cycle source-contract audit

## Result

The audit did **not** produce the intended typed source-derived contract: stage outcome `+-`. It did produce a fresh Agda theorem showing why the current coherence requirements cannot define that contract. The lift itself is neither proved nor refuted.

`TickSourceContractAudit.agda` proves that for **every** external function `f : Schedule → X`, the interpretation

`interpret f t = (f (first-tag t), f (second-tag t))`

satisfies whole-record reconstruction and schedule-swap coherence. Moreover, `interpret` is injective in `f`: these laws preserve, rather than select between, arbitrary externally chosen semantics. This is true for arbitrary target type `X`, including a type of whole external path objects.

Fresh Agda closure passed. Receipt: `results/source-contract-audit.json`.

## Provenance inventory

| Ingredient | Source or added choice? |
|---|---|
| Bool pair, two factor flips, ordered schedule tags | Native source data |
| Tick reconstruction from tags | Existing source classification theorem |
| Reverse operation order and discrete return endpoints | Derived from the flips and schedule |
| Complex completion and C4 state space | Added analytic carrier; not a Tick field |
| Basis embedding of the four labels | Available once a free-vector/coordinate interpretation is chosen; that interpretation is additional structure |
| Inner product, normalization and Born readout | Additional analytic/readout structure |
| Spectral projector `(I-P)/2` | Algebraically derived from the represented flip, conditional on the chosen scalar representation |
| Phase `exp(-i*pi*t)`, branch/sign and time scale | Analytic choices not supplied by the two schedule tags |
| External interval/chart domain and its topology | Chosen interpretation interface, not Cubical `I` |
| Whole-record reconstruction and schedule swap | Follow for every schedule semantics; insufficient to certify source derivation |
| Unit norm, continuity and generator compatibility | Further analytic obligations; do not by themselves settle provenance |

## Contract boundary

The desired shape is a type of analytic interfaces `A`, a realization satisfying endpoint/locality/continuity/coherence laws over `A`, and a predicate `DerivedFromSource A realization`.

The first two components describe an **admissible realization relative to declared analytic choices**. The third component is still missing. Defining it as reconstruction plus schedule swap would admit every supplied schedule adapter, as the checked theorem shows. Merely writing an uninterpreted `DerivedFromSource` field would move the gap rather than close it.

A meaningful next contract must state which choices are permitted premises and what rule makes the remaining construction source-derived: for example a declared free-linearization construction together with explicit naturality requirements. Neither naturality alone nor uniqueness is being asserted here, and no such contract is presently admitted.

## Obstruction check

The existing no-go applies to a total single-valued Cubical-pointwise state correspondence with separated endpoint states. Whole functions on an external metric domain do not instantiate that forbidden interface. This audit therefore neither revives that pointwise route nor infers impossibility of all external metric interpretations.

## Planning consequence

Do not set `source-contract-typed`. The selected one-shot closure portfolio stops on this inconclusive audit, exactly as its declared transition rules require. Record the observed outcome and replan rather than repeatedly recommending the same unattempted audit.

The next bounded task is **specifying the admissible extra structure and source-derivation criterion**, not continuing phase estimates under a claimed source contract. It requires a revised planning action/contract; this audit has not assigned it a fabricated probability or admitted it as a proof node.
