# The ordered Green current is cutoff-independent on the mixed rapid carrier

## Continuous ordered pairing

For radial test functions `f,g` in the two-sided exponential space, define

\[
G(f,g)=\int_{\mathbb R}f(q)(Sg)(q)\,dq.
\]

The order kernel has absolute value one, so

\[
|G(f,g)|
\le \|f\|_1\|g\|_1.
\]

For every `a>0`, weighted Cauchy--Schwarz gives

\[
\|f\|_1
\le
\left(\int_{\mathbb R}e^{-2a|q|}\,dq\right)^{1/2}
\|e^{a|q|}f\|_2
=
a^{-1/2}p_a(f).
\]

Consequently

\[
|G(f,g)|\le a^{-1}p_a(f)p_a(g).
\]

Thus the full ordered Green current is a continuous bilinear form on the
radial test space. No endpoint or relative-response coordinate has been
removed in obtaining this estimate.

## Labelled synthesis

Let

\[
F=\sum_{n\ge1}b_nc_n\tau_{\log n}f,
\qquad
H=\sum_{n\ge1}d_ne_n\tau_{\log n}g,
\]

where the coefficient rows `b_n,d_n` have polynomial-logarithmic growth and
`c,e` belong to the rapid label space. The translation estimate and a stronger
label seminorm imply absolute convergence in every fixed radial seminorm.
Hence

\[
G(F,H)
=
\lim_{A,B}G(F_A,H_B)
\]

for arbitrary cofinal finite label sets `A,B`. The limit is independent of
prime ordering, rectangular versus shell cutoff, and iterated versus joint
cutoff.

This is ordinary continuity of a bilinear map applied after unconditional
convergence; no scalar finite-part prescription is involved.

## Reciprocal orientation

Let radial reflection be `(Rf)(q)=f(-q)`. Directly from the kernel,

\[
RSR=-S.
\]

Therefore

\[
G(Rf,Rg)=-G(f,g).
\]

Reflection is continuous in every symmetric exponential seminorm. It may
therefore be passed through the cutoff limit, giving

\[
G(RF,RH)=-G(F,H)
\]

for the completed labelled syntheses. Reciprocal orientation cannot be lost
through completion on this carrier.

## Dilation bookkeeping

For positive dilation `U_lambda f(q)=f(lambda q)`, the algebraic identity

\[
U_\lambda^{-1}SU_\lambda=\lambda^{-1}S
\]

holds on the common core. On every compact interval of positive dilation
parameters, dilation acts continuously between suitable exponential
seminorms. The degree-minus-one law therefore survives the same completion.

## Result and boundary

On the mixed rapid label--radial carrier, the ordered Green current has:

1. a continuous completed bilinear pairing;
2. cutoff-independent labelled synthesis;
3. exact reciprocal oddness after completion;
4. exact dilation degree minus one.

This closes path independence for the ordered-current coordinate itself. It
does not prove equality of every other five-wall coordinate or identify the
completed scalar zero with a mixed boundary condition. The remaining
comparison problem is finite and typed: constant, delta, primitive, square,
and archimedean wall rows must be checked against the same cutoff transition
maps, together with their cross-polarized Green entries.
