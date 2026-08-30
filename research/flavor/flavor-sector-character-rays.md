# Sector-character coefficient rays (WP350)

## Distinct structural directions

WP349 failed because both sectors occupied the same democratic coefficient ray.
WP350 assigns different permutation characters:

- the up sector is invariant under projector permutations, selecting
  ((1,1,1));
- the down sector is odd under interchange of (P) and (Q), selecting
  ((1,-1,0)).

The corresponding lifts are

\[
Y_u=I+x(P+Q+R),
\qquad
Y_d=2I+y(P-Q).
\]

At (x=y=1), both spectra are nondegenerate and

\[
\operatorname{Tr}([H_u,H_d]^3)=-\frac{3658}{3}i.
\]

Thus distinct symmetry characters can select nonparallel coefficient directions
while retaining generic three-family CP capability.

## Remaining authority

The characters fix directions, not radial amplitudes. The exact CP invariant is

\[
\frac{2i}{9}x^3y^3(y^2-32)(16x^3+65x^2+72x+24),
\]

and its derivatives with respect to both (x) and (y) are nonzero at the
benchmark. These amplitudes retain physical numerical authority.

## Disposition

WP350 is a progressive structural selector of coefficient rays, not a complete
`physical16` selector. A source completion must derive the unequal character
assignments and independently select or normalize both radial amplitudes.

Run `uv run --with sympy python
research/flavor/checkers/wp350_sector_character_rays.py` to regenerate the
exact capability and response audit.
