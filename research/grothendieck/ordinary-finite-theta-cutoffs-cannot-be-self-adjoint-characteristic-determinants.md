# Ordinary Finite Theta Cutoffs Cannot Be Self-Adjoint Characteristic Determinants

## Minimal falsifier

Nima's finite-cutoff requirement is decisive. If a finite completed theta
packet were exactly the characteristic determinant of a finite self-adjoint
operator, every zero in its centered spectral variable would be real.

But the smallest positive reciprocal three-mode packet already violates this.
Let

$$
F_{a,L}(z)=1+2a\cosh(Lz),
\qquad 0<a<\frac12,
\qquad L>0.
$$

This packet has a positive center and equal positive reciprocal side weights.
Its zero equation is

$$
\cosh(Lz)=-\frac1{2a}.
$$

Since $1/(2a)>1$, the zeros include

$$
z=\pm\frac{\operatorname{arcosh}(1/(2a))}{L}
+\frac{(2k+1)\pi i}{L}.
$$

They have nonzero real part. The packet respects positivity, reciprocal
symmetry, and Real symmetry, yet its zeros are off the seam.

No finite self-adjoint matrix $A_L$ can satisfy

$$
F_{a,L}(-i\lambda)=u_L(\lambda)\det(A_L-\lambda)
$$

with $u_L$ nowhere zero under the centered convention, because the two sides
have incompatible zero loci.

## Consequence for the determinant programme

The full determinant identity

$$
\det(\mathcal A_L-\lambda)
=\det(A_{0,L}-\lambda)D_L(\lambda)
$$

is algebraically correct for a self-adjoint block. It cannot equal an
ordinary finite positive reciprocal theta truncation. Therefore the requested
finite-cutoff replay has only three possible outcomes:

1. the finite theta approximant is not the ordinary labelled truncation;
2. its boundary condition already contains completion-dependent, nonlocal
   sewing data;
3. exact determinant identification exists only after the infinite
   restricted-product completion.

The first two options must be source-derived. Otherwise the completion has
been fitted to eliminate the finite off-seam zeros.

## Why this matters

The global Xi function could still be a self-adjoint characteristic section
even though every natural finite source approximant fails to be one. But then
self-adjoint spectrality is an emergent property of completion, not a property
preserved by finite Euler or theta truncation.

That reverses the expected proof order. One cannot prove finite determinant
identities and pass them continuously to the limit. The completion must first
change the admissible object, cancel the finite off-seam divisor, and produce
a new self-adjoint determinant line. This is precisely where circularity can
hide.

The sharp source question is now:

> Which independently defined completion morphism removes every finite
> off-seam zero while preserving the eventual Xi divisor?

Ordinary local uniform convergence cannot explain arbitrary disappearance of
zeros from a compact region: Hurwitz stability preserves isolated zeros under
nondegenerate locally uniform limits. Hence the required completion must
involve a changing domain, a renormalized determinant, or zeros escaping
through a chart boundary rather than ordinary convergence of entire finite
packets.

## Corrected acceptance gates

A viable two-chart construction must explicitly state:

- which finite objects replace ordinary reciprocal theta truncations;
- where their off-seam zeros go under completion;
- whether convergence is local uniform, meromorphic, relative, or only in a
  determinant-line topology;
- which background divisor cancels at each stage;
- why the cancellation is fixed by source sewing rather than by Xi;
- how the limiting self-adjoint domain emerges without being inferred from
  the desired zero set.

The real obstacle is no longer merely the Weyl cut. It is the discontinuous
birth of self-adjoint spectral meaning at infinite completion.
