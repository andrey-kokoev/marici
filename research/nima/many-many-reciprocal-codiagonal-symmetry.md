# Many-many reciprocal codiagonal symmetry

The pair damping coefficient is symmetric:

$$
\kappa_{nm}=\kappa_{mn},
$$

while the forcing coefficients obey

$$
\alpha_{nm}+\alpha_{mn}=1.
$$

Therefore a reciprocal scalar codiagonal should use symmetric output weights `w_nm=w_mn` on the damping/endpoint coordinates and the ordered pair 

$$
\alpha_{nm}Y_{nm}+\alpha_{mn}Y_{mn}
$$

on the forcing coordinate.

This preserves the exchange involution `(n,m) -> (m,n)` and keeps the asymmetric forcing orientation inside a symmetric many-many output.

Status: reciprocal codiagonal symmetry rule fixed; source normalization of the output weights remains open.
