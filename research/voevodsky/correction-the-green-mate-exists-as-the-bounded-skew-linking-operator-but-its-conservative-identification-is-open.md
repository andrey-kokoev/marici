# Correction: the Green mate exists as the bounded skew linking operator, but its conservative identification is open

> **Normalization refinement:** the abstract `diag(alpha_p,lambda_p)` notation below must not be read as a free parameter in the actual prime-cell comparison. The fixed columns of `Q_p^lin` already determine the even line. See `correction-the-actual-prime-cell-comparison-has-no-free-even-alpha.md`.

## Correction

`correction-the-theta-prime-cell-form-is-only-partial-until-its-green-mate-is-constructed.md` overlooked the previously constructed bounded linking operator.

On the retained wall/incidence graph, the continuous functionals \(\gamma_0\) and \(\eta\) define

\[
C f=\binom{\gamma_0f}{\eta(f)}.
\]

For the source coefficient \(c\), put

\[
J_c=
\begin{pmatrix}0&ic\\-ic&0\end{pmatrix}.
\]

Then

\[
\langle Cf,J_cCg\rangle
=ic\left(
\overline{\gamma_0f}\,\eta(g)
-
\overline{\eta(f)}\,\gamma_0g
\right)
=\mathfrak L_c(f,g).
\]

Because \(\gamma_0\) and \(\eta\) are bounded on the graph domain, \(C^*J_cC\) is a bounded self-adjoint Hermitian linking operator. In the analytic-transpose lane the corresponding skew one-leg operator and its two-output block are already constructed.

Thus the mixed theta Green mate is not absent as an analytic operator. One may take its endpoint-to-odd block to be the appropriate off-diagonal component of \(J_c\), equivalently the normalized `K_link=-J_link/2` in the existing two-output packet.

## What remains genuinely open

The constructed object is a source-level linking form. What is unproved is its identification with the independently selected conservative/Stieltjes two-output cell:

\[
G_S=T_p^*G_WT_p
\]

on the common labelled prime-cell domain, including the oriented mixed entry.

Defining the source metric to be the pullback would make this equality tautological. The required theorem must compare the independently constructed forms.

Accordingly:

- bounded mixed Green mate: constructed;
- complete analytic theta block candidate: constructed;
- source-to-conservative quadratic identification: open;
- authoritative independent comparison package: open.

## Exact remaining residual

For ordered source and target cells

\[
G_S=\begin{pmatrix}a_S&r_S+i\ell_S\\r_S-i\ell_S&d_S\end{pmatrix},
\qquad
G_W=\begin{pmatrix}a_W&r_W+i\ell_W\\r_W-i\ell_W&d_W\end{pmatrix},
\]

and \(T_p=\operatorname{diag}(\alpha_p,\lambda_p)\), the mixed residual is

\[
\mathcal E_{12,p}
=(r_S+i\ell_S)-\alpha_p\lambda_p(r_W+i\ell_W).
\]

Its imaginary part is precisely the surviving antiunitary-reflection defect coordinate. Boundedness and correct orientation of the source linking operator do not force this residual to vanish.

## Revised acceptance sequence

1. adopt the already constructed source linking operator as the theta mixed block;
2. expose the independently sourced complete forms on a common domain, using the already fixed \(Q_p^{\rm lin}\);
3. test both diagonal identities and the complex mixed identity;
4. only then promote the linking row into the conservative G4 comparison.

## Claim boundary

This correction closes analytic existence of the mixed theta block. It does not close quadratic functoriality or identify the source form with the conservative/Stieltjes form.
