# One nine-point positive target has exact minimum eight-label support

The previously certified nine-point lower bound is now matched by an EXACT positive construction. For the same fixed strictly positive target `Y=CZ` and moment-curve `Z`, all 36 seven-label supports are excluded by independently replayed rational Farkas certificates. A new rational source matrix has column **3 identically zero**, all other eight columns nonzero, and all **28** ordered minors of its retained columns strictly positive. Its source observation equals the original target in all six coordinates on BOTH rows. The minimum retained minor is

    953709770533/1024000000000000 > 0.

Therefore the **minimum possible number of nonzero source labels for this exact admitted target is eight**. This is a matching lower/upper certificate, not an inference from a numerical optimizer. The numerical five-dimensional affine relaxation narrowed the candidate deletion to label 3; a nonlinear search proposed a point, then all four free kernel coefficients were FROZEN as rationals and checked from scratch. The separate verifier reads the frozen eight-label source matrix, verifies all 12 observed moments and 28 minors, replays all 36 independent seven-label impossibility packets, and refuses four corruption controls.

The explicit free kernel coefficients, in order `(a0,a1,b0,b1)`, are

    (4062,5481,-37665,-105941)/1000000.

The dependent coefficients enforce column 3 equal to zero. Relative to the original nine-label source, the first determinant coordinate is

    q01 = a0*b1-a1*b0 = -223890477/1000000000000 != 0.

Thus this particular connecting source change uses two independent invisible directions, not the rank-one affine shift that made the seven-point fibre a polygon. This does not claim every eight-label witness must have nonzero determinant relative to that original representative.

The conceptual distinction is now concrete:

- some full-dimensional nine-point image cells can be obtained by zero-padding seven-point polyhedral cells;
- those cells cannot cover this target, since NO seven-label source lift exists;
- an eight-label positive source DOES reach it, inside a genuinely higher-support semialgebraic fibre.

This certifies a fixed-target **support threshold**, not a physical history-to-cell matching, a global nine-point triangulation, or any analytic cutoff-completion rate. A subsequent unsourced eight-support FOUR-PAIR candidate now passes an exact positive algebraic lift and local full-image-rank test; see `a-nine-point-eight-support-paired-cell-has-an-exact-full-rank-image-point.md`. The next gate is to SOURCE its history identity, compute its canonical-form pushforward and test boundary residues with determinantal realizability retained.

Reproduce:

    uv run --with sympy python research/nima/checkers/check_nine_point_minimum_eight_support.py
    uv run --with sympy python research/nima/checkers/verify_nine_point_minimum_eight_support.py

Packets: `research/nima/results/nine-point-minimum-eight-support.json` and `nine-point-minimum-eight-support-verification.json`; lower certificate: `nine-point-no-seven-support-verification.json`.
