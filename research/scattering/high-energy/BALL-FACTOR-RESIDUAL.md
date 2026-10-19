# H7 — ball-arithmetic factor residual and bounded-attempt closure

This final cycle of the eight-cycle H7 attempt uses python-flint/Arb at 128 bits to enclose the block-factor reconstruction residual. The platform's NumPy longdouble has only a binary64 mantissa, so it cannot provide the intended precision increase.

## Certified subcalculation, fixed reference

Each regenerated raw H entry, shift and computed L/D factor entry enters Arb as an **exact binary dyadic**. Products and squared Frobenius norms are evaluated as balls, including both off-diagonal orientations. The reference is the Hermitian matrix of those stored binary H entries minus the exact binary shift times I. It is not an enclosure of every original real-valued source assembly operation or of the exact radical CPOSE. Both distinctions are recorded in the receipt.

The factor-generating solves remain floating: their stability is not assumed. The independent ball reconstruction bounds the residual of whichever binary factors they produced. The receipt preserves Arb ball strings and outward-inflated presentation floats. The comparison with separation still uses a **conditional** inverse/D-block separation model from the earlier screen; that model has not become certified merely because this factor residual is enclosed.

## Measured result

The Arb enclosure gives factor residual upper 2.6785542e-10 for the stored binary reference. This is below the prior conditional separation estimate 5.5564738e-8, removing the factor-product arithmetic obstruction for that reference. It does not validate the conditional inverse/D-block bounds or the original source assembly. The final forecast was 0.05 accepted / 0.05 rejected / 0.90 inconclusive; the actual bounded outcome is inconclusive. That forecast is historical and must not rank an unspecified successor.

## Attempt disposition

H7 stays open. This ends the original eight-cycle attempt **inconclusively**, not as a rejection. The factor residual is a useful narrower certified subcalculation for the stored binary reference, but original source assembly, D-block inertia/separation, inverse-factor arithmetic, spectral-frame transfer and the full-band coupled inverse remain separate gates.

No effort budget is automatically renewed. A successor H7 attempt needs an explicitly costed protocol and new forecast. Until that is specified, the planner must not continue recommending the exhausted attempt on the old one-cycle cost. H6 remains an independent executable certification task; H8 remains dependent on its declared premises.

Replay requires NumPy, SciPy and python-flint:

    uv run --with numpy --with scipy --with sympy --with threadpoolctl --with python-flint python research/scattering/high-energy/check_ball_factor_residual.py --check
