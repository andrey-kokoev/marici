# The Schwartz four-trace port canonically supplies the core Clark colocation map

## Source trace and transpose column

On the Schwartz core define

\[
\Gamma_4f
=
\left(
 f(0),
 \int f(x)\,dx,
 f'(0),
 \int xf(x)\,dx
\right).
\]

Its canonical transpose column is the independently source-defined
distributional map

\[
W_\Gamma(a_P,a_Q,a_M,a_J)
=
a_P\delta_0
+a_Q\mathbf1
-a_M\delta_0'
+a_Jx.
\]

With the standard distribution convention

\[
\langle\delta_0',f\rangle=-f'(0),
\]

we have exactly

\[
W_\Gamma^\times=\Gamma_4.
\]

This is not a metric-fitted adjoint. It is the canonical
Schwartz--tempered-distribution transpose of the four source traces.

## Clark reduction

Let

\[
\mathcal O_{\rm Cl}=S_{\rm Cl}\Gamma_4,
\qquad
W_{\rm Cl}=W_\Gamma S_{\rm Cl}^*.
\]

Then

\[
W_{\rm Cl}^\times
=S_{\rm Cl}W_\Gamma^\times
=S_{\rm Cl}\Gamma_4
=\mathcal O_{\rm Cl}.
\]

Use the oriented degree-zero projection

\[
\beta_0(y,b)=-b
\]

for the Grushin border convention

\[
\mathcal G_{\rm Cl}
=
\begin{pmatrix}
P_{\rm loc}&-W_{\rm Cl}\\
-W_{\rm Cl}^\times&0
\end{pmatrix}.
\]

Together with

\[
\beta_{-1}(x,a)=x,
\]

the chain equation becomes

\[
\mathcal O_{\rm Cl}\beta_{-1}
=
\beta_0\mathcal G_{\rm Cl}.
\]

Thus the core characteristic-to-Green Clark chain map is exact with the
source orientation; the earlier minus-colocation version differed only by the
choice of degree-zero projection orientation.

## What is constructed

On the Schwartz/strong-dual source core, this supplies:

- the four-port forcing column;
- the four-port observation row;
- canonical rigged colocation;
- the Clark-reduced chain square;
- retention of the Clark relative kernel before scalarization.

## Remaining identification

The Grushin candidate uses a previously named arithmetic/history column
`W_01` in the completed pencil domain. To promote the core chain map, one must
prove

\[
W_{01}=W_\Gamma
\]

after transport through the Volterra/history and arithmetic incidence maps,
or provide a source comparison between them. Matching dimension and Fourier
order-four action is insufficient.

The remaining gate is therefore no longer abstract colocation. It is the
concrete history-to-moment port identification on the common completed rigged
domain.