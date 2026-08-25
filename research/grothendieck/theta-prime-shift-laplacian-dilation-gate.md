# Prime currents are shift-edge cross terms with a divergent degree budget

Author: marici.Grothendieck

## 1. Hardy shift representation

Work in the Euler half-plane and let

\[
 \mathcal H_+=L^2(\mathbb R_+,dt).
\]

For \(\operatorname{Re}z>0\), use the Cauchy/Laplace feature

\[
 k_z(t)=e^{-\bar zt}.
\]

Let \(R_L\) be the unilateral right shift by \(L>0\):

\[
 (R_Lf)(t)=
 \begin{cases}
 0,&t<L,\\
 f(t-L),&t\ge L.
 \end{cases}
\]

It is an isometry. Direct integration gives the two cross kernels

\[
 \frac{e^{-zL}}{z+\bar w},
 \qquad
 \frac{e^{-\bar wL}}{z+\bar w},
\]

as the two orientations of the pairing between \(k_z\) and its shifted
partner. Hence

\[
\boxed{
 K_L(z,w)
 =\frac{e^{-zL}+e^{-\bar wL}}{z+\bar w}}
\]

is the Hermitian cross kernel of \(R_L+R_L^*\).

For \(L=\log N\) and

\[
 a_N=\frac{\Lambda(N)}{\sqrt N},
\]

the connected prime contribution is

\[
 H_{\mathrm{prime}}(z,w)
 =-\sum_{N\ge2}a_NK_{\log N}(z,w).
\]

## 2. Positive edge dilation

Every shift edge has the positive Laplacian

\[
 \Delta_L=(I-R_L)^*(I-R_L)
 =2I-R_L-R_L^*\ge0.
\]

Therefore

\[
 -(R_L+R_L^*)=\Delta_L-2I.
\]

On quadratic forms, the negatively oriented prime cross term is exactly

\[
\boxed{
-2\operatorname{Re}\langle f,R_Lf\rangle
=\|f-R_Lf\|^2-2\|f\|^2.}
\]

Thus each prime current has a direct positive dilation as an edge energy, but
only after paying a diagonal vertex-degree cost.

## 3. Finite-cutoff degree budget

For a finite prime-power set \(\mathcal N\), put

\[
 A_{\mathcal N}=\sum_{N\in\mathcal N}a_N.
\]

Then

\[
\begin{aligned}
 -\sum_{N\in\mathcal N}a_N
  \langle(R_{\log N}+R_{\log N}^*)f,f\rangle
 ={}&
 \sum_{N\in\mathcal N}a_N
  \|(I-R_{\log N})f\|^2\\
 &-2A_{\mathcal N}\|f\|^2.
\end{aligned}
\]

The first line is manifestly nonnegative. All negativity has been compressed
to the scalar degree term

\[
 -2A_{\mathcal N}I.
\]

This is a real reduction: the many signed prime cross terms become positive
edge energies plus one shared diagonal budget.

## 4. The budget diverges globally

For the cutoff \(N\le Y\),

\[
 A_Y
 =\sum_{p^k\le Y}\frac{\log p}{p^{k/2}}
\]

diverges as \(Y\to\infty\). Therefore the unrenormalized infinite graph
Laplacian and its degree operator do not exist separately as bounded forms.

The explicit formula avoids this separation by pairing the prime
distribution with an admissible logarithmic test and combining it with gamma
and endpoint currents before removing the cutoff.

Consequently, a global positive dilation requires a source-derived identity
of the form

\[
 Q_{\Gamma+\mathrm{end}}^{(Y)}
 -2A_YI
 \longrightarrow Q_{\mathrm{ren}}\ge0
\]

on a common form domain. Neither convergence nor positivity follows from the
edge factorization.

## 5. Relation to local Weil positivity

For logarithmic tests with sufficiently short support, only controlled edge
separations are visible and the archimedean form dominates. The first contact
at \(\log2\) is exactly where the shared degree budget begins to be spent.

This recovers the earlier contraction hierarchy:

- one edge asks for a two-cell contraction;
- two consecutive edges ask for the prime-power triangle defect;
- distinct prime edges ask for the mixed rectangle parity conditions; and
- all visible edges share one archimedean degree budget.

Pairwise shift dilations do not automatically glue because their diagonal
costs add.

## 6. Fill-in obstruction

Eliminating positive internal edge vertices by Schur complement generally
creates effective correlations along paths. For distinct primes \(p,q\), this
can create a direct \(\log(pq)\) channel even though

\[
 \Lambda(pq)=0.
\]

Therefore an admissible dilation must distinguish:

1. internal path propagation through \(p\) and \(q\); and
2. a literal connected boundary atom at \(pq\), which must remain absent.

A scalar Schur complement that identifies these two changes the explicit
formula. The full labelled graph or a typed path groupoid must be retained
until the final readout.

## 7. Explanatory status

The shift-edge factorization explains how a negative prime current can arise
from positive local degrees of freedom. It does not prove the completed form
positive, because the required vertex counterterm is divergent and shared
across all edges.

The surviving theorem is now:

\[
\boxed{
\text{gamma plus endpoint completion is the renormalized vertex degree
of the prime-shift graph, with nonnegative residual energy}.}
\]

If this identity can be derived independently from Poisson/adelic sewing, it
would be a genuine positive dilation. If its residual positivity is exactly
the Weil criterion, the graph construction is only a decomposition.

## 8. Sharp falsifiers

The proposed graph explanation fails if:

1. the completed archimedean current does not match the common-cutoff degree
   subtraction;
2. the residual form has a negative compactly supported test;
3. Schur elimination creates forbidden squarefree von Mangoldt atoms;
4. cutoff changes alter the boundary relation by more than a source unit; or
5. positivity of the large graph form is equivalent to positivity of its
   Weil Schur complement with no independently positive bulk.

## 9. Next attack

Use endpoint-centered gamma defect vectors

\[
 v_N(u)=1-N^{-u}
\]

as candidate renormalized vertex features. Compare their exact positive Gram
form with the degree-subtracted prime-shift energy on the same finite
prime-power label set. The first decisive cases are the \(2,4\) triangle and
the \(2,3,6\) rectangle, because they distinguish Adams path propagation from
forbidden squarefree fill-in.

## 10. Scope

The Hardy-shift kernel, positive edge-Laplacian factorization, finite-cutoff
degree reduction, divergent global budget, and fill-in warning are exact. No
gamma-degree identity, positive global residual, cutoff-independent
self-adjoint dilation, determinant formula, or RH proof is claimed.
