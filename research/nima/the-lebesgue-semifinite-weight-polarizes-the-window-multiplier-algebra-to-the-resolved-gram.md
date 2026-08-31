# The Lebesgue semifinite weight polarizes the window multiplier algebra to the resolved Gram

## Endpoint multiplication algebra

Let

\[
\mathcal A=L^\infty(\mathbb R,dq)
\]

act on \(L^2(\mathbb R,dq)\) by multiplication.  The source coordinate \(q\)
and its Lebesgue measure are already fixed by the Gaussian front

\[
f_0(q)=e^{-\pi q^2}.
\]

On the positive cone of \(\mathcal A\), define

\[
\tau(M_f)=\int_{\mathbb R}f(q)\,dq,
\qquad f\ge0,
\]

allowing the value \(+\infty\).

This is the canonical faithful normal semifinite weight of the commutative
Lebesgue multiplication algebra.  It is a trace on its finite ideal because
the algebra is commutative.  It is not the Hilbert-space operator trace on
\(\mathcal B(L^2)\).

## Square-integrable weight domain

The associated \(L^2\)-ideal is

\[
\mathfrak n_\tau
=
\{M_f:\tau(M_f^*M_f)<\infty\}
=
\{M_f:f\in L^2(\mathbb R)\}.
\]

For \(f,g\in L^2\), Cauchy--Schwarz gives

\[
\tau(M_f^*M_g)
=\int\overline{f(q)}g(q)\,dq,
\]

and

\[
|\tau(M_f^*M_g)|
\le\|f\|_2\|g\|_2.
\]

Thus

\[
\langle M_f,M_g\rangle_\tau
:=\tau(M_f^*M_g)
\]

is exactly the ordinary Lebesgue Hilbert pairing on the finite-weight ideal.
Its completion is canonically \(L^2(\mathbb R,dq)\).

## Admission of the window history

Every window \(W_t\) belongs to \(L^2\), with

\[
\|W_t\|_2^2=2(R(2t)-R(0))<\infty.
\]

Its differentiated front

\[
DW_t=q_t
\]

is a finite Gaussian difference and also belongs to \(L^2\).  Therefore

\[
M_{W_t},M_{q_t}\in\mathfrak n_\tau.
\]

All endpoint and derivative products needed for a finite first-Adams cell lie
in the \(\tau\)-finite \(L^1\) ideal.

## Resolved feature polarization

The selected resolved feature map is

\[
\mathcal Rf=(f,Bf,M_\Phi f).
\]

Since \(B\) is bounded on \(L^2\), it preserves the finite-weight domain.
Equip the three multiplier coordinates with the direct-sum weight

\[
\tau^{(3)}=	au\oplus\tau\oplus\tau.
\]

Then

\[
\begin{aligned}
\langle \mathcal Rf,\mathcal Rg\rangle_{\tau^{(3)}}
&=\tau(M_f^*M_g)
 +\tau(M_{Bf}^*M_{Bg})
 +M_\Phi^2\tau(M_f^*M_g)\\
&=(1+M_\Phi^2)\langle f,g\rangle_2
 +\langle Bf,Bg\rangle_2.
\end{aligned}
\]

Hence

\[
\boxed{
\langle \mathcal Rf,\mathcal Rg\rangle_{\tau^{(3)}}
=g_{\mathrm{res}}(f,g).
}
\]

For \(f=W_L\), \(g=W_{2L}\), this reproduces the complete real resolved
mixed entry, including the explicit positive tail \(g_p\).

## Closedness and radical

The GNS Hilbert space of \((\mathcal A,\tau)\) is \(L^2(\mathbb R)\).  Since
\(B\) is bounded, the resolved feature map is bounded into the threefold GNS
direct sum.  Its graph is closed.

Moreover,

\[
\|\mathcal Rf\|_{\tau^{(3)}}^2
\ge(1+M_\Phi^2)\|f\|_2^2,
\]

so the resolved positive form has zero radical on this domain.

## What this closes

The previously missing polarized endpoint metric is canonical on the
source-generated multiplication algebra:

- it is the Lebesgue semifinite weight, not an arbitrary vector state;
- every window and differentiated front lies in its finite domain;
- its direct-sum resolved polarization is exactly the frozen resolved Green
  form;
- the positive graph is closed and nondegenerate.

## Remaining gate

This construction closes the positive two-column metric identification on the
endpoint multiplier algebra.  It does not yet place the ordered
Stokes/Wronskian linking polarization in the same GNS completion.  That form
contains distributional wall traces and must be shown continuous relative to
the wall-extended graph norm, not merely to \(L^2\).

The earliest local gate is therefore the bounded extension of the ordered
linking form to the joint GNS-plus-wall carrier, followed by radical
compatibility after adding it to the positive resolved block.  Global
prime/grade rigged closed range remains open.  No RH conclusion is authorized.
