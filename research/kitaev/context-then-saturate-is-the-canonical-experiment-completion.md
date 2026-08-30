# Context then saturate is the canonical experiment completion

## Bounded question

Given a base readout family, in what order should executable constructor
contexts and semantic tester saturation be added to obtain the complete
predictive experiment packet?

## Frozen data

Let \(X\) be a state set, let \(M\) be the monoid of source-authorized
constructors acting on \(X\), and let \(\mathcal U\) be the universe of admitted
tests.

Assume \(\mathcal U\) is closed under constructor precomposition:

\[
t\in\mathcal U, G\in M
\quad\Longrightarrow\quad
t\circ G\in\mathcal U.
\]

For \(T\subseteq\mathcal U\), define

\[
\operatorname{Ctx}(T)
=
\{t\circ G:t\in T,\ G\in M\}
\]

and

\[
\operatorname{Sat}(T)
=
\operatorname{Inv}_{\mathcal U}(\operatorname{Eq}(T)).
\]

The identity constructor belongs to \(M\), so both operations are extensive.

## Context closure is a closure operator

Because \(M\) contains the identity and is closed under composition,

\[
T\subseteq\operatorname{Ctx}(T),
\]

\[
T\subseteq T'
\Longrightarrow
\operatorname{Ctx}(T)\subseteq\operatorname{Ctx}(T'),
\]

and

\[
\operatorname{Ctx}(\operatorname{Ctx}(T))
=
\operatorname{Ctx}(T).
\]

It is the least test family containing \(T\) and closed under authorized
precomposition.

## Predictive congruence lemma

Let

\[
R_T=\operatorname{Eq}(\operatorname{Ctx}(T)).
\]

Then \(R_T\) is a constructor congruence. If \(xR_Ty\), then for every base
test \(t\), word \(G\), and constructor \(H\),

\[
t(G(Hx))=t((GH)x)=t((GH)y)=t(G(Hy)).
\]

Therefore

\[
HxR_THy.
\]

This is why context must be closed before declaring the predictive quotient.

## One-pass completion theorem

Define

\[
\operatorname{Comp}(T)
=
\operatorname{Sat}(\operatorname{Ctx}(T)).
\]

Then \(\operatorname{Comp}(T)\) is both saturated and context-closed.

Saturation is immediate from idempotence of \(\operatorname{Sat}\). To prove
context closure, let \(q\in\operatorname{Comp}(T)\). Then \(q\) is constant on
the predictive congruence \(R_T\). For any constructor \(H\), if \(xR_Ty\),
congruence gives \(HxR_THy\), and hence

\[
q(Hx)=q(Hy).
\]

So \(q\circ H\) is also constant on \(R_T\). Closure of \(\mathcal U\) under
precomposition gives

\[
q\circ H\in\operatorname{Comp}(T).
\]

Thus one ordered pass—context first, saturation second—produces a family closed
under both operations.

## Minimality theorem

The family \(\operatorname{Comp}(T)\) is the least saturated,
context-closed admitted test family containing \(T\).

Let \(Q\) contain \(T\), be context-closed, and be saturated. Then

\[
\operatorname{Ctx}(T)\subseteq Q.
\]

Monotonicity of saturation gives

\[
\operatorname{Sat}(\operatorname{Ctx}(T))
\subseteq
\operatorname{Sat}(Q)=Q.
\]

Therefore no iterative alternation is needed under the frozen hypotheses.

## The reverse order can fail

In general,

\[
\operatorname{Ctx}(\operatorname{Sat}(T))
\neq
\operatorname{Sat}(\operatorname{Ctx}(T)).
\]

The reverse order adds every present-readout function and then transports each
one separately. It need not add joint functions of observations obtained in
different contexts.

Saturating after context closure does add every admitted joint function that is
constant on the complete predictive classes.

## Four-state falsifier

Let

\[
X=\{00,01,10,11\},
\]

let the base test \(b_1\) read the first bit, and let the constructor \(S\) swap
the two bits. Let \(M=\{I,S\}\), and let \(\mathcal U\) contain every Boolean
test on \(X\).

Present saturation contains exactly the Boolean functions of \(b_1\). Context
closure of that family contains functions of the first bit and, after swap,
functions of the second bit. It does not contain the joint parity test

\[
p(b_1,b_2)=b_1\mathbin{\mathrm{xor}}b_2.
\]

By contrast,

\[
\operatorname{Ctx}(T)=\{b_1,b_2\}
\]

separates all four states. Its saturation is every Boolean function on \(X\),
including parity.

Thus

\[
p\in\operatorname{Sat}(\operatorname{Ctx}(T))
\]

but

\[
p\notin\operatorname{Ctx}(\operatorname{Sat}(T)).
\]

The missing operation is joint postprocessing across contextual observations.

## Physical interpretation of saturation

Semantic saturation says that a test value factors through the predictive
quotient. It does not automatically construct an apparatus that computes the
test.

If classical postprocessing of a complete record is authorized, many saturated
tests are executable from that record. If contextual observations arise in
mutually exclusive experiments, a joint saturated function may lack a
single-shot implementation.

Therefore distinguish:

- semantic saturation: no new exact state distinction;
- record-computable saturation: derivable from jointly available records;
- physically executable saturation: implemented by a declared tester.

The one-pass theorem is semantic. Instrument accessibility requires an
additional compiler.

## Record compatibility

Suppose tests in \(\operatorname{Ctx}(T)\) require different destructive
contexts. Their values may not coexist on one copy of the state. Joint
postprocessing then requires:

- repeatable preparations or multiple copies;
- compatible nondestructive tests;
- a sequential instrument theorem;
- or an independently derived joint tester.

The Boolean four-state witness is deterministic and permits semantic joint
evaluation. Quantum noncommuting tests expose the stronger compatibility
problem: a saturated function of counterfactual values need not correspond to
one observable.

This is where the quantum coefficient lens adds structure beyond the shared
Carrier Galois geometry.

## Toric-code instance

Start with local syndrome tests and close under authorized local repair
contexts. The resulting equivalence remains coarse on logical sectors. Adding
two source-derived noncontractible loop probes refines the predictive quotient
to the four logical classes.

Saturation then includes every admitted function of the syndrome and two
logical bits. Such a function adds no exact logical distinction. But its
physical measurement may require a compatible Pauli probe circuit; abstract
factorization through the quotient does not supply that circuit.

The order is therefore:

1. derive executable contexts and probes;
2. compute their predictive congruence;
3. identify semantic saturation;
4. separately compile desired saturated functions into compatible instruments.

## Software instance

Future commands followed by current queries generate context closure. Once the
minimal predictive domain state is identified, any pure function of that state
is semantically saturated.

An API endpoint exposing such a function still requires authorization,
implementation, privacy review, and possibly retained fields. Semantic
redundancy means it reveals no new predictive class, not that publishing it is
free or authorized.

Unlike incompatible quantum measurements, software queries can often compute
joint functions from a stored predictive state. Side effects and distributed
consistency can nevertheless break that assumption.

## Port reopening

Reopening a retained port enlarges \(\mathcal U\). Saturation must then be
recomputed in the new tester universe. A test saturated relative to the closed
port may cease to be a complete description when new environment contexts are
admitted.

The old equivalence was not false. It was closed under a smaller counterfactual
packet. The new universe refines the Galois pair.

## DPC: ordered experiment completion

The conjecture is:

> Complete an operational packet in the order dictated by authority: first
> close the source-derived readouts under executable constructor contexts, then
> saturate semantically on the resulting predictive quotient, and finally prove
> which saturated tests are jointly record-computable or physically
> implementable. Reversing these steps launders semantic functions into
> constructors.

The first two steps are exact in the frozen set-theoretic model. The final
compiler is sector-specific.

## Critics

### The tester universe may not be context-closed

Then enlarge it only if precomposition is source-authorized, or restrict the
theorem to the admissible pairs for which it is closed. The hypothesis is an
authority gate.

### Saturation includes arbitrary functions with no laboratory meaning

Only tests already in \(\mathcal U\) are included. Even then, membership is
semantic; implementation remains separate.

### Infinite systems may require transfinite closure

The one-pass theorem avoids alternation when its hypotheses hold, regardless of
cardinality. Computability and finite presentation remain open.

### Redundant tests can improve precision

Correct. Saturation concerns exact partitions. Frame bounds, Fisher
information, and fault tolerance are separate coefficient metrics.

## Machine-readable audit

```json
{
  "code": "context_then_saturate_completion",
  "base_tests": ["..."],
  "constructor_monoid": "M",
  "tester_universe_context_closed": true,
  "predictive_equivalence": "Eq(Ctx(T))",
  "completed_family": "Sat(Ctx(T))",
  "semantic_context_closed": true,
  "candidate_test": "q",
  "semantically_saturated": true,
  "joint_record_computable": false,
  "physical_implementation": "unproved"
}
```

## Exact falsifiers

- Saturation performed before contexts and presented as the complete packet.
- A parity-like joint test omitted even though it factors through the complete
  predictive quotient and belongs to the admitted universe.
- A semantically saturated test presented as an executable apparatus without a
  record or instrument compiler.
- Context closure using an unauthorized constructor.
- The one-pass theorem invoked when \(\mathcal U\) is not closed under
  authorized precomposition.
- A claimed completed family not closed under one admitted constructor context.
- A quantum joint test inferred from incompatible counterfactual observables.
- Exact redundancy used to dismiss robustness or conditioning value.

## Deutschian explanation

Operation order matters even in completing the theory of observations. Future
contexts first determine which state distinctions can ever become visible.
Only afterward can one say which additional tests merely rename or recombine
those distinctions.

Saturating too early sees only functions of the present shadow. Context first
uncovers the predictive state; saturation then describes every admitted
question that factors through it. Physical implementation is a final, separate
constructor problem.

## Claim boundary

This packet proves the one-pass semantic completion and its minimality. It does
not compile saturated tests into compatible physical instruments.

## Process calibration

Pre-objective: excitement 10/10, confidence 9/10, expected information gain
10/10. The target was whether context and saturation require iterative closure
or have a canonical order.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Context then saturation completes the semantic packet in one pass; the
reverse order fails on a four-state bit-swap witness. Joint record and physical
implementation remain independent gates.
