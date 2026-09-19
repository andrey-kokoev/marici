# The reciprocal doubled Euler chart makes the seam scattering transition unitary

The one-chart Euler inverse need not be self-adjoint.  The physical seam uses
the reciprocal pair.  With the source-reflected Euler orientation,

\[
D_-(\lambda)=D_+(\lambda)^*,
\qquad
R_-(\lambda)=R_+(\lambda)^*.
\]

Define

\[
K_+=D_+R_+,
\qquad
K_-=D_-R_-.
\]

Although `K_-` need not literally equal `K_+^*` because the factors occur in
the reverse order, cyclic Fredholm determinant invariance gives

\[
\det_F(I-K_-)
=\det_F(I-D_+^*R_+^*)
=\det_F(I-R_+^*D_+^*)
=\overline{\det_F(I-D_+R_+)}.
\]

Therefore the doubled determinant transition

\[
\mathcal S_{\rm op}(\lambda)
=\frac{\det_F(I-K_+(\lambda))}
       {\det_F(I-K_-(\lambda))}
\]

has unit modulus wherever finite and nonzero, and satisfies

\[
\mathcal S_{\rm op}^{\#}=\mathcal S_{\rm op}^{-1}.
\]

At zeros and poles this is a meromorphic determinant-line statement with the
reciprocal divisor orders exchanged.  Thus seam unitarity and reflected frame
gluing are consequences of the doubled source charts, not of falsely making a
single Euler impedance self-adjoint.

This does not identify `S_op` with the completed Fourier--Tate/Xi transition.
That comparison now reduces to equality on an open Euler chart (or equality of
their logarithmic connections plus one source normalization), after which the
meromorphic identity theorem applies.
