# Clark Differentiation Turns the Affine Origin into the Prime Repair

## Exact transform split

Let

\[
F(z)=\int_0^\infty f(y)e^{izy}\,dy.
\]

Cutting at (L>0) gives

\[
F(z)=B_L(z)+e^{izL}F_L(z),
\]

where

\[
B_L(z)=\int_0^L f(y)e^{izy}\,dy,
\qquad
F_L(z)=\int_0^\infty f(r+L)e^{izr}\,dr.
\]

The finite seam transform (B_L) and translated tail (F_L) are both source-derived components of the exact cut.

## Clark cocycle

Apply the Clark operator

\[
C_a=1+ia\partial_z.
\]

Differentiating the transport phase gives

\[
C_aF
=
C_aB_L
+
e^{izL}\left(C_aF_L-aLF_L\right).
\]

The term (-aLF_L) is forced by the affine cut origin. On the source side this is simply

\[
\left(1-a(r+L)\right)f(r+L)
=
\left(1-ar\right)f(r+L)-aLf(r+L).
\]

For (L=\log p), this is the logarithmic prime repair found earlier in the recursive Clark identity. It is not an additional positive term chosen to repair a sign. It is the derivative cocycle of the prime transport phase.

Successive cuts add the cocycle because their origins add. The repair at (L+M) is the sum of the repairs at (L) and (M) after the appropriate tail transport.

## Mellin residues remain at the physical wall

The same affine-origin rule prevents false Mellin walls. Splitting a Mellin moment gives

\[
\int_0^\infty y^qf(y)\,dy
=
\int_0^L y^qf(y)\,dy
+
\int_0^\infty(r+L)^qf(r+L)\,dr.
\]

The translated tail must retain the global kernel ((r+L)^q). Because (r+L\ge L>0), this tail contribution has no endpoint pole generated at (r=0). All poles caused by the physical endpoint (y=0), including the Gamma-wall residue, remain in the finite seam term.

If one resets the tail kernel to (r^q), the internal cut (y=L) is falsely promoted to a new Mellin wall with residues determined by (f(L)). This is the meromorphic counterpart of the bulk Weyl defect (L T_Lf).

## What has closed

On the affine boundary-bearing cut:

- Fourier–Laplace transport splits exactly;
- Clark differentiation produces the forced logarithmic cocycle;
- Mellin pushforward keeps endpoint poles in the physical seam;
- prime compositions add coherently.

Thus no typed residual remains at finite cut in this three-operation subsystem. The first remaining obstruction is global: whether the primitive, square, and archimedean current families are continuous and compatible in the restricted-product completion of these seam intervals.

## Verification

The dependency-free exact-rational checker `research/grothendieck/checkers/clark_mellin_affine_cut_cocycle.py` verifies the affine Clark repair, global-kernel moment splitting through order six, and additive two-cut cocycle.
