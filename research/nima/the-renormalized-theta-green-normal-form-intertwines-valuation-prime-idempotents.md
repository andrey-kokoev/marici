# The renormalized theta--Green normal form intertwines the valuation prime idempotents exactly

## Labelled carrier

Let

\[
\mathcal L
=
\ell^2\{(p,k)\}
\]

be the source valuation-label carrier, and let \(\mathcal H_{\mathrm{an}}\) be
the analytic theta--Green fiber. The represented source is

\[
\mathcal K
=
\mathcal L\widehat\otimes\mathcal H_{\mathrm{an}}.
\]

For each prime and grade,

\[
P_{p,k}
=
|e_{p,k}\rangle\langle e_{p,k}|
\otimes I.
\]

These are the source prime idempotents.

## Fiberwise normal form

For fixed \(p\), the newly constructed analytic chain consists of:

1. the finite four- or five-grade Gaussian packet;
2. theta-label cutoff in the internal label \(n\);
3. continuum-label wall integral;
4. endpoint half-cell;
5. quarter-gap operator
   \[
   \mathcal C=D_u^2-\frac14;
   \]
6. Green resolvent \(\mathcal C^{-1}\);
7. reciprocal two-ray sewing;
8. ordered Volterra port.

Every operation acts in the analytic factor. Prime dependence enters only
through the scalar parameter

\[
L=\log p
\]

and the diagonal Euler weight.

Therefore the complete finite-cutoff operator has the form

\[
\mathbf G_{N}
=
\bigoplus_{p,k}
P_{p,k}
\left(
I_{\mathcal L}\otimes G_{p,k,N}
\right)
P_{p,k}.
\]

## Exact intertwining

For distinct labels,

\[
P_{q,\ell}\mathbf G_NP_{p,k}=0
\qquad
((q,\ell)\ne(p,k)).
\]

At every finite cutoff,

\[
[\mathbf G_N,P_{p,k}]=0.
\]

The Euler--Maclaurin wall terms preserve this identity because their continuum
integrals and endpoint half-cells are formed inside the same \(p\)-fiber.
They do not average over primes.

Graph convergence preserves commutation with a bounded projection. Hence the
completed normal form satisfies

\[
[\mathbf G,P_{p,k}]=0.
\]

## Adams grade covariance

The Adams edge changes grade but not prime:

\[
A_2P_{p,k}
=
P_{p,2k}A_2.
\]

Consequently, the primitive--square block obeys

\[
P_{q,2k}A_2\mathbf GP_{p,k}
=
0
\qquad
(q\ne p).
\]

Thus the renormalized theta synthesis, Green propagation, and moving-wall
completion do not manufacture cross-prime incidence.

## Cutoff naturality

Let

\[
P_{\le X}
=
\sum_{p\le X,k}P_{p,k}.
\]

Then

\[
P_{\le X}\mathbf G
=
\mathbf GP_{\le X}.
\]

The prime cutoff and theta-label completion limits therefore form a commuting
square on the direct-sum carrier. Combined with the absolute Euler-weighted
bound, this gives cutoff naturality at completion.

## Scalar pushforward

The scalar Euler observer is an augmentation on \(\mathcal L\). It is the
first map in this chain that intentionally forgets prime labels.

Therefore it must be applied only after:

- the wall packet is routed;
- the Green resolvent is formed;
- reciprocal even and odd ports are retained;
- the complete typed block is assembled.

Prime diagonality is now source-authorized by the already admitted valuation
carrier, not inferred from Fourier--Bohr scalar orthogonality.

## Remaining gate

The local and completed Adams normal form now preserves prime labels exactly.
The next unresolved interface is faithfulness of scalar prime pushforward on
the reciprocal two-port system.

The pushforward must retain both:

\[
\text{constant-wall coordinate},
\qquad
\text{ordered-jump coordinate}.
\]

A scalar Euler value alone cannot certify this two-dimensional faithfulness.

## Hostile

Erase \(\mathcal L\) before the Euler--Maclaurin wall is formed. The scalar
theta sum can remain convergent, but the moving wall and reciprocal odd
current can cancel across primes. Reconstructing prime labels afterward does
not restore the lost typed block.
