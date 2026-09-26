# Testing combinators against structural E

## Checked result

`agda/CombinatorsFromRetainedE.agda` separates three capabilities:

1. Pairing, projection, duplication and composition.
2. Applying a function-valued input.
3. Abstracting an input into a function value.

The experiment uses a declared nondependent structural fragment, not the entire
original E/P closure. Its programs contain identity, terminal map, composition,
projections and pairing. Arrow types can occur as objects, but there is no
application or abstraction constructor. Terminal structure is the empty product,
so even this fragment is not claimed to arise from E alone without assumptions.

## What the structural fragment constructs

The uncurried K body is projection:

\[
k(a,b)=a.
\]

Duplication is pairing with identity twice:

\[
\delta(a)=(a,a).
\]

Both computations are checked for all types in the fragment. Thus input reuse
and leaving an input unused in the output are available under the admitted
structural rules.

A retained K computation keeps its input:

\[
\widehat{k}(a,b)=((a,b),a).
\]

First projection recovers the entire input. Ordinary K's output does not: Agda
proves there is no recovery function from Bool to Bool times Bool that recovers
every pair from its first component. Retaining the input is distinct from making
the output projection invertible.

## What the structural fragment cannot construct

Agda proves that no program in this fragment implements

\[
\operatorname{eval}(h,a)=h(a).
\]

The proof covers every finite program tree, not a bounded enumeration. A logical
relation equates ground values and treats any two function-typed inputs as
related. Every structural program preserves that relation. Evaluation fails it:
identity and constant-true functions, both paired with false, are related inputs
but evaluate to different Boolean outputs.

The same argument excludes an uncurried S implementation satisfying

\[
s((f,g),a)=f(a)(g(a)).
\]

Changing f from constant-false to constant-true leaves the inputs related while
changing the required output.

## What additional operations suffice

Using the existing program fragment's explicit application constructor, S's
uncurried body is constructed by projections, pairing and three applications.
Its computation law is checked for arbitrary A, B and C. This definition uses
no abstraction constructor.

Turning the uncurried K body into

\[
a\longmapsto\lambda b.a
\]

uses the existing abstraction constructor explicitly. We do not report that as
a derivation of abstraction from E.

Program syntax can be retained with its Extended derivation through the existing
`GeneratedContinuationContexts` next-Q packaging. This is not an introduction
rule derived in the original twelve-schema Resolve system.

## Scope of the obstruction

This is not an impossibility theorem about every interpretation of E acting on
E. It does not include dependent case analysis, inspection of retained program
codes, recursive interpreters, or new rewrite rules. Such operations can invalidate
the logical-relation invariant and must have their own source justification.

In particular, pairing a function code with an argument code can represent an
application node. It does not by itself establish how that node evaluates.
Constructing the node and supplying its computational rule are separate steps.

The current result isolates application as an additional requirement for the
structural fragment; abstraction remains another explicit requirement. It does
not establish E squared equivalent to P.

The subsequent [E-tree template construction](e-tree-templates.md) adds explicit
inductive syntax elimination and derives scoped template application and K/S
expansion from generic substitution. It retains the distinction between those
expansions and execution of arbitrary application nodes.

## Verification

Fresh safe/cubical compilation of `CombinatorsFromRetainedE` and its dependency
closure passed using the shell runner `checkers/check_cubical_agda.ps1 -Module
CombinatorsFromRetainedE -Fresh`.

Receipt: `results/agda-CombinatorsFromRetainedE.json`.

The universal impossibility theorems are `no-E-application` and `no-E-S`.
The retained-input control is `projection-not-reversible` together with
`K-input-recovered`. These are checked proofs, not finite experimental evidence.
