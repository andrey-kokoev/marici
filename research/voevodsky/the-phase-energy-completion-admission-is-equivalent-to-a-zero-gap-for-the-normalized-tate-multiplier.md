# The phase-energy completion admission is equivalent to a zero-gap for the normalized Tate multiplier

## Multiplier model

The completed regular boundary operator is

\[
\mathcal A_S=M_{a_S}
\]

on

\[
\mathscr E_S
=
\bigoplus_\chi
L^2
\left(
\mathbb R,
 e_S(\chi,t)\frac{dt}{2\pi}
\right),
\]

where

\[
a_S(\chi,t)
=
\frac{w_S(\chi,t)}{e_S(\chi,t)}
\]

and

\[
e_S(\chi,t)\ge1.
\]

The positive boundary operator is

\[
R_S=|\mathcal A_S|=M_{|a_S|}.
\]

## Radical

Let

\[
Z_S
=
\{(\chi,t):a_S(\chi,t)=0\}
\]

modulo the phase-energy measure. Then

\[
\ker R_S
=
L^2(Z_S,e_Sdt/2\pi).
\]

The radical quotient is canonically represented by

\[
\mathscr E_S^{red}
=
L^2(Z_S^c,e_Sdt/2\pi).
\]

## Reduced minimum modulus

For a bounded multiplication operator, the reduced minimum modulus is

\[
\boxed{
\gamma(R_S)
=
\operatorname*{ess\,inf}_{a_S\ne0}|a_S|.
}
\]

The following are equivalent:

1. \(\gamma(R_S)>0\);
2. zero is isolated from the nonzero essential range of \(|a_S|\);
3. \(\operatorname{ran}R_S\) is closed;
4. the quotient form is coercive:
   \[
   \langle u,R_Su\rangle
   \ge
   \gamma(R_S)\|u\|^2
   \quad
   (u\in\mathscr E_S^{red});
   \]
5. the current coercive completion interface can admit the boundary object.

Thus completion admission is exactly a zero-gap theorem for the normalized Tate multiplier.

## Fiberwise criterion

Since the character decomposition is orthogonal,

\[
\gamma(R_S)
=
\inf_\chi
\operatorname*{ess\,inf}_{t:a_S(\chi,t)\ne0}
|a_S(\chi,t)|.
\]

A uniform positive gap must hold simultaneously across every admitted character and conductor.

A sequence \((\chi_n,t_n)\) with

\[
0<|a_S(\chi_n,t_n)|\longrightarrow0
\]

proves

\[
\gamma(R_S)=0.
\]

## Continuous-fiber test

On a fiber where \(a_S(\chi,t)\) has a continuous representative, a sign crossing or any non-isolated zero gives nonzero values arbitrarily close to zero. Hence

\[
\gamma(R_S)=0.
\]

An interval on which \(a_S\) vanishes contributes to the radical. It preserves a positive reduced gap only when the values outside that zero region are uniformly separated from zero.

## Finite-packet radical stability

For the spectrally adapted packet projections \(E_n\), define

\[
R_n=|E_nD_{\lambda_n}E_n|.
\]

Strong convergence

\[
R_nE_n\longrightarrow R_S
\]

does not by itself stabilize kernels. The required radical statement is spectral convergence at zero.

For a positive gap \(g\), choose

\[
0<\eta<g.
\]

Then radical stability follows from convergence of the spectral projections

\[
1_{[0,\eta]}(R_n)
\longrightarrow
1_{\{0\}}(R_S)
\]

on the declared packet system.

When \(g=0\), no fixed \(\eta\) separates radical from arbitrarily small positive spectrum. The appropriate completion retains the spectral filtration

\[
1_{[0,\eta]}(R_S),
\qquad
\eta\downarrow0,
\]

instead of imposing a coercive radical quotient.

## Two completion branches

### Gapped branch

If

\[
\gamma(R_S)>0,
\]

then the existing completion constructor applies after spectral-projection stability is verified. The quotient coercivity bound and reduced minimum modulus may both be chosen below \(\gamma(R_S)\).

### Gapless branch

If

\[
\gamma(R_S)=0,
\]

then the positive boundary object still exists as the bounded operator \(R_S\), and the cofinal absolute-Gram system still converges strongly to it. Completion should use a noncoercive spectral object carrying the filtration near zero.

One suitable target is the diagram

\[
\eta
\longmapsto
1_{[\eta,\infty)}(R_S)\mathscr E_S,
\qquad
\eta>0,
\]

whose members have coercivity bound \(\eta\). The full boundary is recovered as \(\eta\downarrow0\).

## Immediate analytic test

The required source calculation is now scalar and fiberwise:

\[
\boxed{
\inf_\chi
\operatorname*{ess\,inf}_{t:w_S(\chi,t)\ne0}
\frac{|w_S(\chi,t)|}{e_S(\chi,t)}.
}
\]

Its positivity selects the gapped completion branch. A sequence making this ratio tend to zero selects the spectral-filtration branch.
