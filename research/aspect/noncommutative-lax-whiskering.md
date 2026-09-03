# Noncommutative lax whiskering

## Question

What ordered associativity equation replaces the commutative compositor formula when attachment endomorphisms do not commute and transport functors act nontrivially?

## Claim boundary

This packet uses a one-object attachment groupoid to isolate ordered whiskering. Its comparison cells are invertible, so it tests the noncommutative ordering required by lax coherence but not genuinely noninvertible cells.

## Ordered equation

Let the attachment endomorphism group be \(A\), let map labels form \(G\), and let \(\alpha_g\) be the action induced by transport functor \(F_g\). Write the compositor component as \(c(g,h)\in A\). With composition written multiplicatively, associativity requires

\[
c(g,h)c(gh,k)
=
\alpha_g(c(h,k))c(g,hk).
\]

The term \(\alpha_g(c(h,k))\) is left whiskering by \(F_g\). Omitting it or commuting factors is valid only under separately proved triviality or centrality assumptions.

Compatibility of each compositor with the functor action is also required:

\[
\alpha_g\alpha_h
=
\operatorname{Inn}(c(g,h))\alpha_{gh}.
\]

## Gauge-generated coherent fixture

Take \(G=C_3\), \(A=S_3\), and start from the strict trivial action. For a normalized table \(b_g\in S_3\), gauge transport gives

\[
\alpha_g=\operatorname{Inn}(b_g),
\qquad
c(g,h)=b_gb_hb_{g+h}^{-1}.
\]

This construction guarantees the ordered action-compatibility and associativity equations. Choosing noncommuting \(b_1\) and \(b_2\) makes the whiskering observable.

## DPC cycle

### Governing conjecture

Ordered whiskering by the outer transport functor is indispensable in noncommutative lax associativity. The mechanism is hard to vary because one associativity path transports the inner comparison through \(F_g\), while the other does not.

### Rivals

1. The unwhiskered equation \(c(g,h)c(gh,k)=c(h,k)c(g,hk)\) remains valid.
2. The factors may be freely commuted because both paths have the same endpoints.
3. Action compatibility alone forces associativity, so no separate triple equation is needed.

### Risky consequences

A gauge-generated coherent fixture with nontrivial inner actions must satisfy every ordered equation while violating at least one unwhiskered equation. A mutation of one compositor entry can preserve component existence yet violate ordered associativity.

### Falsification attempt

The checker exhaustively evaluates all 27 triples for \(C_3\) with \(S_3\) coefficients. It verifies action compatibility and ordered associativity for the gauge-generated table, records failures of the unwhiskered rival, then mutates one compositor and confirms an ordered coherence failure.

### Residual

The fixture has one attachment object and invertible cells. Object-changing noncommutative lax functors require componentwise whiskering with explicit source and target objects.

### Disposition

All three rivals are rejected. Ordered whiskering plus separate action compatibility and associativity gates are provisionally retained.

## Disposition

Noncommutative attachment coherence cannot reuse a central cocycle formula. Functor action and multiplication order are part of the typed compositor equation.
