# Directly inspected primary-source excerpt

Source: Bondarenko–Radchenko–Seip, *Fourier interpolation with zeros of zeta and L-functions*, arXiv:2005.02996, equation (1.1).

Fetched in iteration4 from `https://arxiv.org/src/2005.02996`.
The response is a gzip-compressed single TeX file, not a tar archive.

- Response SHA-256: `5ee4bbde5a3f4396e972ed214d394f4dc237439f3a5438f02e2efbb196657a58`.
- Decompressed UTF-8 TeX SHA-256: `25c7389c223d34e933ea07e8868764835fe7a17e0cfeb8d0f2b2d4d7ef36e3ac`.
- Decompressed source: 2712 lines.
- The response hash agrees with the earlier repository citation; the excerpt below was freshly read from the response, not inferred from that citation.

Verbatim lines98–110:

```tex
The Riemann--Weil explicit formula (sometimes also called the Guinand--Weil
explicit formula) expresses the familiar duality between the prime numbers and
the nontrivial zeros of the Riemann zeta function $\zeta(s)$ in the following
compelling way:
    \begin{align} \frac{1}{2\pi} \int_{-\infty}^{\infty} f(t) & \left(\frac{\Gamma'(1/4+it/2)}{\Gamma(1/4+it/2)} - \log \pi \right)dt+f\Big(\frac{i}{2}\Big)+f\Big(\frac{-i}{2}\Big) \nonumber \\ \label{eq:RW}
     & = \frac{1}{2\pi} \sum_{n=1}^{\infty} \frac{\Lambda(n)}{\sqrt{n}} \left(\widehat{f}\Big(\frac{\log n}{2\pi}\Big)+\widehat{f}\Big(-\frac{\log n}{2\pi}\Big) \right)+  \sum_{\rho} f\left(\frac{\rho-1/2}{i}\right).
     \end{align}
Here $f(z)$ is a function analytic in the strip $|\im\, z|<1/2+\eps$ for
some $\eps>0$, $|f(z)|\ll (1+|z|)^{-1-\delta} $ for some $\delta>0$ when
$|\re\, z| \to \infty$, and
    \[ \widehat{f}(\xi)\coloneqq
    \int_{-\infty}^{\infty} f(x) e^{-2\pi i x \xi} dx ;\]
$\Lambda(n)$ is the von Mangoldt function defined to be $\log p$ if $n=p^k$, $p$ a prime and $k\ge 1$, and zero otherwise, while the second sum in \eqref{eq:RW} runs over the nontrivial zeros $\rho$ of $\zeta(s)$ (counting multiplicities in the usual way). The Riemann--Weil formula generalizes the classical Riemann--von Mangoldt explicit formula \cite[Ch. 17]{D} and arose to prominence from Weil's work \cite{W}, in which it appeared in a considerably more general form.
```

Application boundary: iteration4 applies this formula to the even test `f(u)=h(u)+h(-u)`, so the imaginary odd digamma contribution cancels. Division by four and the unconditional reflection symmetry of the zeta divisor recover the repository's half-divisor Gaussian convention. This primary-source comparison does not prove RH or supply the full zero divisor numerically.
