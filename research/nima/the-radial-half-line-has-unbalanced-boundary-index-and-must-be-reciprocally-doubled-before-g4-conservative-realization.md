# The radial half-line has unbalanced boundary index and must be reciprocally doubled before G4 conservative realization

## Question

Can the single radial history graph on \(\mathbb R_+\) itself be the conservative first-order block required by G4?

## Claim boundary

No. Its derivative has a one-signed boundary form and admits no skew-adjoint boundary condition on that carrier. The minimal conservative realization is the reciprocal double with opposite derivative orientation. Its diagonal boundary sewing is maximal isotropic and reproduces the source wall Krein matrix. This fixes the differential and boundary part of the finite G4 target, but not its arithmetic loading, Wronskian incidence comparison, or Xi chain map.

## Single radial half-line

Let

\[
D_+=\partial_t,
\qquad
\operatorname{Dom}D_{+,\max}=H^1(\mathbb R_+).
\]

For rapidly decaying \(f,g\), integration by parts gives

\[
\langle D_+f,g\rangle+\langle f,D_+g\rangle
=-f(0)\overline{g(0)}.
\]

The boundary space is one-dimensional and its form is strictly negative. Its only isotropic subspace is zero, which imposes \(f(0)=0\). That condition is skew-symmetric but is not hypermaximal neutral: its Green orthogonal is the full boundary space rather than itself. Equivalently, the first-order half-line derivative has unequal deficiency directions and no skew-adjoint extension on the single channel.

Therefore the radial graph

\[
D_t\rho=e-\frac12w
\]

is a closed forced history graph but not by itself a conservative extension. The wall value \(\rho(0)\) cannot be retained in a skew-adjoint single-channel domain.

## Reciprocal double

Introduce the oppositely oriented partner

\[
D_-=-\partial_t
\]

on a second copy of \(H^1(\mathbb R_+)\), and define

\[
\mathbb D=
\begin{pmatrix}
D_+&0\\
0&D_-
\end{pmatrix}.
\]

For \(F=(f_+,f_-)\) and \(G=(g_+,g_-)\),

\[
\langle\mathbb DF,G\rangle+
\langle F,\mathbb DG\rangle
=
-f_+(0)\overline{g_+(0)}
+f_-(0)\overline{g_-(0)}.
\]

Thus the boundary Green matrix is

\[
J_\partial=
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix}.
\]

This is exactly the real wall Krein form already present in the retained G4 boundary architecture.

## Maximal-isotropic sewing

For a unit scalar \(u\), impose

\[
f_-(0)=u f_+(0).
\]

The graph

\[
\Lambda_u=\{(c,uc):c\in\mathbb C\}
\]

is isotropic because

\[
-|c|^2+|uc|^2=0.
\]

It has half the dimension of the nondegenerate boundary space, hence is maximal isotropic. The corresponding doubled derivative is skew-adjoint once the trace pair is complete.

The source-oriented diagonal sewing uses the reciprocal reversal already fixed by the wall comparison. No free positive metric or boundary phase may be inserted before checking its Real coherence.

## Forced doubled radial equations

The positive radial channel carries

\[
D_+\rho_+=e_+-\frac12w_+.
\]

The reciprocal channel must be written with its opposite orientation:

\[
D_-\rho_-=e_--\frac12w_-.
\]

Writing both equations with \(+\partial_t\) would erase the sign that balances the Green boundary form. Reciprocal transport must intertwine their source terms and wall traces before imposing \(\Lambda_u\).

This gives the minimal differential core of the finite conservative block:

\[
\mathbb T_X^{\rm rad}(z)=
\begin{pmatrix}
\mathbb D-z&U_X^{\rm rad}\\
N_X^{\rm rad}&B_X(z)
\end{pmatrix},
\]

where \(U_X^{\rm rad}\) must land in both oriented history channels.

## Adjoint versus analytic transpose

On the doubled Hilbert boundary carrier, the Green return selected by the Hermitian metric is the adjoint. On the source test-dual rigging, the return produced by the oriented path construction is initially the analytic transpose. They agree only after a Real comparison intertwines the two radial channels and has trivial mixed square.

The reciprocal double therefore does not eliminate the return-type gate. It supplies the carrier on which that gate can be stated without type mismatch.

## Laplace readout

For the positive channel,

\[
zR_+(z)-\rho_+(0)=E_+(z)-\frac12W_+(z).
\]

The oppositely oriented channel has the correspondingly reversed integration-by-parts border. A conservative scalar readout must be formed only after sewing the two wall traces. Applying the one-channel Laplace formula twice with the same sign fails the doubled Green identity.

## Hostiles

A finite checker must reject:

1. a single half-line derivative declared skew-adjoint while retaining a nonzero wall trace;
2. two radial copies with the same derivative orientation;
3. diagonal sewing with a nonunit boundary multiplier;
4. reciprocal source transport that fails to exchange the two oriented equations;
5. analytic transpose replaced by Hermitian adjoint before the Real comparison;
6. scalar Laplace aggregation performed before maximal-isotropic wall sewing.

## Disposition

The previous interface request can be narrowed. G4's conservative differential core, if it realizes the radial response, must contain the reciprocal double \(\partial_t\oplus(-\partial_t)\) with a complete two-channel trace and maximal-isotropic reciprocal sewing. A single radial half-line is structurally insufficient.

The remaining unknowns are the source identification of this doubled carrier with G4, the paired Wronskian and endpoint source terms, the arithmetic feature lift, the adjoint/transpose Real comparison, and the full jet chain map. No RH conclusion is authorized.
