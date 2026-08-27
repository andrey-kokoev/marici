# Disjoint-messenger ray displacement: WP711

## Source-derived vertex correction

WP664 derives the one-loop quartic contribution of each disjoint Dirac
messenger chain from its field-dependent mass supertrace. In the common WP662
normalization, the summed corrections are

\[
N=-8F_n,
\qquad
M=-8F_m,
\qquad
X=0,
\]

where (F_n,F_m\geq0) are sums of multiplicity-weighted fourth powers of
canonical messenger Yukawas. Disjoint topology generates no mixed-norm vertex.

## WP709 response

Substitution into the exact WP709 acceptance functional gives

\[
\delta D
=\frac{N+M-X}{28}
=-\frac{2}{7}(F_n+F_m).
\]

Every nontrivial disjoint messenger completion therefore pushes the regular
WP708 ray toward the radially unstable side at first order. The correction is
a genuine vertex effect, not wavefunction transport, but its sign is opposite
to the required repair.

## Consistency with the cone test

WP665 independently evaluates the raw radial margin on the full positive
boundary and obtains

\[
\left.\frac{d}{dt}(4\lambda^2-\lambda_x^2)\right|_{\lambda_x=2\lambda}
=-32(F_n+F_m)\lambda.
\]

For positive (lambda), this has the same strict outward sign. WP709's local
fixed-ray response and WP665's boundary-vector test therefore agree.

## Disposition

The currently admitted disjoint messenger vertex completion is neither a
selector nor a stability repair. It supplies a source-derived negative
falsifier of the required sign. Opening the ray requires a mixed or bosonic
vertex channel with an independently derived contribution satisfying

\[
N+M-X>0
\]

after all fermion, scalar, gauge, and threshold terms are combined. Merely
adding formal positive Gram coordinates is insufficient; the loop sign and
contact-normal channel must come from the source action.

The smallest exact falsifier is one unit-strength messenger chain,
(F_n=1,F_m=0), which gives (delta D=-2/7).

Reproduce with: uv run --with sympy python research/flavor/checkers/wp711_disjoint_messenger_ray_displacement.py

Generated result: results/wp711_disjoint_messenger_ray_displacement.json.
