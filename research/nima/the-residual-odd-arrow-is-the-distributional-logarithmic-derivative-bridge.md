# The residual odd arrow is the distributional logarithmic-derivative bridge

Event 10278 removes the smooth archimedean current from the zero-section
problem. The remaining scalar current is the arithmetic argument derivative.

For \(\sigma>1\),

\[
\frac{\zeta'}{\zeta}(\sigma+it)
=
-\sum_{n\ge1}
\frac{\Lambda(n)}{n^{\sigma+it}}.
\]

Therefore

\[
\frac{d}{dt}\arg\zeta(\sigma+it)
=
\operatorname{Re}
\frac{\zeta'}{\zeta}(\sigma+it)
=
-\sum_{n\ge1}
\frac{\Lambda(n)}{n^\sigma}
\cos(t\log n).
\]

With the standard normalization

\[
S_\sigma(t)=\frac1\pi\arg\zeta(\sigma+it),
\]

the prime odd current is

\[
J_{P,\sigma}(t)\,dt
=
-\frac1\pi
\sum_{n\ge1}
\frac{\Lambda(n)}{n^\sigma}
\cos(t\log n)\,dt.
\]

This is the exact arithmetic residual that must complement the smooth Tate
current.

## Boundary typing

The prime series is absolutely convergent only for \(\sigma>1\). The desired
critical boundary \(\sigma\downarrow1/2\) is not a pointwise or Hilbert limit.
It must be interpreted as a distributional boundary value of
\(\zeta'/\zeta\), with poles retained rather than hidden.

For a test function \(\varphi\),

\[
\langle J_{P,\sigma},\varphi\rangle
=
-\frac1\pi
\sum_{n\ge1}
\frac{\Lambda(n)}{n^\sigma}
\operatorname{Re}\widehat\varphi(\log n).
\]

Ordinary Schwartz decay of \(\widehat\varphi(x)\) is only polynomial in \(x\)
and does not offset the exponential density of labels \(n=e^x\) at the
critical exponent. The source test space must impose the corresponding
exponential Fourier decay, or obtain the boundary by meromorphic
continuation in a declared analytic dual.

This recovers the projective exponential rigging found earlier: the
prime-to-zero bridge is continuous only after its Laplace order is typed.

## Pole and jump content

Away from zeros and the pole, the boundary current is the ordinary real part
of \(\zeta'/\zeta\). Distributionally, continuation also records:

- atomic phase jumps at zeros;
- the pole contribution at \(s=1\);
- endpoint/branch terms.

Consequently the theorem

\[
J_P
=
dS
\]

is already the prime-to-zero spectral identification theorem in
distributional form. It cannot be assumed as a harmless Fourier identity.

The correctly scoped constructor hierarchy is now

\[
-2\,d\vartheta
\quad+\quad
-2\pi\,dS
\quad+\quad
\text{endpoint terms}
\quad\longrightarrow\quad
-2\pi\,dN.
\]

The first arrow is closed by the holomorphic Tate coefficient. The second is
the unresolved Euler logarithmic-derivative boundary theorem.

## Next executable gate

For finite cutoff \(X\), define

\[
J_{P,\sigma}^{(X)}(t)
=
-\frac1\pi
\sum_{n\le X}
\frac{\Lambda(n)}{n^\sigma}
\cos(t\log n).
\]

The next theorem must prove:

1. cutoff naturality in the exponential test rigging;
2. convergence for \(\sigma>1\);
3. meromorphic continuation as a dual-valued family;
4. identification of its critical boundary with the complete
   zero/pole divisor current;
5. preservation of reciprocal orientation and branch conventions.

This is now the earliest unresolved arithmetic–analytic interface. The gamma
side is explicit; the hard residual is precisely the completed explicit
formula.
