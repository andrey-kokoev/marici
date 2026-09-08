# Generic orientation-valued polygon residue factorization

## Question

How do generic Laurent coefficient factorization and normal-orientation transport compose into one typed residue statement?

## Claim boundary

The construction is generic for finite polygon dissections. Executable evidence is exhaustive only for polygon sizes three through seven. The result is not an analytic residue theorem until local coordinates and a meromorphic differential normalization are supplied.

Let `m_n` be the planar triangulation weighted sum and `D` a dissection. Coefficient extraction along every channel in `D` gives

\[
\operatorname{Coeff}_D(m_n)=\prod_{R\in\pi_0(P_n\setminus D)}m_R.
\]

The generic face-product bijection identifies triangulations containing `D` with independent triangulations of its regions, proving the scalar identity. Attach the orientation line

\[
\operatorname{or}(D)=\det(\mathbb Z^D).
\]

For an ordering `sigma` of `D`, the ordered differential residue and `[sigma]` transform by the same permutation sign. Their tensor is therefore independent of `sigma`. For nested disjoint cuts, wedge transport of orientation lines is associative and carries the Koszul interchange sign. Hence direct residue along `D`, every iterated residue order, and the regional product agree in the orientation-valued target.

The checker enumerates all dissections, all retained residual monomials, and every cut ordering for `n=3..7`. It compares direct coefficient extraction, sequential extraction, regional multiplication, and determinant-line sign transport.

## Disposition

Generic coefficient factorization and generic orientation transport compose without an additional sign choice. The remaining analytic promotion requires a local normal coordinate, meromorphic form normalization, and contour or boundary-value prescription.
