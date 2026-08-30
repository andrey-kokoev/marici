# Safe coherence flattening is a negative-cohomology vanishing theorem

## Theorem

Fix chain maps (F,G:C^\bullet\to\bar C^\bullet), and suppose at least
one homotopy (S:F\Rightarrow G) exists.  Every other homotopy is
(S+Z), where

\[
Z\in Z^{-1}\operatorname{Hom}(C,\bar C).
\]

Two such witnesses are related by a degree (-2) comparison precisely
when their difference is a boundary.  Therefore the set of homotopy
witnesses modulo 2-homotopy is a torsor for

\[
H^{-1}\operatorname{Hom}(C,\bar C).
\]

Consequently:

\[
\boxed{
H^{-1}\operatorname{Hom}(C,\bar C)=0
\iff
\text{the homotopy witness is unique up to a 2-cell}.
}
\]

This is the exact algebraic condition under which a compiler may erase
the identity of a first-level comparison path, subject still to source
authority for the flattening operation.

## Finite rank certificate

For the finite segment

\[
H^{-2}\xrightarrow{\partial_{-2}}H^{-1}
\xrightarrow{\partial_{-1}}H^0,
\]

the obstruction dimension over a field is

\[
\dim H^{-1}
=
\dim H^{-1}_{\rm chain}
-\operatorname{rank}(\partial_{-1})
-\operatorname{rank}(\partial_{-2}).
\]

Here the chain condition guarantees
(\operatorname{im}\partial_{-2}\subseteq
\ker\partial_{-1}).  A machine certificate contains the two matrices,
their product-zero check, and the resulting dimension.

Two one-dimensional examples over (mathbf F_2):

- safe: (partial_{-2}=1, partial_{-1}=0), so every ambiguity is a
  higher boundary and (H^{-1}=0);
- unsafe: (partial_{-2}=0, partial_{-1}=0), so
  (dim H^{-1}=1).

The endpoint maps and first homotopy equation can be identical in both
cases.  The difference lies entirely in the available higher coherence.

## Depth-(r) truncation

Erasing comparison data through depth (r) requires

\[
H^{-j}\operatorname{Hom}(C,\bar C)=0,
\qquad 1\le j\le r.
\]

Vanishing only at degree (-1) licenses only first-level path
flattening.  It does not license wholesale conversion of a constructor
tree into a flat authority token.

## Compiler protocol

1. Verify the endpoint chain-map and homotopy equations.
2. Construct the bounded negative Hom differential matrices.
3. Check every consecutive product is zero.
4. Compute the requested negative cohomology dimensions.
5. Reject flattening at the first nonzero dimension.
6. Even on vanishing, require a named source-authorized flattening
   constructor; algebraic uniqueness does not manufacture authority.

```json
{
  "code": "coherence_flattening_obstructed",
  "first_nonzero_degree": -1,
  "cohomology_dimension": 1
}
```

## Research boundary

This converts an open-ended higher-coherence warning into a bounded
linear-algebra gate for finite complexes.  It does not assert that the
relevant complexes are finite, that their negative cohomology vanishes,
or that flattening preserves non-algebraic support and fault semantics.

