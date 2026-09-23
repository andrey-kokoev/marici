# The global four-pair bosonic target coefficient has a compact two-sheet trace

## Arbitrary target, not another fixed-target sample

In the first-pivot target chart write `Y=[I₂|B]` with `B` two-by-four, and the retained eight external rows as `Z=[Z_L|Z_R]` with `Z_L` eight-by-two and `Z_R` eight-by-four. **At every such target**, the explicit ambient transformation

    G(B) = [[-B, I₂], [I₄, 0₄ₓ₂]] ∈ SL(6)

sends `Y(B)` to the sourced localization plane `Y₀=[0₍₂ₓ₄₎|I₂]` and sends external data to `[z|h]` with

    z = Z_R − Z_L B,       h = Z_L.

More importantly, HOLD `G(B)` fixed when varying the target to `B′`: `Y(B′)G(B)=[B′−B|I₂]`. Thus the oriented row-major target-chart differential is **exactly** `d⁸U=d⁸B` at the chosen `B`; there is no guessed sign, power or normalization. The universal source/Y0 Jacobian factorization now supplies an explicit global target coefficient on the nondegenerate two-sheet open set:

    ω_B(B;Z) = Tr_{C(v)z=0} [ −det(C(v)h)^4 /
                (w2 w4 w5 w6 w7 w8 u(t−u) det(∂(C(v)z)/∂v)) ].

Here `C(v)` is the declared four-pair chart, `v=(w2,w4,w5,w6,w7,w8,t,u)`, and the trace sums BOTH algebraic solutions. The inside is an explicitly rational element of the generic degree-two fibre algebra, so its field trace is a global RATIONAL coefficient in `(B,Z)` on this chart's simple-fibre open set. It is a **compact rational expression**, not an expanded numerator or pole factorization. It retains the earlier `−1` source-orientation relation to the published ordered α dlog chart.

An independent exact checker derives `det ∂B/∂v = det(C(v)h)^(-4) det ∂(C(v)z)/∂v` directly on each sheet, then tests the expression against the original eight-by-eight target Jacobian at THREE rational targets: two frozen positive targets and a third target with an **independent** positive moment-curve external `Z`. Both algebraic sheets agree separately; the full trace agrees where prior traces were frozen. The `Y0` polynomial result supplies the separately justified nilpotent specialization in its own chart; one must NOT insert rank-four-body data directly into the displayed B-chart denominator.

## Residual

An expanded numerator and explicit global pole divisor remain uncomputed. The external `⟨5678⟩` residue has been independently matched in the Y0 chart, but the arbitrary-Y pole divisor has not been factorized. Positive image coverage, authored nine-point generalized-R history and the global amplitude sum are separate open tasks.

Checker: `research/nima/checkers/check_four_mass_global_target_trace_by_recentring.py`; result: `research/nima/results/four-mass-global-target-trace-by-recentring.json`.
