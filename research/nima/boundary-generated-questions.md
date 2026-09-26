# Operations and questions from a common typed boundary

## Candidate principle and test

A retained construction can supply a boundary for another construction. An
operation extends that boundary when its required evidence is supplied. The
associated question is the type of missing evidence.

The test here starts with the existing comparison-rule signature, abstracts
its missing evidence fields, and uses the resulting type both as a question
and as the input to the actual rule constructor. No desired truth table is
supplied. This establishes a rule-relative common construction pattern; it
does not select the rule signature itself.

SCC obligations: forward realization, route/coherencer compatibility, and
readout descent. Model: `nima-boundary-generated-questions`.

## One boundary, an operation, and a question

A complete a contains its retained code and a value v_a. Put
\(A_a=\operatorname{El}(\operatorname{retained}(a))\). For complete a,b,
define the missing comparison evidence:

\[
K(a,b)=\sum_{e:A_a\simeq A_b}
          \bigl(e(v_a)=v_b\bigr).
\]

An inhabitant contains an actual invertible map and its compatibility witness.
These are exactly the evidence arguments of the existing `compare-rule`.
Given a seed family S, applying that rule also requires the endpoint derivations:

\[
\operatorname{Der}_S(a)\times\operatorname{Der}_S(b)\times K(a,b).
\]

The checked `Application.perform` consumes these data and returns the existing
`Resolve` derivation of the comparison package. Endpoint completeness and
endpoint derivability from S are distinct requirements.

For any already formed rule r, the same pattern is

\[
P_S(r)=\prod_{i:\operatorname{Arity}(r)}
             \operatorname{Der}_S(\operatorname{input}(r,i)),
\]

\[
\operatorname{apply}_r:P_S(r)\to\operatorname{Der}_S(\operatorname{output}(r)).
\]

The rule's boundary determines both the premise question and the operation
consuming its answer. A formed comparison rule already contains e and its
witness; K is obtained by abstracting those fields before forming the rule.

The Boolean question is

\[
D(K(a,b))=\neg\neg K(a,b).
\]

Its actual filler remains separately retained. The module explicitly stores
both endpoints and the entire filler in another complete Q and proves filler
recovery. Its concrete resolution instance also retains the whole comparison
derivation as next-Q, with a recovery theorem.

## Source-generated, nontrivial examples

Start with the unit package U. Apply the actual retained-family E constructor:

\[
S=\sum_{i:\mathbf1}\mathbf1,
\qquad
C=\sum_{i:\mathrm{Bool}}\mathbf1.
\]

Both assemblies are complete. The module derives both from the unit seed with
the existing E rule. Their indices are explicitly supplied fixture data; this
experiment does not derive the index family.

| Question | Checked result | Reason |
|---|---|---|
| Can S be constructed from the unit seed? | Yes | An actual E-rule derivation is supplied. |
| Can C be constructed from the same seed? | Yes | Another actual E-rule derivation is supplied. |
| Is there an invertible pointed comparison U to S? | Yes | The unit and unit-pair isomorphism supplies K(U,S). |
| Is there an invertible pointed comparison U to C? | No | Such an equivalence would identify the two branch values. |

Thus the predicate is informative even though every endpoint is a complete Q.
It is generated from the comparison constructor's required evidence, rather
than from the existence of the packages.

The invertibility condition matters. Agda also proves that merely asking for
a point-preserving function between two complete packages is always answered
by the constant function with value v_b. Merely generating a typed question
does not guarantee that it distinguishes constructions.

## Transformation, coherence, and retained distinctions

Supplied fillers compose and invert. Given fillers a' to a and b to b', the
module constructs a map

\[
K(a,b)\to K(a',b').
\]

Transport back gives an equivalence between the Boolean question types:

\[
D(K(a,b))\simeq D(K(a',b')).
\]

This requires the actual boundary comparisons. It is not invariance under an
unspecified change of construction. The formal theorem here is equivalence
of the truth types; it does not assert inverse laws for the unreflected filler
transport or a complete higher-coherence theorem.

For a four-value E package with selected value (0,0), identity and coordinate
swap both fill its self-comparison boundary. They are distinct: their values
at (0,1) differ. Agda proves both

\[
\neg(f_{\mathrm{id}}=f_{\mathrm{swap}}),
\qquad
\eta(f_{\mathrm{id}})=\eta(f_{\mathrm{swap}}).
\]

Taking paths between these fillers produces a further typed question. Its
emptiness in this example is proved. Equality of Boolean answers does not
supply that higher witness.

An invertible pointed comparison is not literal equality of complete packages.
It compares their interpreted value types and selected values while the
result retains both original codes and witnesses. If preservation of further
structure is required, it must occur among the comparison constraints.

## What this does not determine

The finite hostile keeps the same four retained objects and tests two policies:

1. Admit every pointed bijection between their value sets.
2. Admit only literal identity maps at each object.

Both policies have identities, inverse maps, and associative composition. The
first admits U to S and six self-comparisons of the four-value object. The
second excludes U to S and admits only one such self-comparison.

The second policy is an alternative signature, not a model of the existing
unrestricted `compare-rule`. The test shows that these coherence conditions
and these objects do not alone select the comparison policy. It does not
exclude a stronger principle that also constrains the allowed maps, universal
properties, or E/P structure.

The current calculus still has twelve rule schemas. Expressing all their
applications as boundary filling unifies their interface; it does not prove
that one law generates the schemas or every higher filler.

## Scientific consequence

The common boundary construction connects five of the earlier questions:
operations consume fillers; predicates name missing fillers; truth concerns
those types; transport uses boundary comparisons; retention preserves the
chosen evidence beyond its Boolean answer.

The remaining higher question is now more precise:

**What in the retained structure determines which boundary constraints and
fillers are admissible?**

A proposed answer must distinguish competing comparison policies by a source
requirement. Coherence alone, in the tested sense, is insufficient. A universal
completion property is a candidate additional requirement, but no such
selection theorem is established here.

## Verification

- `agda/BoundaryGeneratedQuestions.agda`: generated question, actual rule
  application, E derivations, next-Q recovery, positive and negative fillers,
  witness distinction, and transported truth equivalence.
- `checkers/check_boundary_questions.ps1`: fresh headless closure and rejection
  of `negative/BoundaryBadWitnessCollapse.agda` at the mismatched projections.
- `checkers/check_boundary_questions.py`: exact filler enumeration and finite
  groupoid-law checks for the two policies, with formal source-hash audit.
- `results/agda-BoundaryGeneratedQuestions.json`,
  `results/boundary-questions-formal-audit.json`,
  `results/boundary-questions.json`: verification receipts.

Fresh Agda closure, the intended rejection, and the SCC audit passed. The
proofs retain the declared rule-relative scope.
