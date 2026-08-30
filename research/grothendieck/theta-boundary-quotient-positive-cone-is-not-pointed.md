# Theta boundary-quotient positive cone is not pointed

## Relative germ space

Let `V` be a real vector space of asymptotic regulator germs at
`epsilon=0`, and let `B` contain the declared divergent boundary germs. Let
\(V_+\) consist of germs \(F\) for which \(F_\varepsilon\ge0\) whenever
\(\varepsilon>0\) is sufficiently small.

The relative detector lives in the quotient `V/B`. The obvious attempted
order is the image cone

\[
 \overline V_+=\{[F]:F\in V_+\}.
\]

## Non-pointedness theorem

Assume `B` contains one positive divergent germ

\[
 b_\varepsilon=\varepsilon^{-a},\qquad a>0.
\]

For every constant germ `c`, both

\[
 b_\varepsilon+c>0,
 \qquad
 b_\varepsilon-c>0
\]

for all sufficiently small `epsilon`. Since `[b]=0` in `V/B`, this gives

\[
 [c]=[b+c]\in\overline V_+,
 \qquad
 -[c]=[b-c]\in\overline V_+.
\]

Therefore

\[
 \overline V_+\cap(-\overline V_+)
 \supseteq\{[c]:c\in\mathbb R\}.
\]

In particular, the induced cone is not pointed on the scalar detector line.
It cannot distinguish positive, negative, and zero finite parts.

## Meaning

This is stronger than saying that one positivity proof fails. Ordinary bulk
order does not descend to a useful order on the relative boundary quotient.
The divergent boundary direction is an order unit large enough to make both
orientations of every finite scalar class appear positive before quotienting.

Hence the RH-bearing orientation cannot be inherited from

\[
 (V,V_+)\longrightarrow V/B.
\]

It must use structure discarded by that quotient: a paired bulk--boundary
object, a source connection, an indefinite/Krein form with a selected
polarization, or a conservation current whose sewing law fixes the relative
orientation.

## Sharp acceptance gate

A proposed theta order must specify a cone `C_rel` on the coupled relative
object and prove:

1. `C_rel` is source-derived before finite-part evaluation;
2. it is invariant under admissible regulator changes and Poisson sewing;
3. its scalar projection is pointed off the critical seam; and
4. the hostile pair `b+c`, `b-c` cannot both represent positive elements of
   `C_rel` for nonzero `c`.

Failure of item 4 proves that the proposed structure is merely the collapsed
bulk cone in new notation.

## Scope

The theorem concerns the order geometry of boundary renormalization. It does
not exclude a stronger source-derived relative cone; it proves that such a
cone is genuinely additional structure and cannot be obtained by naively
quotienting eventual positivity.
