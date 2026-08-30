# 2283 — The Gram-Wall Tensor Kernel Survives in the Direct Gaussian Score Port

## Supported tensor cone

Entry 2281 proves that the frozen spectral Gaussian tensor transfer loses rank
only on

\[
Z_{\rm Gram}=\{q\cdot(p_1\times p_2)=0\}.
\]

On this wall, the projections of the three hard momenta into the transverse
polarization plane are collinear.  The scalar-plus-two-tensor transfer has rank
two, so its supported observation cone carries one rank-one kernel class.

For the representative \(q\parallel p_1\), the transported scalar and
surviving tensor rows are

\[
(1,1,1),
\qquad
(0,1,1),
\]

and the supported kernel is

\[
K_{\rm Gram}=\mathbb Q\langle(0,1,-1)\rangle.
\]

The other two cyclic representatives are obtained by permuting occurrence
labels.

## Alternate admitted port

The direct Gaussian boundary-state score of Entries 2235–2236 is not obtained
by transporting the tensor polarization through \(q^\perp\).  Its fixed
scalar-plus-quadrupole matrix remains

\[
Q=
\begin{pmatrix}
1&2&0\\
1&-1&-1\\
1&-1&1
\end{pmatrix},
\qquad
\det Q=-6.
\]

At the representative wall, its cross score evaluates on the tensor kernel as

\[
(0,-1,1)(0,1,-1)^T=-2.
\]

Thus the direct score port is injective on the supported tensor kernel.  By
cyclic covariance, the same holds on the other labelled representatives; more
generally, invertibility of \(Q\) means it is injective on every possible
rank-one tensor kernel.

## Supported comparison cone

The tensor-only cone has rank-one supported cohomology on \(Z_{\rm Gram}\).
After adjoining the already admitted direct Gaussian score port,

\[
\boxed{
H^\bullet\operatorname{Cone}
(T_{\rm tensor}\oplus Q)|_{Z_{\rm Gram}}=0.
}
\]

Therefore the Gram-wall class is not lost from the complete admitted port
family.  Its classification is

\[
\boxed{
\text{existing Gram support}
+\text{tensor transport projection}
+\text{recovery in direct score readout}.
}
\]

This defeats the hard falsifier on the only finite-\(q\) rank-loss support of
the frozen spectral source.

## Qualification

The direct score remains a boundary-state susceptibility.  Entry 2283 proves
algebraic recovery in the admitted source port family, not experimental ease
of preparing or measuring that port.

## Verification

`research/benincasa/checkers/gram_wall_supported_detector_cone.rs` verifies the
representative supported kernel, direct-score rank, and recovery coefficient.
