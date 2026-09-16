# One principal-value channel minimally Fourier-saturates the history trace port

## Question

Does quarter-turn closure require the entire response function, or does one additional nonlocal trace close the seam-history orbit?

## Claim boundary

At seam zero on the Schwartz core, one principal-value channel is sufficient. Replacing the identically zero causal left-endpoint coordinate by this channel gives an exact four-dimensional order-four trace representation. This does not yet treat a moving seam or completed prime/grade assembly.

## Saturated traces

Define

$$
B(g)=g(0),
\qquad
Q(g)=\int_{\mathbb R}g(x)\,dx,
$$

$$
A(g)=\int_{-\infty}^0g(x)\,dx,
\qquad
C(g)=\operatorname{pv}\int_{\mathbb R}\frac{g(x)}x\,dx.
$$

For causal history \(Hg\), these contain seam flux \(B\), total endpoint jump \(Q\), and seam value \(A\). The causal left endpoint is always zero and carries no additional source information.

## Fourier action

The Heaviside distribution identity gives

$$
A(\widehat g)
=
\frac12B(g)-\frac1{2\pi i}C(g).
$$

Also

$$
B(\widehat g)=Q(g),
\qquad
Q(\widehat g)=B(g).
$$

Applying Fourier once more and using \(\mathcal F^2g(x)=g(-x)\) yields

$$
C(\widehat g)
=2\pi iA(g)-\pi iQ(g).
$$

Thus for

$$
\Gamma_{\rm sat}(g)=(B(g),Q(g),A(g),C(g))^T,
$$

one has

$$
\Gamma_{\rm sat}(\widehat g)
=T_{\rm sat}\Gamma_{\rm sat}(g),
$$

where

$$
T_{\rm sat}
=
\begin{pmatrix}
0&1&0&0\\
1&0&0&0\\
\frac12&0&0&-\frac1{2\pi i}\\
0&-\pi i&2\pi i&0
\end{pmatrix}.
$$

## Order-four check

Direct substitution gives

$$
T_{\rm sat}^2(B,Q,A,C)
=
(B,Q,Q-A,-C),
$$

which is exactly reflection of origin value, total mass, negative-half-line mass, and the odd principal-value kernel. Hence

$$
T_{\rm sat}^4=I.
$$

## Minimality

Without \(C\), Fourier transport of \(A\) leaves the span of \((B,Q,A)\). Once \(C\) is added, its Fourier image lies in that span. Therefore one new nonlocal channel is both necessary and sufficient for finite quarter-turn closure at the fixed seam.

## History interpretation

The minimally saturated fourth presentation is

$$
V_4^{\rm sat}
=
\bigl(
\text{seam flux},
\text{total endpoint jump},
\text{seam value},
\text{Hilbert principal value}
\bigr).
$$

It retains the three nonredundant causal-history traces and replaces the identically zero left endpoint by the missing Fourier-conjugate observation.

## Disposition

The fixed-seam history trace port admits an exact minimal Fourier saturation by one principal-value channel. It now carries a genuine order-four analytic action on the Schwartz/strong-dual core. Moving-seam covariance and semilocal completion remain to verify.