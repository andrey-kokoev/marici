# The Renormalized Prime Graph Bound Is RH in Disguise

## Raw trivializations fail everywhere in the critical half-strip

For real $\sigma$ with $1/2<\sigma<1$,

$$
P_X(\sigma)=\sum_{p\le X}p^{-\sigma}
$$

diverges as $X\to\infty$. Correspondingly, the finite Euler sections

$$
E_X(\sigma)=\prod_{p\le X}(1-p^{-\sigma})^{-1}
$$

grow without bound even at points where the completed zeta section is
nonzero. Their inverses tend to zero.

Therefore no uniform graph-norm or inverse bound on the raw finite
trivializations can hold throughout an open RH half-sector. The divergence is
the deterministic mean prime-density wall, not a zero event.

## Source-fixed mean subtraction

The logarithmic derivative packages prime powers through the Chebyshev
function $\psi$:

$$
-\frac{\zeta'(s)}{\zeta(s)}
=s\int_1^\infty\psi(x)x^{-s-1}\,dx
$$

for $\operatorname{Re}s>1$. Subtracting the continuum mean $\psi(x)\sim x$
gives

$$
-\frac{\zeta'(s)}{\zeta(s)}-\frac{s}{s-1}
=s\int_1^\infty(\psi(x)-x)x^{-s-1}\,dx.
$$

The pole carrier $s/(s-1)$ is the deterministic boundary current. The
remaining connection is the Mellin transform of the arithmetic fluctuation
$\psi(x)-x$.

## Why the proposed bound is not yet an explanation

The classical RH-strength estimate

$$
\psi(x)-x=O\left(x^{1/2}\log^2x\right)
$$

makes the fluctuation integral converge on every closed half-plane
$\operatorname{Re}s\ge1/2+\varepsilon$. Conversely, holomorphic control of
the completed logarithmic derivative throughout $\operatorname{Re}s>1/2$,
with the corresponding growth needed for Mellin inversion, yields the same
prime-counting barrier and excludes off-seam zeros.

Thus a uniform completed graph-norm estimate formulated only as a bound on the
renormalized prime connection is RH in another coordinate. It is a valid
equivalent target but not a Deutschian explanation.

This also separates two kinds of escape:

- mean escape is universal and occurs throughout the critical half-strip;
- fluctuation escape is divisor-bearing and is controlled by
  $\psi(x)-x$.

Only the second can encode off-seam zeros. Any completion topology that does
not type these two channels separately will mistake ordinary renormalization
for spectral loss.

## Corrected operator target

The next advance cannot be another direct estimate of the fluctuation Mellin
transform. It must represent $\psi(x)-x$ as a source-derived boundary flux or
commutator of a fixed completed operator. Then self-adjointness or a conserved
current could force the support of its index without first proving the RH
prime-counting bound.

The required identity has the Sommerfeld form

$$
(2\operatorname{Re}s-1)\mathcal N_s
=J_s(\infty)-J_s(0),
$$

but now its boundary term is explicitly the mean-subtracted prime fluctuation
current. The construction must:

1. produce the continuum mean wall independently;
2. retain the primitive and square currents rather than hide them in the
   subtraction;
3. identify the residual $\psi-x$ as a typed operator boundary flux;
4. prove the flux vanishes for an admissible zero-state;
5. obtain positivity or faithfulness of $\mathcal N_s$ from the full
   tail--seam state;
6. reject a hostile source by failure of the flux identity before locating
   its zeros.

Without such an operator identity, the derived-limit formulation remains an
exact description of where RH lives, but not a mechanism explaining why the
defect is seam-supported.
