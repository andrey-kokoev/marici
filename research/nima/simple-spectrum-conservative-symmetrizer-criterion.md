# Simple-spectrum conservative symmetrizer criterion

Assume the finite carrier generator `A` is Hermitian with simple spectrum. In an orthonormal eigenbasis,

$$
A=\operatorname{diag}(\lambda_i).
$$

Every Hermitian `K` satisfying

$$
AK=KA
$$

is diagonal in this basis:

$$
K=\operatorname{diag}(k_i),
\qquad k_i\in\mathbb R.
$$

For the bordered metric

$$
J=\operatorname{diag}(\alpha,K),
\qquad \alpha\in\mathbb R,
$$

the port equation `Kb=alpha c` becomes

$$
k_ib_i=\alpha c_i
$$

coordinatewise.

## Nondegenerate criterion

A nondegenerate symmetrizer exists exactly when one can choose `alpha != 0` and real `k_i != 0` such that:

1. `b_i=0` if and only if `c_i=0`;
2. whenever `b_i` and `c_i` are nonzero,
   $$
   \frac{c_i}{b_i}\in\mathbb R\setminus\{0\};
   $$
3. on coordinates where `b_i=c_i=0`, choose any nonzero real `k_i`.

Indeed, after fixing any nonzero real `alpha`, set

$$
k_i=\alpha\frac{c_i}{b_i}
$$

on the active support.

## Positive criterion

A positive symmetrizer exists exactly when the common active support condition holds and all active real ratios have one positive sign after the boundary orientation is fixed. With `alpha>0`, this is

$$
\frac{c_i}{b_i}>0
$$

for every active eigenchannel. Inactive `k_i` may then be chosen positive.

Thus the conservative gate separates into three source tests:

- support matching;
- reality of each eigenchannel port ratio;
- common positivity orientation of those ratios.

An indefinite solution establishes reciprocal spectral symmetry only. Positive confinement requires the final common-sign test.

Status: simultaneous finite simple-spectrum symmetrizer and colocation criterion proved. Evaluation on the source-derived Xi/Green ports remains open.
