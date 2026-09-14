# Complete polyphase CP branches reconstruct the prime heat magnitude

## Residue-class completion

For an integer dilation \(r\), define grade branches

\[
S_{r,j}e_n=e_{rn+j},
\qquad
0\leq j<r.
\]

Their ranges are mutually orthogonal and jointly cover every target grade. Each branch has a completely positive square lift

\[
\mathcal E_{r,j}(X)=S_{r,j}^*XS_{r,j}.
\]

Branch composition follows the digit law

\[
S_{r,j_2}S_{r,j_1}e_n
=e_{r^2n+rj_1+j_2}.
\]

Thus repeated binary refinement generates all residue classes modulo \(2^m\), not only the divisible-grade Adams ray.

## Heat weighting

For positive grade weights \(w_n\), attach the diagonal branch multiplier

\[
m_{r,j,t}(n)
=
\sqrt{\frac{w_{rn+j}}{w_n}}
\exp\left(
-\frac t2\bigl((rn+j)^2-n^2\bigr)(\log p)^2
\right).
\]

Applied to the heat state with coefficient

\[
\sqrt{w_n}e^{-tn^2(\log p)^2/2},
\]

the branch produces exactly

\[
\sqrt{w_{rn+j}}e^{-t(rn+j)^2(\log p)^2/2}.
\]

Summing squared norms over every residue branch reconstructs the complete positive prime-grade heat magnitude. This repairs the support loss of the single Adams branch.

## Boundary

The construction applies to positive prime magnitudes. In the completed explicit formula the prime heat sector enters with a negative sign. Therefore an orthogonal direct sum of these CP branches gives the wrong sign for the Weil observer.

Endpoint and gamma cannot be added as independent positive summands to repair it; earlier sectorwise no-go results forbid that move.

Hence the polyphase construction supplies a complete positive carrier for the unsigned prime heat source, but the RH-bearing step remains a coupled indefinite-to-positive transformation incorporating endpoint and gamma before terminal polarization.

The next candidate must therefore be a Julia/Schur-type colligation in which the positive prime CP row is a contractive off-diagonal channel against an archimedean state space, rather than a negative direct summand.

## Verification

```text
python research/voevodsky/checkers/check_complete_grade_polyphase_CP_decomposition.py
```

Artifacts:

- `research/voevodsky/checkers/check_complete_grade_polyphase_CP_decomposition.py`
- `research/voevodsky/results/complete_grade_polyphase_CP_decomposition.json`
