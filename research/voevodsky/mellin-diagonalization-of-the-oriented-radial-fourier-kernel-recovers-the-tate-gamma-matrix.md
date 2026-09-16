# Mellin diagonalization of the oriented radial Fourier kernel recovers the Tate gamma matrix

## Question

How does the explicit oriented log-radial Fourier sewing appear in the spectral presentation?

## Claim boundary

Fourier transform in logarithmic radius converts the Hankel kernel into spectral reflection multiplied by an explicit two-by-two Tate gamma matrix. This analytically links the oriented radial and canonical-dual spectral presentations on a common test core. Endpoint distributional completion remains separate.

## Logarithmic Fourier transform

For

$$
K_{\epsilon',\epsilon}(v,u)
=
e^{(u+v)/2}
 e^{-2\pi i\epsilon\epsilon'e^{u+v}},
$$

set \(w=u+v\). With logarithmic Fourier convention

$$
\widehat g(t)=\int_{\mathbb R}e^{-itu}g(u)\,du,
$$

the Hankel dependence gives

$$
\widehat{W_{\rm or}g}_{\epsilon'}(t)
=
\sum_{\epsilon=\pm1}
 m_{\epsilon\epsilon'}(t)
 \widehat g_\epsilon(-t).
$$

The minus sign is the spectral reflection forced by the sum kernel.

## Gamma multipliers

For \(\sigma=\pm1\),

$$
m_\sigma(t)
=
\int_{\mathbb R}
 e^{w/2}e^{-2\pi i\sigma e^w}e^{-itw}\,dw.
$$

Putting \(x=e^w\) gives the oscillatory Mellin integral

$$
m_\sigma(t)
=
\int_0^\infty
 x^{-1/2-it}e^{-2\pi i\sigma x}\,dx.
$$

By analytic continuation of the gamma integral,

$$
m_\sigma(t)
=
(2\pi)^{-1/2+it}
\Gamma\left(\frac12-it\right)
\exp\left[-\frac{i\sigma\pi}{2}
\left(\frac12-it\right)\right].
$$

Therefore the oriented spectral multiplier is

$$
G(t)=
\begin{pmatrix}
 m_+(t)&m_-(t)\\
 m_-(t)&m_+(t)
\end{pmatrix},
$$

followed by \(t\mapsto-t\).

## Parity branches

Passing to radial parity coordinates diagonalizes the matrix. The even and odd branches have multipliers

$$
\gamma_+(t)=m_+(t)+m_-(t),
\qquad
\gamma_-(t)=m_+(t)-m_-(t).
$$

These are the two archimedean Tate gamma branches, up to the fixed normalization constants of the chosen Fourier/Mellin conventions. Their reflected ratios are unimodular on the sewing axis because \(W_{\rm or}\) is unitary.

## Mixed presentation square

Let \(\mathcal M_{\log}\) denote logarithmic Mellin/Fourier transform and \(R_t\) spectral reflection. On the common Schwartz core,

$$
\mathcal M_{\log}W_{\rm or}
=
G(t)R_t\mathcal M_{\log}.
$$

Thus the radial-to-spectral presentation map analytically intertwines actual Fourier sewing with canonical-dual gamma reflection. This is the nontrivial mixed square previously visible only as reciprocal branch swap after taking the half-turn.

## Domain boundary

The oscillatory gamma integral is initially regularized in its convergence strip and then continued. For comb seeds, all formulas are interpreted in the test/strong-dual pairing. No claim places raw combs in the Green Hilbert graph.

## Disposition

The explicit radial Fourier kernel and the Tate spectral action are analytically the same operator under logarithmic Mellin transform. This constructs a genuine nontrivial radial-to-spectral Fourier intertwiner on the common test/dual core, with exact gamma matrix and spectral reflection.