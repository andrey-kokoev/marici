# The Wronskian odd port is the boundary phase-velocity certificate

The proposed Hermite--Biehler lift gives a precise role to the previously identified Wronskian centroid.

Write
\[
E(x)=A(x)-iB(x)
\]
on the real seam, with \(A\) and \(B\) real. The boundary phase satisfies
\[
\frac{d}{dx}\arg E(x)
=
\operatorname{Im}\frac{E'(x)}{E(x)}
=
\frac{A'(x)B(x)-A(x)B'(x)}
{A(x)^2+B(x)^2},
\]
up to the sign chosen in \(E=A-iB\).

Define the Wronskian
\[
W_{A,B}(x)
=
A(x)B'(x)-A'(x)B(x).
\]
Then
\[
\frac{d}{dx}\arg E(x)
=
-\frac{W_{A,B}(x)}{|E(x)|^2}.
\]

Thus the Wronskian odd port is not merely an orientation bit. It is the local phase velocity of the common outgoing determinant section.

A strict sign law
\[
W_{A,B}(x)>0
\]
or its conventionally reversed form implies monotone boundary phase. Consequently:

- zeros of \(A\) and \(B\) interlace;
- all regular parity crossings have one Maslov sign;
- each crossing is simple;
- the signed winding equals the unsigned zero count;
- the Wronskian magnitude supplies the crossing margin.

At a zero \(A(x_0)=0\) with \(B(x_0)\neq0\),
\[
W_{A,B}(x_0)
=
-A'(x_0)B(x_0).
\]
Therefore the zero is simple exactly when the Wronskian does not vanish there.

This unifies several previously separate ports:

- reciprocal odd current fixes the sign of \(W\);
- Wronskian centroid measures phase speed;
- determinant lens supplies \(|E|^2=A^2+B^2\);
- additive parity sections supply \(A\) and \(B\).

The source theorem should be stronger than checking the Wronskian at sampled zeros. It should derive a kernel identity
\[
W_{A,B}(x)
=
\|\Gamma_{\mathrm{state}}(x)\|^2
\]
or a positive weighted variant from the one-sided Green energy.

For a de Branges function, the reproducing kernel on the diagonal is proportional to
\[
\frac{W_{A,B}(x)}{\pi}.
\]
Hence positivity of the Wronskian is the boundary shadow of positivity of the de Branges space.

However, boundary Wronskian positivity alone does not prove the full upper-half-plane inequality
\[
|E^{\#}(z)|<|E(z)|.
\]
One also needs the correct analytic class, zero-freeness of \(E\) in the upper half-plane, and control at infinity. The logical order is:

1. construct entire or bounded-type \(E\);
2. prove upper-half-plane zero-freeness from one-sided passivity;
3. derive the positive Wronskian identity on the seam;
4. conclude Hermite--Biehler under the applicable analytic theorem.

The raw one-sided transform orientation must be frozen carefully. For a positive rapidly decaying forcing,
\[
E(iy)
\]
and
\[
E^{\#}(iy)
\]
reverse their relative size when the sign of the exponential is reversed. The outgoing convention must be derived from the system flux, not chosen after testing the inequality.

The Riemann--von Mangoldt asymptotic becomes a Wronskian integral:
\[
N(T)
\sim
\frac{1}{\pi}
\int_0^T
\frac{|W_{A,B}(x)|}{A(x)^2+B(x)^2}\,dx,
\]
with endpoint and phase conventions calibrated. The archimedean term must dominate the mean phase velocity.

The smallest hostile has correctly interlacing sampled zeros but a Wronskian that changes sign between them. Its signed spectral flow can backtrack.

A second hostile proves \(W>0\) on the seam but \(E\) has an upper-half-plane zero. It does not establish Hermite--Biehler.

A third hostile flips the one-sided exponential convention to make the imaginary-axis inequality pass while reversing the source causal orientation.

Thus the next executable source identity is:

> The completed theta-tail Green form equals the Wronskian of the two reciprocal parity sections.

If established with a positive state norm, it closes the crossing-sign gate and ties the old odd port directly to de Branges phase geometry.
