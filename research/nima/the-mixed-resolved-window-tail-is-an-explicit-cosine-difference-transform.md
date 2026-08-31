# The mixed resolved window tail is an explicit cosine-difference transform

## Result

**Superseded frontier, retained as the Fourier reduction.** The scalar below
has since been reduced to an explicit autocorrelation difference and proved
strictly positive using the additional source factorization
\(b_\Phi(\xi)=2\pi i\xi\widehat K_+(\xi)\). The general hostile test in this
packet applies to arbitrary nonnegative spectral densities, not to the frozen
theta-tail density.

The formerly unresolved real scalar

\[
g_p=\langle BW_L,BW_{2L}\rangle,
\qquad L=\log p,
\]

can be reduced further without fitting any Green entry.  With the repository
Fourier convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(q)e^{-2\pi iq\xi}\,dq,
\]

write

\[
\rho=-H',\qquad
b_\Phi(\xi)=h_\Phi(\xi)-M_\Phi.
\]

The front symmetry makes \(\rho\) even and real, so \(\widehat\rho\) is real
and even.  Distributionally away from \(\xi=0\),

\[
2\pi i\xi\widehat H(\xi)=-\widehat\rho(\xi).
\]

Since

\[
W_t(q)=H(q+t)-H(q-t),
\]

translation gives

\[
\widehat W_t(\xi)
=-\frac{\sin(2\pi t\xi)}{\pi\xi}\widehat\rho(\xi).
\]

The removable value at \(\xi=0\) is obtained by continuity.  Substitution in
the already established Plancherel formula yields

\[
\boxed{
 g_p=
 \frac1{\pi^2}
 \int_{\mathbb R}
 |b_\Phi(\xi)|^2|\widehat\rho(\xi)|^2
 \frac{\sin(2\pi L\xi)\sin(4\pi L\xi)}{\xi^2}\,d\xi .
 }
\]

Equivalently, using \(2\sin a\sin2a=\cos a-\cos3a\),

\[
\boxed{
 g_p=
 \frac1{2\pi^2}
 \int_{\mathbb R}
 \frac{|b_\Phi(\xi)|^2|\widehat\rho(\xi)|^2}{\xi^2}
 \bigl(\cos(2\pi L\xi)-\cos(6\pi L\xi)\bigr)\,d\xi .
 }
\]

Thus the mixed tail entry is one cosine-difference transform of the frozen
nonnegative spectral density

\[
\Xi_\Phi(\xi)
:=\frac{|b_\Phi(\xi)|^2|\widehat\rho(\xi)|^2}{\xi^2}.
\]

## Zero-frequency regularity

Because

\[
b_\Phi(0)=h_\Phi(0)-M_\Phi=0,
\]

the apparent \(\xi^{-2}\) singularity is removable under the existing first
moment/domain assumptions.  Independently, the sine product is
\(O(L^2\xi^2)\).  This agrees with the established graph-domain finiteness of
the two window vectors.

## Hostile sign test and its scope

The factor

\[
\sin(2\pi L\xi)\sin(4\pi L\xi)
\]

changes sign. An arbitrary nonnegative spectral density concentrated where
the two sines have opposite signs makes the integral negative. Thus diagonal
positivity alone cannot determine the sign.

That hostile does **not** preserve all frozen source structure. For the actual
theta tail,

\[
\Xi_\Phi(\xi)=4\pi^2|\widehat{K_+*\rho}(\xi)|^2,
\]

and the autocorrelation factorization proves \(g_p>0\). The earlier correction
that \(g_p\) has no unknown complex phase remains valid.

## Closed analytic input

The formerly requested source identity is now known:

\[
b_\Phi(\xi)=2\pi i\xi\widehat K_+(\xi),
\qquad
\Xi_\Phi(\xi)=4\pi^2|\widehat{K_+*\rho}(\xi)|^2.
\]

Consequently,

\[
g_p=2\bigl(C_{K_+*\rho}(L)-C_{K_+*\rho}(3L)\bigr)>0.
\]

The Stieltjes endpoint Green identity is still not used: it has a different
metric carrier.

## Current frontier

The analytic mixed-tail value and sign are closed. The remaining local gate is
the independently sourced coefficient-side Green comparison and the typed
transport between the boundary-Stokes and theta/Wronskian odd lines.
Radical descent, full-pushout closed range, and prime-uniform coercivity remain
open. No RH conclusion is authorized.
