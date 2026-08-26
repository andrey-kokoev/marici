# Bilateral valuation shift lifts the odd Euler current before scalarization

## Question

The primitive and square currents cannot be continued separately as scalar
functions without importing the zeta divisor.  Can their reciprocal odd
channel instead be retained as a source operator on a common direct--dual
state space?

## Doubled valuation chain

For each prime \(p\), glue the direct and reciprocal valuation cones along
their common primitive boundary.  The resulting algebraic chain has basis

\[
\{e_j:j\in\mathbb Z\}.
\]

Its Hilbert completion is

\[
\mathcal H_p=\ell^2(\mathbb Z).
\]

Define the bilateral shift and reciprocal reflection by

\[
U_pe_j=e_{j+1},
\qquad
R_pe_j=e_{-j}.
\]

Then

\[
U_p^*=U_p^{-1},
\qquad
R_pU_pR_p=U_p^{-1}.
\]

Unlike the one-sided valuation shift, \(U_p\) is unitary.  The doubled source
therefore supplies a native common metric and adjoint transport.

## Operator-valued odd cumulants

Let \(L_p=\log p\).  For \(k\ge1\), define

\[
\mathcal J_{p,k}(z)
=
\frac{p^{-k/2}}{k}
\left(
e^{kzL_p}U_p^k
-e^{-kzL_p}U_p^{-k}
\right).
\]

Reciprocal reflection gives

\[
R_p\mathcal J_{p,k}(z)R_p
=
-\mathcal J_{p,k}(-z).
\]

On the critical seam \(z=it\),

\[
\mathcal J_{p,k}(it)^*
=
-\mathcal J_{p,k}(it).
\]

Thus \(i\mathcal J_{p,k}(it)\) is self-adjoint.  Seam unitarity and odd
boundary polarization are now operator identities before any scalar prime
sum is formed.

## Boundary readout recovers the scalar sinh tower

Let \(e_0\) be the primitive vacuum and let \(\ell_p\) be the algebraic
augmentation distribution

\[
\ell_p(e_j)=1.
\]

Then

\[
\ell_pU_p^{\pm k}e_0=1,
\]

so

\[
\ell_p\mathcal J_{p,k}(z)e_0
=
2\frac{p^{-k/2}}{k}
\sinh(kz\log p).
\]

Summing these boundary matrix coefficients reproduces
\(\log\gamma_p(z)\).  The scalar odd Euler channel is therefore the
augmentation readout of a prior bilateral operator current.

## Global assembly is not yet an operator sum

There are two inequivalent ways to place the local operators over all primes.
The block-diagonal direct sum

\[
\bigoplus_p\mathcal J_{p,k}(z)
\]

is controlled by a supremum, not a prime sum, and is bounded wherever the
local norms are uniformly bounded.  By contrast, an additive generator on a
restricted tensor product, or its action on a reference vacuum, is controlled
by summability across primes.  The source has not yet supplied the global
assembly functor, so these constructions must not be identified.

For the additive restricted-product interpretation, the connected formal tail
is

\[
\mathcal J_{\ge3}(z)
=
\sum_p\sum_{k\ge3}\mathcal J_{p,k}(z).
\]

If it is realized as a sum of operators acting on distinct tensor factors,
absolute operator-norm summability follows from the scalar majorant for

\[
|\Re z|<\frac16.
\]

This is a sufficient realization-dependent statement, not a property of the
block direct sum.  The canonical pre-scalar regularity test is instead the
vacuum cocycle; it is derived separately in the next packet.

## Relation to reciprocal graph coercivity

On each local doubled chain, the transport is normal because \(U_p\) is
unitary.  Hence the metric self-commutator vanishes in the bulk.  Any failure
of a future global comparison \(T_z\) to satisfy

\[
\|T_z^*T_z-T_zT_z^*\|<c
\]

must arise from the primitive/square boundary domains, archimedean incidence,
or restricted-product completion.

Kitaev's criterion then has a correctly typed possible use: if a completed
source comparison on the common doubled Hilbert space satisfies

\[
T_z^*T_z+T_zT_z^*\ge cI
\]

and its self-commutator norm is strictly below \(c\), then both \(T_z\) and
\(T_z^*\) are bounded below.  None of those inequalities is asserted yet.

## What this construction achieves

It provides:

- a source-native common metric for the reciprocal sectors;
- an operator lift of every odd determinant cumulant;
- exact seam skew-adjointness;
- the local input from which the primitive and square boundary currents can be
  typed by their global vacuum cocycle;
- an absolutely summable connected tail in the additive restricted-product
  realization around the seam.

It avoids prime-zeta continuation entirely.

## Remaining obstruction

The augmentation \(\ell_p\) is not a Hilbert vector.  Across all primes, the
primitive and square currents require a common rigged domain on which:

- the reflected operators are adjoints;
- the augmentation boundary forms are continuous;
- cutoff inclusions are equicontinuous;
- the archimedean boundary packet couples without scalarizing either current.

The even hostile multiplier remains invisible to the transition current.  It
will be rejected only if it cannot be realized by a source-authorized change
of the full bordered operator and its determinant section.

## Next exact target

Construct the finite-prime direct sum

\[
\mathcal J_X(z)
=
\mathcal J_{1,X}(z)
+\mathcal J_{2,X}(z)
+\mathcal J_{\ge3,X}(z)
\]

on the doubled valuation module, then add the two archimedean boundary
components \((1/2,z)\).  The first required identity is a source-derived
boundary form pairing \(z\) with the odd arithmetic current before the
augmentation readout.

The falsifier is a domain mismatch: if the primitive/square form domains on
the two reciprocal cones cannot be identified by \(R_p\), the common-adjoint
graph construction fails.

## Result

The odd Euler sinh tower has a canonical pre-scalar operator lift on the
bilateral valuation chain.  The doubled prime shift supplies the common metric
and reciprocal adjoint; only the boundary currents and global completion can
create nonnormality or loss of observability.
