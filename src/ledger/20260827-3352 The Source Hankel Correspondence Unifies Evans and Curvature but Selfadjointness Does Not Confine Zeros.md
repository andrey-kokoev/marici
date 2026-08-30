# The Source Hankel Correspondence Unifies Evans and Curvature, but Selfadjointness Does Not Confine Zeros

Define the source Hankel history operator

\[
(\mathsf H_f\varphi)(q)
=\int_0^\infty f(q+a)\varphi(a)\,da.
\]

On the character `e_z(a)=e^{za}`, it produces the complete tail path `G_z`.
Endpoint evaluation gives the Evans transform, while source pairing gives the
ordered autocorrelation. Thus Evans and curvature are two covector faces of
one source-derived history correspondence.

For real theta forcing, the kernel is symmetric. Superexponential decay makes
the operator Hilbert--Schmidt and selfadjoint. Nevertheless selfadjointness has
no zero-confinement force for the endpoint matrix coefficient. The exact
two-cell Hankel matrix

\[
\begin{pmatrix}1&2\\2&0\end{pmatrix}
\]

is real symmetric and comes from nonnegative source data, while its endpoint
coefficient on `(1,r)` vanishes at `r=-1/2`, corresponding to
`z=-log 2+(2k+1)pi i` off the seam.

The canonical selfadjoint carrier is therefore not a Hilbert--Polya operator
whose spectrum is the Riemann zero set. Zeros remain cancellations of one
rigged matrix coefficient. A further theta/modular law must constrain the
distinguished endpoint covector and character orbit.

Research packet:
`research/grothendieck/the-source-hankel-correspondence-unifies-evans-and-curvature-but-selfadjointness-does-not-confine-zeros.md`

Exact checker:
`research/grothendieck/checkers/check_selfadjoint_hankel_endpoint_hostile.py`

The checker passes 6/6 exact tests.
