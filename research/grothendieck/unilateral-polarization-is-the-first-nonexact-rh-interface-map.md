# Unilateral polarization is the first nonexact RH interface map

## The surviving map

The injective trace sewing operator is conjugated Fourier and therefore flat.
Source Mellin evaluation is also reciprocal-covariant before a tail boundary
condition is chosen. The first operation that does not preserve the reciprocal
symmetry is restriction to one scale half-line.

Let

\[
P_+f=\mathbf 1_{[0,\infty)}f,
\qquad
P_-f=\mathbf 1_{(-\infty,0]}f,
\]

and let scale reflection be

\[
(Sf)(q)=f(-q).
\]

Then

\[
SP_+S=P_-,
\qquad
[P_+,S]\ne0.
\]

Thus reciprocal reflection does not descend within either unilateral
polarization. It exchanges the two polarized sectors.

## Endpoint shadow

For a real positive-side source `f`, define

\[
A(z)=\int_0^\infty f(q)e^{zq}\,dq.
\]

Transporting the constructed positive tail and reconstructing the native
reciprocal tail give different endpoint values. Their residual is

\[
C_f(z)
=A(-\overline z)-\overline{A(z)}.
\]

For real `f`,

\[
C_f(z)
=-2\int_0^\infty f(q)\sinh(\overline zq)\,dq.
\]

This is the endpoint shadow of the failure of `P_+` to be reciprocal
invariant. It vanishes at `z=0`, is odd under reciprocal parameter reversal,
and is generally nonzero both off the seam and at nonzero seam height.

No zero data or division by the completed transform enters this formula.

## Bilateral completion

For an even bilateral source, write

\[
A_+(z)=\int_0^\infty f(q)e^{zq}\,dq,
\qquad
A_-(z)=A_+(-z).
\]

The completed scalar readout is

\[
X(z)=A_+(z)+A_-(z)
\]

up to the retained completion units and endpoint terms. A zero imposes the
anti-diagonal endpoint relation

\[
(A_+(z),A_-(z))=(a,-a).
\]

It does not make either unilateral endpoint vanish. Therefore the candidate
zero-state naturally belongs to the kernel of the augmentation

\[
\epsilon(a_+,a_-)=a_++a_-,
\]

while `C_f` records the mismatch between the two unilateral reconstruction
routes.

## Exact interface object

The smallest post-trace interface packet is consequently not another Fourier
operator. It contains:

1. the two polarized source sectors `P_+H` and `P_-H`;
2. reciprocal exchange `S` between them;
3. the common endpoint space;
4. the augmentation `epsilon`;
5. the route-mismatch cocycle `C_f`;
6. any source-authorized modular cell whose boundary equals that cocycle.

The relevant homology question is whether `C_f` is a boundary of the frozen
primitive, square, archimedean, and mixed-seam filling packet. Merely defining
its antiderivative is an adaptive-cell repair and is inadmissible.

## Important consequence

The two half-planes are not created by two unrelated analytic functions.
They are scalar shadows of two complementary polarizations of one bilateral
source. Their distinction arises only after applying the noninvertible
projections `P_+` and `P_-`. The seam is where reciprocal exchange compares
the polarized presentations unitarily; the possible loss of meaning is the
failure of a polarized state to possess a compatible mate under the full
boundary conditions.

## Finite falsifier

Choose a finite source basis stable under reflection and represent `P_+`,
`P_-`, `S`, endpoint evaluation, and the declared modular filling map `M`.
Compute

\[
R=C-\partial M
\]

as a typed endpoint functional before scalar summation.

- If `R` is nonzero, the modular-current conservation route fails at that
  packet.
- If `R=0`, compute whether the anti-diagonal augmentation state is a
  boundary or a genuine normalized interface class.
- If cancellation occurs only after forgetting channel labels, it does not
  establish the source identity.

## Scope

This identifies unilateral polarization as the first nonexact operation after
flat trace sewing and types the known seam cocycle as its endpoint shadow. It
does not construct the modular filling cell, prove the cocycle exact, prove
off-seam interface acyclicity, or prove RH.
