# 2674 — The Finite Cotangent–Transitivity Complex Has Dimensions Eight and Fifteen

## Frozen map

Let \(R=P/I\) be the length-seven localized Cayley–Menger quotient. The three labelled Kodaira–Spencer sections define the full \(R\)-linear transitivity map

\[
\kappa:R^3\longrightarrow R^4.
\]

Unlike the earlier rank of three displayed section vectors, this map includes multiplication by all seven standard monomials in every source direction.

## Exact finite result

Across A, B, and HOMA and primes 32003 and 65521,

\[
\operatorname{rank}_{\mathbb F_p}(\kappa)=13.
\]

Since the source and target dimensions are \(21\) and \(28\), respectively,

\[
\dim\ker\kappa=8,
\qquad
\dim\operatorname{coker}\kappa=15.
\]

The dimensions replicate uniformly.

## Narrow result

The correctly typed finite cotangent-transitivity object is a nontrivial two-term complex with cohomological dimensions \(8\) and \(15\). The earlier unique relation among the three displayed pair wedges is only a low-generator shadow of this larger module-level structure.

Consequently, Entry 2662's rank-four visible obstruction must be located as a secondary operation on this \((8,15)\) interface. It cannot be classified solely by the three scalar pair labels.

## Artifacts

- `research/benincasa/marici-gm/src/bin/cm_normal_tower_rank.rs`
- `research/benincasa/checkers/check_cm_conormal_kodaira_spencer.py`
- `research/benincasa/results/cm-conormal-kodaira-spencer.json`

## Next falsifier

Export bases for \(\ker\kappa\) and \(\operatorname{coker}\kappa\), then derive the induced tracked-reduction connection on those quotient objects. Test whether the visible curvature obstruction descends to a basis-independent map from the eight-dimensional kernel to the fifteen-dimensional cokernel or its appropriate shifted endomorphism.
