# Joint refutation and Wolfram's identity: two proof phases

## Frozen question and scope

The operator asked for a verbose proof with two phases: construct the question that refutes a joint answer, then determine when the construction satisfies Wolfram's identity.

SCC obligations: forward realization, route/coherencer compatibility, and readout descent.

- Conjecture: small set-valued retained actions admit an empty question, joint questions, and a joint-refutation question with a natural map-space universal property. The Wolfram expression is equivalent as an action to double negation of its third input. Recovery of that input requires exactly propositionality and double-negation stability of its answer types.
- Rivals: a Boolean table must be supplied first; changing reference objects destroys the construction; set-valuedness alone makes Wolfram's identity hold; truth reflection recovers retained answer choices.
- Tests: construct the initial and product universal properties, both curry maps and recovery proofs, naturality in the test question, equivariant Wolfram comparisons, sufficient and necessary conditions, and a Boolean-answer loss control.
- Inputs: the existing retained structure and set-valued actions, plus the ambient empty, pair, and function types. The bare retained-change record does not generate an empty type. The two meanings of E/P in the old and new drafts are not identified.
- Disposition: fresh safe Cubical Agda compilation and the intended false/true rejection pass. The construction is a question over the retained structure, not a new operation on its raw object labels. The exact comparison with the old NAND code concerns value types, not whole code packages.

## Terms and notation

A question A assigns an answer type A(p) to each object p. A retained change e:E(p,q) acts by a map A_e:A(p) -> A(q). The action includes unit and composition witnesses. These maps are invertible by the earlier `action-iso` theorem.

In this proof each A(p) is a small set. This permits distinct answers; it only makes witnesses of any fixed equality equal. A proposition is more restrictive: any two of its answers are equal. A proposition may be empty.

Write Map_E(X,Y) for a family of functions f_p:X(p) -> Y(p), together with proofs

\[
Y_e(f_p(x))=f_q(X_e(x)).
\]

The object indices, source changes and action laws remain parameters. Here P and E mean the current object and change fields. They do not mean the earlier dependent-product and dependent-sum constructors.

## Phase 1: construct the joint-refutation question

### Empty question and joint answers

The empty question 0 has answer type 0 at every object. It has a unique map into any question: there are no source answers to process. `zero-initial` proves contractibility of that map space. The empty type is admitted by the ambient type theory; the retained-change record alone does not generate it.

The joint question J(A,B) has answer type A(p) times B(p), acted on componentwise:

\[
J(A,B)_e(a,b)=(A_e(a),B_e(b)).
\]

Its unit and composition paths are pairs of the input action paths. Giving a map into the joint question is equivalent to giving one map into each input:

\[
\operatorname{Map}_E(X,J(A,B))
\simeq\operatorname{Map}_E(X,A)\times\operatorname{Map}_E(X,B).
\]

Projection and pairing are inverse, including their compatibility proofs. This is `joint-universal`.

### Joint refutation and its change rule

Define

\[
N(A,B)(p)=(A(p)\times B(p))\to\mathbf0.
\]

An answer to this question takes a proposed joint answer to the empty type. For e:p -> q, define

\[
N(A,B)_e(n)(a_q,b_q)
=n\bigl(A_{e^{-1}}(a_q),B_{e^{-1}}(b_q)\bigr).
\]

The proposed answers at q are moved back to p, where n applies. Thus the function-space domain occurs contravariantly. The inverse change supplies the required map; no truth table chooses it.

Any function type T -> 0 is a proposition. Given two such functions, function extensionality reduces their equality to each hypothetical t:T. Applying either function to t gives a value of 0, from which the required equality follows by empty elimination. Hence N(A,B)(p) is a proposition and in particular a set.

The displayed change maps satisfy unit and composition laws because both sides of each law are answers to the same propositional question. No proof irrelevance is assumed for the input questions or for the original source structure.

### Universal property and recovery

For every test question X, there is an equivalence

\[
\operatorname{Map}_E(X,N(A,B))
\simeq
\operatorname{Map}_E(J(X,J(A,B)),\mathbf0).
\]

Its maps are explicit:

\[
\Phi(f)_p(x,(a,b))=f_p(x)(a,b),
\qquad
\Psi(g)_p(x)(a,b)=g_p(x,(a,b)).
\]

Both are compatible with E-changes. Their target answer types are propositions, so the required compatibility paths exist. Applying the two formulas in either order recovers the original component functions by evaluation. The compatibility witnesses are also recovered: their types are propositions because the target fibers are sets.

`nand-universal` checks these inverse maps. `universal-natural` checks that precomposing a test map h:Y -> X commutes with the displayed conversion, as an equality of maps with their compatibility witnesses.

This specifies NAND without supplying Boolean values. It is the empty-target function-space universal property in the category of the stated actions.

### Retention and the old constructor

`RetainedNand` stores both input action records; its result is computed from those fields. `recover-left` and `recover-right` recover the inputs by reflexivity. This is separate from a claim that the result alone encodes its inputs. Selected change data must likewise not be replaced by their induced truth effect.

At every retained object p, `old-constructor-comparison` is the identity equivalence between the new answer type and the value type of the old indexed `nandCode(A(p),B(p))`. The old sum/product code and the new E-action record are not identified as whole packages.

## Phase 2: determine the exact Wolfram law

Write A | B for N(A,B), and define

\[
W(A,B,C)=((A\mid B)\mid C)\mid(A\mid((A\mid C)\mid A)).
\]

The exact result is

\[
W(A,B,C)\simeq\neg\neg C,
\qquad \neg C=(C\to\mathbf0).
\]

For questions, this is `wolfram-double`: an `ActionIso` with compatible forward and backward maps and their recovery witnesses. The underlying value-type proof is imported from the earlier `QBooleanity` theorem, not inferred from a Boolean table.

### The two value-level proof maps

Fix an object p and suppress that index. An answer w:W accepts a pair

\[
u:\neg(\neg(A\times B)\times C),
\qquad
v:\neg\bigl(A\times\neg(\neg(A\times C)\times A)\bigr)
\]

and returns a value of 0.

Given n_C:C -> 0, define

\[
u(n_{AB},c)=n_C(c),
\qquad
r(a',c)=n_C(c),
\qquad
v(a,h)=h(r,a).
\]

Then w(u,v) is a value of 0. This defines W -> double-negation C.

Conversely, let d:(C -> 0) -> 0. Given u and v of the displayed types, define, for each c:C,

\[
h_c(n_{AC},a')=n_{AC}(a',c),
\qquad
n_{AB,c}(a,b)=v(a,h_c),
\qquad
n_C(c)=u(n_{AB,c},c).
\]

Then d(n_C) is a value of 0. This defines double-negation C -> W. Both W and double-negation C are propositions, so the two composites recover their inputs. The same fact makes these maps compatible with retained changes at every object.

### Necessary and sufficient condition

A proposition C is double-negation stable when it has a map

\[
s_C:\neg\neg C\to C.
\]

Every type has the other map, eta_C(c)(n)=n(c). If C is a stable proposition, these maps are inverse because their source and target are propositions. Therefore

\[
W(A,B,C)\simeq\neg\neg C\simeq C.
\]

Conversely, an equivalence W(A,B,C) equiv C implies that C is a proposition, since W is one. Composing the proved map double-negation C -> W with the proposed equivalence gives stability of C.

`wolfram-stable` and `wolfram-necessary` prove both directions for the action-valued questions, point by point. The resulting law is an `ActionIso`. It is not an asserted equality of arbitrary action records.

Negations are stable propositions. If d:double-negation(N(A,B)), a joint refutation is given by

\[
(a,b)\longmapsto d\bigl(\lambda n.\,n(a,b)\bigr).
\]

Thus stable propositions are closed under N, and the Wolfram law holds on that truth domain. The old proof of the Boolean algebra on stable truth types remains applicable; this new module supplies compatibility with the retained actions.

### Reflection and the information boundary

The construction D(A)=double-negation A is a reflection. For every stable propositional question T, `reflection-universal` proves

\[
\operatorname{Map}_E(D(A),T)\simeq\operatorname{Map}_E(A,T).
\]

This says which truth questions can receive the result. It does not make D(A) equivalent to arbitrary A.

`ConstantBool` is a valid set-valued question with two distinct answers. Its double negation is a proposition. `concrete-nonboolean-question` proves that the Wolfram expression on this question cannot be equivalent to the question itself, in the original inhabited Boolean model.

This does not refute NAND on Boolean bits. A two-answer type Bool is not an empty-or-unit truth type. `no-boolean-recovery` also excludes every decoder that would recover both Boolean answers from their double-negation images.

## Verification and next boundary

Formal root: `agda/RetainedNandPhases.agda`.

```powershell
pwsh -NoProfile -File research/nima/checkers/check_graded_boundary_coherence.ps1 -Module RetainedNandPhases -ReceiptStem retained-nand-phases -NegativeModules RetainedNandBadReflection
```

Fresh safe compilation and the deliberate false/true reflection-decoder rejection pass. The runner uses `-NoNewWindow`, fresh interfaces, and source/compiler/library hash checks. An initial elaboration failure required explicit action objects in product and composition maps; no mathematical assumptions changed.

Receipt: `results/retained-nand-phases-formal-audit.json`.
Source-bound checker: `checkers/check_retained_nand_phases.py`.
SCC model: `nima-retained-nand-phases`.

The new result supplies universal properties and retained-change compatibility, while preserving the earlier value-type construction. It does not remove the admitted empty type, prove an equivalence of whole old/new constructor packages, or treat all sets as Boolean truth types. For a complete package with an existing answer, mere inhabitation is already true. The next source question must therefore specify a possibly empty compatibility question rather than re-test that package's known inhabitation.
