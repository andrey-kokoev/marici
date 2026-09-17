# Correction: q-C is an exact radial-to-spectral intertwiner

The proposed q-C multiplicativity defect compared two different constructions:

1. lattice Pontryagin characters;
2. additive Fourier transported through the nonlinear radial chart.

Their kernels differ, so direct character conjugacy fails. This does not define the historical q-C square.

The historical comparison uses oriented half-density radialization followed by logarithmic Mellin transform. The oriented radial Fourier operator has kernel

$$
K_{\epsilon',\epsilon}(v,u)
=
e^{(u+v)/2}
e^{-2\pi i\epsilon\epsilon'e^{u+v}}.
$$

Logarithmic Mellin transform sends it to spectral reflection multiplied by the Tate gamma matrix

$$
G(t)=
\begin{pmatrix}
m_+(t)&m_-(t)\\
m_-(t)&m_+(t)
\end{pmatrix},
$$

where

$$
m_\sigma(t)
=
(2\pi)^{-1/2+it}
\Gamma\left(\frac12-it\right)
\exp\left[
-\frac{i\sigma\pi}{2}
\left(\frac12-it\right)
\right].
$$

On the common Schwartz core,

$$
\mathcal M_{\log}W_{\mathrm{or}}
=
G(t)R_t\mathcal M_{\log}.
$$

This is the historical q-C intertwiner. The two routes have the same target and agree exactly on the common core.

Consequences for the defect programme:

| Claim | Resolution |
|---|---|
| tail can realize a multiplicativity defect | true in the finite Walsh scout |
| finite factorization mechanism | exact in that scout |
| historical defect and leakage share a target | rejected as an ill-typed identification |
| historical range inclusion | inapplicable to q-C |
| uniform Douglas bound | inapplicable to q-C |
| refinement-compatible defect lift | inapplicable to q-C |

The mapping-cylinder and A-infinity constructions remain valid universal resolutions for the artificial character-to-radial comparison. They are not the historical q-C comparison.

The historical frontier is endpoint and graph completion of the exact Mellin intertwiner, including compatibility with observation and regulator faces.
