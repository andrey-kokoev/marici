# The Legendre gamma tail has two leading rank-one parity channels

For the normalized Legendre basis on `[-L,L]`, the Fourier amplitudes used in
the compact-window calculation are

\[
V_n(u)=2L\sqrt{\frac{2n+1}{2L}}\,(-1)^{\lfloor n/2\rfloor}j_n(Lu).
\]

The fixed-order spherical-Bessel asymptotic is

\[
j_n(x)=\frac{\sin(x-n\pi/2)}x+O_n(x^{-2}).
\]

After the declared phase normalization this becomes

\[
V_{2k}(u)=
2\sqrt{\frac{4k+1}{2L}}\frac{\sin(Lu)}u+O_k(u^{-2}),
\]

\[
V_{2k+1}(u)=
-2\sqrt{\frac{4k+3}{2L}}\frac{\cos(Lu)}u+O_k(u^{-2}).
\]

Hence the high-frequency gamma matrix does not have an arbitrary dense tail.
Its leading term is rank one on each parity block:

\[
M_{\Gamma,\mathrm{tail}}
\sim c_e(R)e e^T\oplus c_o(R)o o^T,
\]

where

\[
e_k=\sqrt{4k+1},\qquad o_k=\sqrt{4k+3},
\]

and `c_e,c_o` are positive scalar integrals of the gamma multiplier against
`sin^2(Lu)/u^2` and `cos^2(Lu)/u^2`. The next terms are finite sums of
oscillatory moments with powers `u^{-3},u^{-4},...` because each integer-order
spherical Bessel function has an exact finite sine/cosine inverse-power
expansion.

This supplies the missing structured-tail architecture:

1. expand every `j_n(Lu)` exactly into finite sine/cosine inverse powers;
2. collect the tail matrix into finitely many parity-preserving low-rank
   coefficient matrices;
3. enclose scalar moments
   `integral_R^infinity g(u) sin(2Lu)/u^m du`, their cosine analogues, and the
   nonoscillatory logarithmic moments;
4. add the resulting interval matrix to the directed finite-range gamma
   quadrature.

The leading positive rank-one terms must not be discarded: previous scalar
floors failed precisely because they erased their mode distribution. For
`N=80`, this reduction is finite and independent of the number of prime
channels. Prime translations remain exact physical overlap matrices.
