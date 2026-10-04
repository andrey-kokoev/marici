# Explicit dependent-application extension

## Question and contract

Close the smallest execution gate for Yoneda: from certified f:(a:A)→B(a)
and x:A, derive the evaluated codomain package with both operands retained.
Do not admit the computed result or its beta proof as new seeds.

The prior twelve-rule endpoint obstruction remains valid. This packet introduces
ONE separately named rule schema; it does not pretend to derive that rule from
the frozen core. All six frozen core source hashes remain unchanged.

## Checked construction

`NativeApplicationExtension.agda` defines `Application` parameters containing
A, B, typed input/output codes, f and x. There is no supplied result-value field
and no supplied beta-witness field. Two typed premise ports require derivations
of the actual function and argument packages. Its result is

```text
remember(function-input,
  remember(argument-input, pack(result-code(x), f(x))))
```

This is a new computational rule with semantics defined by dependent application
in the host type theory. Safe Agda checks it without new postulates. The runtime
is the disjoint sum of the twelve old schemas and this schema. Original inputs
and outputs remain definitionally unchanged, and `embed` translates every old
derivation without changing its endpoint or seed witnesses.

The rest uses existing rules:

1. `execute` constructs the application derivation from its two premises.
2. `coherencer` uses the old reflexivity rule to construct its beta path. This
   works because the output value is definitionally f(x).
3. `assemble` uses the old P-kind rule to retain the result and its coherencer
   together, with both actual derivations.
4. `reify` puts that full endpoint-and-derivation pair into a package one universe
   higher. `recover-combined` and `recover-history` recover the exact package
   and derivation by refl.

The fourth step forms a higher-universe constructor package. It does not supply
an admission certificate for a subsequent higher-level execution.

## Tests and disposition

`ApplicationExtensionRegression.agda` imports the previous obstruction fixture
unchanged. With its SAME two seed constructors, the extension derives the exact
retained Bool-result endpoint that the old runtime provably cannot derive.
`not-an-old-macro` retains that old impossibility theorem beside the new derivation.
The beta coherencer, combined derivation and reified package are all instantiated.

A second fixture checks a genuinely dependent codomain: B(false)=Unit and
B(true)=Bool. The general application theorem is universe-polymorphic and not
restricted to these fixtures.

`ApplicationExtensionBadArgument.agda` deliberately puts a function certificate
at the argument port. It must reject with `UnequalTerms` rather than accepting
an untyped or incomplete application. Fresh positive compilation and this
negative control pass.

DPC boundary:

- Problem: the old closure can retain an opaque function but cannot produce the
  specified evaluated codomain endpoint from its two input seeds.
- Conjecture: one dependent application schema suffices for this endpoint,
  with beta coherence and combination handled by old rules.
- Rivals: result-seed injection, missing argument premise, wrong dependent
  codomain, and packaging an externally completed proof instead of deriving it.
- Risky consequence: the old blocked fixture must become derivable under the
  unchanged seed policy; changing an argument certificate must fail.
- Strongest test: fresh general proof, imported old obstruction, both dependent
  branches, native beta/combination derivations, and the intended rejection.
- Disposition: the extension passes. It is a strict increase in derivability,
  not an equivalence with the old twelve-rule closure.

## Remaining Yoneda work

This closes application and dependent specialization in the EXTENDED runtime.
It does not yet construct all Yoneda inverse laws, function extensionality,
or equivalence assembly as native derivations. No finished Yoneda proof was
admitted to obtain this result. The next bounded target is one naturality-law
specialization using this rule, with its source law and arguments retained.

## Reproduction

```text
pwsh -NoProfile -File research/nima/checkers/check_application_extension_kernel.ps1
python research/nima/checkers/check_application_extension.py
python research/aspect/scc/scc.py check nima-application-extension
```

Fresh execution: `structured_command_execution:e_16084_1791130377305129900_19`.
Audit: `structured_command_execution:e_16084_1791130619976321700_20`.
Receipts: `research/nima/results/application-extension-kernel.json` and
`research/nima/results/application-extension-audit.json`. They bind compiler,
source and driver digests. No commit or push was performed.
