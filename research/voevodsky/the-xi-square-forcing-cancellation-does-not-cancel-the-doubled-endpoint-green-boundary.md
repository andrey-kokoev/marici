# Xi-square forcing cancellation does not cancel the doubled endpoint Green boundary

## Audit target

After rejection of the unchanged Evans state, the surviving source-forward candidate is the full tail-state modification. This note tests whether the existing reciprocal Wiener--Hopf identity already closes its Green balance.

## One-sided identity

For each stable tail,

\[
(z+\bar w)\langle G_w,G_z\rangle
=\overline{G_w(0)}G_z(0)-\mathcal F(w,z),
\]

where

\[
\mathcal F(w,z)=\langle f_w,G_z\rangle+\langle G_w,f_z\rangle.
\]

The source-fixed sum/difference rotation factors this exactly as

\[
\mathcal F(w,z)=\langle I_w,I_z\rangle-\langle O_w,O_z\rangle,
\qquad
I_z=(f_z+G_z)/\sqrt2,
\quad O_z=(f_z-G_z)/\sqrt2.
\]

Thus the full outgoing feature is \(Y_z=(G_z(0),O_z)\), not merely \(O_z\).

## Reciprocal scalar cancellation

The established Wiener--Hopf relation

\[
R(z)+R(-z)=\Xi(z)^2
\]

gives, in the Hermitian lane,

\[
\mathcal F_{\rm dbl}(w,z)
=-\Xi(z)^2-\overline{\Xi(w)^2}.
\]

Consequently \(\mathcal F_{\rm dbl}(w,z)=0\) when both parameters are Xi zeros.

## Residual that remains

Summing the two one-sided identities still gives

\[
(z+\bar w)K_{\rm dbl}(w,z)
=E_{\rm dbl}(w,z)-\mathcal F_{\rm dbl}(w,z),
\]

with

\[
E_{\rm dbl}(w,z)=
\overline{G_w^+(0)}G_z^+(0)+
\overline{G_w^-(0)}G_z^-(0).
\]

At Xi zeros this specializes only to

\[
(z+\bar w)K_{\rm dbl}(w,z)=E_{\rm dbl}(w,z),
\]

not to zero. On the diagonal,

\[
2\operatorname{Re}z\,K_{\rm dbl}(z,z)
=|G_z^+(0)|^2+|G_z^-(0)|^2.
\]

The right side is nonnegative and is generally not zero. Therefore scalar Xi-square forcing cancellation alone cannot prove seam confinement. Declaring the endpoint sum zero would be an additional theorem and, on nonzero Xi histories, would already carry the confinement step.

## Exact remaining gate

One must exhibit a source-derived typed reciprocal sewing map whose boundary relation accounts for the two endpoint coordinates together with every difference port. Equivalently, one must verify the augmented two-height identity

\[
I-\Theta(w)^*\Theta(z)
=(1-\overline{\lambda(w)}\lambda(z))F(w)^*F(z)
\]

for the same state and all declared primitive, square, seam, archimedean, reciprocal, and linking labels. Abstract Fourier unitarity and the scalar identity \(R(z)+R(-z)=\Xi(z)^2\) do not identify this typed map.

The first admissible falsifier remains one nonzero labelled entry of

\[
\mathcal R_X(w,z)=I-\Theta_X(w)^*\Theta_X(z)
-(1-\overline{\lambda(w)}\lambda(z))F_X(w)^*F_X(z).
\]

No such finite residual is evaluable until an authoritative typed `U_G4`/`Theta_X` packet is exposed.

## Disposition

The full tail-state modification survives the unchanged-Evans numerical falsifier, but its closure is authority-blocked at typed endpoint sewing. The scalar Xi-square relation must not be promoted to complete-port conservation.
