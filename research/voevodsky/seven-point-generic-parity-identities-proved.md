# All15 generic parity identities now proved

The exact calculation has crossed from restricted kinematic families to the full six-independent-modulus chart. All15 Ward-reduced quartic differences are identically zero over Q(a,b,c,d,e,f). Combined with the generic termwise Ward checks and the universal3-dimensional single-flavor basis, this establishes equality of the complete degree(4,4,4,4) eta tensors on the regular chart, not just gluon components or sampled points.

The successful checker is `check_seven_point_generic_quartics.py`; result is `results/seven-point-generic-quartics-lcm.json`. The previous generic-term artifact remains a construction checkpoint from a timed-out monolithic checker, with its passed=false status intentionally unchanged. Its12 completed terms and Ward assertions are the precise input to the new successful proof; the result binds those bytes by SHA256.

Algorithm: factor each rational summand, take the factorwise polynomial denominator LCM, clear numeric denominators exactly, and sum the resulting integer polynomial numerators using FLINT. Crucially remove the common nonzero numerator factor before expansion. This is legitimate in the polynomial integral domain. The earlier implementation reached14 identities but the last process exited during a very large expansion; common-factor removal resolves that bottleneck. No float conversion, random evaluation, modular zero heuristic, or interpolation is involved.

After the incremental success, ran the optimized checker with --fresh. ALL15 identities were recomputed successfully in a single bounded invocation; none relied on the resumed ledger. Output records current checker and source hashes. Reproduce:

uv run --with sympy --with python-flint python research/voevodsky/checkers/check_seven_point_generic_quartics.py --fresh

Scope: the amplitude equality is generic on the explicitly established projective kinematic chart, wherever the source formulas and spinor frames are regular. It retains Parke-Taylor prefactors and Fourier signs; momentum delta, coupling and a shared overall phase are stripped consistently. Extension across poles is a rational identity statement, not assignment of finite values at singular kinematics. Relating charts uses the standard projective/covariant amplitude interpretation, not an extra numeric test.

Next close the reproducibility chain: separate generic term construction from the obsolete slow simplification loop, regenerate the12 terms from source in a fresh end-to-end run, rerun the15 identities, and package the universal Ward and chart certificates with source hashes. This will remove reliance on a partial-construction artifact. A positive-cell/contour derivation remains a different optional task; no claim about the parked nine-point contour follows from this parity identity.
