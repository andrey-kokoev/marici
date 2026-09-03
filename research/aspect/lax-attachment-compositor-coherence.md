# Lax attachment-compositor coherence

## Question

How must attachment transport be typed when staged and direct constructions are related by noninvertible comparison cells?

## Claim boundary

This packet fixes lax and oplax orientations and tests them in a finite thin attachment category. It does not infer which orientation an optical interface physically supplies; that direction must come from the source construction.

## Directed comparison cells

For covariantly written transport functors \(F_f\), a lax compositor has direction

\[
\mu_{g,f}:F_gF_f\Longrightarrow F_{gf},
\]

with unit

\[
\eta:\operatorname{Id}\Longrightarrow F_{\mathrm{id}}.
\]

An oplax compositor reverses both comparison directions:

\[
\bar\mu_{g,f}:F_{gf}\Longrightarrow F_gF_f,
\qquad
\bar\eta:F_{\mathrm{id}}\Longrightarrow\operatorname{Id}.
\]

Contravariant attachment indexing reverses map order but does not erase the distinction between lax and oplax cell directions.

Both structures require naturality in every attachment morphism, two unit triangles, and an associativity diagram. No inverse comparison may be used unless independently constructed.

## Finite orientation fixture

Let the attachment category be the chain

\[
0<1<2.
\]

Let the map-label monoid contain an identity and an idempotent label \(a\). Define the upward saturation functor

\[
U(x)=\min(x+1,2).
\]

Since \(U(x)\le U^2(x)\), the comparison \(U\Rightarrow U^2\) exists, but \(U^2\Rightarrow U\) fails at \(x=0\). Thus the idempotent relation \(a^2=a\) admits the oplax compositor and rejects the lax one.

For downward saturation

\[
D(x)=\max(x-1,0),
\]

one has \(D^2(x)\le D(x)\). The lax compositor exists and the oplax compositor fails at \(x=2\).

Because the category is thin, every well-typed naturality, unit, and associativity diagram commutes uniquely. Existence and orientation remain substantive gates.

## DPC cycle

### Governing conjecture

The source-derived order between direct and staged attachment constructions uniquely determines lax versus oplax orientation; irreversibility alone does not. The mechanism is hard to vary because a directed comparison exists exactly when every component has the required source-to-target morphism.

### Rivals

1. Lax and oplax orientations are interchangeable notation even when comparison cells are noninvertible.
2. Every irreversible attachment process has one universal orientation.
3. A missing comparison can be supplied by formally reversing the available cell.

### Risky consequences

The same attachment chain and idempotent map law must select opposite orientations for upward and downward saturation. Each rejected direction must fail at an explicit endpoint, while every admitted diagram must commute without inverses.

### Falsification attempt

The checker exhaustively evaluates all objects and map-label pairs. Upward saturation admits every oplax component but lacks the lax component \(2\to1\) at zero. Downward saturation admits every lax component but lacks the oplax component \(0\to1\) at two. It then checks all triples for well-typed associativity paths.

### Residual

Thinness makes parallel arrows equal automatically, so the fixture tests typing and orientation but not equality of distinct composite 2-cells in a nonthin category.

### Disposition

All three rivals are rejected. Source-derived directed comparison is retained as the orientation authority; noninvertibility prohibits silently switching lax and oplax conventions.

## Disposition

Lax attachment semantics is appropriate only when staged transport maps to direct transport; oplax semantics is appropriate for the reverse source-derived comparison. Neither direction follows from the word “irreversible.”
