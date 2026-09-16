# The proposed relative-to-absolute Mosco statement is not yet well typed

## Proposed statement

The frontier has been written schematically as

\[
\underset{\alpha}{\operatorname{Mosco\!-\!lim}}\;
q_\alpha^{relative}
=
q_{|\mathcal A_S|}.
\]

Before proving Mosco convergence, one must decide what
\(q_\alpha^{relative}\) means. The two natural interpretations have different limits.

## Signed relative readout

The exact regulated relative feature has a signed readout

\[
s_\alpha(g,h)
=
\langle X_\alpha^Tg,X_\alpha^Th\rangle
-
\langle X_\alpha^0g,X_\alpha^0h\rangle.
\]

Its established boundary value is the Tate form

\[
s(g,h)
=
\langle g,\mathcal A_Sh\rangle_{\mathscr E_S}.
\]

Therefore the signed relative forms can converge only to the form of
\(\mathcal A_S\), not to the form of \(|\mathcal A_S|\), unless
\(\mathcal A_S\) is already nonnegative.

Moreover ordinary Mosco convergence is formulated for closed lower-semibounded forms. The signed Tate forms are not the positive forms required by the proposed target.

Thus the assignment

\[
q_\alpha^{relative}:=s_\alpha
\]

makes the proposed statement false or ill typed.

## Total Gram of the fixed Krein splitting

A second possible interpretation is the ordinary positive Gram

\[
t_\alpha
=
G_\alpha^T+G_\alpha^0.
\]

For the fixed-signature eight-leg feature,

\[
G_\alpha^T-G_\alpha^0=D_\alpha,
\]

but this does not imply

\[
G_\alpha^T+G_\alpha^0=|D_\alpha|.
\]

A fixed Krein splitting is generally nonminimal. It can contain a balanced positive summand invisible to the signed difference. Hence its total Gram need not converge to
\(|\mathcal A_S|\).

Thus the assignment

\[
q_\alpha^{relative}:=t_\alpha
\]

is positive but has the wrong target unless a minimalization theorem removes its balanced excess.

## Correct finite positive candidate

Suppose the two physical positive Grams have a common face

\[
G_{phys,\alpha}^T
=B_\alpha^*B_\alpha+R_\alpha^T,
\]

\[
G_{phys,\alpha}^0
=B_\alpha^*B_\alpha+R_\alpha^0.
\]

The appropriate positive residual form is

\[
r_\alpha(g)
=
\langle g,(R_\alpha^T+R_\alpha^0)g\rangle.
\]

Equivalently,

\[
r_\alpha
=
G_{phys,\alpha}^T+G_{phys,\alpha}^0
-2B_\alpha^*B_\alpha.
\]

Its signed companion is

\[
R_\alpha^T-R_\alpha^0=D_\alpha.
\]

For the target to be \(q_{|\mathcal A_S|}\), one must additionally show that the residual pair becomes asymptotically minimal:

\[
R_\alpha^T
\sim
(\mathcal A_S)_+,
\qquad
R_\alpha^0
\sim
(\mathcal A_S)_-.
\]

Only then does

\[
R_\alpha^T+R_\alpha^0
\sim
|\mathcal A_S|.
\]

## Internal cell versus minimal boundary

Strict commutativity of the two polarized sub-tetrahedra proves that their common face is the same:

\[
B_\alpha^T=B_\alpha^0.
\]

It does not prove that the complementary residual pair is the minimal Jordan pair of its signed difference. A positive cell can retain balanced residual mass in both polarities.

Therefore local cell commutativity closes common-face equality but does not by itself close absolute-Gram minimalization.

## Correct order of the global gate

The regular boundary problem has three stages.

1. **Define the positive residual form**
   \[
   r_\alpha
   =R_\alpha^T+R_\alpha^0.
   \]

2. **Prove asymptotic minimality** by showing that balanced residual mass disappears in the phase-energy topology.

3. **Prove Mosco convergence** of \(r_\alpha\) to the closed form of \(|\mathcal A_S|\).

The current repository proves the signed boundary identification, but it has not yet supplied stage 2 globally.

## Immediate falsification test

If there exists a nonzero positive form \(K_\alpha\) such that

\[
R_\alpha^T
=(D_\alpha)_++K_\alpha,
\]

\[
R_\alpha^0
=(D_\alpha)_-+K_\alpha,
\]

then

\[
R_\alpha^T-R_\alpha^0=D_\alpha
\]

while

\[
r_\alpha
=|D_\alpha|+2K_\alpha.
\]

Thus signed convergence gives no information about the disappearance of
\(K_\alpha\). This balanced excess is the exact obstruction to the proposed absolute-form limit.

## Revised statement

After constructing the common-face residuals, the meaningful target is

\[
\underset{\alpha}{\operatorname{Mosco\!-\!lim}}\;
r_\alpha
=
q_{|\mathcal A_S|},
\]

where

\[
r_\alpha
=
G_{phys,\alpha}^T+G_{phys,\alpha}^0
-2B_\alpha^*B_\alpha.
\]

This statement is positive and well typed. It remains open because global asymptotic minimality and the Mosco liminf/recovery estimates have not been proved.

## Disposition

The notation \(q_\alpha^{relative}\) currently conflates the signed relative readout with the positive absolute residual. The signed form has limit \(\mathcal A_S\); the positive residual is the candidate for the limit \(|\mathcal A_S|\).

The first active task is therefore not yet a Mosco estimate. It is construction and asymptotic minimalization of the positive residual forms \(r_\alpha\).
