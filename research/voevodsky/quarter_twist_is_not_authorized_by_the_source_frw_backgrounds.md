# The quarter twist is not authorized by the source FRW backgrounds

## Question

Does the cosmological source authorize the quarter-twist value needed to turn the equal-order relative residue into the conductor sign involution?

## Claim boundary

This audits the explicit FRW values listed in the source. It does not exclude analytic continuation to another power-law background, but such continuation would require separate physical and contour authority.

## Source values

Equation (2.13) of *Cosmology meets cohomology* uses the same parameter \(\varepsilon\) in the FRW metric and lists

\[
\varepsilon=0 \quad\text{for de Sitter},
\]

\[
\varepsilon=-1 \quad\text{for flat space},
\qquad
\varepsilon=-2 \quad\text{for radiation domination},
\qquad
\varepsilon=-3 \quad\text{for matter domination}.
\]

The later relative Gauss–Manin matrices are proportional to this \(\varepsilon\).

## Monodromy test

The equal-order normal residue has nonzero eigenvalues two. For any listed source value, the corresponding local monodromy eigenvalue is

\[
\exp(2\pi i\,2\varepsilon)=1.
\]

The conductor Kummer involution instead requires eigenvalue \(-1\). The smallest twist values producing that sign are

\[
\varepsilon=\pm\frac14
\]

modulo half-integer shifts and convention-dependent overall sign.

Neither quarter value occurs among the four source backgrounds. Therefore the conditional conjugacy between the relative normal involution and \(M_1M_2\) is an analytic twist construction, not a physical consequence of the source cosmologies.

## Consequence

The nearby-cycle route now separates into two claims:

- the integral residue and lattice calculations are source-derived and remain valid for symbolic \(\varepsilon\);
- the order-two Kummer monodromy comparison requires a quarter twist absent from the listed FRW backgrounds.

A contour prescription cannot repair this by assertion. It must derive an effective local exponent of one quarter from a source integrand, an additional local system, or a separately authorized stacky descent. An ordinary ramified pullback only multiplies residues and cannot divide an integer FRW exponent to one quarter.

## Disposition

Physical monodromy authority is absent for the quarter twist. The exact next acceptance test is a source-derived fractional local system or stacky character with exponent one quarter while preserving the selected integral pairing. Until then, the monodromy conjugacy is conditional and nonphysical.
