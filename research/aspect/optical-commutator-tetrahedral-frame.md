# Tetrahedral optical syndrome frame

The axis probe set identifies the four coherent residue coordinates, but it is
not the best-conditioned four-probe instrument. The noise-optimal minimal
frame uses four dual-rail states whose Bloch vectors are the vertices of a
regular tetrahedron.

For each pure target probe with Bloch vector r, the control-Y first-jet row is,
up to a common minus sign,

    [1, r_z, r_x, r_y].

Choose the four sign triples

    (1, 1, 1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1)

and divide each by the square root of three. Their sum is zero and their frame
operator is four-thirds times the three-dimensional identity. Consequently
the syndrome Gram matrix is diagonal with entries 4, 4/3, 4/3, 4/3. Its
singular values are 2 and three copies of 2/sqrt(3), so its condition number is
sqrt(3).

This is optimal among all four pure-state probes. The identity column always
has squared norm four. The three-dimensional Bloch block always has trace
four, so its smallest eigenvalue cannot exceed four-thirds. Therefore no such
frame can have condition number below sqrt(3). The centered isotropic
tetrahedron attains the bound.

The earlier rail-zero, rail-one, plus-X, plus-Y probes remain a transparent
calibration basis. The tetrahedral set is the production acquisition frame:
it spreads coherent-error uncertainty isotropically and minimizes the worst
inverse amplification at fixed four-probe count.

The frozen epsilon equal to 0.01 falsifier remains unchanged. This is an
instrument-conditioning theorem, not a physical execution or interaction-net
promotion claim.
