# The ordered linking port is continuous on the centered Evans rigging but its shell value remains open

## Question

Does the ordered Stokes/Wronskian linking port create a new rigging obstruction
for the exact Evans residual?

## Claim boundary

No, provided the G4 port uses the already source-declared wall trace, incidence
coordinate, and uniformly bounded arithmetic loading. Its linking functional is
continuous on the retained wall graph, and the centered prime weights place its
adjoint sequence in \(U_{\rm ar}\). This proves existence, not the shell value,
normalization comparison, or cancellation.

## Existing labelled bound

On the resolved-plus-wall graph, retain

\[
 \gamma_0f=f(0)
\]

and the incidence coordinate \(\eta(f)\). Both are components of the graph
norm. For a source loading \(c_p\), the ordered linking polarization is

\[
 \mathfrak L_{c_p}(f,g)
 =ic_p\left(
 \overline{\gamma_0f}\,\eta(g)
 -\overline{\eta(f)}\,\gamma_0g
 \right).
\]

Therefore

\[
 |\mathfrak L_{c_p}(f,g)|
 \le 2|c_p|\|f\|_{G,\rm wall}\|g\|_{G,\rm wall}.
\]

The retained primitive/square source loadings satisfy

\[
 \sup_p|c_p|<\infty.
\]

Thus the labelled direct sum of linking forms is bounded before any
codiagonalization.

## Application to the Evans history

At every Xi zero, the exact Evans history belongs to the whole-line
\(H^1\) graph. Its seam value is continuous by the one-dimensional trace
theorem, and its incidence coordinate is already part of the declared joint
graph. Consequently

\[
 \sup_p
 |\mathfrak L_{c_p}(c_{\log p},u_z)|
 \le C_L\|u_z\|_{G,\rm wall}
\]

for a constant independent of \(p\). On compact parameter subsets of the Xi
divisor, the right side is uniformly bounded.

## Centered arithmetic adjoint

The centered G4 incidence contributes the arithmetic half-density
\(p^{-1/2}\), while the source adjoint contributes \((\log p)^{-1}\). Hence
the linking coordinate of the arithmetic residual obeys

\[
 |r_p^{({\rm link})}(z)|
 \le
 \frac{C_L\|u_z\|_{G,\rm wall}}{p^{1/2}\log p}.
\]

With

\[
 \|r\|_U^2=\sum_p(\log p)|r_p|^2,
\]

we obtain

\[
 \|r^{({\rm link})}(z)\|_U^2
 \le C_L^2\|u_z\|_{G,\rm wall}^2
 \sum_p\frac1{p\log p}<\infty.
\]

Thus the ordered linking port is a continuous \(U\)-valued component of the
Evans adjoint residual.

## Parameter-root vectors

For a zero of multiplicity \(m\), every
\(\partial_z^ju(\cdot;z_0)\), \(0\le j<m\), lies in the same graph domain.
The identical estimate proves

\[
 r^{({\rm link})}_{U,j}(z_0)\in U.
\]

Therefore the linking contribution introduces no separate distributional
failure in the multiplicity chain.

## What remains source-sensitive

Continuity does not identify the local Stokes scalar with the final
half-density Wronskian scalar. That comparison must retain:

- the ordered source slots;
- reciprocal sign;
- wall and incidence normalization;
- the prime and grade labels;
- the frozen G4 coefficient rather than a coefficient copied from a different
  quadratic block.

If the final G4 construction changes \(c_p\) or removes either retained
coordinate, the bound must be rechecked. No coefficient may be fitted after
examining Xi zeros.

## Shell consequence

Every port in the proposed prime-shell residual is now a legitimate bounded
pairing on the centered Evans rigging, assuming its declared source comparison.
The remaining finite falsifier is numerical or exact evaluation of

\[
 I_n^{(0)}+I_n^{(1)}+I_n^{({\rm wall})}
 +I_n^{({\rm recip})}+I_n^{({\rm link})}.
\]

The ordinary term is eventually sign-definite. Continuity of the other four
terms does not force their sum to cancel it.

## Disposition

The ordered linking port does not block domain construction or arithmetic
summability. The unresolved gate is its source-normalized shell value and the
full cancellation identity. No RH conclusion is authorized.
