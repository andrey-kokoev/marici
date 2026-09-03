# Falsification attempt on cyclic-evidence discharge

## Question

Is a strict contraction constant on a complete typed space, or a uniquely fixing invariant, sufficient to discharge a cyclic evidence component?

## Claim boundary

This packet attacks underspecified discharge schemas, not Banach's fixed-point theorem.

## Bold conjecture under test

An evidence strongly connected component is admissible when it carries one listed discharge certificate, including contraction below one on a complete typed space or an independently grounded invariant that uniquely fixes the component.

## Hostile 1: contraction without an invariant self-map

Let the complete metric space be

\[
X=[0,1]
\]

with the usual metric, and define the displayed constructor

\[
T(x)=1+\frac{x}{2}.
\]

For all `x,y` in `X`,

\[
|T(x)-T(y)|=\frac12|x-y|,
\]

so the Lipschitz constant is exactly `1/2`. Yet `T` is not a self-map of `X`: for example `T(1)=3/2`. Its fixed point is `2`, outside `X`. A checker that verifies completeness and contraction but omits codomain closure falsely discharges the cycle.

Thus a contraction certificate must include the typed arrow `T:X->X`, not merely a formula and a Lipschitz estimate on inputs from `X`.

## Hostile 2: uniqueness without existence

A grounded invariant can prove that any admissible fixed point must equal a named value without proving that the value satisfies the defining equations. Equivalently, `at most one` can hold vacuously when there are no solutions. For example, over the real numbers the equation

\[
x^2+1=0
\]

has at most one solution equal to any prescribed candidate only under a vacuous implication, but has no real solution. A unique-fixing invariant therefore needs separate existence and satisfaction certificates.

## Hostile 3: quotient uniqueness without separatedness

If the comparison uses a pseudometric or quotient seminorm, contraction yields uniqueness only modulo zero-distance equivalence. Two distinct presentations can remain fixed while having distance zero. A transfer registry that reports literal uniqueness silently promotes quotient uniqueness to representative uniqueness.

## Strongest residual

The discharge-mode list is not sufficient as named. Each mode needs a complete theorem interface. Mode labels otherwise absorb precisely the missing hypotheses the registry is intended to expose.

## Surviving conjecture

A cyclic component is discharged only by an instantiated theorem certificate whose full hypotheses are checked. For Banach discharge these include:

- a complete separated metric object `X`;
- a typed self-map `T:X->X`;
- a uniform contraction constant strictly below one;
- compatibility of the metric quotient with the claimed identity strength;
- existence and uniqueness conclusions stated at the correct quotient level;
- a recovery check that the fixed point satisfies the original component equations.

Other discharge modes require equally explicit theorem interfaces. A mode name alone has no admission force.

## Disposition

Revise. Replace the enumeration of discharge labels by a registry of theorem schemas with required hypotheses, conclusion strength, quotient semantics, checker reference, and deliberate missing-hypothesis counterfixtures.
