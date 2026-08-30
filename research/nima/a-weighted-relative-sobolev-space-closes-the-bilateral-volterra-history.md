# A weighted relative Sobolev space closes the bilateral Volterra history

## Relative history space

Fix \(\epsilon>0\) and let

\[
w(u)=(1+|u|)^{1+\epsilon}.
\]

Define \(\mathcal H_{\mathrm{rel}}\) as the space of locally absolutely continuous functions \(f\) such that

\[
f'\in L^2(\mathbb R,w\,du)
\]

and the two endpoint limits \(f(-\infty)\), \(f(+\infty)\) exist. Use the graph norm

\[
\|f\|_{\mathrm{rel}}^2
=
\int_{\mathbb R}w(u)|f'(u)|^2\,du
+
|f(-\infty)|^2
+
|f(+\infty)|^2.
\]

Because \(w^{-1}\in L^1\), Cauchy--Schwarz gives

\[
\|f'\|_1
\le
\|w^{-1/2}\|_2\,
\|w^{1/2}f'\|_2.
\]

Thus endpoint traces are continuous and the endpoint difference is constrained by

\[
f(+\infty)-f(-\infty)
=
\int_{\mathbb R}f'(u)\,du.
\]

This realizes the wall coordinates and the derivative energy in one closed relative graph.

## Closed Volterra lift

Let the source space be

\[
\mathcal E_w
=
L^1(\mathbb R)\cap L^2(\mathbb R,w\,du)
\]

with its sum norm. For

\[
(H_+g)(u)=\int_{-\infty}^u g(v)\,dv,
\]

one has

\[
(H_+g)'=g,
\qquad
\operatorname{Tr}_-H_+g=0,
\qquad
\operatorname{Tr}_+H_+g=\int g.
\]

Hence

\[
H_+:\mathcal E_w\longrightarrow\mathcal H_{\mathrm{rel}}
\]

is continuous. Its reflected adjoint history has endpoint vector \((\int g,0)\). Their even and odd combinations have endpoint vectors

\[
Sg:\quad
\left(\frac12\int g,\frac12\int g\right),
\]

\[
Tg:\quad
\left(-\frac12\int g,\frac12\int g\right).
\]

Thus constant-wall and oriented-jump coordinates are explicitly separated.

## Relative Green pairing

The odd incidence should be defined by the derivative Green pairing

\[
\mathfrak b_-(f,g)
=
-\int_{\mathbb R}f(u)g'(u)\,du
\]

on the source core, rather than by pretending both factors lie in unweighted \(L^2\). For the theta packet,

\[
(T\Phi)'=\Phi,
\]

so

\[
\mathfrak b_-(\Phi,T\Phi)
=
-\|\Phi\|_2^2.
\]

The even incidence is the wall pairing of the mass coordinate with the constant endpoint vector and equals \(m^2/2\). Both extend continuously on the theta-generated finite-energy subspace.

## Reflection

Reflection acts by

\[
(Rf)(u)=f(-u).
\]

It exchanges endpoint traces, preserves the weighted derivative norm, fixes the constant-wall line, and reverses the oriented-jump line. Therefore \(R\) is unitary on \(\mathcal H_{\mathrm{rel}}\), with exactly the required reciprocal typing.

## Translation and moving weights

A fixed polynomial weight is not uniformly translation invariant. At Mellin displacement \(L\), use the transported weight

\[
w_L(u)=w(u+L)
\]

with the corresponding endpoint half-density metric. Translation is then isometric between the object-indexed relative spaces. Demanding uniform boundedness in one fixed \(w\)-space along an unbounded Adams ray would recreate the earlier topology false positive.

## Remaining gate

The bilateral Volterra constructor is now closable in a concrete wall-extended graph space. The next task is to show the source prime/grade incidence maps land in the transported spaces \(\mathcal E_{w,L}\) with uniform intensive-order bounds and preserve the prime spectral idempotents.
