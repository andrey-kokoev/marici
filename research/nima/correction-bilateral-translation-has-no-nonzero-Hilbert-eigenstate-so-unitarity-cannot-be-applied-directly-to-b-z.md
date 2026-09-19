# Correction: bilateral translation has no nonzero Hilbert eigenstate, so unitarity cannot be applied directly to b_z

## Spectral fact

On `L^2(R)`, bilateral translation

\[
(U_Lf)(t)=f(t-L)
\]

is unitary. Under Fourier transform it is multiplication by

\[
e^{-iL\xi}.
\]

If a nonzero `f in L^2(R)` satisfied

\[
U_Lf=\lambda f,
\]

then its Fourier transform would be supported on the level set

\[
\{\xi:e^{-iL\xi}=\lambda\}.
\]

For `|lambda| != 1` this set is empty. For `|lambda|=1` it is countable and has
Lebesgue measure zero. An `L^2` function supported there is zero. Therefore
bilateral translation has no nonzero Hilbert eigenvectors at any spectral
value.

## Rigged eigenvectors

Plane waves provide generalized eigenvectors on the unit circle, and complex
exponentials provide analytic generalized eigenfunctionals off it. They are
not vectors with finite positive `L^2` norm. Consequently the step

\[
\|U_Lb_z\|=|p^{-z}|\|b_z\|
\]

is unavailable for a rigged eigenfunctional.

A positive energy `E_p(b_z)>0` in the corrected pair carrier does not by itself
place the same `b_z` in the bilateral translation Hilbert space. An explicit
energy-preserving embedding would be required, and exact eigenstate membership
would contradict the continuous-spectrum fact above.

## Correct use of the dilation

The bilateral dilation can establish operator adjunction

\[
U_L^*=U_{-L}
\]

and can transport wave packets, ports, and boundary distributions. It cannot
turn a scalar spectral zero into a normalizable translation eigenvector.

A valid confinement argument must instead use one of:

- a bounded boundary or Weyl function whose star law descends from the unitary
  dilation;
- a spectral measure statement with a source-derived atom, followed by proof
  that such an atom can exist;
- a characteristic-function zero theorem for the compressed conservative
  colligation;
- a Green boundary identity on actual domain vectors.

## Disposition

The direct norm-eigenvalue argument is rejected. The bilateral port lift
remains useful only as a route to an adjoint boundary law or characteristic
function. Rigged eigenstate language alone cannot combine generalized
translation eigenvalues with the positive retained bulk norm.