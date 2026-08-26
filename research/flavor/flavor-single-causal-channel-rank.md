# Single causal channel rank theorem (WP390)

## Deutsch question

What source constructor makes a generic positive-definite portal impossible
and forces WP389's Gram matrix to lose exactly one rank?

## One-channel theorem

Let one independently admitted source channel couple to the invariant response
coordinates through the amplitude

\[
A_v=g_1X+g_2Y,
\]

with positive susceptibility $\chi$. Its induced positive response is

\[
V=\chi A_v^2,
\qquad G_1=\chi vv^T,
\qquad v=(g_1,g_2)^T.
\]

Therefore $\det G_1=0$ identically. In WP389 notation,

\[
a=\chi g_1^2,\qquad
b=\chi g_2^2,\qquad
\kappa=2\chi g_1g_2,
\]

so $\kappa^2=4ab$ follows without coefficient tuning. The kernel selects

\[
g_1X+g_2Y=0.
\]

This is the sought structural explanation of rank-one saturation, conditional
on the claim that there is exactly one causal channel.

## Hostile completion theorem

Add a second positive channel with coupling vector $w$ and susceptibility
$\eta$. Exact expansion gives

\[
\det(\chi vv^T+\eta ww^T)
=\chi\eta(v_1w_2-v_2w_1)^2.
\]

The shell kernel survives only if the second channel is absent or exactly
collinear with the first. Any noncollinear positive correction makes the Gram
matrix full rank. Even an arbitrarily small channel lifts the determinant
linearly in its susceptibility.

The smallest hostile completion is $v=(1,0)$ and $w=(0,1)$, for which the
determinant is $\chi\eta>0$. Thus “one shared cause” is falsifiable: discover
one independently supported noncollinear response channel.

## What remains unexplained

Single-channel causation forces rank one but does not predict the shell ratio,

\[
\frac{X}{Y}=-\frac{g_2}{g_1}.
\]

It also does not prove its own uniqueness. A microscopic theory must enumerate
the allowed mediator, threshold, and radiative channels and show that every
one is forbidden or aligned by a source principle that was fixed before the
flavor answer.

An experimental rank test requires two independently excited source-error
directions and a calibrated two-response instrument. The acceptance condition
is a vanishing smallest singular value with uncertainty small enough to reject
the nearest noncollinear completion. Algebraic rank without such an instrument
is not executable control.

## Disposition

WP390 supplies the first structural mechanism forcing WP389 saturation: a
unique shared causal channel. It is a genuine conditional selector rather
than a presentation rigidifier. Its live falsifiers are an additional
noncollinear source channel, a resolved positive second singular value, or
instability of alignment under RG and threshold completion.

The remaining selector gate is an independent derivation of channel
uniqueness and $g_2/g_1$, followed by a calibrated rank measurement on the
complete admitted ensemble.

Run `uv run --with sympy python
research/flavor/checkers/wp390_single_causal_channel_rank.py` to regenerate
the result.
