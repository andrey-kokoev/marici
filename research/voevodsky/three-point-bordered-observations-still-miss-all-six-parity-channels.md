# Three-point bordered observations still miss all six parity channels

## Exact finite result

For the four-prime event-segmented route source, let K_d be the full interval signature at degree d. Their ranks are

    d:          0   1   2   3   4
    rank K_d:   1   1  18  18  24.

Let S be the eighteen previously selected two-point rows. The new exact checker constructs rational matrices R_d and verifies every entry of

    K_d = R_d S,       d=0,1,2,3.

The sparse reconstruction rows are stored in `results/theta-low-degree-bordered-obstruction.json`. Both K_2 and K_3 have kernel exactly im(K), where K is the existing 24-by-6 parity basis and K* K=4I.

The stacked degree-zero-through-three observation therefore has rank eighteen. The fourth-degree restriction K_4 K has rank six; the previously selected six rows complete S with determinant one.

## Consequence for analytical enhancements

Any linear map L_d applied to the degree-d interval signature satisfies

    L_d K_d K = 0,       d<=3.

This includes the tensorized common-history, endpoint, Wronskian, Laplace, and jet columns constructed in `theta-packet-bordered-lift-from-the-prior-polarized-pair-crossing.md`. It also includes joint linear readouts combining different degrees through three. Completion or a changed output norm preserves these exact equalities wherever the readouts extend continuously.

The statement concerns these operations on the fixed signature data. An additional independently measured source channel can carry other information.

## Strictly positive source counterexample

Let k be the first parity column and set

    c_plus  = (1/24) 1 + k/48,
    c_minus = (1/24) 1 - k/48.

Every coordinate is strictly positive and each vector sums to one. The checker verifies

    K_d c_plus = K_d c_minus,       d=0,1,2,3,
    K_4 c_plus != K_4 c_minus,
    B(c_plus-c_minus) = e_1/12,

where B=K*/2.

Thus arbitrary deterministic postprocessing of the complete aggregated data through degree three also cannot recover the four-point parity response on this source class. The failure already occurs for strictly positive probability mixtures. Positivity constraints alone do not identify the hidden channels.

## Source adapter requirement

The new bordered analytical lift acts on event-segmented signatures already supplied by the source. To obtain those signatures from an independently given physical source, the adapter must preserve route-conditioned event order before aggregation, or provide equivalent extra information.

In particular, taking tensor powers of an aggregated one-point observation does not produce the source mixture's event-segmented multipoint signature. It inserts cross-route terms and has no access to the distinction between the two positive packets above. The same counterexample rules out recovery from the full aggregated two- and three-point signatures.

The sharp next source question is therefore: which independently admitted observation distinguishes c_plus from c_minus? The existing selected degree-four signature coordinates do so exactly. A realization claiming parity recovery must exhibit their source implementation or an equivalent six-channel measurement.

## Verification

Fresh command:

    uv run --with sympy python research/voevodsky/checkers/check_theta_low_degree_bordered_obstruction.py

Passed: exact rational reconstruction identities, both kernel ranks, all positive-mixture comparisons, degree-four parity rank, and the unimodular completion. This certifies the finite source statement; the analytic consequences follow from composition with the bounded column maps previously constructed.
