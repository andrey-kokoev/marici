# Reachable concurrency classification and root-fixed confluence

Status: written proof for constructor-generated mixed programs under the prior phase/linearity/freshness premises, not a formal verification of Python or arbitrary imported graphs.

## Exhaustive phase classification

Only one program instruction is active. A successor gate's principal faces an auxiliary continuation until its predecessor's complete DONE. Published observation pairs and dormant operands do not reduce.

Within an acknowledged query there is at most one COPY and exactly one query controller (QB/QS/QR), replaced eventually by at most one EA. Thus the only distinct concurrently enabled pairs are COPY with QB, QS, QR or EA. QS can consume a copied prefix while COPY advances the residual input, even though it blocks when it reaches the copying frontier. Query completion excludes COPY, so no release latch overlaps it.

An isolated add or union has one controller and no eraser; gates and query-to-choice latches have one principal redex. In conditional insertion, PICK creates one insertion and one rejected-budget EA. Therefore possible overlaps are ABc/ASc/ARc with EA. Once insertion DONE exists, JOIN can overlap EA; after JOIN fires, JOINR waits for EA's DONE and cannot overlap EA. No insertion remains at JOIN eligibility. These give four more families.

Scanner preparation is serial DC then PREP then DC then READY then START, each gated by the preceding completion. Its query phase has the same four COPY overlaps. TEST/CHOOSE wait for query completion. False-path insertion is isolated and NEXT waits for it; true/zero cleanup is serial EA/latch/EA, not parallel. Recursive FUEL restores the single-active-phase invariant. Hence no new families arise from fuel recurrence or repeated scan instructions.

Exactly eight unordered concurrent kind families suffice: COPY with QB/QS/QR/EA, and EA with ABc/ASc/ARc/JOIN. In particular two gate releases, two EAs, union plus other work, and cursor-copy plus query cannot coexist as enabled independent redexes in this domain.

## Representability of the diamonds

Inspect the rule templates for these families: every external boundary slot connects to a fresh port; none uses an outside-to-outside splice. An auxiliary edge between the two removed pairs therefore becomes a wire between fresh ports belonging to their two replacement subgraphs. It cannot become a closed wire-only component with no surviving agent. All other outside peers survive or likewise attach to fresh endpoints. Linearity and fresh allocation preserve distinct endpoints.

The outside-to-outside rules (ULc--N, READY--DONE, scanner support return on terminal cases) occur only in serial phases. Their representability follows from the existing complete disjoint chain/continuation invariant, and they are never one arm of a two-redex critical diamond. Thus the earlier arbitrary-graph splice concern does not remain an unproved concurrency case for constructor-reachable states.

Distinct principal pairs cannot share an agent. Both remain enabled after reducing the other, and substitution on disjoint boundary slots commutes. Pair the new names by redex identity and local allocation ordinal, fixing every surviving agent and port label. Both orders give the same graph under that bijection and the same allocator increment. This establishes the one-step commuting diamond modulo fresh names for every possible distinct simultaneous choice. A repeated choice trivially agrees; each typed principal pair has one rule.

## Consequence and limits

Reduction is equivariant under these root-fixing name bijections: rules use kind prefixes and port labels, not numeric identifiers, and future fresh allocations remain outside live names. On the quotient by such renaming, local confluence plus the established termination of finite-program/fuel executions yields a unique normal form. Public RET/ACK/OUT roots are fixed, so terminal support and typed observations are scheduler-independent. Diagnostic allocation identities and dictionary enumeration order are not claimed equal; intermediate publication times may differ.

Fresh executable support now covers all eight families, adding a two-cell query to witness COPY/QS. All115 diamonds across686 raw states pass exact port/wire bijections and metadata checks. Witnessing every family is not a substitute for the universal phase argument above, nor an exhaustive enumeration of all typed heads/contexts.

Next assurance task: link this confluence result into the consolidated theorem and closure, and audit the observation boundary under arbitrary valid scheduling (monotone published values, no completion before normal form). Avoid confusing unique final results with identical intermediate traces or scheduler-independent publication timing. This closes an important theoretical milestone without requiring new instruction forms.
