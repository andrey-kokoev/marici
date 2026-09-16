# Segmentwise triangulation of C13 into the C12 direction

## Question

Do the first segments of the eight-node edge

\[
C_{13}:V_1\longrightarrow V_3
\]

have source-derived triangulations in the \(C_{12}\) direction, and which segment is the first unresolved one?

## Claim boundary

This packet audits formulas already present in prior semilocal research. It distinguishes an existing source theorem from a formula reconstructed only by choosing a pullback. It does not identify an ordinary finite-norm positive Green realization or prove positivity of the Weil form.

Use \(k\) only for realization dimension. For edge subdivision position write

\[
C_{ij}[r],\qquad r=0,\ldots,7,
\]

and

\[
\sigma_{ij}[r]:C_{ij}[r]\longrightarrow C_{ij}[r+1],
\qquad r=0,\ldots,6.
\]

The adjacent triangular comparison is

\[
H_{123}[r]:
\sigma_{32\mid13}[r+1]\sigma_{13}[r]
\Rightarrow
\sigma_{12\mid13}[r].
\]

## Vertex and edge typing

The four semilocal presentations are:

\[
V_1=\text{source test and polarization presentation},
\]

\[
V_2=\text{semilocal geometric presentation},
\]

\[
V_3=\text{dual and canonical spectral presentation},
\]

\[
V_4=\text{cutoff finite-part trace presentation}.
\]

The edge \(C_{13}\) is the source-to-spectral comparison. It is not the boundary-four-front-to-Euler map. Its eight nodes and seven arrows are already listed in `the-source-to-spectral-edge-has-an-eight-node-factorization-from-convolution-polarization-to-the-dual-canonical-connection.md`.

The unsubdivided edge \(C_{12}\) is the integrated semilocal representation

\[
C_{12}(g)=U_S(g),
\]

with polarized law

\[
U_S(g_1*g_2^*)=U_S(g_1)U_S(g_2)^*.
\]

## Segment r = 0

The operation is observer-to-convolution polarization:

\[
g\longmapsto g*g^*.
\]

The \(C_{12}\)-direction realization is source-derived from the star-representation law

\[
U_S(g*g^*)=U_S(g)U_S(g)^*.
\]

Status: source-verified.

## Segment r = 1

The operation is convolution polarization to multiplicative Mellin boundary value. Mellin transform sends convolution to multiplication, while the integrated representation sends convolution to operator composition. The positive face \(H_{123}\) is exact unitary Gram transport.

Status: source-verified.

## Segment r = 2

The operation inserts the dual Euler multiplier

\[
A_S^+(s)=
\prod_{p\in S\setminus\{\infty\}}
L_p(1/2+is)^{-1}.
\]

The semilocal Sonin amplification satisfies

\[
\mathcal F_\mu w_S(\Sigma_Sf)(s)
=
A_S^+(s)\mathcal F_\mu w(f)(s).
\]

Thus \(\Sigma_S\) is the geometric realization of this segment.

Status: source-verified.

## Segment r = 3

Let

\[
\xi_+=\Omega_S^+f,
\qquad
\xi_-=\Omega_S^-f.
\]

The two maps \(\Omega_S^+\) and \(\Omega_S^-\) are independently source-derived unitary identifications. Their relative scattering operator is

\[
(\Omega_S^+)^*\Omega_S^-=M_{J_S^{-1}}.
\]

Hence

\[
\sigma_{13}[3](\xi_+)
=
(\xi_+,M_{J_S^{-1}}\xi_+).
\]

Under the Hardy--Titchmarsh unitary \(\mathcal T_S\), the geometric triangulation is

\[
\sigma_{12\mid13}[3](\xi_+)
=
\left(
\mathcal T_S^{-1}\xi_+,
\mathcal T_S^{-1}M_{J_S^{-1}}\xi_+
\right).
\]

This pair is source-authorized because both spectral identifications are source-derived; it is not merely a pullback selected to force commutativity.

Status: source-verified.

## Segment r = 4

The operation sends the canonical and dual pair to the bilinear source-duality pairing

\[
B_S(\xi,\eta)=\int_{\mathbb R}\xi(s)\eta(s)\,ds.
\]

Its geometric transport is

\[
B_S^{\mathrm{geom}}(x_+,x_-)
=
B_S(\mathcal T_Sx_+,\mathcal T_Sx_-).
\]

The semilocal duality theorem identifies this with the original source pairing. This is a bilinear pairing between contragredient spaces, not the Hermitian product on either spectral space separately.

Status: source-verified.

## Segment r = 5

The operation retains the source-duality pairing and exposes the relative scattering phase. Let the two source-derived geometric identifications be

\[
\Sigma_S^\pm
=
\mathcal T_S^{-1}\Omega_S^\pm\mathcal T_\infty.
\]

Their relative geometric operator is

\[
\mathscr R_{\mathrm{geom},S}
=
(\Sigma_S^+)^*\Sigma_S^-.
\]

Unitary conjugation gives

\[
\mathscr R_{\mathrm{geom},S}
=
\mathcal T_\infty^*
M_{J_S^{-1}}
\mathcal T_\infty.
\]

Thus the geometric triangulation adjacent to \(\sigma_{13}[5]\) sends the transported source pairing to the same pairing together with \(\mathscr R_{\mathrm{geom},S}\). Applying the spectral realization sends this operator to \(M_{J_S^{-1}}\), so \(H_{123}[5]\) is exact unitary conjugation.

This segment uses the relative unitary between two source identifications. The Tate/reference relative projection pair belongs to the later positive realization across \(C_{34}\); it is not required to define this \(C_{12}\)-direction transfer.

Status: source-verified.

## Segment r = 6

The terminal operation differentiates the relative phase:

\[
V_{\mathrm{loc},S}
=\frac1{2i}\partial_s\log J_{\mathrm{loc},S}.
\]

Transport it to the source realization by

\[
V_{\mathrm{geom},S}
=\mathcal T_\infty^*M_{V_{\mathrm{loc},S}}\mathcal T_\infty.
\]

Conjugating the differentiated-pairing Green identity by \(\mathcal T_\infty\) proves \(H_{123}[6]\). The finite-interval boundary term is retained; contour displacement places its limiting residues at the half-density endpoints. Prime extension is additive because \(J_{S\cup\{q\}}=J_SJ_q\), hence \(V_{S\cup\{q\}}=V_S+V_q\).

Status: source-verified.

## C14 compatibility

At each subdivision position the reconstructed transfer satisfies the other boundary route in the signed asymptotic category:

\[
\sigma_{24}\sigma_{12\mid13}[r]
=
\sigma_{34}\sigma_{13}[r].
\]

The weak form is the tetrahedral equation

\[
H_{124}[r]\circ(H_{234}[r]*C_{12}[r])
=
H_{134}[r]\circ(C_{34}[r]*H_{123}[r]).
\]

Prior work proves strict successor naturality of \(H_{123},H_{124},H_{134}\), uniquely recovers \(H_{234}\) by faithful right whiskering along the integrated observer representation, and propagates the equation through all \(7^3\) translated tetrahedra. Thus segmentwise \(C_{14}\) compatibility is complete in the signed asymptotic category. The later relative-positive feature construction supplies the regulator-relative lift. A simultaneous-regulator ordinary finite-norm Hilbert lift remains stronger.

## Corrections recorded

1. \(C_{13}\) is the global source-to-spectral edge, not a local boundary-to-Euler edge.
2. \(C_{34}\) is complete on the Bruhat--Schwartz core in the iterated-regulator relative positive-feature category; only stronger ordinary-Hilbert and simultaneous-regulator realizations remain open.
3. All seven \(C_{13}\) segments, \(r=0,\ldots,6\), have source-supported \(C_{12}\)-direction triangulations.
4. A dedicated eight-node semantic factorization of \(C_{12}\) has not been located. Segmentwise triangulation supplies all seven subdivision transfers on the observer-generated range.

## Disposition

All seven segmentwise triangulations survive the source-identity audit. Their compatibility with the \(C_{14}\) route holds throughout the seventh edgewise subdivision in the signed asymptotic category and lifts to the iterated-regulator relative-positive category. This constructs the subdivided \(C_{12}\) comparison on the observer-generated semilocal carrier. No simultaneous-regulator ordinary finite-norm Hilbert promotion is asserted.