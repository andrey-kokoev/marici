# Gauge interchange in the scalar Markov Green sector

## Question

Does the scalar Markov Green fragment admit a sourced interchange cell between horizontal chain concatenation and vertical gauge isometries?

## Claim boundary

This packet treats vertex-sign gauge isometries of normalized scalar Green chains. It does not prove interchange for general vertical maps, gauge quotients, or operator-valued kernels.

## Vertical gauge arrows

For a chain Gram matrix \(G(a_1,\ldots,a_n)\), choose vertex signs

\[
\varepsilon=(\varepsilon_0,\ldots,\varepsilon_n),
\qquad \varepsilon_i\in\{\pm1\},
\]

and let \(D_\varepsilon\) be diagonal. The vertical arrow is the isometry

\[
G\longmapsto D_\varepsilon G D_\varepsilon.
\]

It sends each edge parameter to

\[
a_i' = \varepsilon_{i-1}\varepsilon_i a_i.
\]

The transformed matrix is again the path-product Gram matrix for \((a_1',\ldots,a_n')\), because intermediate signs cancel in every nonadjacent product.

## Horizontal composition

Two chains concatenate only when their shared vertex normalization and gauge sign agree. Under that admission predicate, concatenate their ordered edge lists and omit one copy of the shared vertex.

## Interchange

Let chains \(A,B\) have compatible endpoint and startpoint gauges. There are two routes:

1. gauge \(A\) and \(B\), then concatenate;
2. concatenate \(A\) and \(B\), then apply the concatenated vertex gauge.

Both routes produce the same transformed edge list and hence the same full Gram certificate. The interchange cell is the identity isometry on that common matrix.

Vertical composition also acts pointwise: composing sign gauges multiplies their vertex signs. Therefore horizontal concatenation commutes with vertical gauge composition on every admitted square.

## Hostile test

If the two gauges assign different signs to the shared vertex, there is no concatenated vertical arrow. Silently choosing either sign changes the first edge of one segment and can change cross pairings. The square is noncomposable rather than noncommuting.

## Disposition

The scalar Markov Green fragment now has analytic associators, pentagon coherence, and a restricted interchange law for vertex-sign gauge isometries. General interchange remains open.

## Verification

- `research/voevodsky/checkers/check_markov_green_gauge_interchange.py`
- `research/voevodsky/results/markov_green_gauge_interchange.json`
