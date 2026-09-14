# The prolate transition trace is logarithmic even though the full time--band trace is quadratic

## Correction to the crude trace bound

The inequality

\[
0\le B-B^2\le B,
\qquad
B=PQP,
\]

is true but too crude for cutoff asymptotics.

In the real local time--band model,

\[
\operatorname{Tr}(B)
\asymp
\Lambda^2,
\]

not `O(log Lambda)`. Therefore the logarithmic transition estimate must be proved directly from `B-B^2`; it cannot be inferred from the full phase-space trace.

## Real local model

On `L2(R)`, let

\[
P_\Lambda
=1_{[-\Lambda,\Lambda]}
\]

and

\[
Q_\Lambda
=\mathcal F P_\Lambda\mathcal F^{-1}.
\]

With the Fourier convention

\[
(\mathcal Ff)(\xi)
=
\int f(x)e^{-ix\xi}dx,
\]

the kernel of `Q_Lambda` is

\[
q_\Lambda(u)
=
\frac{
\sin(\Lambda u)
}{
\pi u
}
\]

up to the convention-dependent `2pi` normalization.

## Transition trace as an off-diagonal norm

Let

\[
B_\Lambda
=P_\Lambda Q_\Lambda P_\Lambda.
\]

Then

\[
\boxed{
\operatorname{Tr}
(B_\Lambda-B_\Lambda^2)
=
\|P_\Lambda Q_\Lambda(I-P_\Lambda)\|_{HS}^2.
}
\]

Since the kernel is

\[
1_{|x|\le\Lambda}
q_\Lambda(x-y)
1_{|y|>\Lambda},
\]

this is a boundary-crossing integral rather than the full phase-space volume.

## Exact symmetric-difference reduction

For any convolution projection `Q` with kernel `q`,

\[
\|[P_F,Q]\|_{HS}^2
=
\int_\mathbb R
|q(u)|^2
|F\triangle(F+u)|du.
\]

The two off-diagonal blocks have equal Hilbert--Schmidt norm, so

\[
\|P_FQ(I-P_F)\|_{HS}^2
=
\frac12
\|[P_F,Q]\|_{HS}^2.
\]

For `F=[-Lambda,Lambda]`,

\[
|F\triangle(F+u)|
=
\begin{cases}
2|u|,&|u|\le2\Lambda,\\
4\Lambda,&|u|>2\Lambda.
\end{cases}
\]

Therefore

\[
\boxed{
\begin{aligned}
\operatorname{Tr}(B_\Lambda-B_\Lambda^2)
&=
\int_{|u|\le2\Lambda}
|u||q_\Lambda(u)|^2du\\
&\quad+
2\Lambda
\int_{|u|>2\Lambda}
|q_\Lambda(u)|^2du.
\end{aligned}
}
\]

## Logarithmic main term

Substitute the sinc kernel into the first integral:

\[
\begin{aligned}
I_1
&=
\frac{2}{\pi^2}
\int_0^{2\Lambda}
\frac{\sin^2(\Lambda u)}{u}du\\
&=
\frac{2}{\pi^2}
\int_0^{2\Lambda^2}
\frac{\sin^2v}{v}dv.
\end{aligned}
\]

Using

\[
\int_0^T
\frac{\sin^2v}{v}dv
=
\frac12\log T+O(1),
\]

we obtain

\[
I_1
=
\frac1{\pi^2}
\log(2\Lambda^2)
+O(1)
=
\frac{2}{\pi^2}
\log\Lambda
+O(1).
\]

The tail satisfies

\[
I_2
=
2\Lambda
\int_{|u|>2\Lambda}
|q_\Lambda(u)|^2du
=O(1),
\]

because `|q_Lambda(u)|<=1/(pi|u|)`.

Hence

\[
\boxed{
\operatorname{Tr}
(B_\Lambda-B_\Lambda^2)
=
\frac{2}{\pi^2}
\log\Lambda
+O(1)
}
\]

under the displayed Fourier convention.

## Contrast with the full prolate trace

The diagonal kernel of `Q_Lambda` is

\[
q_\Lambda(0)
=
\frac\Lambda\pi.
\]

Thus

\[
\boxed{
\operatorname{Tr}(B_\Lambda)
=
\int_{-\Lambda}^{\Lambda}
q_\Lambda(0)dx
=
\frac{2}{\pi}
\Lambda^2.
}
\]

The two traces measure different populations:

- `Tr(B)` counts all concentrated time--band modes;
- `Tr(B-B^2)` counts only modes in the transition region between eigenvalues zero and one.

Only the second controls sewing.

## Consequence for the sewing estimate

For an observer `H=U(g)U(g)*` whose one-sided cutoff commutator has cutoff-independent Hilbert--Schmidt norm,

\[
|\mathcal E_\Lambda(g)|
\le
\sqrt{
\operatorname{Tr}(B_\Lambda-B_\Lambda^2)
}
\|[P_\Lambda,H]\|_{HS}.
\]

Therefore the real local model gives

\[
\boxed{
\mathcal E_\Lambda(g)
=O_g(\sqrt{\log\Lambda})
=o_g(\log\Lambda).
}
\]

This proves equality of leading volume densities between Connes's product trace and the positive triple compression in the local model.

## What remains semilocally

The semilocal `P_Lambda` and `Q_Lambda` act on `L2(X_S)` with possible infinite angular multiplicity. Connes's theorem proves traceability only after observer insertion; it does not show that the bare operator `B_(Lambda,S)-B_(Lambda,S)^2` is trace class. Thus the direct semilocal analogue is only a conditional diagnostic. The source-typed target must retain observer smoothing and, for the outside channel, the second cutoff.

## Finite-place expectation

At a nonarchimedean place, module balls and Fourier-dual balls are stratified by valuation shells. The transition region is discrete. Its size should be controlled by the number of shells crossed by the cutoff, hence logarithmic in the module cutoff.

This is an expectation, not yet a proved semilocal bound. Coupling through `O_S*` means the placewise shell counts cannot simply be added without checking quotient multiplicities.

## Updated criterion

For each finite angular-mode cutoff, `Tr(B-B^2)=O(log Lambda)` remains the correct diagnostic. On the full semilocal carrier, the correct Gate-A target is instead an observer-weighted two-cutoff sewing estimate; the bare trace may be infinite.

## Disposition

The earlier sufficient hypothesis `Tr(PQP)=O(log Lambda)` is false in the standard local model and must not be used. The correct direct estimate is

\[
\boxed{
\operatorname{Tr}(PQP-(PQP)^2)
=O(\log\Lambda).
}
\]

It follows from the boundary-crossing sinc-kernel integral and proves that the positive and product cutoffs have the same leading volume density locally. The semilocal transition-trace estimate is the next unresolved analytic gate.
