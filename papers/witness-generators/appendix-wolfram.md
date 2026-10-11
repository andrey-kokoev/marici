# Separate note: constructive joint refutation and retained proof assembly

Archived from the former manuscript appendix; not part of the selected-step tutorial. This example exercises the basic rule compiler, **not** the stronger refinement composer. It is not evidence for a WG-specific proof-search advantage or for novelty of the refinement interface.

## A.1. A constructive explanation of Wolfram's expression

For types A and B, define joint refutation

\[
N(A,B)=(A\times B)\to\mathbf 0.
\]

This uses products, function types and an empty target. It does not start with a supplied Boolean table. Let

\[
W(A,B,C)=N(N(N(A,B),C),N(A,N(N(A,C),A))).
\]

### Proposition A.1: exact constructive value

For arbitrary types A,B,C in the declared universe,

\[
W(A,B,C)\simeq\neg\neg C.
\]

To construct the forward map, take w:W and n:C→0. Define

\[
u(k,c)=n(c),\qquad
v(a,h)=h\bigl((\lambda(a',c).n(c)),a\bigr).
\]

Then w(u,v) is empty, giving the required double negation.

Conversely, take d:¬¬C and inputs u,v of the displayed types. For c:C define

\[
h_c(r,a')=r(a',c),\qquad
k_c(a,b)=v(a,h_c),\qquad
n(c)=u(k_c,c).
\]

Then d(n) is empty. Both W and ¬¬C are propositions, so the two maps are inverse. This is the prior constructive result in `QBooleanity.agda`; the displayed proof is not claimed as new logical mathematics. The automatically generated backward map makes a different valid choice of the available A witness inside h, with the same type.

If C is a double-negation-stable proposition, W is equivalent to C. Conversely, an equivalence W≃C makes C propositional and yields a double-negation eliminator. Thus the stable-proposition condition is substantive, not an implicit assumption that every type is a Boolean truth value.

The derivation explains the nested expression as a routing of refutations. Function introductions determine subgoals, pairing assembles inputs, and application consumes them. Weakening permits unused assumptions such as B; contraction permits reuse. These are capabilities of the ambient intuitionistic calculus, not consequences of the bare generator interface.

## A.2. Generate witnesses and retain their construction

A bounded Python search accepts the map types as goals. It uses variable lookup, pairing, projections, abstraction and application, with cycle rejection and explicit search bounds. It reads neither the earlier witness terms nor published equational certificates. This is synthesis from a supplied target, not discovery of Wolfram's expression.

The emitter produces intrinsically typed Agda proof trees. A rule frame contains one selected inference and its certified premises. Each frame is executed through a rule-specific WG, and recursive assembly invokes these steps throughout the tree. `construct-correct` proves preservation of the complete tree; `trace` retains the actual compiler edge at every node; `execution-sound` proves interpretation preservation for all declared atom interpretations and environments.

The final equivalence interprets these WG-assembled proofs. Successful construction is therefore connected to individual rule steps, rather than only wrapping a completed equivalence as one supplied computation. The search algorithm itself remains external: the formal assembler consumes a successful typed derivation and does not prove that the search finds it.

The historical searches produced 22- and 25-node terms for the two directions in 36 and 32 recursive visits. A further request produced a joint-input swap in 9 term nodes and 6 visits without an added theorem-specific rule. These are deterministic fixture counts, not comparative performance results. They exclude types, libraries, the generic equivalence proof and implementation size. They were not rerun during the matched refinement comparison or this editorial revision.

A bounded request for unrestricted double-negation elimination did not succeed; this is not a noninhabitation theorem. Independently, a mistyped derivation is rejected by Agda. The three requests demonstrate reuse within one logical fragment, not breadth across unrelated construction domains.

## A.3. Scope and evidence

Wolfram's single-axiom characterization starts with an arbitrary binary operation on a nonempty set and shows that the axiom forces Boolean-NAND structure. Proposition A.1 instead starts with joint refutation and explains its expression. Its short proof is not a shorter proof of that converse. The existing converse formalization replays published certificates of McCune and collaborators.

Nor have we shown that tetrahedral completion selects the exact nesting. Retained boundary questions and their Boolean reflection are already implemented, but presenting a particular filling question through a general Boolean identity is not a derivation of that identity from tetrahedral incidence.

The search rules are standard natural deduction, as explained by Wadler's *Propositions as Types*, section 3. No matched ordinary proof-search baseline is provided for this appendix. The main text's matched refinement experiment is a different comparison and does not establish an advantage for this search.

The Python search and emitter are outside the trusted proof kernel; the emitted terms and indexed certificates are checked. This does not make the Python algorithm itself verified. The existing indexed-pattern warning in `RefutationConstructionWG` concerns unsupported computation on transported indices; no extracted-runtime refinement claim is made.

Historical sources are `research/nima/agda/QBooleanity.agda` and `research/voevodsky/agda/{RefutationConstructionWG,GeneratedWolframConstruction,WolframConstructedEquivalence}.agda`. Search/emission uses `research/voevodsky/checkers/synthesize_wolfram_refutations.py`; historical logs are under `research/voevodsky/results/wg-ucc-audit/`. These are separate from the tutorial's comparison checks. Related references requiring final bibliographic review:

- McCune, W., Veroff, R., Fitelson, B., Harris, K., Feist, A., and Wos, L. *Short Single Axioms for Boolean Algebra*. Journal of Automated Reasoning 29 (2002), 1–16. Published proof-certificate provenance.
- Wolfram, S. *Logic, Explainability and the Future of Understanding* (2018). Public motivation concerning explanation versus machine-checkable proof.
- Wadler, P. *Propositions as Types*. Author-hosted expanded online version, section 3; source recorded in `references/sources.json`.
