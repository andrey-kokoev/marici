# Regulated theta autocorrelation is an explicit zeta–Barnes integral

Let

$$
K(s)=\int_0^\infty\kappa(r)r^{s-1}\,dr
$$

be the Mellin transform of the universal ratio profile. Direct beta integration gives

$$
\begin{aligned}
K(s)=\frac34\Bigg[&
-6B\left(\frac{s+2}{2},\frac{7-s}{2}\right)
+23B\left(\frac{s+4}{2},\frac{5-s}{2}\right)\\
&-6B\left(\frac{s+6}{2},\frac{3-s}{2}\right)
\Bigg],
\end{aligned}
$$

initially on the common convergence strip. In particular,

$$
K(1)=0,
\qquad
K(2)=-2.
$$

Mellin inversion gives

$$
\kappa(me^t/n)
=\frac1{2\pi i}\int_{(c)}K(s)e^{-ts}n^sm^{-s}\,ds.
$$

Substitution into the regulated autocorrelation and absolute interchange in its initial convergence region yields

$$
A_{\Phi,\varepsilon}(t)
=\frac{e^{t/2}}{2\pi i}
\int_{(c)}
K(s)e^{-ts}
\zeta(1+\varepsilon-s)
\zeta(\varepsilon+s)
\,ds.
$$

This formula supplies meromorphic continuation in `epsilon` by contour displacement and the standard continuation of zeta and beta/gamma factors. It also locates the two arithmetic poles at

$$
s=\varepsilon
\quad\text{and}\quad
s=1-\varepsilon.
$$

At `epsilon=0`, the second pole meets the zero

$$
K(1)=0,
$$

which is the analytic form of the zero-mass cancellation. The surviving derivative and contour residues encode the finite seam/archimedean correction; `K(2)=-2` fixes the first moment normalization.

The global forcing reservoir is obtained by the additional Laplace transform in `t`. Thus its prime-compatible continuation has been reduced to a zeta–beta Barnes integral with explicit poles and residues.

Status: regulated arithmetic kernel meromorphically represented; contour shift, finite-part evaluation, and identification of each residue with the declared source currents remain open.
