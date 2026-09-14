# The conductor intertwiner realizes the shared boundary vector

## Question

Does an existing source-derived comparison object realize the degree-zero boundary generator required by the minimal two-leg source complex?

## Claim boundary

This identifies the shared boundary vector inside the audited orientation-twisted conductor lattice. It does not construct the two degree-one chains, the relative pair, or the Leray-tube integration pairing.

## Required boundary

The minimal source complex requires one degree-zero generator \(r\) with target image

\[
F_0(r)=
\begin{pmatrix}1\\-1\\1\end{pmatrix}.
\]

## Existing intertwiner

The audited conductor basis is

\[
(g_{101},g_{110},\widetilde g_{111}),
\]

and its integral intertwiner is

\[
J=
\begin{pmatrix}
2&0&1\\
0&2&1\\
0&0&1
\end{pmatrix}.
\]

Its image consists exactly of vectors \((u,v,w)\) whose coordinates have equal parity. The required boundary vector has three odd coordinates and therefore lies in \(\operatorname{im}J\).

Using the audited integral inverse,

\[
a=\frac{u-w}{2},
\qquad
b=\frac{v-w}{2},
\qquad
c=w,
\]

we obtain

\[
J
\begin{pmatrix}0\\-1\\1\end{pmatrix}
=
\begin{pmatrix}1\\-1\\1\end{pmatrix}.
\]

Thus the shared boundary generator has the unique conductor preimage

\[
r_{\rm cond}=-g_{110}+\widetilde g_{111}.
\]

## Consequence

Object assignment is no longer empty in degree zero. The minimal source boundary is represented in the orientation-twisted conductor frame with an exact integral comparison. The remaining missing objects are two labelled degree-one chains whose boundaries are \(r_{\rm cond}\) and \(-r_{\rm cond}\), plus the residue-compatible cycle-form pairing sending them to the logarithmic and face legs.

## Strongest falsification attempt

Read the existing intertwiner and inverse formulas from the Benincasa result. Verify the image parity condition, solve for the required preimage integrally, require uniqueness from \(\det J=4\), and replay the matrix product. Retain the source audit's statement that the bulk relative Stokes scalar and support-sensitive extension remain missing.

## Computed result

The audited matrix has determinant 4 and the required target vector satisfies its equal-parity image condition. Its unique rational preimage is the integral vector \((0,-1,1)^T\), and direct multiplication recovers \((1,-1,1)^T\). The stored inverse formula and source-orientation-twist classification agree.

## Disposition

The degree-zero source object is realized in the audited orientation-twisted conductor lattice as \(-g_{110}+\widetilde g_{111}\). No degree-one source chain has materialized. The remaining gate is now two labelled chains with boundaries \(r_{\rm cond}\) and \(-r_{\rm cond}\), together with the residue-compatible relative Stokes pairing. The audited source still marks the bulk scalar and support-sensitive extension as missing.
