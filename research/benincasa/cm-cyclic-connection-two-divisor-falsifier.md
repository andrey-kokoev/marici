# Cyclic quadratic connection: two-divisor falsifier

## Frozen question

Entry 2593 proves that the source-derived cyclic transverse-curvature class
defines a horizontal line after quotienting by the three first-normal classes.
The smallest authorized logarithmic model for its scalar connection is

\[
\omega_i
=
c_{\rm soft}\,\partial_{s_i}\log(s_1s_2s_3)
+
c_\Lambda\,\partial_{s_i}\log\Lambda_P,
\qquad s_i=P_i^2,
\]

where

\[
\Lambda_P
=s_1^2+s_2^2+s_3^2
-2s_1s_2-2s_1s_3-2s_2s_3.
\]

The constants were required to be independent of the kinematic sample. No
additional factor was admitted after seeing the data.

## Exact modular test

The quotient connection was computed at five off-divisor squared-momentum
points. Each point supplies three directional equations. The same calculation
was repeated over the independent primes 32003 and 65521.

Solving the two-parameter model from two equations leaves 13 nonzero residuals
among the remaining 13 equations at each prime. Thus the failure is not a bad
prime or a single exceptional sample.

The derivative implementation varies the overridden squared momenta directly
inside both the Cayley--Menger polynomial and all three labelled normal
linears. The established rank-four horizontality test continues to pass.

## Narrow conclusion

The quotient line is horizontal, but its connection is not a constant-residue
sum of the labelled soft logarithms and the momentum-triangle logarithm.

This does not establish a new pole divisor. It leaves three possibilities:

1. a nonconstant regular connection on the existing base;
2. a more complicated rational gauge presentation whose intrinsic support is
   still contained in existing Cayley--Menger support;
3. an additional authorized discriminant visible only after exact
   characteristic-zero reconstruction.

The failed ansatz must not be repaired by adding factors inferred from these
samples.

## Artifacts

- `research/benincasa/checkers/check_cm_cyclic_connection_poles.py`
- `research/benincasa/results/cm-cyclic-connection-poles.json`
- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`

