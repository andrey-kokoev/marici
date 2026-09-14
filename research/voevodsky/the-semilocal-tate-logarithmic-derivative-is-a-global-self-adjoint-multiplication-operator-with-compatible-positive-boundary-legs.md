# The semilocal Tate logarithmic derivative is a global self-adjoint multiplication operator with compatible positive boundary legs

## Angular Mellin carrier

Let

\[
\mathscr H_S
=
\bigoplus_{\chi\in\widehat K_S}
L^2
\left(
\mathbb R,
\frac{ds}{2\pi}
\right)
\]

be the angular Mellin decomposition of the semilocal observer carrier. The observer transform is

\[
\mathcal M_Sg
=
(m_{g,\chi}(s))_\chi.
\]

With normalized compact angular Haar measure and Mellin convention,

\[
\boxed{
\|g\|_2^2
=
\sum_\chi
\int
|m_{g,\chi}(s)|^2
\frac{ds}{2\pi}.
}
\]

## Real Tate symbol

On the unitary axis, each local/product Tate gamma factor is unimodular:

\[
|\gamma_\chi(s)|=1.
\]

Define

\[
\boxed{
w_\chi(s)
=
\frac1i
\partial_s
\log\gamma_\chi(s)
=
2V_\chi(s).
}
\]

For a consistently chosen branch away from discrete winding jumps, `w_chi(s)` is real almost everywhere. Branch changes alter only the separately tracked integer spectral-flow/endpoint datum, not the a.e. derivative.

The normalization is chosen so that

\[
\boxed{
W_S(g*k^*)
=
\sum_\chi
\int
\overline{m_{k,\chi}(s)}
w_\chi(s)
m_{g,\chi}(s)
\frac{ds}{2\pi}.
}
\]

If the relative projection formula is written with `V_chi/pi` against `ds`, this is the same identity because `w_chi=2V_chi` and the carrier measure is `ds/(2pi)`.

## Multiplication operator

Define

\[
\boxed{
(A_Sm)_\chi(s)
=w_\chi(s)m_\chi(s)
}
\]

with maximal domain

\[
\boxed{
D(A_S)
=
\left\{
m\in\mathscr H_S:
\sum_\chi
\int
|w_\chi(s)|^2
|m_\chi(s)|^2
\frac{ds}{2\pi}
<\infty
\right\}.
}
\]

Because `w_chi` is a real measurable function on the disjoint-union spectral space,

\[
\boxed{
A_S=A_S^*.
}
\]

No lower bound is required for self-adjointness.

## Closed Weil form

The canonical form domain is

\[
\boxed{
\mathcal D_S
=D(|A_S|^{1/2})
}
\]

or explicitly

\[
\mathcal D_S
=
\left\{
m:
\sum_\chi
\int
|w_\chi(s)|
|m_\chi(s)|^2
\frac{ds}{2\pi}
<\infty
\right\}.
\]

Define

\[
\boxed{
q_S(m,n)
=
\langle
|A_S|^{1/2}m,
\operatorname{sgn}(A_S)
|A_S|^{1/2}n
\rangle.
}
\]

This is a closed symmetric indefinite form on `D_S`, and

\[
q_S(\mathcal M_Sg,
\mathcal M_Sk)
=W_S(g*k^*).
\]

Smooth compactly supported observers lie in `D_S` because their angular Mellin transforms decay rapidly while logarithmic gamma derivatives have at most polynomial/logarithmic growth.

## Global positive boundary legs

Let

\[
A_{S,+}
=
\max(A_S,0),
\qquad
A_{S,-}
=
\max(-A_S,0).
\]

Define

\[
\boxed{
R_{S,+}
=A_{S,+}^{1/2},
\qquad
R_{S,-}
=A_{S,-}^{1/2}.
}
\]

Both are closed operators with common intersection form domain `D_S`. The global positive boundary feature is

\[
\boxed{
\Phi_S^{boundary}(g)
=
(R_{S,+}\mathcal M_Sg,
R_{S,-}\mathcal M_Sg)
\in
\mathscr H_S
\oplus
\mathscr H_S.
}
\]

Its ordinary positive norm is

\[
\boxed{
\|\Phi_S^{boundary}(g)\|^2
=
\langle
\mathcal M_Sg,
|A_S|\mathcal M_Sg
\rangle.
}
\]

With the fundamental symmetry

\[
J_S
=
\begin{pmatrix}
I&0\\
0&-I
\end{pmatrix},
\]

one has

\[
\boxed{
\langle
\Phi_S^{boundary}(g),
J_S\Phi_S^{boundary}(k)
\rangle
=W_S(g*k^*).
}
\]

## Packet-successor compatibility

Let

\[
E_0
\subset
E_1
\subset
\cdots
\subset
\mathcal D_S
\]

be any increasing observer packets. Do not take the positive part of the compressed finite Gram matrix. Instead restrict the same global legs:

\[
\Phi_{S,r}^{boundary}
=
\Phi_S^{boundary}|_{E_r}.
\]

For the inclusion `i_(r,r+1)`,

\[
\boxed{
\Phi_{S,r+1}^{boundary}
i_{r,r+1}
=
\Phi_{S,r}^{boundary}.
}
\]

Thus every packet-successor square commutes exactly.

This repairs the obstruction

\[
(i^*Ai)_+

e
i^*A_+i
\]

because global functional calculus is performed before packet restriction.

## Relation to packetwise Jordan legs

The finite matrix Gram form is

\[
W^{E_r}
=(\Phi_S^{boundary}|_{E_r})^*
J_S
(\Phi_S^{boundary}|_{E_r}).
\]

Its intrinsic Jordan decomposition need not coincide with the restriction of `A_(S,+/-)`. Nevertheless both have the same signed readout.

The global restriction is the coherent choice; the packetwise Jordan decomposition is the minimal finite-dimensional choice. Coherence, not finite-dimensional minimality, selects the former.

## Semilocal endpoint convention

In Connes's semilocal theorem, each local principal-value distribution is normalized by its additive character. Under the local Tate transform, that normalization is already encoded in the choice of gamma factor and its spectral-flow branch.

Therefore no independent point-evaluation endpoint form is appended to `A_S` in this semilocal construction. Adding one would double-count the local normalization.

For the globally completed explicit formula, pole evaluations at `s=0,1` are additional boundary channels. They require graph-domain summands and are not claimed to be included here.

## Sonin sector

The multiplier realization describes the Tate--Hardy boundary form. It does not by itself identify the exact eigenvalue-one intersection

\[
P_{\{1\}}(B_\Lambda)
\]

inside the prolate tower.

A physical semilocal positive filler must map the stable Sonin atom into a null, endpoint, or separate positive summand according to the source theorem. The present construction supplies the global boundary carrier but not that physical identification.

## Cutoff convergence target

The centered scalar theorem gives, for observers in `D_S`,

\[
C_{\Lambda,S}(g,k)
\longrightarrow
\langle
\Phi_S^{boundary}(g),
J_S\Phi_S^{boundary}(k)
\rangle.
\]

To obtain convergence of positive legs, one needs cutoff residual maps

\[
R_{\Lambda,+},
\bindnasrepma
R_{\Lambda,-}
\]

on the same source graph domain satisfying

\[
R_{\Lambda,\pm}g
\longrightarrow
R_{S,\pm}\mathcal M_Sg.
\]

This remains the physical prolate bulk-removal theorem.

## Positivity gate

The semilocal Weil form is positive on a source subspace exactly when

\[
R_{S,-}\mathcal M_Sg
=0
\]

for every observer in that subspace.

The global two-polarity construction therefore packages, but does not prove, positivity.

## Disposition

The semilocal Tate boundary has a global closed realization:

\[
\boxed{
A_S
=
\bigoplus_\chi
M_{(1/i)\partial_s\log\gamma_\chi}.
}
\]

Its spectral square roots give compatible positive and negative boundary legs on every observer packet. The packet-successor coherence problem is solved at the abstract Tate boundary. The remaining gate is the intertwiner from orthogonally bulk-removed prolate residuals to these global Mellin multiplication legs, including the Sonin atom.
