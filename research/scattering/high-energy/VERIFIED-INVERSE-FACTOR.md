# VF1 cycle 2 — verified residual-controlled inverse factor

The saved binary L multipliers define a unit block-lower-bidiagonal factor. The checker reconstructs an approximate inverse W one row at a time using binary floating products, but does **not** assume those products are exact or stable. Arb independently encloses each block of LW-I, and the squared Frobenius norms of W and the residual. It uses the verified Neumann criterion

    eta=||LW-I||_F<1,
    ||L^-1||_2 <= ||W||_F/(1-eta).

No uncontrolled covariance-error propagation and no gamma arithmetic model remain in this subcalculation. Matrices enter Arb as exact binary dyadics; residual dot products and endpoint bounds are ball-enclosed at 128 bits.

Together with the certified binary D separation d from cycle 1, this gives separation(LDL*) >= d/||L^-1||² for the covered leading factor. The full claim is made only if all 49 block rows are covered. Timing limits must produce explicit leading-subsystem coverage rather than silently asserting a full-factor bound. The runner stops beginning new rows after 240 seconds to leave time for receipt closure within the 300-second pilot budget. Replay fixes the saved row coverage.

## Durable continuation

The last binary inverse row and outward cumulative squared-norm bounds are saved in `results/verified-inverse-frontier.v1.npz` and hash-bound by the receipt. This allows a later cycle to continue with missing rows rather than recomputing the verified prefix. Replay refuses a differing frontier. The cumulative bounds are outward floats interpreted as exact dyadics when resumed, not rounded ball midpoints.

## Scope

Even full coverage only certifies the binary factor comparison matrix. The prior H-LDL* ball residual must be linked to these exact factor bytes; original source assembly and exact energy reference must then be enclosed to transfer inertia. The stored spectral-frame bridge and full-band nonsymmetric matching inverse remain further gates. H7 stays open.

Two VF1 execution cycles are spent; one remains. Next action depends on coverage: finish remaining inverse rows if any, otherwise establish factor-residual linkage and assess the source-reference bridge. No stationary solve or threshold search is repeated.

Replay in the pinned source environment with python-flint:

    python research/scattering/high-energy/check_verified_inverse_factor.py --check
