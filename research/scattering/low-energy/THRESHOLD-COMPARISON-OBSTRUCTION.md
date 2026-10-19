# C6 — no shared-frame flux-isometric threshold intertwiner

## Inputs and exact scope

C1 gives S_rim(1/2+k²)->-I4 in operator norm. C11 gives the metric-whitened coefficient S_port(2-2cos(k))->S0=I3-2ww*, where ||w||=1. Its eigenvalues are -1,1,1. The endpoint-versus-coefficient convention contributes only a common phase, already allowed by C6.

C6 requires the **same** isometry V:C3->C4 on incoming and outgoing fibers. Separate input and output maps, extra channels, a different metric or a non-isometric projection are not its claim.

## Limiting contradiction

If a regular family existed, its limiting equation would be

    -V0 = alpha0 V0 S0.

Multiplication by V0* gives -I3=alpha0 S0. The left side is scalar and S0 has both eigenvalue signs, so no unit-modulus alpha0 can satisfy this equation.

## Quantitative version

For any isometry V and |alpha|=1, not necessarily with limits,

    ||-V-alpha V S0|| = ||I3+alpha S0||
                      = max(|1-alpha|,|1+alpha|) >= sqrt(2).

The inequality follows from |1-alpha|²+|1+alpha|²=4. It is sharp at alpha=+i or -i. Isometry preserves the operator norm of the factor it multiplies; no selected input eigenvector is discarded.

For the actual scattering matrices, the triangle inequality gives

    ||S_rim(k)V-alpha V S_port(k)||
      >= sqrt(2) - ||S_rim(k)+I4|| - ||S_port(k)-S0||.

The two error norms tend to zero by C1/C11. For sufficiently small positive k the right side is strictly positive, uniformly over all V and alpha. Hence the asserted exact intertwining equality is impossible.

This proves C6 and, within the same shared-isometry/common-phase class, shows that dropping continuity of V or alpha alone would not repair it. No analogous assertion is made for independent incoming/outgoing identifications. C2's completeness conjecture is not a premise.

## Verification

`check_threshold_comparison.py` freshly replays the C1 and C11 certificates, checks the exact Householder rank/sign facts, and verifies the polynomial phase bound and its sharp case. The norm/limit argument above is analytic; no finite scan of phases or energies replaces it. No source-owner solver, physical calibration or particle channel identification is introduced.
