# An unshaped residual pulse cannot exactly implement the polar transfer

## Question and conjecture boundary

Test the simplest direct spectral implementation suggested by the source residual:
one constant pulse of Hc=[[0,Bsharp],[B,0]], with the inherited metrics. This
candidate is reconstructed from the actual B, not from the desired polar W.
Even granting this coupling as available and allowing a final memory phase
correction, it cannot exactly transfer the complete positive bright sector.

This is a falsifier of that one-pulse route, NOT of the broader conjecture of
arbitrary-accuracy spectral compilation. Approximate long-pulse recurrence,
switched controls and source-supported spectral shaping remain distinct options.
No new coupling is physically admitted by this calculation.

## Exact source certificate

The checker reconstructs S=Bsharp B, the actual five-dimensional bright
restriction, and its four-dimensional positive invariant image. It checks the
stored restriction entrywise, positive energy pivots, and

    Hc^sharp=Hc,
    Hc^2=diag(S,B Bsharp).

The positive bright spectrum contains the rational eigenvalue

    lambda_r=4485/3292

and the three roots of the primitive integer cubic

    10837264 x^3 - 43349056 x^2 + 44361887 x - 6431463.

Its degree-three reduction modulo 11 has no root. The receipt enumerates all
11 residues, with nonzero evaluations and nonzero leading coefficient. Therefore
the cubic is irreducible over Q; each root is irrational. Exact positivity
ensures all four channels are positive. No floating eigenvalue threshold is used.

## Obstruction

For a normalized S eigenvector x with eigenvalue lambda>0, define

    y=B x/sqrt(lambda).

Then y has the same metric norm as x, and Hc restricts to sqrt(lambda) times
the exchange matrix on (x,y). A ready-memory input evolves under pulse area t as

    (x,0) -> (cos(t sqrt(lambda)) x, -i sin(t sqrt(lambda)) y).

The polar target has zero native component on every positive channel. Exact
transfer would therefore require

    t sqrt(lambda)=(2k_lambda+1) pi/2

for every positive bright eigenvalue. Comparing a cubic root lambda_c with
lambda_r gives

    lambda_c/lambda_r=((2k_c+1)/(2k_r+1))^2,

a rational number. That contradicts irrationality of lambda_c and rationality
of the nonzero lambda_r. A final memory phase cannot repair a nonzero native
component. This obstruction precedes any additional relative-sign requirement.

It proves no exact single-pulse implementation at any real pulse area. It gives
no uniform positive error floor when pulse area is unbounded. In particular,
noncommensurate frequencies alone do not falsify an approximation conjecture.

## Disposition

The direct spectral route cannot be justified merely by exponentiating B's
unshaped off-diagonal coupling once. It needs an actual approximate recurrence
argument with resource/error bounds, a switched synthesis, or a permitted
spectral-shaping construction. Defining a normalized coupling from W would
instead reuse the target and would require its own source-control synthesis.

The higher conjecture remains unrefuted. Its fair-search/evaluator route is not
affected by this exact one-pulse obstruction. No optimizer or general spectral
compiler was specified or executed here.

## Verification

    python research/strominger/checkers/check_encoder_single_residual_pulse.py

Fresh execution passes exact reconstruction, positivity, square identity,
characteristic factorization and modular irreducibility checks. Receipt:
`results/encoder-single-residual-pulse.json`, including source/checker hashes.
The transfer formula and irrational-ratio argument are written mathematics,
not a formal-kernel proof. Predecessor suites were not freshly rerun. No graph
publication, commit or push.
