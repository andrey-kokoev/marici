# Wolfram proof architecture: commutativity is the first structural gate

Date: 2026-10-06. Actor: marici.Voevodsky. Follow-up to ledger 4307.

## Dependency measurement

`checkers/audit_wolfram_dependencies.py` extracts the named equation DAG from the current generated `WolframConverse.agda`, including the multiline Sh_2-to-Sh_1 bridge. Source hashes and the complete DAG are in `results/wg-ucc-audit/proof-dependencies.json`. An initial parser dropped that multiline bridge; the corrected parser asserts its three dependencies and checks that t3 reaches sh2. Only the corrected output is retained.

The reconstruction uses t80, t83, t91, t93 and t130 directly, together with double negation from t95 and Sheffer laws t147 and t158. Their combined ancestor closure includes all 161 named equations. Removing unused named equations therefore does not shorten this source certificate.

This is a source-level dependency count, not normalization of primitive proof operations. In particular, 161 includes the two axiom wrappers and bridge conventions and is not interchangeable with the earlier 92+67 positive-equation counts.

## A checked structural replacement

Use the reversed stroke convention of the published certificate. Let

\[
(((x*(y*x))*x)*(y*(z*x)))=y
\]

be Sh_2. If the stroke is commutative, then

\[
x*(u*x)=(u*x)*x=(x*u)*x.
\]

Taking u=y*x transforms the first operand of Sh_1 into that of Sh_2. Hence Sh_1 follows from Sh_2 and commutativity using two commutativity instances, congruence and transitivity. No associativity assumption is used: NAND is not associative.

`research/nima/agda/WolframCommutativeBridge.agda` checks this argument with only Cubical Prelude imported. It neither imports the published converse nor claims to derive commutativity. A fresh safe headless check exited 0; log `results/wg-ucc-audit/commutative-bridge.log`.

The old sh1 closure contains 94 named equations. The union of the original axiom and the existing earlier commutativity lemma s2426 contains 92. These numbers exclude the new bridge's inference cost, so they are not a measured proof-length victory. The structural advantage is a simpler stated interface: the published bridge's three opaque intermediate lemmas can be replaced by commutativity alone.

## Proposed proof architecture and exact obstruction

Target a direct derivation of commutativity from Sh_2, then use the checked bridge to Sh_1 and the existing Boolean reconstruction as an initial downstream baseline. The current proof of this early commutativity lemma already consumes 92 named equations; therefore citing it merely hides nearly the entire first published certificate.

The first experimental objective is a shorter independently produced commutativity certificate, not a shorter evaluation program. It has a two-variable target and requires no supplied Boolean structure. A successful candidate can then be tested on the remaining absorption/involution/distributivity gates. No claim is made that commutativity must be the optimal intermediate goal; failure to simplify it motivates a different structural factorization.

## Axiom-only search experiment

`checkers/search_wolfram_commutativity.py` runs the existing weight/age completion engine in both the original and reversed stroke conventions. Each run has a 60-second search budget, a 1,000-record cap and equation weight limit 80. The standard four basis goals remain unchanged; commutativity is the primary reported target, not an added premise. This is not yet a goal-directed search strategy.

Both runs ended unresolved, each with 93 records (the axiom plus 92 new equations). The original convention examined 135,838 overlaps; the reversed convention examined 135,142. No basis goal was proved. Independent checking binds the certificates to the explicit input axioms and rejects a mutated conclusion in both cases. Generated `research/voevodsky/agda/CommutativitySearchOriginal.agda` and `CommutativitySearchReversed.agda` each passed a fresh safe Cubical check with only Prelude imported. The certificates, summary and compiler logs are under `results/wg-ucc-audit/`.

These consequences are independently generated, but neither run supplies commutativity or a shorter complete derivation. Time-budget exhaustion is not a mathematical obstruction. The experiment does not measure a competitive search baseline or connect this Python search to a WG construction theorem. The next strategy change should target the commutativity goal (for example backward obligations combined with forward completion), not simply count more consequences from the same weight-only frontier.

The deliverable now is a checked conditional bridge, an explicit costly gate, and two independently checked unsuccessful bounded searches. WG has not yet independently generated the missing commutativity proof, and the overall Wolfram proof has not been shown shorter. Neither this bridge nor the source-DAG audit changes the existing theorem's premises or replaces its generated file.
