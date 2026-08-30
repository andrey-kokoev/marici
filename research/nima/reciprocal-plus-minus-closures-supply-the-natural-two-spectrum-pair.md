# Reciprocal plus/minus closures supply the natural two-spectrum pair

The scalar scattering and scalar Weyl pictures identify a canonical candidate for the missing reference extension.

Let
\[
g(z)
\]
be the symmetry-protected scalar dark return. Assume it is Schur in the upper half-plane and has unit-modulus boundary values on the regular seam.

The two source reciprocal closures are the phases
\[
C_{+}=+1,
\qquad
C_{-}=-1.
\]
Their scalar Evans sections are
\[
D_{+}(z)=1-g(z),
\qquad
D_{-}(z)=1+g(z).
\]

On the seam, write
\[
g(x)=e^{i\phi(x)}.
\]
Then

- \(D_{+}(x)=0\) when
  \[
  \phi(x)\in2\pi\mathbb Z;
  \]
- \(D_{-}(x)=0\) when
  \[
  \phi(x)\in(2\mathbb Z+1)\pi.
  \]

If the phase is monotone, these two spectra interlace automatically.

The Cayley transform
\[
m(z)
=
i\,\frac{1+g(z)}{1-g(z)}
=
i\,\frac{D_{-}(z)}{D_{+}(z)}
\]
is a scalar Nevanlinna function. Its poles are the \(+\) closure spectrum and its zeros are the \(-\) closure spectrum.

Thus the source supplies the complete two-spectrum Weyl data without inventing interlacing poles:

\[
\text{reciprocal }+\text{ closure}
\longleftrightarrow
\text{reference poles},
\]
\[
\text{reciprocal }-\text{ closure}
\longleftrightarrow
\text{candidate zeta spectrum},
\]
or vice versa according to the frozen sign convention.

This is a much stronger architecture than choosing a reference sequence after observing the zeros. Both closures arise from the same return \(g\) and differ only by the source involution character.

The finite determinant ratio also has exact authority:
\[
\frac{D_{-}}{D_{+}}
=
\frac{1+g}{1-g}.
\]
No canonical product or zero-dependent interpolation is required.

The remaining source obligations are:

1. derive the scalar protected return \(g(z)\) from the doubled theta-wall colligation;
2. prove \(g\) is Schur from the energy identity;
3. prove its seam boundary value is inner or lossless;
4. prove \(C_{\pm}=\pm1\) are the actual reciprocal parity closures;
5. identify one of \(D_{\pm}\) with the completed \(\xi\)-section up to a nowhere-zero factor;
6. independently characterize the other extension spectrum;
7. prove minimality so the Cayley transform is the full dark Weyl function.

There is one sign subtlety. The Cayley transform shown maps the unit disk to one half-plane under a chosen convention. Replacing \(i\) by \(-i\) may be required by the Green form. The source flux orientation must decide the sign.

This construction predicts that zeta zeros should interlace a second canonical arithmetic spectrum. That reference spectrum is experimentally accessible from the same finite cutoff colligation by flipping only the reciprocal closure sign.

The sharp numerical pilot is therefore:

1. build finite-cutoff \(g_X(x)\);
2. locate crossings of \(g_X(x)=+1\);
3. locate crossings of \(g_X(x)=-1\);
4. test interlacing and cutoff stability;
5. compare one crossing family with zeta ordinates without fitting the other.

The smallest hostile derives \(D_{-}\) from \(\xi\) and defines
\[
D_{+}
\]
by inserting artificial interlacing poles. It does not produce a common Schur return.

A second hostile constructs both scalar sections but their ratio fails the Nevanlinna sign test. Then they are not spectra of two self-adjoint rank-one extensions.

A third hostile proves the \(\pm\) closures at finite cutoff while the phase frame flips with cutoff, destroying stable interlacing.

This is now the cleanest source-authorized two-spectrum candidate in the programme:

> The two reciprocal parity closures of one conservative dark return should produce the zeta spectrum and its canonical interlacing reference spectrum.
