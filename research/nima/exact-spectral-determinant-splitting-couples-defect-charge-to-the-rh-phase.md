# Exact spectral determinant splitting couples defect charge to the RH phase

## Record

The coupled invariant is not obtained by taking an ordinary top exterior power of an infinite-dimensional complement. It is produced by the determinant functor applied to an exact contour-spectral decomposition of the Fredholm pencil.

On a \(\Gamma\)-admissible patch, let \(T\) denote the reduced Fredholm pencil and let \(P_\Gamma\) be its finite-rank Riesz projection. Write
\[
\mathcal H^{\mathrm{red}}=\mathcal D\oplus\mathcal Q,
\qquad
\mathcal D=\operatorname{ran}P_\Gamma,
\qquad
\mathcal Q=\operatorname{ran}(I-P_\Gamma).
\]
The restriction \(T_{\mathcal Q}\) is invertible relative to the selected spectral window. The determinant functor supplies the multiplicative isomorphism
\[
\operatorname{Det}(T)
\cong
\det(C_{\mathcal D})\otimes\operatorname{Det}(T_{\mathcal Q}),
\]
where \(C_{\mathcal D}\) is the finite defect complex. The second factor is a relative or regularized Fredholm determinant line, never the ordinary determinant of the infinite complement.

## Connection constraint

Let the three lines carry connections
\[
\nabla^{T},\qquad \nabla^{\mathcal D},\qquad \nabla^{\mathcal Q}.
\]
The determinant-splitting isomorphism must be horizontal. In a compatible local trivialization its one-forms satisfy
\[
A_T=A_{\mathcal D}+A_{\mathcal Q},
\]
and therefore
\[
F_T=F_{\mathcal D}+F_{\mathcal Q}.
\]
Thus defect charge and complement phase cannot be independently assigned. A proposed pair of connections is inadmissible whenever its tensor curvature disagrees with the ambient source determinant connection.

On a zero-charge patch, \(\mathcal D=0\) and
\[
\det(C_{\mathcal D})\cong\mathbb C
\]
canonically, with its trivial connection. Hence
\[
\operatorname{Det}(T)\cong\operatorname{Det}(T_{\mathcal Q}),
\]
so the entire RH-bearing phase lies in the invertible-complement determinant line.

## Crossing clutch

Suppose an analytic one-parameter family \(T(t)\) has a single contour crossing at \(t_0\). On the two sides of \(t_0\), spectral splittings differ by a finite generalized eigenspace \(E\). Their determinant factorizations are related by a clutching map transferring
\[
\det(E)
\]
between the defect and complement factors while preserving the ambient line.

Locally, if the reduced finite crossing operator has determinant
\[
d(t)=(t-t_0)^m u(t),\qquad u(t_0)\ne0,
\]
then \(m\) is the algebraic crossing multiplicity. Under the analytic Fredholm determinant identification, this equals the zero order of the ambient determinant section. For a regular self-adjoint crossing, the orientation is the sign of the crossing form
\[
\Gamma_{t_0}(v)=\langle v,\dot T(t_0)v\rangle,
\]
and its signed contribution is spectral flow. In the non-self-adjoint pencil, algebraic multiplicity remains defined, but orientation requires an additional real or reciprocal structure; it must not be fabricated from the scalar determinant alone.

This gives the local conservation law:
\[
\operatorname{ord}_{t_0}\det_{\mathrm{Fred}}T
=
\dim_{\mathrm{alg}}E,
\]
with signed refinement only when the orientation structure is supplied.

## Categorical crossing cell

A contour-crossing cell has four typed data:

1. the incoming spectral decomposition;
2. the outgoing spectral decomposition;
3. the finite crossing complex \(E\);
4. a determinant-functor clutching isomorphism preserving the ambient source line.

Forgetting \(E\) loses charge. Forgetting the clutching isomorphism loses phase. Forgetting orientation permits scalar determinant preservation while reversing the crossing class.

## Hostile checks

1. **Infinite determinant fallacy.** No ordinary determinant is taken on \(\mathcal Q\).
2. **Independent-connection fallacy.** The defect and complement connections must tensor to the ambient connection.
3. **Curvature mismatch.** \(F_{\mathcal D}+F_{\mathcal Q}\ne F_T\) falsifies the coupled constructor.
4. **Scalar-only crossing.** Equal scalar determinants do not preserve crossing orientation.
5. **Multiplicity loss.** Geometric rank alone can miss Jordan-chain algebraic multiplicity.
6. **Unoriented nonnormal crossing.** Spectral-flow language is unavailable without the required real/self-adjoint structure.
7. **Zero-sector phase leakage.** On \(\mathcal D=0\), no phase may be attributed to defect holonomy.

## Next constructor

Build the determinant-splitting clutching cube for cutoff, parameter, reciprocal, and contour-crossing directions. Its faces must express:

- Kato/Sz.-Nagy transport of the finite defect complex;
- relative determinant transport on the invertible complement;
- horizontality of the tensor decomposition;
- reciprocal compatibility of the crossing orientation.

The cube's residual is the first single obstruction that simultaneously detects defect-charge mismatch, determinant anomaly, and orientation reversal. Vanishing of this residual would bind the integer zero multiplicity to the completed analytic phase rather than merely placing them side by side.
