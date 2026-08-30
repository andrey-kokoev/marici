# Optical commutator error syndrome

Detection is not yet diagnosis. The next rung linearizes the noncentral residue
around the protected odd-intersection word and asks whether optical probes can
identify its complete coherent first jet.

After the ideal signal word, write a small residual unitary as

    exp(i (gamma I + epsilon_z Z + epsilon_x X + epsilon_y Y)).

The four coefficients describe, respectively, branch phase, relative rail
phase, coherent rail mixing, and quadrature rail mixing. For a target state
psi, the control Y derivative at the ideal point is the negative expectation
of the corresponding generator in psi.

Use four source-fixed probes: rail zero, rail one, plus-X, and plus-Y. Ordering
the error coordinates as I, Z, X, Y, their unsigned expectation matrix is

    [1,  1, 0, 0]
    [1, -1, 0, 0]
    [1,  0, 1, 0]
    [1,  0, 0, 1].

Its determinant is minus two. Therefore the four Y first jets identify all
four coherent error coordinates locally.

Two hostiles show why this is a genuine extra rung.

First, delete any one of the four probes and the map cannot have rank four.
Second, keep every probe but read only control X. Its derivative at the ideal
point vanishes in every coherent direction because cosine is even. X detects
finite loss only at second order; Y carries the signed first-order syndrome.

The frozen epsilon equal to 0.01 mismatch remains unchanged. This syndrome map
adds localization, not a replacement falsifier. It does not infer an
interaction-net lift or claim physical data.
