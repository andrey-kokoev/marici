# The primitive line can be the codomain of the Clark polarization but not its state carrier

## Question

Can the rank-two Clark seam pair be compiled faithfully into one complex
primitive or anomaly line?

## Rank obstruction for a scalar state coordinate

Let the source first-jet carrier be

\[
V=\mathbb C^2
\]

with the nondegenerate Clark mismatch

\[
\Delta_a=
\begin{pmatrix}
0&2ia\\
-2ia&0
\end{pmatrix},
\qquad a\ne0.
\]

Suppose a linear scalar coordinate

\[
c:V\to\mathbb C
\]

were claimed to carry this form through a scalar metric (mu). Then

\[
\Delta_a=c^*\mu c.
\]

But the right side has rank at most one, while (Delta_a) has rank two.
Therefore no single complex linear state coordinate carries the Clark seam
form.

The obstruction is stronger for a positive scalar energy: (c^*c) is
positive semidefinite, whereas (Delta_a) has signature ((1,1)).

## A line can carry the evaluated relation

For two jet vectors (x,y\in V), define

\[
\omega_a(x,y)=x^*\Delta_a y.
\]

This is a scalar-valued sesquilinear relation. In coordinates,

\[
\omega_a(x,y)
=2ia\bigl(\overline{x_1}y_2-\overline{x_2}y_1\bigr).
\]

Thus one complex line can be the codomain of the determinant-like
polarization. It does not become the carrier of either input state.

Because (Delta_a) is nondegenerate, the mate-valued map

\[
x\longmapsto\omega_a(x,-)
\]

is injective into (V^*). A single evaluated scalar
(omega_a(x,y)) is not injective in (x) or (y). Faithfulness belongs to
the complete family of mates, not to one scalar outcome.

## The three coefficient lenses

The Clark seam now exhibits the coefficient-lens distinction exactly.

### Additive scalar lens

It records one evaluated current or a sum of such currents. It can transport
(omega_a(x,y)) after both arguments and their incidence are fixed. It
cannot reconstruct the rank-two jet carrier.

### Determinant-line lens

It records the oriented area of a pair. This is the minimal natural codomain
for the Clark symplectic polarization. Its composition law is multiplicative
or cocyclic, and it retains orientation information that an unsigned norm
loses.

### Ordered operator lens

It retains the full jet and the noncommuting transformations acting on it.
This lens is required when later constructors must act separately on (F)
and (F'), or when order of Clark, reflection, and arithmetic operations
matters.

These are not three implementations of the same state. They preserve
different levels of constructor history.

## Typing the primitive anomaly line

A map into one primitive line is admissible in either of two ways:

1. as the scalar codomain of the already-formed relation
   (omega_a(x,y));
2. as a state quotient only after a source theorem restricts admissible jets
   to a line on which every downstream target is fiber-constant.

Without the second theorem, treating the primitive line as the state carrier
is premature quotienting.

The compiler must therefore declare whether it consumes:

- one jet state;
- a pair of jet states;
- an oriented determinant;
- or an ordered operator word.

The same complex scalar type cannot silently stand for all four.

## Associator consequence

For a ternary or network composition, every intermediate binary seam must
retain the full symplectic port unless a named polarization has already
consumed it and no later operation needs the separate jet directions.

Pairwise scalar currents do not determine a higher-order relation without a
proved factorization or coherence theorem. This is the lower-arity control
identified by Aspect's relational-hypergraph correction.

## Falsifier certificate

    {
      "code": "primitive_line_mistyped_as_clark_state_carrier",
      "source_rank": 2,
      "source_signature": [1, 1],
      "scalar_state_metric_rank_max": 1,
      "scalar_line_allowed_as_relation_codomain": true,
      "state_reconstruction_allowed": false
    }

## Disposition

One primitive complex line can carry the evaluated Clark polarization, but it
cannot replace the rank-two first-jet state. The source jet must remain until
the relation is formed, unless an additional source restriction proves a
faithful rank-one quotient for every downstream constructor.

## Claim boundary

This theorem concerns linear state compression and the bilinear Clark
polarization. It does not determine the actual arithmetic incidence into the
primitive line, prove a determinant cocycle, or establish higher-arity
factorization.
