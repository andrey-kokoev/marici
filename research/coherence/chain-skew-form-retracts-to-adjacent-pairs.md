# The ordered chain skew form reduces to adjacent hyperbolic pairs

## Chain form

For ordered points, write adjacent propagators as nonzero scalars

\[
x_i=e^{-t(a_{i+1}-a_i)}.
\]

The antisymmetric pair matrix has entries

\[
M_{ij}=x_i x_{i+1}\cdots x_{j-1},\qquad i<j.
\]

## Exact minimalization

There is a determinant-one triangular change of basis \(P\) such that

\[
\boxed{
P^TMP
=
\begin{pmatrix}0&x_0\\-x_0&0\end{pmatrix}
\oplus
\begin{pmatrix}0&x_2\\-x_2&0\end{pmatrix}
\oplus\cdots
\oplus H_{\rm odd},
}
\]

where

\[
H_{\rm odd}=
\begin{cases}
0,&n\text{ even},\\
[0],&n\text{ odd}.
\end{cases}
\]

The reduction is constructive. At each pair \((k,k+1)\), elementary congruence shears remove its couplings to every later generator. The multiplicative chain identity ensures that the untouched tail is again a chain form, so the operation iterates.

## Homotopy interpretation

Each nondegenerate block

\[
\begin{pmatrix}0&x\\-x&0\end{pmatrix}
\]

is a paired, acyclic sector: one generator contracts against its partner. The large relation matrix is therefore equivalent to a direct sum of adjacent contractible pairs.

At even size nothing remains. At odd size exactly one zero line remains:

\[
\boxed{
\text{chain relation system}
\simeq
\text{adjacent contractible pairs}
\oplus
\text{one residual line if odd}.
}
\]

This is the previously hidden simplification. Pfaffian matching cancellation is the determinant-line shadow of eliminating those contractible sectors. The odd cofactor state is the original-coordinate presentation of the surviving zero line.

## Consequences recovered at once

The normal form explains:

1. **Even amplitude**
   \[
   \operatorname{Pf}M=x_0x_2\cdots x_{2m-2}.
   \]

2. **Odd residual** — one unpaired line survives.

3. **Even-cut factorization** — the normal form already splits at every even boundary.

4. **Parity-polarized refinement** — inserting a pair either adds one hyperbolic block or changes the chosen contraction pairing, producing the direct/inverse factor.

5. **Minimum matching** — adjacent pairs are not selected after summing matchings; they are the canonical pivots of the minimal skew normal form.

## What “homotopy” means here

The verified statement is an exact congruence of skew forms. Interpreting each invertible two-dimensional block as contractible promotes it to a deformation retract in the associated skew self-dual complex. That promotion requires choosing the complex differential represented by the form, but no further matching identity is needed.

Thus the tower can be compressed to

\[
\boxed{
\bigoplus_r H(x_{2r})
\oplus
\mathbb K^{n\bmod2},
}
\]

where \(H(x)\) is a weighted two-generator hyperbolic/contractible plane.

## Verification

The exact-rational checker constructs the congruence and verifies it in 100 cases of sizes two through eleven:

```text
python research/coherence/check_chain_skew_minimal_model.py
```

Artifacts:

- `check_chain_skew_minimal_model.py`
- `chain-skew-minimal-model.v1.json`
