# Generating continuation certificates and auditing parameter origins

## Result

The continuation maps and universal inverse witnesses are now generated for
product swap and currying by a typed program fragment with no arbitrary-function
or arbitrary-equivalence constructor. The programs, inverse paths and universal
certificate can be retained together as another Q.

This required an **explicit, separate extension**. The original twelve rule
schemas were not changed. The audit also proves that they can encode any
already-supplied function through unrestricted index parameters. The issue is
therefore source certification, not lack of semantic expressive power.

SCC obligations: forward realization, route/coherencer compatibility, and
readout descent. Model: `nima-generated-continuation-contexts`.

## Two facts about the original closure

`ResolutionMapIntroductionGap.agda` proves an exhaustive syntactic result:
none of the twelve original rule outputs has a bare `maps` constructor at its
root. Consequently,

\[
\operatorname{Resolve}_S(\operatorname{mapPackage}(Q,R,f))
\to S(\operatorname{mapPackage}(Q,R,f)).
\]

A package at that exact interface must already be a seed. This does not say
that function values cannot be produced under Pi or another retained code.

The same module proves the opposite semantic control. Given any supplied
function f:A to B and the unit seed U, form

\[
F_f(a)=E(B,\lambda b.U,f(a)),
\qquad
P_f=P(A,F_f).
\]

The existing E and P rules derive P_f, and

\[
\operatorname{value}(P_f)(a)=(f(a),\star),
\qquad
\pi_1\circ\operatorname{value}(P_f)=f.
\]

Here f is already present in the E-rule index argument. It has not been
computed from U. A seed list is not the whole source specification when rule
parameters can carry arbitrary computations.

This is why a proof of closure membership alone cannot establish that the
operating structure generated the function used in that proof.

## An explicitly generated context fragment

`GeneratedContinuationContexts.agda` defines types with ground types, a
terminal type, binary products and function types. The terminal type is
interpreted by the empty product. Ground types remain declared inputs.

Its program constructors are:

- identity and composition;
- the terminal map;
- two projections and pairing;
- function application;
- abstraction over an extended context.

There is no constructor taking an arbitrary function and calling it a program.
These are an explicit nondependent cartesian-closed fragment, chosen to realize
the preceding universal product/function requirements. They are not claimed
to follow syntactically from the original resolution schemas.

For a generated program t:A to B, the context transformer itself is a program:

\[
\operatorname{pre}(t): (B\to X)\to(A\to X),
\qquad
\operatorname{pre}(t)(h)(a)=h(\llbracket t\rrbracket(a)).
\]

Its construction uses projections, composition, application and abstraction.
The continuation h is a formal input, not a new seed for each possible h.
The construction is uniform in the target type X.

## Constructed universal witnesses

Two checked structural instances are:

\[
A\times B\simeq B\times A,
\]

\[
((A\times B)\to C)\simeq(A\to(B\to C)).
\]

Both forward and backward maps are generated programs. Their inverse paths
compute by the product/function beta and eta laws. For each target X, those
programs generate the two continuation maps, and their inverse paths supply
an equivalence

\[
(T\to X)\simeq(S\to X),
\]

where S and T are the source and target of that structural instance. No
universal-equivalence certificate is inserted as a seed.

The generic helper requires generated forward/backward programs and their
inverse laws. It is not an algorithm that discovers inverses for arbitrary
programs. In the two instances, the inverse programs are explicit and the
laws are checked by reduction. The prior universal-selection theorem can then
consume the resulting quantified continuation certificate.

## Integration and retention

A new `Extended` derivation type contains the old seed/rule cases and one
explicit program-introduction case. That case accepts typed program syntax,
not an arbitrary map. The old resolution derivations embed into it.

The generated forward and backward continuation packages have `Extended`
derivations from an empty seed family. Their exact bare-map packages do not
have such derivations in the original `Resolve`; the map-root theorem proves
this distinction.

A source record retains domain and codomain syntax and the entire program. A
certificate retains both programs, the inverse paths, and the constructed
universal test family. Both are packaged as next-level Qs with checked source
recovery. The universe level rises because program/type-valued syntax is
retained.

Raw programs are not identified by their interpreted maps. Agda proves that
identity and identity followed by identity are distinct programs. Their maps
are definitionally equal. Consequently there cannot be a function from
interpreted endomaps back to source programs that recovers every original
program. Producer information must be retained when it is available; it
cannot in general be reconstructed from the resulting function.

## What the extension does not enforce

The module explicitly proves that the original arbitrary-function encoding
survives in `Extended`, through the embedding of old derivations. Adding a
certified fragment does not impose its provenance discipline on every old
rule parameter.

The established division is:

| Object | Status |
|---|---|
| Original arbitrary index/family parameters | Supplied data; may contain entire functions |
| Swap and currying programs | Generated from the declared structural fragment |
| Their continuation maps and inverse certificates | Constructed from those programs and computed inverse laws |
| Fully dependent context syntax | Not implemented in this fragment |
| Uniform source certification for all original rule parameters | Still open |

The remaining task is to require an appropriate source derivation for index,
family and witness parameters when claiming that an operation was generated.
External inputs may remain legitimate inputs, but must not be reported as
derived computations. A common boundary or universal-property interface by
itself does not provide this origin evidence.

## Verification

Formal sources:

- `agda/ResolutionMapIntroductionGap.agda`
- `agda/GeneratedContinuationContexts.agda`

The shell runner `checkers/check_generated_contexts.ps1` freshly compiles the
closure and checks two intended failures: projection followed by duplication
is not a two-sided inverse, and equal interpreted maps do not identify distinct
program syntax.

`checkers/check_generated_contexts.py` independently interprets typed program
trees on finite carriers. It checks 40 inverse-value cases and 275 continuation
cases, with two of the latter being the critical currying witness contexts.
It does not enumerate all higher-order continuation spaces. Twenty supplied
function tables test the original parameter-encoding control and are explicitly
classified as supplied rather than generated.

Receipts: `results/agda-GeneratedContinuationContexts.json`,
`results/generated-contexts-formal-audit.json`, and
`results/generated-contexts.json`. Fresh Agda checks, both rejections and the
source-bound SCC audit passed.
