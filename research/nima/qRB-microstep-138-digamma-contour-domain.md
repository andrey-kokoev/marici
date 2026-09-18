# qRB microstep 138: digamma contour-shift domain

The imaginary continuation shifts the Gaussian contour by

$$
\operatorname{Im}u=\frac{d}{4\sigma}.
$$

The digamma factor `psi(1/4+iu/2)` has its nearest pole at `u=i/2` and reflected pole at `u=-i/2`. Therefore a direct contour shift without residue terms is valid only in the strip

$$
|d|<2\sigma.
$$

For larger translation separation, the contour crosses digamma poles and the continued gamma channel acquires explicit residue contributions. Those residues are part of the endpoint/boundary package and cannot be silently omitted.

Status: local imaginary-continuation identity is valid in `|d|<2 sigma`; global translate-Gram continuation requires residue bookkeeping across strip crossings.
