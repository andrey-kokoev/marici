# Wiener–Khinchin gives a rigorous source proof of the Xi-square autocorrelation

Let the completed theta forcing be normalized so that its bilateral Laplace transform is

$$
\Xi(z)=\xi\left(\frac12+z\right)
=\int_{\mathbb R}\Phi(u)e^{zu}\,du.
$$

The completed source is real and even. Define

$$
A_\Phi(t)=\int_{\mathbb R}\Phi(u)\Phi(u+t)\,du.
$$

Fubini is valid here at the level of the completed source, without expanding into theta labels. Its bilateral Laplace transform is

$$
\begin{aligned}
\int_{\mathbb R}A_\Phi(t)e^{zt}\,dt
&=\int\!\int\Phi(u)\Phi(u+t)e^{zt}\,du\,dt\\
&=\left(\int\Phi(u)e^{-zu}\,du\right)
  \left(\int\Phi(v)e^{zv}\,dv\right)\\
&=\Xi(-z)\Xi(z).
\end{aligned}
$$

By the Xi reflection symmetry,

$$
\Xi(-z)=\Xi(z),
$$

and therefore

$$
\boxed{
\mathcal B A_\Phi(z)=\Xi(z)^2.
}
$$

Equivalently, with `s=1/2+z`,

$$
A_\Phi(t)
=\frac{e^{t/2}}{2\pi i}
\int_{(c)}\xi(s)^2e^{-st}\,ds.
$$

This proves the scalar Xi-square autocorrelation identity directly and rigorously. The finite-cutoff ratio kernel and Mellin regulator are diagnostics of how arithmetic labels reconstruct this already well-defined completed identity; they are not needed to define it.

The stable-tail forcing term is now the positive-time Hardy projection

$$
\langle\Phi,G_z\rangle
=-\int_0^\infty e^{-zt}A_\Phi(t)\,dt.
$$

Thus the one-sided Green reservoir is canonically the causal projection of the inverse bilateral transform of `Xi^2`. This is the direct scalar coupling between the Xi section and the positive Green system.

Status: scalar Xi/Green coupling proved at completed-source level; typed arithmetic lift and reciprocal port compatibility remain open.
