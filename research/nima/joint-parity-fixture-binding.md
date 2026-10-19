# The native parity observer versus the frozen matrix fixture

## Result

An exact, invertible STATIC map between the four native parity output records and the four selected matrix corners exists. It reproduces the matrix values, fixed-reference residuals, and mixed trace exactly.

But it fails the existing target operation even on individually admissible self-compositions. The failure is already visible in the fixed-reference scalar trace. Thus matching a nonzero mixed rectangle does not establish operation-preserving descent.

No fixture values, reference, source words or primitive response operations were changed to obtain this result.

## Frozen inputs

Source: the four actual seam return words, compiled and observed by the freshly checked native joint-parity module:

    C00: AB BA          -> (1,1)
    C01: AB BC CA       -> (1,0)
    C10: AD DB BA       -> (0,1)
    C11: AD DB BC CA    -> (0,0).

Target: arrow slots(i,j)=(0,0),(0,1),(1,0),(1,1) of the EXISTING137-row shared-leg fixture, with

    Cij=Yj Xi,
    X0=Y0=I, X1=I+H/3, Y1=I+K/5,
    d=2I, r=d^-1=I/2.

The target operation under test is the previously declared reference-return composition b r_b a, not ordinary matrix multiplication substituted for record typing.

These four selected records have distinct carrier target keys. Therefore only their FOUR SELF-PAIRS are admitted by that operation within this subset. The checker verifies that and never treats all16 numeric products as typed record compositions. The source words are A-to-A loops and can be concatenated, so a full endpoint binding would have additional obligations even before numerical comparison.

## Exact static interpolation

Order the source point basis as(0,0),(0,1),(1,0),(1,1). Their target images are respectively C11,C10,C01,C00.

There is a unique linear map from this four-dimensional indicator space to the four entries of a2-by2 matrix sending those basis vectors to the frozen target corners. Its determinant is -1/225. The analogous linear extension of the four residual values Cij-d has determinant+1/225.

Both maps reproduce their four corner values exactly. The source mixed record vector(1,-1,-1,1) maps to

    [[0,0],[0,1/15]].

The corresponding fixed-reference trace table is

    (-29/15, -2, -2, -2),

or, as a function of parity bits(a,b),

    -2 + (1-a)(1-b)/15.

That formula is determined by the existing matrix fixture; it is not a gain selected to make the source conjunction diagnostic fit. Its numerical constants remain imported target data, not derived source physics.

This interpolation is an audit control, not an admitted source map. Four independent output records can carry four independent matrix coordinates without any agreement of their operations.

## Repetition tests the operation, not just the table

The native four-cycle C11 has zero parity shift. One execution and two successive executions therefore give exactly the same finite observer state(0,0).

A map out of that finite state which fits the original corner must assign both observations the same matrix

    M=C11=[[1,1/3],[1/5,16/15]].

At the existing target port, self-composition is admitted and instead produces

    M r M = [[8/15,31/90],[31/150,271/450]],

which is not M.

The fixed-reference scalar already separates them:

    tr(M-d)     = -29/15,
    tr(M r M-d) = -1289/450,
    difference  = -419/450.

No postprocessing function of the unchanged parity output can give those two distinct readings. This is not only a failure of the linear interpolation; even a nonlinear map agreeing on the frozen point has the same collision.

All four admissible corner self-compositions fail the fitted operation square. Their native parity actions square to the zero-shift state, whereas their target reference-return products do not equal the matrix fitted to that state.

## What the result rules out—and what it leaves available

It rejects factoring this target composition/readout contract through the FINITE parity observer while retaining the frozen corner agreement. It does not reject:

- the finer geometric current state;
- full directed histories and their retained native execution;
- another explicitly specified target operation;
- a different response interpretation retaining more than parity.

In particular, the native geometric construction was never claimed to return its full state whenever its parity reader returns. It remains available as a candidate source for a finer response representation.

This result is also not an identification of the four-corner trace with the complete137-member rung4 mean. It tests a specific existing local response and an already admitted follow-up operation. The full source-to-rung endpoint and observation binding remains separate.

The next useful representation problem must therefore consume more of the existing geometric state or retained path than this finite observer does. Merely scaling its nonzero mixed contrast, adding another coordinate fit on the same four points, or renaming its four values "rung4" cannot solve the repetition collision.

## Verification

    uv run research/nima/checkers/check_joint_parity_fixture_binding.py

27 exact checks pass. The checker freshly reruns the native parity linearization audit and the existing endpoint-composition gate, which reruns the original rung/shared-leg fixture checks. It verifies both static determinants, all corner matches, the mixed image, exact fixed-reference scalar table, target pair admission, and all four self-product failures.

The native Agda proof receipt and source hashes are validated by its existing checker; Agda itself was not rebuilt in this step. No new formal theorem about matrix representations is claimed.

Artifacts:

- `checkers/check_joint_parity_fixture_binding.py`
- `results/joint-parity-fixture-binding.json`

No source-selected physical descent or calibration is marked complete.
