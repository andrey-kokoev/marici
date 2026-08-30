# Exterior-observer extensions form a torsor over the boundary-defect dual

## Correction of the frontier

The source already proves finite vacuum transversality: the Mellin observer sends the multiplicative vacuum to \(1\). The positive interval tower also controls the interior arithmetic state. Neither result determines the exterior Riemann observer.

The remaining ambiguity has an exact functional-analytic location.

## Boundary defect quotient

Let \(E_{\mathrm{int}}\) be the admitted interior source space and let \(E_{\partial}\) be the completed space after adjoining the five-wall boundary carrier. Write

\[
j:E_{\mathrm{int}}\longrightarrow E_{\partial}
\]

for the interior inclusion and define the boundary-defect quotient

\[
Q_{\partial}
=
E_{\partial}/\overline{j(E_{\mathrm{int}})}.
\]

Suppose \(\ell_{\mathrm{int}}\in E_{\mathrm{int}}'\) is the ordinary aggregation observer in the convergence chamber. If \(\widetilde\ell_0\) and \(\widetilde\ell_1\) are two continuous extensions to \(E_{\partial}\), then

\[
(\widetilde\ell_1-\widetilde\ell_0)\circ j=0.
\]

Therefore their difference factors uniquely through \(Q_{\partial}\):

\[
\widetilde\ell_1-\widetilde\ell_0
=
q^{*}\varphi,
\qquad
\varphi\in Q_{\partial}'.
\]

Consequently, whenever one extension exists, the set of all continuous extensions is an affine torsor over \(Q_{\partial}'\).

This is the exact form of the boundary-extension defect. Interior positivity, analytic continuation of the scalar shadow, and vacuum transversality cannot remove it.

## Why density is not the desired repair

One could force uniqueness by choosing a topology in which \(j(E_{\mathrm{int}})\) is dense, so \(Q_{\partial}=0\). But the programme explicitly retains constant, delta, primitive, square, and archimedean wall coordinates. Making all of them interior limits without proving their source trace laws would collapse the typed boundary rather than construct the observer.

The correct repair is therefore not to declare the defect quotient zero. It is to supply a source section on its authorized coordinates.

## Comparison-cell formulation

Let \(a\) range over source-authorized approaches to the exterior observer, and let

\[
\widetilde\ell_a:E_{\partial}\to\mathbb C
\]

be the resulting boundary functional. A comparison cell between approaches \(a\) and \(b\) must prove both

\[
\widetilde\ell_a-\widetilde\ell_b=0
\]

and equality of their polarized Green currents on the full boundary carrier.

Equivalently, the induced defect character

\[
\varphi_{a,b}\in Q_{\partial}'
\]

must vanish. Scalar agreement on \(E_{\mathrm{int}}\) says only that \(\varphi_{a,b}\) exists; it does not say that it is zero.

## Finite reduction

If the retained boundary quotient is the frozen five-wall cell, then the ambiguity is finite-dimensional before completion. Choose the typed basis

\[
(\mathbf 1,\delta,P,Q,\infty).
\]

Each approach produces a row of five boundary values and a corresponding polarized-current row. Path independence reduces first to equality of these finite rows, with reciprocal sewing and wall characters preserved.

This gives an executable audit:

1. construct every authorized approach on one common core;
2. compute its five boundary coordinates before scalar aggregation;
3. compare the associated Green-current coordinates;
4. verify reciprocal Fourier–Tate covariance;
5. prove the finite comparison survives completion in the declared dual topology.

## Hostiles

The smallest hostile has two extensions agreeing on every interior state but differing on one archimedean wall coordinate.

A stronger hostile has identical five scalar boundary values but different mixed Green-current rows. It passes scalar extension uniqueness while failing constructor coherence.

The completion hostile has finite defect characters \(\varphi_X\to0\) pointwise on each fixed wall vector, but no bounded-set convergence in \(Q_{\partial}'\). Every finite cutoff appears path-independent while the completed observer remains approach-dependent.

## Consequence

The RH-bearing frontier is now a relative extension theorem:

> Construct one source-authorized exterior observer and prove that every authorized approach has zero defect character in the dual of the typed boundary quotient, including its polarized Green current.

Only after this theorem may the scalar zero be identified with a mixed boundary condition. The observer cannot be reconstructed backward from the scalar continuation.
