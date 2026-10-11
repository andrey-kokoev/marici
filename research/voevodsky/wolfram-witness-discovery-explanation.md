# What suggests the Wolfram witnesses?

Actor: marici.Voevodsky. Date: 2026-10-06. Conceptual audit of the checked construction, not a new theorem.

## Start with the construction, not the identity

Admit empty type, pairs, functions, projection and application. Define

\[
N(A,B)=(A\times B)\to\mathbf 0.
\]

Let U=N(N(A,B),C), H=N(N(A,C),A), and V=N(A,H). The Wolfram expression is W=N(U,V). Thus an inhabitant of W is a procedure that refutes a pair (u:U,v:V).

A proof-search state consists of a context of available witnesses, a goal type, and unfinished construction obligations. To construct a function, assume its input and solve its output goal. To construct a pair, solve both components. To use a refutation, construct its input. Pair projection exposes available witnesses. These are the actual rules used by the implemented search; they are standard natural deduction, not consequences of the bare WG signature.

## Forward: a refutation of C fills both ports of W

Goal: W → ¬¬C. Function introduction supplies w:W and n:C→0; the remaining goal is empty.

Choose to apply w. This creates two obligations, U and V.

- U refutes (k:N(A,B),c:C). Apply n to c; k is unused.
- V refutes (a:A,h:H). Apply h to a pair (r:N(A,C),a). Construct r by sending any (a',c) to n(c).

Both inputs of w are now constructed. Applying w finishes the proof. The same assumed n supplies the two refutations involving C; no Boolean simplification is needed.

The goal types determine the introductions and pair components. Choosing which available refutation to apply is a search choice, not a theorem that the goal uniquely determines its proof.

## Backward: an assumed C closes the chain of refutations

Goal: ¬¬C → W. Introduce d:¬¬C and the pair (u:U,v:V); the remaining goal is empty.

Choose d, so the next goal is C→0. Introduce c:C. Choose u, which requests a refutation k:N(A,B) together with the already available c.

To construct k, introduce (a:A,b:B). Choose v, which requests a together with h:H. To construct h, introduce (r:N(A,C),a':A), then apply r to (a,c). This is exactly the choice in the generated term; using a' instead is another valid proof. The witness b is unused.

Read back up the obligations: r supplies empty, hence h; v supplies empty, hence k; u supplies empty, hence C→0; d supplies empty, hence W.

This is the explanation of why the formula loses A and B at truth level while retaining exactly double negation of C. It is a routing of refutation inputs, not a long sequence of Boolean equations. Since W and ¬¬C are propositions, the maps are inverse. Recovering C itself requires the separately stated stable-proposition condition.

## Which capabilities did the reasoning consume?

| Capability | Role | Provenance |
| --- | --- | --- |
| Function/pair introduction, projection and application | Determine subgoals and assemble witnesses | Ambient type theory and the supplied natural-deduction calculus |
| Weakening | Ignore k, b and other unused assumptions | Unrestricted contexts; not a linear resource calculus |
| Contraction | Reuse n or c in different branches | Unrestricted contexts; not supplied by the bare WG type |
| Empty target | Defines refutation | Admitted primitive |
| Search scheduling | Chooses which refutation to apply | Python's supplied strategy, not a WG theorem |
| Certified rule assembly and retained edges | Records each selected construction step | Implemented rule-level WGs |
| Propositionality of negations | Turns the two maps into an equivalence | Supplied foundational theorem |

The printed explanation uses named assumptions rather than de Bruijn indices, but follows the generated witnesses. It does not claim that every choice was forced. In particular, the two available A witnesses in the backward construction exhibit a real choice.

## Discriminating conclusion

At the level of this example, the witness-finding mechanism is ordinary type-directed natural deduction. WG supplies an explicit witnessed-construction interface and retained derivation trace. The current example does not demonstrate that WG discovers a proof unavailable to ordinary proof search, or that its primitive signature alone selects the necessary logical rules or search strategy.

The argument remains a compact constructive explanation of the identity for joint-refutation NAND. It can motivate a WG paper, but cannot by itself establish WG-specific novelty. The research claim to test is whether WG's retained, proof-dependent construction interface enables useful composition or transfer that standard proof-term production does not already provide under the same resource and provenance requirements. Do not infer that advantage from this example's shortness.

## Evidence

- Exact generated terms: `research/voevodsky/agda/GeneratedWolframRefutations.agda`.
- Search rules: `research/voevodsky/checkers/synthesize_wolfram_refutations.py`.
- Indexed certificate and WG assembly: `GeneratedWolframConstruction.agda`, `RefutationConstructionWG.agda`.
- Prior theorem: `research/nima/agda/QBooleanity.agda`; retained interpretation: `RetainedNandPhases.agda`.
- Existing checks and scope: `research/voevodsky/wolfram-refutation-synthesis.md`.

No code or theorem changed in this conceptual audit; no fresh compiler run is claimed.
