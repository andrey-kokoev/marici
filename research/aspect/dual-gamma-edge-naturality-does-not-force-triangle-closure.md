# Dual-gamma edge naturality does not force triangle closure

## Closed edge

Benincasa's first labelled edge now intertwines all 11,521 ordinary exact relations and all 480 gamma-derivative generators at two primes. The quotient transport has rank 26 and carries the source-fixed residue sign. This closes local and one-edge ambiguity.

## Next obstruction

Let the three labelled conductor transitions act on the common one-dimensional Bockstein line by nonzero units

\[
u_{12},\quad u_{23},\quad u_{31}.
\]

Each edge can satisfy its own naturality square. Global descent additionally requires

\[
u_{31}u_{23}u_{12}=1.
\]

The product is the triangle holonomy. It is invisible to any checker that inspects only one edge at a time.

## Hostile

Take edge units ((-1,1,1)). Every edge is an invertible scalar transport, and a Bockstein value can be propagated naturally across each edge. After the complete circuit, however, the value (1) returns as (-1). The cycle residual is nonzero.

A closed control is ((-1,-1,1)), whose product is (1).

Therefore edgewise naturality, full rank, primitive independence, and fixed local units do not force global chart descent.

## Deutsch gate

The explanation closes globally only after all three dual-gamma edges are constructed independently from the source and their signed composite is the identity on:

1. the rank-26 quotient;
2. the common Bockstein target line;
3. the declared epsilon normal coordinate.

A fitted inverse for the third edge is inadmissible. Its construction must precede evaluation of the triangle product.

## Verification

```text
uv run python research/aspect/checkers/check_dual_gamma_triangle_holonomy_hostile.py
```
