# Aspect's six-rung tester defers the missing primitive-seed sewing

## Audit object

The structure under test has two parts:

1. a completed result: positive forward/backward scale recursion is an
   invertible localization and preserves a hostile primitive divisor;
2. a proposed replacement: a non-triangular source relation must constrain
   the primitive seed across the two reciprocal scale directions.

These two parts have different dispositions in Aspect's tower.

## Rung-by-rung result

### Realization

The exact rational source is realized. Positive recursion gives

\[
F=\frac{R}{1-cw},
\]

and reciprocal doubling gives

\[
F_{\rm rec}=
\frac{(1+2w)(1+2w^{-1})}
{(1-cw)(1-cw^{-1})}.
\]

### Tester

The tester observes positive coefficients, exact recursion, reciprocal
symmetry, regular denominators, and the surviving reciprocal off-unit zero
pair. The witness passes 11 exact gates.

### Falsifier compiler

The smallest repair mutation—add the reciprocal recursion—fails. It preserves
the same hostile divisor. This separates genuine cross-direction sewing from
the product of two one-directional completions.

### Ontology falsifier

The old language treated `forward completion + backward completion` as the
candidate global object. The hostile introduces a legitimate new distinction:

`independent reciprocal localization` versus `a relation that constrains the
primitive seed jointly`.

That is a cross-coordinate composition/port-creation extension in Aspect's
rung-four language. It cannot be erased merely because the previous carrier
had no coordinate for it.

### Admissibility governor

The new term has:

- source provenance: the theta/Tate reciprocal scale directions;
- a type: a relation between their primitive-remainder ports;
- a separating family: the actual theta seed versus the positive reciprocal
  hostile seed;
- non-alias evidence: every product of independent geometric localizations
  preserves the hostile divisor.

It does not yet have a derived operational constructor or a bounded test of
that constructor. Therefore its correct rung-five disposition is `defer`, not
`admit` and not `reject`.

### Portfolio controller

Because the candidate is deferred, rung six must not schedule it as an
eligible experiment. The already admitted `mixed_prime_incidence` capability
remains valid for testing common-prefix gluing, but it must not be credited
with the new primitive-seed orientation gain. Those are distinct quotient
directions.

Prime-local charts and mirrored scale towers remain duplicate or unfaithful
probes for the RH-bearing distinction. Scheduling more of them would be cheap
alias capture, which Aspect's controller correctly rejects.

## Verdict

The current structure passes the new tester as a successful falsifier and
produces one correctly deferred ontology extension. It does not pass as an RH
mechanism.

The next admissibility obligation is now precise: derive from theta/Tate data
a non-triangular primitive-seed sewing constructor and a bounded witness that
distinguishes it from reciprocal positive localization. Until then, the
research programme should preserve this as a deferred constructor rather than
schedule further recursion variants.

