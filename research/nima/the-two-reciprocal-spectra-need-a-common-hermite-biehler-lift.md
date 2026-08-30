# The two reciprocal spectra need a common Hermite--Biehler lift

The scalar return
\[
g(z)
\]
and the closure factors
\[
1-g(z),
\qquad
1+g(z)
\]
live naturally in the upper-half-plane transfer-function category. They are not automatically entire characteristic sections comparable with \(\xi\).

A common determinant-line lift is required.

Suppose the source colligation provides a holomorphic reference section \(E(z)\), zero-free in the upper half-plane, such that
\[
g(z)
=
\frac{E^{\#}(z)}{E(z)},
\qquad
E^{\#}(z)=\overline{E(\bar z)}.
\]
Then
\[
1-g(z)
=
\frac{E(z)-E^{\#}(z)}{E(z)},
\]
\[
1+g(z)
=
\frac{E(z)+E^{\#}(z)}{E(z)}.
\]

The actual entire or meromorphic closure sections are the numerators
\[
A(z)
=
\frac{E(z)+E^{\#}(z)}{2},
\]
\[
B(z)
=
\frac{E(z)-E^{\#}(z)}{2i}.
\]
Up to fixed phases, \(A\) and \(B\) are the two reciprocal parity determinants.

If
\[
|E^{\#}(z)|<|E(z)|
\]
in the upper half-plane, then \(E\) is Hermite--Biehler and
\[
g=\frac{E^{\#}}{E}
\]
is Schur. The zeros of \(A\) and \(B\) are real, simple under regularity, and interlace.

This makes the authority order exact:

\[
\text{source colligation}
\to
E
\to
g=E^{\#}/E
\to
(A,B)
\to
\text{two extension spectra}.
\]

The forbidden reverse order is:

\[
\xi\text{ zeros}
\to
A
\to
\text{choose interlacing }B
\to
E=A-iB.
\]

The common lift also resolves a normalization issue. Multiplying \(E\) by a real entire zero-free factor multiplies both \(A\) and \(B\) coherently and leaves \(g\) unchanged. Multiplying the two closure sections independently generally destroys the existence of one common return.

The source should therefore produce \(E\) as a perturbation determinant, Jost section, or outgoing reference determinant before either parity closure is imposed. The reciprocal involution then produces \(E^{\#}\).

The candidate \(\xi\) identification is one of
\[
A(z)
=
N(z)\,
\xi\left(\frac12-iz\right)
\]
or
\[
B(z)
=
N(z)\,
\xi\left(\frac12-iz\right),
\]
with \(N\) a source-derived real entire zero-free factor. The other numerator is the canonical companion spectrum.

This architecture has a decisive noncircular theorem:

> The energy identity proves \(E\) is Hermite--Biehler before the scalar Mellin comparison identifies one of its real or imaginary parts with \(\xi\).

If the identification is established first and Hermite--Biehler is then inferred from RH-equivalent inequalities, the proof is circular.

Completion gates are:

1. finite-cutoff sections \(E_X\) exist with a common phase frame;
2. \(E_X^{\#}/E_X\) equals the protected return \(g_X\);
3. \(E_X\) converges locally uniformly after source-authorized normalization;
4. the upper-half-plane zero-free property survives;
5. \(A_X,B_X\) converge as determinant-line sections;
6. one limit is identified with \(\xi\), and the other remains independently defined.

The smallest hostile constructs Schur functions \(g_X\) but chooses incompatible outer factors \(E_X\), so no completed determinant-line lift exists.

A second hostile identifies
\[
A=\xi
\]
and chooses \(B\) by solving the Hermite--Biehler inequality. That imports the desired zero geometry into the companion.

A third hostile proves \(g\) is inner but not meromorphic or continuable across the seam. Then \(A\) and \(B\) exist only as boundary distributions, not entire sections.

Thus the next irreducible constructor is the common outgoing determinant section \(E\). It is the bridge from passive scattering to an entire two-spectrum theory.
