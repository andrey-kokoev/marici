# Kinetic-normalization descent: WP666

## Missing interface

WP664 is written in canonical field coordinates. The admitted source registry
does not yet supply the two-triplet kinetic normalization. With

\[
\frac{Z}{2}(\partial n)^2+y,n\mathcal O+\lambda|n|^4,
\]

the field redefinition \(n'=sn\) gives

\[
Z'=\frac{Z}{s^2},\qquad y'=\frac{y}{s},\qquad
\lambda'=\frac{\lambda}{s^4}.
\]

Raw \(y^4\) therefore does not descend under field-coordinate changes. The
canonical strength

\[
\widehat F=\frac{y^4}{Z^2}
\]

does descend. Likewise the physical radial margin is represented by

\[
\widehat D=rac{4\lambda_n\lambda_m-\lambda_x^2}
{Z_n^2Z_m^2}.
\]

## Hostile pair

The raw packets \((Z,y)=(1,1)\) and \((4,2)\) have raw fourth powers one and
sixteen, but both have \(y^4/Z^2=1\). They are the same canonical coupling
written in different scalar coordinates. A stability verdict based on raw
\(y^4\) would distinguish presentation rather than physics.

## Disposition

WP664's numerical bound is a valid conditional theorem in canonical
coordinates. It is not evaluable from the current source packet until the
kinetic Gram is derived or the entire flow is expressed in descending hatted
variables. The missing constructor is precisely the source-to-canonical
normalization map already identified in WP626.

This repairs typing; it selects no coefficient or flavor point. The next gate
is a source-derived kinetic Gram and canonical threshold matching.

Reproduce with: uv run --with sympy python research/flavor/checkers/wp666_kinetic_normalization_descent.py

Generated result: results/wp666_kinetic_normalization_descent.json.
