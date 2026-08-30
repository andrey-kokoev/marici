# Source Lyapunov variance-changing port

## Constructor

Let `E` be the source test space, `E'` its continuous dual, and let the
source dynamics provide a positive generator `L:E->E`.  Define the smoothing
covariance `G:E'->E` by the weak Lyapunov equation

`L G + G L' = I`.

This is not a direct pairing of two covectors.  It is an explicit
variance-changing map.  Once `G` exists, the completed boundary currents may
be compared through

`B_G(lambda,mu)=<lambda,G mu>`.

For a positive finite source generator the solution is

`G = integral_0^infinity exp(-t L) exp(-t L') dt`.

The formula makes the scale depend on the already normalized source
generator, rather than on observed seam data.

## Minimal Fourier cell

Take the Fourier quarter-turn `J` and the isotropic source generator `L=I`.
For a general symmetric covariance

`G=[[a,b],[b,c]]`,

the Lyapunov equation gives

`2G=I`.

Therefore `a=c=1/2` and `b=0`.  Fourier invariance follows automatically.
The scalar freedom left by Fourier symmetry alone is gone.

The hostile rescaling `G=r I` passes Fourier symmetry for every positive
`r`, but its Lyapunov residual is `(2r-1)I`; it passes only at `r=1/2`.

## What must be sourced

This construction moves the problem exactly once.  The remaining datum is
not a covariance scale but a normalized source generator `L` and the unit
forcing on its right-hand side.  If either is freely rescaled, the ambiguity
returns.  In the theta apparatus the normalization must descend from the
heat equation, Haar half-density, or the metaplectic commutator—not from a
measured zero or a fitted Green norm.

For the prime rigging, the decisive analytic question is whether the
source-derived semigroup maps the primitive and augmentation currents from
`E'` into `E` strongly enough that the integral converges in the test-space
topology.  Failure of that integral is a clean rejection, not permission to
insert a weighted Hilbert pivot.

## Optical execution

Implement `L` as the measured drift matrix of a stable two-quadrature linear
optical network.  Inject a preregistered unit white forcing fixed by the
commutator or shot-noise reference.  The stationary covariance must solve the
same Lyapunov equation.  Tomography then checks three independent claims:

- equal diagonal covariances;
- zero cross covariance;
- absolute diagonal value `1/2` in the source units.

The third claim distinguishes this constructor from Fourier symmetry alone.

## Status

The finite selector theorem is exact.  Its application to the completed
adelic theta boundary remains conditional on a source-derived `L`, a sourced
unit forcing, and convergence of the semigroup integral on the rigged space.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_source_lyapunov_variance_changing_port.py
```
