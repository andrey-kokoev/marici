# Combining H234 and H134 localizes the open class to the kernel of positive-to-signed forgetfulness

## The combined horn

For each refinement stage \(k\), use the four semilocal faces

\[
H_{123,k},\quad H_{124,k},\quad H_{134,k},\quad H_{234,k}.
\]

Their tetrahedral equation is

\[
\boxed{
H_{124,k}\circ(H_{234,k}*\eta_{12,k})
=
H_{134,k}\circ(\eta_{34,k}*H_{123,k}).}
\]

Right whiskering along the integrated observer representation
\(\eta_{12,k}=U_{S,k}^{obs}\) is faithful on the observer-generated geometric
subcategory. Hence \(H_{234,k}\) is uniquely recovered from the other three
faces.

The recovered representative is

\[
H_{234,\Lambda}^{obs}(U_S(h))
=
\operatorname{Tr}(P_\Lambda\widehat P_\Lambda U_S(h))
-2h(1)\log\Lambda
-\langle M_{g_h},\mathcal L_S\rangle,
\]

which lies in the rapid-decay ideal. Therefore the displayed tetrahedral
identity holds in the signed asymptotic quotient \(\mathsf{Asym}_S\).

## k-axis consequence

All stage faces are obtained by successor/refinement whiskering. Consequently

\[
\mathsf S_k(H_{234,k})=H_{234,k+1},
\qquad
\mathsf S_k(H_{134,k})=H_{134,k+1},
\]

and the combined horn commutes with the \(k\)-successor. Existing propagation
covers all \(7^3=343\) translated tetrahedra.

Thus, at signed asymptotic level,

\[
\boxed{
\Delta_{\mathrm{pyr},k}=0
\quad\text{naturally in }k.}
\]

This is stronger than merely knowing that the DG discrepancy is closed.

## Where the unresolved class lives

Let

\[
\mathsf{Pos}_S\longrightarrow\mathsf{Asym}_S
\]

be the forgetful passage from positive Hilbert/Green realizations to signed
relative-trace modifications. The combined horn proves that the image of the
physical discrepancy vanishes in \(\mathsf{Asym}_S\).

Therefore any remaining obstruction belongs to the kernel of this forgetful
map:

\[
\boxed{
[\Delta_{\mathrm{phys},k}]
\in
\ker\!igl(
H(\mathsf{Pos}_S)
\to
H(\mathsf{Asym}_S)
\bigr).}
\]

It is not another signed trace or coherence obstruction. It is specifically a
failure—or still-unproved existence—of a positive metric lift of an already
coherent signed horn.

## Concrete meaning of the lift

On face \(234\), the lift requires the physical common remainder

\[
G_{\mathrm{phys},\alpha}^T-(D_\alpha)_+
=
G_{\mathrm{phys},\alpha}^0-(D_\alpha)_-
\succeq0.
\]

On face \(134\), it requires the boundary realization of the Sonin Green form
to equal the transported completed endpoint swap form.

The tetrahedral equation says these are not independent choices. A positive
lift of one face fixes the required lift of the other by faithful whiskering,
provided the lift remains inside the source-authorized positive category.

## Reduced target

The next theorem should therefore not re-prove the signed faces. It should prove
that right whiskering remains liftable on the positive fiber over the already
recovered signed face:

\[
\boxed{
R_{12}^{Pos}:
\operatorname{Lift}_{Pos}(H_{234,k})
\longrightarrow
\operatorname{Lift}_{Pos}
\bigl(
H_{134,k}\circ(\eta_{34,k}*H_{123,k})
\circ H_{124,k}^{-1}
\bigr)
}
\]

has a source-authorized point, naturally in \(k\).

Existence of that point is exactly the combined positive filler. Uniqueness,
when needed, follows only after quotienting feature-range unitary freedom.

## Conclusion

Combining the Morse and conductor faces reveals that the signed coherence
problem is already solved. The remaining problem is a positive lifting class
in the kernel of positive-to-signed forgetfulness, compatible with the
\(k\)-successor.
