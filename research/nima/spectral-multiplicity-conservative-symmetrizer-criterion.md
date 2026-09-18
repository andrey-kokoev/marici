# Spectral-multiplicity conservative symmetrizer criterion

Let `A` be self-adjoint with spectral representation

$$
\mathcal H\simeq\int_\Lambda^\oplus\mathcal H_\lambda\,d\mu(\lambda),
\qquad
(Af)(\lambda)=\lambda f(\lambda).
$$

A bounded self-adjoint operator `K` commutes with `A` exactly when it is decomposable:

$$
(Kf)(\lambda)=K(\lambda)f(\lambda),
\qquad K(\lambda)=K(\lambda)^*
$$

almost everywhere.

For port vectors `b,c`, the colocation equation

$$
Kb=\alpha c
$$

is therefore the fiberwise equation

$$
K(\lambda)b(\lambda)=\alpha c(\lambda)
$$

for almost every `lambda`.

## Multiplicity-one case

If `dim H_lambda=1` almost everywhere, then `K(lambda)=k(lambda)` is real. A bounded nondegenerate symmetrizer with bounded inverse exists precisely when, on the active support,

$$
r(\lambda)=\frac{c(\lambda)}{b(\lambda)}
$$

is real almost everywhere and satisfies

$$
0<m\le |r(\lambda)|\le M<\infty,
$$

while `b` and `c` have the same essential support. On the inactive complement choose any bounded real weight bounded away from zero.

A uniformly positive symmetrizer exists exactly when, after fixing `alpha>0`,

$$
0<m\le r(\lambda)\le M<\infty
$$

almost everywhere on the active support.

## Higher multiplicity

For fibers of dimension greater than one, existence requires a measurable essentially bounded field of invertible Hermitian operators `K(lambda)` carrying `b(lambda)` to `alpha c(lambda)`. The pointwise necessary scalar condition is

$$
\langle c(\lambda),b(\lambda)\rangle\in\mathbb R,
$$

with uniform bounds needed for a bounded inverse. Positivity requires this scalar to be positive on active fibers and a uniformly positive measurable extension.

## Application boundary

The derivative/history generator must first be placed in an authorized self-adjoint spectral representation. The stable half-line generator used by the Xi Rosenbrock pencil is not automatically self-adjoint, so this theorem cannot yet be applied directly. A source-derived conservative dilation or Green realization is required first.

Status: infinite-dimensional spectral symmetrizer criterion proved; applicability to the Xi history pencil is blocked by the missing conservative realization of its generator.
