# The minimal joint boundary reservoir is a two-port Weyl matrix whose cross-entry is the Evans observer

## Why the one-port completion fails

For a history generator \(D\), source incidence \(B_f\), and endpoint observation \(E_0\), the physical Evans transfer is

\[
F(z)
=
E_0(D-z)^{-1}B_f.
\]

The canonical one-port symmetric completion instead produces

\[
B_f^\times(D-z)^{-1}B_f,
\]

which is source autocorrelation. It is quadratic in \(f\) and does not equal the endpoint transfer.

Therefore source return and endpoint evaluation must remain distinct ports.

## Joint boundary map

Use the two-component boundary observation

\[
J^\times u
=
\begin{pmatrix}
B_f^\times u\\
E_0u
\end{pmatrix}.
\]

Its transpose is the two-column incidence

\[
J
=
\begin{pmatrix}
B_f&E_0^\times
\end{pmatrix}.
\]

Here \(E_0^\times\) is a boundary distribution in a rigged realization, or the Riesz representative of the endpoint trace after passing to an admitted graph metric.

The associated Weyl matrix is

\[
M(z)
=
J^\times(D-z)^{-1}J.
\]

Explicitly,

\[
M(z)
=
\begin{pmatrix}
B_f^\times R_zB_f
&
B_f^\times R_zE_0^\times
\\
E_0R_zB_f
&
E_0R_zE_0^\times
\end{pmatrix},
\qquad
R_z=(D-z)^{-1}.
\]

The physical Evans observer is exactly the lower-left cross-entry:

\[
F(z)=M_{21}(z).
\]

Thus the joint reservoir contains both autocorrelation and the physical one-point transfer without identifying them.

## Symmetric bulk descriptor

The corresponding system-level block is

\[
\mathbb A
=
\begin{pmatrix}
D&B_f&E_0^\times\\
B_f^\times&0&0\\
E_0&0&0
\end{pmatrix}.
\]

On a valid rigged domain this is formally self-transpose. The spectral weight may be taken as

\[
P
=
\operatorname{diag}(I_{\rm history},0,0).
\]

The frozen two-port coordinates carry boundary data but no artificial spectral mass.

## Weyl identity

If the descriptor relation is closed and selfadjoint, its Poisson operator satisfies

\[
M(z)-M(w)^*
=
(z-
\overline w)
\gamma(w)^*P\gamma(z).
\]

This is the desired determinant--Green mate. It simultaneously compares all four source/endpoint matrix entries and preserves the distinction between the physical transfer and source autocorrelation.

## Why matrix positivity is not enough

For \(\operatorname{Im}z>0\), the Weyl identity gives matrix positivity of the appropriate imaginary part. But a positive matrix-valued Herglotz function can have a vanishing off-diagonal entry.

Therefore positivity of the full two-port Weyl matrix does not imply

\[
M_{21}(z)
\ne0.
\]

Zero exclusion for the Evans entry is an incidence-chamber condition: the distinguished source-to-endpoint minor must remain nonsaturated.

## Birman--Schwinger chamber

After eliminating a coercive complementary block, the chamber condition should take the form

\[
K_X(z)
=
B_X(z)^{-1/2}
U_X(z)U_X(z)^*
B_X(z)^{-1/2},
\]

with

\[
\|K_X(z)
\|<1.
\]

Then

\[
R_X(z)
=
B_X(z)^{1/2}
(I-K_X(z))
B_X(z)^{1/2}
\]

is strictly positive, preventing saturation of the distinguished cross-port incidence.

This chamber estimate is additional to the Weyl identity. It is not supplied by 4-simplex coherence alone.

## Relation to the five-vertex architecture

The two-port Weyl reservoir supplies the missing typed carrier shared by:

- reciprocal realization \(R\);
- determinant/cofactor realization \(D\);
- Green boundary realization \(G\).

The weighted Weyl identity is the shared \(R\)-\(D\)-\(G\) coherence cell. The open-minor estimate is the chamber condition allowing this cell to participate in the prospective 4-simplex.

## Remaining domain work

To turn the formal block into an admitted constructor, one must prove:

1. \(E_0\) is continuous on the chosen history graph domain;
2. \(B_f\) and \(B_f^\times\) are opposite rigged incidences;
3. the three-by-three relation is closed and selfadjoint;
4. its cross Weyl entry equals the completed Xi/Evans section up to a nowhere-zero unit;
5. the distinguished chamber estimate holds.

## Disposition

The minimal bulk completion is not a one-port adjoint block. It is a two-port source/endpoint Weyl system. This constructs the correct formal shared carrier for the missing reciprocal--determinant--Green triangle and isolates the remaining theorem as a cross-entry incidence-chamber bound.
