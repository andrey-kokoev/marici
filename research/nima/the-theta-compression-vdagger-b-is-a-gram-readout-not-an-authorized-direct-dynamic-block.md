# The theta compression V-dagger B is a Gram readout, not an authorized direct dynamic block

## Correction

The bounded map

\[
V^\dagger B:U_{\rm ar}\to\mathbb C_\theta
\]

exists on the retained metric carrier. Existence of this composite does not
authorize placing it as an independent off-diagonal block in the source
pencil.

## Two categorical roles

The map \(V^\dagger B\) is obtained by:

1. sending the arithmetic state into the history target through \(B\);
2. applying the theta covector \(V^\dagger\).

It is therefore a downstream compression or mixed Gram readout.

A direct dynamic block

\[
R:U_{\rm ar}\to\mathbb C_\theta
\]

would be an additional primitive arrow in the source differential. The fact
that a composite with the same endpoints exists does not make it such an
arrow.

## Resolved saturated ordering

The source-authorized joint graph retains typed outputs in direct sum and has
zero cross block before downstream codiagonalization. Its Gram is

\[
G_{\rm joint,res}
=(1+M_\Phi^2)I+B^*B.
\]

This ordering explicitly rejects inserting a wall--tail mixed term merely
because the scalar compression can be formed.

By the same rule, the minimal three-port source pencil must use

\[
R=0
\]

unless a separate source constructor supplies a direct arithmetic--theta
arrow.

## Propagated cross term

When theta and arithmetic ports both couple to a common history block,
eliminating that block may produce the Schur cross return

\[
V^\dagger(A-z)^{-1}B.
\]

This term is authorized by the declared two-step path through history. It is
not the instantaneous compression \(V^\dagger B\).

The two expressions coincide only under an additional resolvent identity that
is absent here.

## Effect on the source Schur matrix

With \(D_\theta=0\) and no independently authorized direct cross block, the
history-eliminated characteristic is

\[
M_{\theta U}(z)
=
\begin{pmatrix}
V^\dagger R_HV & V^\dagger R_HB\\
B^\dagger R_HV & D_U+B^\dagger R_HB
\end{pmatrix},
\qquad
R_H=(A-z)^{-1},
\]

up to the frozen adjoint signs.

This is the minimal source Schur matrix. Adding \(V^\dagger B\) would count a
second path not present in the retained differential.

## Status of the compression coefficients

The coefficients

\[
\langle\Phi,b_{p,k}\rangle
\]

remain valid and useful as:

- arithmetic-to-theta observations;
- G1 incidence compressions;
- mixed Gram entries;
- finite residual diagnostics.

They are not bulk coupling coefficients without a promotion theorem.

## Disposition

The earlier claim that \(R=V^\dagger B\) closes the direct cross-reservoir
constructor is withdrawn. The bounded compression exists, but source ordering
sets the primitive direct block to zero. G4 must use the propagated history
cross return or construct a genuinely new direct arrow with independent
authority. No RH conclusion is authorized.
