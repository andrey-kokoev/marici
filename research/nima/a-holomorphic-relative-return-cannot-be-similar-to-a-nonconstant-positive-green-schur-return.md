# A holomorphic relative return cannot be similar to a nonconstant positive Green Schur return

## Proposed comparison

The preceding reduction isolated a tempting sufficient condition

\[
S(s)K_{\rm rel}(s)S(s)^{-1}=Q_G(s),
\]

where \(K_{\rm rel}\) is the analytic closed-loop return and \(Q_G\) is the
positive G3 Schur return.  On a complex open parameter set, this condition is
generically impossible.

## Holomorphic positivity obstruction

Let \(U\subset\mathbb C\) be connected and open.  Suppose \(Q:U\to\mathcal
S_2\) is holomorphic and \(Q(s)\) is self-adjoint for every \(s\in U\).  For
fixed vectors \(u,v\), polarization expresses

\[
\langle u,Q(s)v\rangle
\]

through diagonal matrix coefficients.  Each diagonal coefficient

\[
\langle u,Q(s)u\rangle
\]

is holomorphic and real-valued.  By the open mapping theorem it is constant.
Polarization then shows every matrix coefficient is constant, hence \(Q\) is
constant.

Therefore a nonconstant holomorphic family cannot remain positive
self-adjoint throughout a complex open set.

## Similarity obstruction

Assume \(K_{\rm rel}(s)\) is holomorphic in \(\mathcal S_2\) and holomorphically
similar to a positive self-adjoint \(Q_G(s)\) on \(U\).  Similarity preserves
regularized spectral invariants.  In finite cutoff it preserves

\[
\operatorname{Tr}K_{\rm rel}(s)^m
=
\operatorname{Tr}Q_G(s)^m.
\]

The right side is real and nonnegative for every positive integer \(m\).  Each
left side is holomorphic.  Thus every such trace is constant on \(U\).

The prime-loop factor

\[
(I-L(s))^{-1}
\]

makes the finite relative return nonconstant unless the incidence return
vanishes labelwise.  Hence the proposed holomorphic similarity cannot hold on
a complex open chart for the nontrivial source cone.

## Raw block mismatch

The obstruction is also visible before spectral invariants.  The basic G3
energy

\[
\|\mathcal Ay\|^2+\|Jx-y\|^2
\]

has raw Gram blocks

\[
J^*J,
\qquad -J^*,
\qquad I+\mathcal A^*\mathcal A.
\]

The analytic cone instead uses

\[
I-L(s),
\qquad -B(s)^\dagger,
\qquad I-A(s).
\]

Replacing \(I-L\) by \(J^*J\), or \(I-A\) by
\(I+\mathcal A^*\mathcal A\), changes an analytic pencil into a positive
energy Gram.  No provenance identity currently authorizes either
replacement.

## Correct G3-to-G4 arrow

The comparison must therefore be weaker and parameter-typed.  The Green form
is obtained by pairing the analytic equation with a source conjugate or
reciprocal state, not by holomorphic similarity of the two operator families.
The required statement has the form

\[
\mathcal C_{\rm FP}(s)\psi=0
\Longrightarrow
\mathfrak G_s(\psi,\psi)=0,
\]

followed by the G3 coercive decomposition of \(\mathfrak G_s\).  Its
antisymmetric boundary term is killed by the maximal-isotropic endpoint
relation, while its bulk term contains the signed displacement from the
critical seam.

This is a kernel-state Green identity.  It need only act on the kernel at the
same parameter and may use the reciprocal/conjugate parameter involution.  It
is not a holomorphic operator similarity.

## Unit theorem must not be inferred

G3 coercivity can exclude analytic cone kernels in the off-seam region after
the kernel-state Green identity is proved.  It cannot make
\(d_{\rm rel}\) a nowhere-zero unit on the seam, where the signed bulk term
vanishes.  A global unit theorem would remove all relative collisions,
including those that may encode the Xi divisor, and is stronger than the RH
implication actually required.

Thus the relative determinant should not automatically be multiplied into the
already completed Xi section as a unit.  The source Xi determinant line and
the cone determinant line must instead be related by a divisor-preserving
kernel comparison.

## Revised G4 frontier

The holomorphic-similarity route is rejected.  The admissible remaining arrow
is:

1. Xi-section zero gives a kernel of the completed analytic cone with matching
   algebraic multiplicity;
2. the cone kernel satisfies the maximal-isotropic Green identity;
3. the G3 positive form forces the real displacement from the seam to vanish.

Step 2 is constructed at the domain level.  Step 1 remains the determinant
section-to-kernel comparison.  No RH conclusion is authorized.
