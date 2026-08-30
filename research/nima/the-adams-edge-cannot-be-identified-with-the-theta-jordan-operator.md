# The Adams edge cannot be identified with the theta Jordan operator

## Type separation

The universal matrix
\[
J_3=
\begin{pmatrix}
0&0&0\\
-6&6&0\\
4&-14&20
\end{pmatrix}
\]
is the three-grade quotient or front block of the theta completion polynomial.
It acts on analytic polynomial grade.

The primitive-to-square Adams datum has a different source type. The Gaussian
cell
\[
\alpha_{p,1}=W_{2\log p}-W_{\log p}
\]
is a comparison 2-cell between scale transport and valuation transport. It is
not an endomorphism of theta polynomial grade and not an object-level map
\(F_{p,1}\to F_{p,2}\).

Therefore the Adams edge cannot be declared equal to \(J_3\), nor to
\(\exp(J_3)\), merely because both appear in the same completed packet.

## Correct diagram

The source-authorized structure must have two directions:
\[
\begin{array}{ccc}
\text{primitive defect packet}
&\xrightarrow{\Gamma_{2;p,1}}&
\text{square defect packet}\\
\downarrow\mathcal J_{P,p}
&&
\downarrow\mathcal J_{Q,p}\\
\text{theta grade/history carrier}
&\xrightarrow{\mathcal C\ \text{or }J_\infty}&
\text{completed theta carrier}.
\end{array}
\]
Here:

- \(\Gamma_{2;p,1}\) is a closable boundary correspondence extracted from the
  mixed Green form;
- \(J_\infty\) is the full theta grade operator, with \(J_3\) only a qualified
  finite shadow;
- the bulk cell supplies a comparison between the two composite routes.

The desired theorem is a naturality or Beck–Chevalley comparison cell for this
square, not equality of its horizontal arrows.

## Consequence of the cyclic calculation

The exact odd cyclic column
\[
(-4,20,-8)^\mathsf T
\]
records how one connection vector enters the first three odd theta grades. It
can define one column of the vertical incidence map. It does not define the
horizontal primitive-to-square correspondence.

This resolves the question “\(J_3\), its exponential, or another Adams
matrix”: none is source-typed as the Adams edge. The Adams object is a mixed
boundary correspondence; \(J_3\) belongs to analytic completion.

## Earliest missing constructor

The first missing datum remains the mixed form
\[
b_{\alpha,p}(x,y)
\]
derived from the bulk cell after the moving-center and half-density transports.
It must satisfy:

\[
|b_{\alpha,p}(x,y)|
\le
\eta_p\,c_1[x]^{1/2}c_2[y]^{1/2},
\qquad \eta_p\le1,
\]
and annihilate both energy radicals. Only then does Riesz factorization produce
the defect-space contraction underlying \(\Gamma_{2;p,1}\).

After that, the theta cyclic columns must prove the naturality comparison with
the completed analytic branch.

## Hostile

Set \(\Gamma_{2;p,1}=J_3\). The formula may reproduce the scalar three-grade
theta polynomial, but its domain is analytic grade rather than the primitive
defect space, and it does not arise from the mixed bulk-cell polarization. It
is rejected as ill-typed before any norm estimate.

## Revised frontier

The next calculation is not another Jordan matrix. It is the polarized
bulk-cell form in the transported relative Green domain, followed by radical
descent and its normalized coupling norm.
