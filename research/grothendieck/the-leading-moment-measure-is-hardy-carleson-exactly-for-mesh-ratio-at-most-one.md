# The leading moment measure is Hardy-Carleson exactly for mesh ratio at most one

## Question

Although the moment-to-Hardy identity map is unbounded, is the reverse Hardy-to-moment inclusion controlled for the leading archimedean measure?

## Claim boundary

Yes, with an exact mesh-ratio boundary. For the leading gamma difference measure at `kappa=h/t`, the embedding

\[
H^2(\mathbb D)\longrightarrow L^2(\mu_\kappa)
\]

is bounded exactly when `kappa<=1`. This is the reverse of the comparison needed to transfer a Hardy bound into the moment norm, so it does not prove the cone.

## Leading measure in Bernstein coordinates

The leading difference moments are

\[
d_n(\kappa)=\frac1{\sqrt\pi}
\int_0^\infty r^{-1/2}e^{-r}(1-e^{-\kappa r})e^{-n\kappa r}\,dr.
\]

Set

\[
z=1-e^{-\kappa r}.
\]

Then the associated measure on `(0,1)` has density, up to a positive `kappa`-dependent constant,

\[
d\mu_\kappa(z)
=z\,[-\log(1-z)]^{-1/2}
(1-z)^{1/\kappa-1}\,dz.
\]

Near `z=1`, its tail satisfies

\[
\mu_\kappa([1-\varepsilon,1])
\asymp_\kappa
\varepsilon^{1/\kappa}
[\log(1/\varepsilon)]^{-1/2}.
\]

## Carleson test

A finite positive measure supported on a radius of the disk defines a bounded embedding from `H2` into its `L2` space exactly when

\[
\mu([1-\varepsilon,1])=O(\varepsilon).
\]

The displayed tail meets this condition when `1/kappa>1`. At `kappa=1`, the extra logarithmic factor still makes the tail `O(epsilon)`. For `kappa>1`, the ratio to `epsilon` diverges. Therefore

\[
\mu_\kappa\text{ is an }H^2\text{-Carleson measure}
\quad\Longleftrightarrow\quad
\kappa\le1.
\]

## Direction of the arrow

For `kappa<=1`, one obtains

\[
\|p\|_{L^2(\mu_\kappa)}
\le C_\kappa\|p\|_{H^2}.
\]

The required transfer from a zero-side Hardy estimate to the archimedean moment topology would need the opposite inequality. That reverse inequality fails exponentially on `p_m=(1-z)^m`.

For `kappa>1`, even the Hardy-to-moment embedding fails, so the common graph-norm construction is strictly necessary to place both forms on one domain.

## Interpretation

The boundary `h=t` is a topology transition for the leading observer measure. It does not mark a sign change or physical process. It records when mass near the Bernstein endpoint `z=1` becomes too heavy for Hardy evaluation control.

## Disposition

Use the Carleson embedding only to transport source constructions from Hardy space into the moment space when `h<=t`. It cannot transport lower bounds in the reverse direction, and it supplies no route for `h>t` without a stronger domain.