# A positive collocating port metric exists exactly when the source endpoint pairing is positive

## Abstract one-port problem

Let \(X\) be a Hilbert space, let

\[
B:\mathbb C\to X,\qquad Bc=bc,
\]

with \(b\ne0\), and let

\[
C:X\to\mathbb C,\qquad Cx=\langle c,x\rangle
\]

for the Riesz vector \(c\) in the reference metric.

Seek a bounded positive invertible metric operator \(G\) such that the output
is the adjoint of the input in the \(G\)-metric:

\[
C=B^{*_{G}}.
\]

Since

\[
B^{*_{G}}x=\langle Gb,x\rangle,
\]

the equation is exactly

\[
Gb=c.
\]

## Exact feasibility criterion

If \(G>0\), then

\[
Cb
=
\langle c,b\rangle
=
\langle Gb,b\rangle
>
0.
\]

Thus positivity of the scalar endpoint pairing is necessary.

It is also sufficient. Put \(e_1=b/\|b\|\) and decompose

\[
c=\alpha e_1+d,
\qquad
d\perp e_1.
\]

The condition is

\[
\alpha\|b\|=\langle c,b\rangle>0.
\]

If \(d\ne0\), let \(e_2=d/\|d\|\). On
\(\operatorname{span}\{e_1,e_2\}\), choose

\[
G=
\begin{pmatrix}
\alpha/\|b\| & \|d\|/\|b\|\\
\|d\|/\|b\| & \gamma
\end{pmatrix},
\]

with

\[
\gamma>
\frac{\|d\|^2}{\alpha\|b\|}.
\]

Extend \(G\) by the identity on the orthogonal complement. Then \(G\) is
positive invertible and \(Gb=c\). The case \(d=0\) is immediate.

Therefore

\[
\exists\,G>0,\ G^{-1}\in\mathcal B(X),\ Gb=c
\quad\Longleftrightarrow\quad
Cb>0
\]

after the source phase convention makes the pairing real.

## Application to the theta scalar cone

For the doubled tail source,

\[
Bc=(fc,fc),
\]

and

\[
C(g_+,g_-)=g_+(0)+g_-(0).
\]

Hence

\[
CB=2f(0).
\]

For the standard theta forcing with source-fixed positive normalization,

\[
f(0)>0.
\]

Thus there is no finite algebraic obstruction to a positive collocating metric.
The previously observed inequality \(C\ne B^*\) is a defect of the plain
bulk metric, not a proof that every positive metric fails.

## Determinant preservation

Changing the Hilbert metric does not alter the algebraic blocks
\(A_z,B,C,D\) or their Schur complement

\[
S_\partial(z)=D-CA_z^{-1}B.
\]

Therefore a source-authorized collocating metric would repair port adjointness
without changing the already established scalar determinant provenance.

This is categorically different from adding a fitted feedback block, which
changes the Schur complement.

## Uniform completion criterion

Pointwise existence is insufficient. For a cutoff family
\((b_X,c_X)\), define

\[
\eta_X
=
\frac{\operatorname{Re}\langle c_X,b_X\rangle}
{\|b_X\|\,\|c_X\|}.
\]

A uniformly positive angle

\[
\inf_X\eta_X>0
\]

together with uniform control of \(\|b_X\|/\|c_X\|\) and its reciprocal yields
uniformly bi-bounded choices of \(G_X\). If \(\eta_X\to0\), every collocating
metric becomes ill-conditioned in the source frame.

Thus the completion gate is an absolute frame condition, not merely
\(C_XB_X>0\) at each cutoff.

## Source-authority gate

The existence construction above is not yet a theta theorem. It chooses
\(\gamma\) and the complement metric freely.

The admissible metric must be independently produced by the complete
polarized Green form, including:

- the tail graph;
- endpoint wall and jump ports;
- primitive and square anomaly lines;
- connected determinant-three tail;
- archimedean attachment;
- reciprocal sewing.

The exact audit is then

\[
G_{\mathrm{src}}b=c.
\]

If this identity holds, port closure is source-derived. If it fails, the
abstract existence of another \(G\) is irrelevant.

## Multiport extension

For \(B:U\to X\) and \(C:X\to U\), collocation requires

\[
GB=C^*.
\]

A necessary condition is positivity of the finite port Gram

\[
CB:U\to U.
\]

On the reduced port support, strict positivity of \(CB\) and compatibility of
the kernels are the finite-rank analogues of the one-port criterion.
Completion again requires uniform metric equivalence.

This is the correct form for the full boundary packet.

## Hostiles

1. Conclude from \(C\ne B^*\) that no positive collocating metric exists.
2. Choose \(G\) from the equation \(Gb=c\) and call it source-derived.
3. Verify only \(Cb>0\) at every finite cutoff while the angle tends to zero.
4. Rescale \(b\) and \(c\) reciprocally without preserving the source frame.
5. Use an indefinite metric when a positive source metric is claimed.
6. Repair adjointness by changing \(C\), thereby changing the scalar divisor.

## Verdict

For one port, positive metric collocation is possible exactly when the
source endpoint pairing \(CB\) is positive. The standard theta forcing passes
this algebraic feasibility test because \(CB=2f(0)>0\).

The determinant can remain unchanged under this repair. The live theorem is
now source-specific and quantitative:

\[
G_{\mathrm{src}}B=C^*
\]

with \(G_{\mathrm{src}}\) the complete polarized Green metric and uniformly
bounded equivalence through completion.
