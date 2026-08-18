# 783 — The Cayley--Menger Contour Family Is Source-Normalized Before Weighted Specialization

## Question

Entries 781--782 close the parameter-space-thimble shortcut and show that the
rational exceptional line

\[
\ell_{\rm exc}=\mathbf Q\langle[0:1:0:-3]\rangle
\]

has no canonical affine generator in the serialized master frame. Does the
frozen primary construction contain a different source of physical
normalization?

## Source audit

The answer is narrower than either “yes” or “the source route is exhausted.”

The one-loop paper arXiv:2408.16386 defines the periods as pairings

\[
I(X)=\int_{\Gamma_X}u\,\varphi
\]

between twisted cocycles and fiber cycles. Its cited primary construction,
Benincasa--Vazao arXiv:2402.06558v3, gives the three-site cycle and loop measure
explicitly.

With

\[
y_{12}=|\ell|,\qquad
y_{23}=|\ell+P_2|,\qquad
y_{31}=|\ell-P_1|,
\]

the squared tetrahedron volume is the Cayley--Menger determinant of the six
lengths

\[
(y_{12},y_{23},y_{31},P_1,P_2,P_3).
\]

Equation (A.11) defines the physical loop contour by the simultaneous minor
inequalities

\[
\Gamma_3(P)=
\left\{
(-1)^{k+1}\operatorname{CM}(I_k,J_k)\ge0
\text{ for all prescribed minors},\ k=1,2,3
\right\}.
\]

Its boundary contains

\[
\operatorname{CM}(y^2,P^2)=0,
\]

where the tetrahedron becomes coplanar. Equation (A.12) also fixes the loop
measure, including the prefactor

\[
\frac{2\pi^{(d-3)/2}}{\Gamma((d-3)/2)}
\]

and the powers of the full determinant and its external \((2,2)\)-minor.

Thus the source supplies more than a homotopy class: it supplies an oriented
semialgebraic fiber-cycle family, its boundary stratification, and a normalized
measure.

## Type distinction

This does not contradict Entry 781. The source still supplies no Lefschetz
thimble in the external parameter base. Instead it supplies the incidence
family

\[
\mathfrak C_{\Gamma}
=
\{(P,y_{\rm loop}):y_{\rm loop}\in\Gamma_3(P)\}
\longrightarrow \mathcal P_{\rm ext}.
\]

This is a chain in the total space of the loop-variable family, not a chain in
the external base alone. Its weighted nearby specialization is nevertheless a
legitimate candidate for the missing physical source object, provided it is
constructed before projection to the coefficient system.

What remains absent is the map

\[
\operatorname{Sp}_{\rm wt}(\mathfrak C_{\Gamma})
\longrightarrow
\mathcal E_{\rm exc}
\]

into the rank-four exceptional coefficient block. Consequently neither its
image in \(\ell_{\rm exc}\), its deck character, nor its scalar pairing has yet
been computed.

## Narrow result

\[
\boxed{
\begin{gathered}
\text{The parameter-space-thimble route is exhausted,}\
\text{but the source-normalized Cayley--Menger contour family remains a}\
\text{distinct, correctly typed candidate for weighted specialization.}
\end{gathered}
}
\]

The normalization problem is therefore no longer “find a preferred rational
generator.” It is:

\[
\text{derive whether the normalized physical fiber-chain family maps to the
projective extension line.}
\]

No affine generator of \(\ell_{\rm exc}\) is selected by the present audit.

## Next finite falsifier

Freeze equations (A.7)--(A.12) and the weighted Rees charts of Entries
778--780. Then:

1. pull back the full incidence family \(\mathfrak C_\Gamma\), including every
   Cayley--Menger minor inequality;
2. compute its strict transform and exceptional boundary current chartwise;
3. retain the source prefactor and orientation;
4. derive the \(\mu_2\)-action, trace, and overlap homotopy;
5. construct the coefficient comparison map without choosing
   \((0,1,0,-3)\);
6. test whether its image lies in \(\ell_{\rm exc}\).

If the exceptional image is transverse to \(\ell_{\rm exc}\), this physical
activation route closes. If it lies in the line, the source measure supplies a
candidate affine normalization whose regulator-hierarchy invariance must then
be proved.

## Evidence packet

- `research/benincasa/cayley-menger-contour-family-gate.json`
- arXiv:2408.16386, equations (6), (7), and (12)--(17)
- arXiv:2402.06558v3, equations (3.6)--(3.10) and (A.7)--(A.12)
