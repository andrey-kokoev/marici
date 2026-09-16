# The prime-power translation Laplacian is the first explicit source-derived positive spectral carrier candidate

## Objective

Seek a positive arithmetic Hilbert feature before invoking zeros, Blaschke factors, or an assumed positive de Branges kernel.

The prime part of the explicit formula is built from correlations at logarithmic prime-power displacements. Such correlations admit a canonical graph-Laplacian completion.

## Translation representation

Let

\[
\mathcal H_{src}
=L^2(\mathbb R,dt/2\pi)
\]

be the Mellin boundary carrier. Logarithmic translation of the original source becomes the unitary character representation

\[
(U_\ell m)(t)
=e^{it\ell}m(t).
\]

Thus prime-power evaluation of a convolution square is a matrix coefficient of \(U_\ell\).

For each prime power \(q=p^j\), set

\[
\ell_q
=\log q
\]

and use the positive arithmetic weight

\[
a_q
=\frac{\Lambda(q)}{\sqrt q}.
\]

Only positivity of \(a_q\) is used in the Hilbert construction.

## Finite prime-power feature

For a finite prime-power set \(Q\), define

\[
\Phi_Qm
=
\bigoplus_{q\in Q}
\sqrt{a_q/2}
(I-U_{\ell_q})m.
\]

This maps into

\[
\mathcal K_Q
=
\bigoplus_{q\in Q}
\mathcal H_{src}.
\]

Its Gram operator is

\[
L_Q
=
\Phi_Q^*\Phi_Q
=
rac12\sum_{q\in Q}
a_q
(2I-U_{\ell_q}-U_{-\ell_q}).
\]

Therefore

\[
L_Q\succeq0.
\]

No zero data or divisor factorization enters this positivity theorem.

## Correlation expansion

For every \(m\in\mathcal H_{src}\),

\[
\|\Phi_Qm\|^2
=
\sum_{q\in Q}a_q\|m\|^2
-
\sum_{q\in Q}a_q
\operatorname{Re}
\langle m,U_{\ell_q}m\rangle.
\]

The second term has exactly the sign and displacement pattern of the symmetric prime-power correlation channel in the explicit formula.

Thus the negative-looking prime correlation can be rewritten as

\[
-\sum_{q\in Q}a_q
\operatorname{Re}
\langle m,U_{\ell_q}m\rangle
=
\|\Phi_Qm\|^2
-
A_Q\|m\|^2,
\]

where

\[
A_Q
=
\sum_{q\in Q}a_q.
\]

The price of the positive factorization is the diagonal counterterm

\[
A_QI.
\]

## Completed arithmetic decomposition target

Let \(Q_Q^{arith}\) denote the endpoint--gamma--prime form truncated to \(Q\). The desired exact comparison has the shape

\[
Q_Q^{arith}(m)
=
\|\Phi_Qm\|^2
+
Q_{\Gamma,\partial}(m)
-
A_Q\|m\|^2.
\]

Define the renormalized archimedean-endpoint residual

\[
R_Q^{\Gamma,\partial}(m)
=
Q_{\Gamma,\partial}(m)
-
A_Q\|m\|^2.
\]

Then

\[
Q_Q^{arith}(m)
=
\|\Phi_Qm\|^2
+
R_Q^{\Gamma,\partial}(m).
\]

This isolates the exact place where positivity can fail. The prime-power channel itself has a source-derived positive Hilbert feature; the issue is whether the completed diagonal renormalization and endpoint channel form a positive residual.

## Symmetric edge interpretation

Each prime power contributes one weighted undirected edge between a source state and its logarithmic translate. The operator

\[
2I-U_\ell-U_{-\ell}
\]

is the Laplacian of that edge.

Hence \(L_Q\) is the weighted Laplacian of the finite arithmetic translation graph. Prime extension adds positive edges:

\[
Q\subset Q'
\quad\Longrightarrow\quad
L_Q\preceq L_{Q'}.
\]

This gives strict functoriality under prime cutoff before renormalization.

## Convolution naturality

A convolution successor acts in Mellin variables by multiplication with \(m_a\). Since \(U_\ell\) is also a multiplication operator,

\[
U_\ell M_{m_a}
=
M_{m_a}U_\ell.
\]

Therefore

\[
(I-U_\ell)M_{m_a}
=
M_{m_a}(I-U_\ell).
\]

The prime edge feature is exactly natural under admitted convolution multipliers; no commutator correction occurs in the Mellin chart.

## Infinite prime-power carrier

The formal infinite feature is

\[
\Phi_{prime}m
=
\bigoplus_q
\sqrt{a_q/2}(I-U_{\ell_q})m.
\]

Its natural form domain is

\[
\mathcal D_{prime}
=
\left\{
m:
\sum_q
a_q
\|(I-U_{\ell_q})m\|^2
<\infty
\right\}.
\]

On this domain, the monotone limit

\[
L_{prime}
=
rac12\sum_q
a_q
(2I-U_{\ell_q}-U_{-\ell_q})
\]

defines a closed positive quadratic form.

The unrenormalized diagonal coefficient \(A_Q\) diverges. Therefore the completed arithmetic form cannot be obtained by separating the two diagonal and correlation sums after passing to the infinite cutoff. Their finite-cutoff pairing must be retained until gamma and endpoint renormalization is included.

## Relation to the augmented horn

A successful arithmetic realization would combine:

\[
\Phi_{prime},
\qquad
\Phi_\Gamma,
\qquad
\Phi_\partial
\]

into one feature \(\Phi_{arith}\) satisfying

\[
A_{S,r}^*A_{S,r}
=
\Phi_{arith,r}^*
\Phi_{arith,r}.
\]

The interior and endpoint defect rows would then need to arise as a joint contraction of this common carrier.

The prime Laplacian supplies the first explicit positive summand of such a carrier. It does not yet supply the completed diagonal residual or the defect-row contraction.

## Hostile audit

A formal manipulation that drops

\[
-A_Q\|m\|^2
\]

would make every prime truncation positive but would no longer equal the explicit formula.

Likewise, absorbing this term into an unspecified infinite constant would hide the entire arithmetic sign problem. The diagonal counterterm must be matched exactly against the gamma, endpoint, and cutoff normalization.

## Next calculation

On the fixed normalization of the completed Weil form, compute the finite-cutoff identity

\[
Q_{\Gamma,\partial,Q}
-
A_QI
\]

on translated Gaussian packets.

The decisive alternatives are:

1. it has an independent positive feature and a monotone limit;
2. it combines with a finite-dimensional endpoint row by a Schur complement;
3. it remains indefinite, showing that the edge-Laplacian carrier alone is insufficient.

This calculation is normalization-sensitive and must retain the exact endpoint residues.

## Disposition

The prime-power correlations admit a canonical, zero-free, source-derived positive realization as a weighted translation Laplacian.

The full arithmetic positivity problem is reduced, in this presentation, to the renormalized archimedean-endpoint diagonal residual and its coupling to the odd endpoint row. No positivity claim is made for that residual yet.
