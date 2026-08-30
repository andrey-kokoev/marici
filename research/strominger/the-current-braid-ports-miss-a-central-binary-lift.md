# The Current Braid Ports Miss a Central Binary Lift

## Question

Does projective nonabelian monodromy terminate the zero-defect coherence
tower?

## Central hostile

Let

\[
\Omega=(\sigma_1\sigma_2\sigma_3)^4.
\]

For the four-strand spherical braid group, the standard group theorem says
that \(\Omega\) is the nontrivial generator of the order-two center.

Every previously constructed port misses it:

- its endpoint permutation is the identity;
- its action on the static \(A_3\) endpoint lattice is the identity;
- its exponent sum is twelve, hence zero in both \(\mathbb Z/6\) and
  \(\mathbb Z/3\);
- under the projective matrix detector,

\[
TUT=
\begin{pmatrix}0&1\\-1&0\end{pmatrix},
\qquad
(TUT)^2=-I,
\qquad
(TUT)^4=I.
\]

Thus the current joint observation packet identifies the identity braid with
a nontrivial central braid.

## Consequence

A further binary central lift is necessary. It records whether a projectively
trivial loop lifts to the trivial or nontrivial central class.

This is a necessity theorem, not yet a termination theorem. To prove that the
binary lift is sufficient, one must still establish

\[
\ker(\text{endpoint},\rho)=\langle\Omega\rangle.
\]

The exact kernel equality is not inferred from the matrix hostile.

## Shift in perspective

The projective port did not merely leave an unspecified residual kernel. It
forgot a specifically typed distinction: the lift of projective monodromy
through a central double cover. The next rung is therefore not another scalar
moment. It is a lift datum.

## Verification

```powershell
uv run --with sympy python research/strominger/checkers/central_full_twist_hostile_checks.py
```
