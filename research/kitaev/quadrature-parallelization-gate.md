# Complementary sheet forms require a common amplitude frame

## Bounded question

Does retaining both sheets automatically upgrade the two rank-one energies
to \(2|\psi|^2\) when the sheet action also transports the amplitude?

## Two inequivalent sums

Let

\[
E_+=I+Q,
\qquad
E_-=I-Q,
\qquad
R^TQR=-Q.
\]

If both forms are evaluated on one already identified amplitude vector, then

\[
x^TE_+x+x^TE_-x=2x^Tx.
\]

This is the positive-definite common-frame sum.

But the sheet transport sends \(x_-=Rx_+\). Pulling the minus-sheet energy
back along that transport gives

\[
R^TE_-R=R^T(I-Q)R=I+Q=E_+.
\]

Therefore the covariantly transported sum is

\[
x^TE_+x+(Rx)^TE_-(Rx)=2x^TE_+x,
\]

which is still rank one at \(|\lambda|=1\). The same null quadrature survives.

## Parallelization theorem

To add quadratic forms on different sheet fibers, one needs an explicit
comparison map

\[
P:V_+\longrightarrow V_-.
\]

The pulled-back total form is

\[
H_P=(I+Q)+P^T(I-Q)P.
\]

Full finite positivity is exactly the condition \(H_P>0\). At
\(\theta=0\):

- \(P=I\) gives \(H_P=2I\), rank two;
- \(P=R\) gives \(H_P=2(I+Q)\), rank one.

Both maps are orthogonal. Consequently orthogonality, sheet equivariance, and
individual nonnegativity do not select the comparison that closes the null
direction.

## Explanatory consequence

The earlier statement “opposite sheets sum to the norm” contained an implicit
fiber identification. The genuine architecture has four layers:

```text
two sheet fibers
    -> sheet transport R
    -> independently typed amplitude parallelization P
    -> scalar sum H_P
```

The torsor displacement labels the sheets; it is not automatically the
parallelization used to add their energies. In fact, using the displacement
itself is the exact failure case.

This makes the RH diagnostic stricter. Grothendieck must derive not only an
opposite spin-two character, but also the comparison by which the direct and
reciprocal Green amplitudes enter one quadratic form. A choice of \(P=I\)
made solely because it produces \(2I\) would fit the desired answer.

## Falsifier and boundary

The finite falsifier is

\[
R^T(I-Q)R=I+Q.
\]

It refutes the claim that covariant retention of both sheets alone guarantees
strict positivity.

This packet does not determine Grothendieck's actual comparison map. The
doubled-tail operator, endpoint pairing, Clark shear, and Mellin normalization
must type it. Even a positive finite \(H_P\) would still require completion
stability and exclusion of uncontrolled distributional states.

## Verification

Run:

```text
uv run --with sympy python research/kitaev/checkers/check_quadrature_parallelization_gate.py
```

The checker verifies both sums symbolically over
\(\mathbf Q[c,s]/(c^2+s^2-1)\) and specializes at \(\theta=0\) to certify the
rank-two versus rank-one distinction.
