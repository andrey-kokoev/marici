# The Apparent Principal Mixed Curvature Is a Trivial-Source Artifact

## Question

Does the principal exceptional column require a new horizontal--vertical
homotopy in the relative logarithmic de Rham--Čech bicomplex?

## Typed calculation

Return to the complete weighted pullback of the reconstructed two-variable
connection on

\[
u=e,\qquad v=2-e+2e^2t,
\]

with shear weights \((0,0,4,2)\).  The committed reconstruction and shear use
the convention

\[
dF=A F,
\qquad
A^S=dS\,S^{-1}+SAS^{-1}.
\]

Let \(R_e(t)=\operatorname{res}_{e=0}A_e\) and
\(T(t)=A_t|_{e=0}\).  Exact rational reconstruction gives

\[
R_e=
\begin{pmatrix}
-\frac32&0&0&0\\
0&4&0&0\\
0&-\frac1{2(t^2-1)}&\frac72&0\\
0&\frac3{2(t^2-1)}&0&\frac52
\end{pmatrix},
\qquad
T=\operatorname{diag}\!\left(0,\frac{2t}{t^2-1},0,0\right).
\]

The exceptional coefficient of the full flatness equation vanishes:

\[
\boxed{\partial_tR_e+[R_e,T]=0.}
\]

Split the matrices into their upper and lower two-dimensional blocks.  The
principal map is the complete lower-left block

\[
C_E=
\begin{pmatrix}
0&-\frac1{2(t^2-1)}\\
0&\frac3{2(t^2-1)}
\end{pmatrix}.
\]

Its inherited source and target connections are

\[
A_P=\operatorname{diag}\!\left(0,\frac{2t}{t^2-1}\right),
\qquad A_E=0.
\]

Consequently

\[
\boxed{
\partial_tC_E-A_EC_E+C_EA_P=0.
}
\]

Thus the principal block is already a strict morphism of connections.  No
mixed homotopy \(H\) is required at this indicial grade.

## Source of the earlier defect

If the second principal-source direction is instead forced to carry the
trivial tangential connection, its flattened column produces

\[
-\frac{3t}{(t^2-1)^2}e_4\,dt.
\]

That is exactly the previously reported defect.  It is therefore not an
obstruction supplied by the geometry; it is the artifact of discarding the
source connection before forming the bicomplex.

## Consequence

The minimal relative logarithmic de Rham--Čech object must retain the full
two-dimensional principal source block and its induced connection.  The fixed
projective line remains nonhorizontal, but the source-derived principal map is
horizontal.  The next test is cohomological: totalize this strict block map and
ask whether its cone isolates a rank-one horizontal class after endpoint
Čech incidence and physical relative-cycle pairing.

## Verification and scope

The exact audit is implemented by
`research/nima/audit_weighted_exceptional_mixed_flatness.py` and recorded in
`research/nima/weighted-exceptional-mixed-flatness.json`.  It reproduces the
apparent defect under the forced-trivial-source assumption and verifies both
the full residue flatness equation and the strict block-morphism equation.

The calculation inherits Entry 793's bounded rational-reconstruction caveat:
it is exact over the reconstructed \(\mathbb Q\)-candidate and reduces to the
two reconstruction primes, but it is not an independent characteristic-zero
derivation from the original source integrals.

Allocator claim: `seqclaim-f2e0d5f1ce1d7c5ddfc407af`.
