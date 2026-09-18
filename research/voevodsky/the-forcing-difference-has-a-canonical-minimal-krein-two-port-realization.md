# The forcing difference has a canonical minimal Krein two-port realization

## Residual kernel

The stable-history sign ledger isolates

\[
D(w,z)=A(z)+\overline{A(w)},
\qquad
A(z)=R(z)-R(-z).
\]

This is the forcing-difference kernel required by the positive doubled bulk identity.

## Canonical realization

Define the two-coordinate feature

\[
v_z=\binom{1}{A(z)}
\]

and the exchange metric

\[
J_{\rm mix}=
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Then, exactly,

\[
v_w^*J_{\rm mix}v_z
=A(z)+\overline{A(w)}
=D(w,z).
\]

Thus the forcing difference already has a canonical source-derived mixed-block realization. Its two coordinates are the retained constant forcing amplitude and the causal-odd response amplitude. No square root, sampled Gram diagonalization, or fitted positive feature is used.

In the analytic-transpose lane the same formula is

\[
v_w^\top J_{\rm mix}v_z=A(z)+A(w).
\]

## Signature and minimality

The eigenvalues of \(J_{\rm mix}\) are \(+1\) and \(-1\). Equivalently, under

\[
P=\frac1{\sqrt2}
\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
P^*J_{\rm mix}P=\operatorname{diag}(1,-1).
\]

Hence this is a Krein supply port, not a positive energy port.

A one-dimensional positive realization would have the form

\[
D(w,z)=\overline{h(w)}h(z),
\]

forcing \(D(z,z)=|h(z)|^2\ge0\). But

\[
D(z,z)=2\operatorname{Re}A(z)
\]

is the sign-indefinite oscillatory separation current off the seam. Therefore no positive rank-one realization can represent the full kernel. The two-port mixed realization is minimal whenever \(A\) is nonconstant: the kernel matrix on a packet has rank at most two and has rank two for any two points with distinct real affine data not lying in one degenerate proportional feature line.

## Green-cycle insertion

The exact positive-bulk identity is

\[
(z+\bar w)(K_-+K_+)
=E_--E_++D(w,z).
\]

Consequently the boundary supply can be written

\[
E_--E_++v_w^*J_{\rm mix}v_z.
\]

At Xi zeros, seam matching cancels \(E_--E_+\), but the mixed port remains. Closing the Green cycle requires an arithmetic/linking boundary map whose pulled-back Krein form is \(-J_{\rm mix}\) on the feature span. It does not require, and cannot use, a positive rank-one shadow.

## Refined lattice coordinate

Separate existence of the supply shape from arithmetic identification:

- \(m=1\): the minimal mixed forcing-difference two-port is analytically formed;
- \(a_{\rm mix}=0\): no source-derived arithmetic/linking map has yet been proved to pull its boundary form back to \(-J_{\rm mix}\).

Thus the local frontier is

\[
(g_{\rm oriented},m,a_{\rm mix})=(0,1,0).
\]

The positive Green cycle remains open, but its missing object is now a comparison of two explicit indefinite forms rather than construction of an unknown positive feature.

## Claim boundary

This realizes the forcing-difference kernel and fixes its signature. It does not prove the arithmetic mixed-block identity, global cutoff summability, unchanged-Evans membership, or RH.
