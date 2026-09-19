# The relative scattering determinant is only the boundary-return factor, not the completed Xi transition

The operator constructed from

\[
K=(I-L)^{-1}C(I-A)^{-1}B
\]

is a relative correction after factoring the bare Euler loop.  Its Fredholm
determinant satisfies the Schur factorization

\[
\det(I-L-R)
=\det(I-L)\det_F(I-K)
\]

at finite cutoff and in every admitted relative determinant chart.  Therefore
the seam ratio

\[
\mathcal S_{\rm op}
=\det_F(I-K_+)/\det_F(I-K_-)
\]

contains only the boundary-mediated return factor.

The completed Fourier--Tate determinant transition also contains the graded
bare Euler line, endpoint/archimedean line, and relative boundary-return
factor. The graded Euler line is itself decomposed—not supplemented—by its
primitive, square, and connected factors:

\[
\mathcal S_{\rm Euler}^{\rm gr}
=\mathcal S_{\rm prim}\mathcal S_{\rm sq}\mathcal S_{\det_3}.
\]

Consequently comparing `S_op` alone with the Xi transition is ill-typed and
generically false. The correctly typed total transition is

\[
\mathcal S_{\rm tot}
=\mathcal S_{\rm Euler}^{\rm gr}
 \mathcal S_{\rm end/\infty}
 \mathcal S_{\rm op}
=\mathcal S_{\rm prim}\mathcal S_{\rm sq}\mathcal S_{\det_3}
 \mathcal S_{\rm end/\infty}\mathcal S_{\rm op}.
\]

Including both `S_Euler` and the three factors separately would double-count
the first two cumulants and connected tail. Only `S_tot` can be compared with
the completed theta/Fourier--Tate line. The relative scattering construction
closes one factor and its Green orientation; it does not by itself compile Xi.
Equality on the Euler half-plane is meaningful only with this exclusive
either/or presentation of the graded Euler line.
