# Affine symmetry-center authority (WP308)

## Exact nonzero fixed point

For one weak-basis-invariant coordinate, define the affine reflection

\[
r_a(x)=2a-x
\]

and invariant potential

\[
V_a(x)=(x-a)^2.
\]

The action is an exact involution, the fixed locus is the singleton $x=a$,
and the strictly convex potential has the same unique minimum. This is a
structural source zero with respect to every parameter except the center.

## Center-authority kernel

The selected point obeys

\[
\frac{dx_*}{da}=1.
\]

Two realizations of the same abstract $Z_2$, centered at $a=1$ and $a=2$,
select different physical values. Translating to $y=x-a$ makes the action the
linear reflection $y\mapsto-y$ and the minimum $y=0$, but reconstructing
physical $x$ still requires the offset $a$.

Thus the abstract symmetry does not determine a nonzero number. Numerical
authority resides in the affine embedding of the symmetry.

## Reference rule and classification

If $a$ is supplied by a reference port, it defines a new relational
experiment over the port stabilizer groupoid. It does not reveal an absolute
center belonging to the original experiment.

The affine action is a genuine point selector only if source geometry fixes
$a$ with physical units and no surviving modulus. Otherwise it rigidifies a
presentation around an unspecified reference and fails WP307's robust
source-zero gate.

Run `uv run --with sympy python
research/flavor/checkers/wp308_affine_symmetry_center_authority.py` to
regenerate the exact affine-symmetry audit.
