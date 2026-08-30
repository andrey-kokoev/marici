# The prime-loop companion linearization is finite-full but never uniformly Morita-full

## The canonical finite linearization

At cutoff \(X\), let

\[
L_X(s)e_p=p^{-s}e_p,\qquad p\le X.
\]

The ordinary Euler determinant has the exact two-sided companion realization

\[
\mathcal T_X(s)=
\begin{pmatrix}
I & L_X(s)\\
I & I
\end{pmatrix}.
\]

Eliminating the first sector gives

\[
\det \mathcal T_X(s)=\det(I-L_X(s)).
\]

Thus the prime-loop determinant already admits a two-sided linking presentation before any analytic completion. Unlike a scalar border, its Schur complement is the nontrivial operator \(I-L_X\), so the elimination does not collapse the construction to a one-dimensional readout.

The two off-diagonal arrows are nevertheless asymmetric:

\[
M_X=L_X(s),\qquad N_X=I.
\]

The identity return is a companion-linearization choice. It is not automatically the source-derived reciprocal sewing map.

## Finite fullness

For every finite cutoff and finite \(s\), all diagonal entries \(p^{-s}\) are nonzero. Hence \(L_X(s)\) is invertible. On the finite prime carrier, the two links therefore have full support and the companion block is algebraically full.

This explains why every finite determinant packet can pass a support audit.

## Uniform fullness fails exactly

On the ordinary prime Hilbert space,

\[
\sigma_{\min}(L_X(s))
=
\min_{p\le X}|p^{-s}|.
\]

For \(\sigma=\operatorname{Re}s>0\),

\[
\sigma_{\min}(L_X(s))
=
p_X^{-\sigma},
\]

where \(p_X\) is the largest retained prime. Therefore

\[
\lim_{X\to\infty}\sigma_{\min}(L_X(s))=0.
\]

The failure is uniform on every compact set with positive lower real part. If \(C\) is such a compact and \(\sigma_C=\inf_{s\in C}\operatorname{Re}s>0\), then

\[
\inf_{s\in C}\sigma_{\min}(L_X(s))
\le p_X^{-\sigma_C}\longrightarrow0.
\]

Consequently the elementary Euler link is finite-full but never uniformly Morita-full in the unweighted prime norm.

## Condition-number form

The defect is not merely a common scalar decay. For fixed \(\sigma>0\),

\[
\|L_X(s)\|=2^{-\sigma},
\qquad
\|L_X(s)^{-1}\|=p_X^{\sigma}.
\]

Hence

\[
\kappa(L_X(s))
=
\|L_X(s)\|\,\|L_X(s)^{-1}\|
=
\left(\frac{p_X}{2}\right)^\sigma
\longrightarrow\infty.
\]

No cutoff-independent change of coordinates uniformly equivalent to the source norm can repair this collapse.

## Consequence for the linking-block programme

A positive lower Morita margin on the whole completed prime carrier is too strong for the source Euler loop. It would reject the exact finite operator whose powers generate all Euler multiplicities.

The completion gate must instead be one of the following typed statements:

1. **Rigged fullness:** the link is an isomorphism between different weighted source and target rungs, with the weights recorded as part of the object type.
2. **Local finite-energy fullness:** lower bounds are required only on a source-authorized observable or defect subspace.
3. **One-sided determinant completion:** Schatten control is imposed on the connected return while primitive and square losses are routed through boundary anomaly lines.
4. **Boundary-relative fullness:** the completed linking relation is Fredholm only after quotienting or adjoining the seam and archimedean boundary objects.

These alternatives are not equivalent. The source constructor must select one.

## Relation to Schatten-three completion

The connected powers of \(L(s)\) may enter a Schatten-three or relative determinant completion even though \(L(s)\) itself has no lower bound. Schatten convergence controls compact determinant data; it does not imply Morita invertibility.

Therefore the two desired properties must remain separate:

\[
\text{relative determinant-class completion}
\quad\not\Rightarrow\quad
\text{uniform linking fullness}.
\]

Conversely, imposing uniform fullness on the raw prime loop would destroy the correct Euler decay.

## Reciprocal typing obstruction

The companion identity

\[
\det
\begin{pmatrix}
I&L_X\\
I&I
\end{pmatrix}
=
\det(I-L_X)
\]

proves existence of a finite two-sided linearization, but not constructor authority. The return arrow \(I\) must still be derived from reciprocal sewing, endpoint transport, or a declared evaluation-coevaluation pair.

If the source reciprocal arrow differs from \(I\), the correct determinant is the Schur return

\[
\det(I-N_XL_X),
\]

and equality with the Euler determinant requires an intertwining theorem, not a choice of basis.

## Hostile tests

1. Every finite \(L_X\) is invertible, but its minimum singular value tends to zero.
2. The determinant converges in an Euler region while the inverse-link norm diverges.
3. A companion identity return reproduces the determinant but has no reciprocal source authority.
4. A cutoff-dependent reweighting makes \(L_X\) isometric while its equivalence constants to the source norm diverge.
5. Schatten-three convergence of connected powers is mistaken for a lower linking margin.

## Verdict

The prime-loop operator supplies a canonical finite two-sided companion block, but it simultaneously falsifies uniform Morita fullness on the raw completed prime Hilbert carrier.

The next theorem cannot ask for a global positive lower linking margin. It must construct the source-typed relative or rigged linking category in which Euler decay is part of the object metric, then prove that the reciprocal return is authorized and that the remaining defect space is uniformly observed.
