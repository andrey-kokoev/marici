# The three-prime Green pairing must retain joint cut attachments

The three-prime reconstruction criterion gives a decisive pairing test. On the 48-dimensional source of six prime orders and eight markings, put the graded local signed form on each typed route attachment, with marking degree r carrying sign (-1)^r. This is a nondegenerate joint-cut form.

Let g0 be the alternating permutation sum of the 000 markings and g1 the alternating sum of the 001,010,100 markings. These are exactly the two joint-marginal ghosts from the cut reconstruction calculation. Their joint pairing matrix is

    [[ 6,  0],
     [ 0,-18]].

Hence both missing directions are visible to the joint signed form. In contrast, every terminal form pulled back through either individual-cut observation annihilates these ghosts, because both observations annihilate them. Therefore no Green pairing descended solely from terminal rejoining can equal the joint pairing.

The same obstruction survives positive mixtures. The two distinct positive probability vectors

    1/48 + g0/96,    1/48 - g0/96

have identical individual-cut and terminal observations, but their difference has nonzero joint signed norm. This is a genuine attachment-correlation obstruction, not merely a signed-vector artifact.

## Consequence for the Clark construction

The analytical Clark form must be assembled on the joint typed cut carrier before any cut deletion. Its local sheet-reduced Green mates may then be tensorized over the three event slots and pushed through the actual rejoining maps. Rejoining can produce a contragredient mate, but it cannot be used to define the pairing by pullback after the joint information has been discarded.

This separates three claims:

1. joint-cut faithfulness, already proved by local injectivity;
2. existence of a nondegenerate joint signed pairing, verified here at the graded coefficient level;
3. equality of that pairing with the full arithmetic Clark kernel, which remains to be checked analytically with all cross-cut terms.

The present calculation is deliberately not a sampled numerical Clark-kernel claim. It is the negative-control certificate that any proposed terminal Green descent must fail unless it retains an equivalent attachment datum.

Verification:

    uv run --with sympy python research/grothendieck/checkers/check_joint_cut_green_comparison.py

Passed. Certificate: `research/grothendieck/results/joint-cut-green-comparison.json`.
