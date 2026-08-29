# Optimal comparison-loop probes

For real route unitaries, the control-X fringe on a normalized probe x is the quadratic form

    x transpose(U_A) U_B x.

Only the symmetric part contributes. Its smallest and largest eigenvectors therefore give the globally optimal two-probe fringe contrast. They are computed from the frozen route programs before physical acquisition.

This replaces six generic probes with two extremal probes. X and Y are still acquired for both probes so an unexpected complex phase is not silently discarded. Bypass trials remain route-labelled.

The optimization changes the acquisition design, not the route compilers or the source lift. It cannot select which lift is physical.

