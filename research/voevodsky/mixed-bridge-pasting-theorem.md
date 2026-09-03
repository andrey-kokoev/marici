# Mixed bridge pasting theorem at finite rank

## Question

Are typed mixed bridges closed and associative under chained algebraic quotients and analytic Schur elimination?

## Claim boundary

This packet proves the generic scalar-block identity underlying finite mixed pasting. It covers arbitrary rational entries satisfying the stated invertibility and positivity predicates. It does not establish unbounded completion or source a gauge Gram form.

## Generic bridge

Let

\[
G=\begin{pmatrix}
a&b&c\\
b&d&e\\
c&e&f
\end{pmatrix}
\]

be positive definite. The first bridge eliminates the kernel tag with pivot \(a\). Its transported blocks are

\[
d_1=d-\frac{b^2}{a},\qquad
e_1=e-\frac{bc}{a},\qquad
f_1=f-\frac{c^2}{a}.
\]

The second bridge eliminates the next kernel tag and yields

\[
f_{12}=f_1-\frac{e_1^2}{d_1}.
\]

Direct elimination of the joint kernel block gives

\[
f_{(12)}=f-\frac{dc^2-2bce+ae^2}{ad-b^2}.
\]

Symbolic reduction proves \(f_{12}=f_{(12)}\) under \(a\ne0\) and \(ad-b^2\ne0\). Positive definiteness supplies these predicates and positivity of every intermediate Schur form.

## Closure

A bridge composite is formed by:

1. composing the algebraic quotient maps;
2. taking the union of their typed kernels;
3. transporting all surviving Gram blocks by the first Schur complement;
4. checking exact equality between the intermediate target form and the next bridge's source form;
5. retaining the direct joint Schur certificate.

The identity above proves the resulting target form is independent of binary parenthesization. Matrix block inversion extends the same argument to finite blocks whenever each pivot certificate is invertible.

## Hostile countermodel

If the first bridge retains the raw cross block \(e\) instead of \(e_1=e-bc/a\), its second quotient is

\[
f_1-\frac{e^2}{d_1},
\]

whose difference from the direct quotient is generically nonzero. The checker factors the numerator of this residual and verifies it is not the zero polynomial. Transported cross data are therefore necessary, not decorative.

## Disposition

Finite mixed bridge pasting is closed and associative under complete bridge certificates and invertible pivots. The checked identity supplies the previously missing finite categorical theorem. The remaining nonredundant frontier is completion: determine whether these bridge certificates survive passage from finite Gram objects to closed forms and common-core operators.

## Verification

- `research/voevodsky/checkers/check_mixed_bridge_pasting_theorem.py`
- `research/voevodsky/results/mixed_bridge_pasting_theorem.json`
