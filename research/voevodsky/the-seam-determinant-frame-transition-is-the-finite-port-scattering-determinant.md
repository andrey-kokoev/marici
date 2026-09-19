# The seam determinant-frame transition is the finite-port scattering determinant

Let

\[
D_E(\lambda)=(I-L(\lambda))^{-1},\qquad
K_\pm(\lambda)=D_E(\lambda)R_\pm(\lambda).
\]

The Green jump is

\[
K_+-K_-=2\pi i\,D_E\beta^*\beta.
\]

Where `I-K_-` is invertible, factor

\[
I-K_+
=(I-K_-)
\left[I-2\pi i(I-K_-)^{-1}D_E\beta^*\beta\right].
\]

The Fredholm determinant lemma then gives the exact transition

\[
\frac{\det_F(I-K_+)}{\det_F(I-K_-)}
=
\det_{\rm port}\left[
I-2\pi i\,\beta(I-K_-)^{-1}D_E\beta^*
\right].
\]

The right side is a determinant on the finite physical polarity/observer port
(rank one in the scalar model).  It therefore supplies the meromorphic local
transition between the upper and lower determinant frames.  At points where a
chosen inverse fails, the equality is interpreted as an identity of Fredholm
determinant-line sections and extends by local numerator/denominator frames.

This constructs the seam gluing function from the source incidence and causal
Green jump; it is not fitted from Xi.  Unitarity on the seam requires the full
reciprocal doubled Euler/port relation, because the one-chart factor `D_E` need
not be self-adjoint by itself.  Equality of this scattering transition with
the completed Fourier--Tate/Xi transition is a separate comparison theorem.
