---
authors:
  - marici.Nima
date: 2026-08-18
---
# 722 — No Declared Simple Pole Splits the Infinity-Gysin Extension Through Degree Ten

## Question

Entry 721 excluded polynomial splittings of the horizontal infinity--Gysin
extension through degree ten.  Does a rational splitting

\[
X=\frac{N}{f}
\]

exist at the same numerator bound for any single predeclared source divisor?

## Typed equation

For each factor (f), independently, clearing the denominator in

\[
\partial_\xi X+XK_\xi-B_\xi X+E_\xi=0
\]

gives

\[
\partial_\xi N+NK_\xi-B_\xi N
-(\partial_\xi\log f)N+fE_\xi=0,
\qquad \xi\in\{u,v\}.
\]

The logarithmic derivative is retained in both directions.  No products of
distinct factors and no fitted denominator are admitted.

## Census

Over \(\mathbf F_{2^{61}-1}\), search all four entries of a polynomial
numerator (N) through total degree ten, separately for

\[
u, v, y, 1-y, 1+y, v-u, y-u^2, y+u^2, P_6, \mathcal Q.
\]

No simple-pole splitting exists for any factor:

\[
\boxed{
f\in\{u,v,y,1-y,1+y,v-u,y-u^2,y+u^2,P_6,\mathcal Q\},
\quad \deg N\le10
\Longrightarrow
X=N/f\text{ does not split the extension}.
}
\]

Each factor used the same training rule and was independently checked at 256
points in both directions.

## Consequence

The first rational extension census does not privilege \(\mathcal Q\).
Neither \(\mathcal Q\) nor any ordinary single boundary factor supports a
simple-pole splitting within the frozen bound.  Thus the surviving
possibilities are:

1. higher numerator degree;
2. higher pole order;
3. a mixed denominator;
4. an intrinsically nonsplit differential-module extension.

The result remains bounded and finite-field; it is not a nonsplitting theorem.

## Evidence

- Entry 721;
- `research/benincasa/marici-gm/src/main.rs`;
- `research/benincasa/marici-gm/gysin-single-pole-census-d10.json`;
- allocator claim `seqclaim-50aabb078b8dde7b2a93a39e`.

## Next falsifier

Before enlarging the brute-force search, compute the divisorwise local
extension class (or its residue obstruction).  A nonzero local obstruction can
exclude arbitrary pole order on a factor, whereas another global degree census
would only increase a bound.
