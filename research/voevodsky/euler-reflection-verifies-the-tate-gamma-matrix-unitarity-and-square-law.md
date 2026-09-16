# Euler reflection verifies the Tate gamma matrix unitarity and square law

## Question

Do the signs and \(2\pi\)-normalization in the oriented Mellin gamma matrix satisfy the exact Fourier square and unitarity identities?

## Claim boundary

Yes. Direct parity diagonalization followed by Euler's reflection formula gives product \(+1\) on the even branch and \(-1\) on the odd branch. Hence the orientation-coordinate matrix product is the channel swap, and both branches have unit modulus on the critical line.

## Parameters

Put

$$
a=\frac12-it,
\qquad
1-a=\frac12+it.
$$

The oriented kernel multipliers are

$$
m_\sigma(t)
=(2\pi)^{-a}\Gamma(a)e^{-i\sigma\pi a/2}.
$$

The orientation matrix is

$$
G(t)=
\begin{pmatrix}
m_+(t)&m_-(t)\\
m_-(t)&m_+(t)
\end{pmatrix}.
$$

## Parity branches

Diagonalizing by the even and odd orientation vectors gives

$$
\gamma_{\rm ev}(t)
=m_+(t)+m_-(t)
=2(2\pi)^{-a}\Gamma(a)
\cos\left(\frac{\pi a}{2}\right),
$$

and

$$
\gamma_{\rm odd}(t)
=m_+(t)-m_-(t)
=-2i(2\pi)^{-a}\Gamma(a)
\sin\left(\frac{\pi a}{2}\right).
$$

These are the real trivial-character and sign-character Tate gamma branches in the declared additive Fourier normalization.

## Even product

Using

$$
\Gamma(a)\Gamma(1-a)=\frac\pi{\sin(\pi a)},
$$

and

$$
\cos\left(\frac{\pi(1-a)}2\right)
=\sin\left(\frac{\pi a}2\right),
$$

one gets

$$
\gamma_{\rm ev}(t)\gamma_{\rm ev}(-t)
=
\frac{2}{\sin(\pi a)}
\cos\left(\frac{\pi a}2\right)
\sin\left(\frac{\pi a}2\right)
=1.
$$

## Odd product

Similarly,

$$
\gamma_{\rm odd}(t)\gamma_{\rm odd}(-t)
=
-\frac{2}{\sin(\pi a)}
\sin\left(\frac{\pi a}2\right)
\cos\left(\frac{\pi a}2\right)
=-1.
$$

Therefore, in parity coordinates,

$$
G(t)G(-t)
\sim
\operatorname{diag}(1,-1).
$$

Returning to orientation coordinates gives

$$
G(t)G(-t)
=
\begin{pmatrix}0&1\\1&0\end{pmatrix}
=W_1.
$$

This is exactly Fourier square as reflection/channel exchange.

## Unitarity

For real \(t\), \(1-a=\overline a\). The even branch obeys

$$
\gamma_{\rm ev}(-t)
=\overline{\gamma_{\rm ev}(t)},
$$

whereas the explicit factor \(-i\) in the odd branch gives

$$
\gamma_{\rm odd}(-t)
=-\overline{\gamma_{\rm odd}(t)}.
$$

Combining these conjugation laws with the two product identities yields

$$
|\gamma_{\rm ev}(t)|=1,
\qquad
|\gamma_{\rm odd}(t)|=1.
$$

Hence \(G(t)\) is unitary almost everywhere on the real spectral line.

## Oscillatory continuation

The entry formula starts from

$$
\int_0^\infty x^{a-1}e^{-2\pi i\sigma x}\,dx
=(2\pi)^{-a}\Gamma(a)e^{-i\sigma\pi a/2}
$$

for \(0<\operatorname{Re}a<1\), interpreted as the boundary value obtained by inserting \(e^{-\varepsilon x}\) and taking \(\varepsilon\downarrow0\). Here \(\operatorname{Re}a=1/2\), so no further meromorphic crossing is needed.

## Disposition

The candidate Tate gamma matrix passes all normalization gates: correct oscillatory boundary phase, correct \(2\pi\) power, unit modulus on the spectral line, and exact square law \(G(t)G(-t)=W_1\). The prior tentative target \(I\) was wrong in orientation coordinates because Fourier square exchanges the two radial channels.