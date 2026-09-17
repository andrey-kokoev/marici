# qRB microstep 48: normalized sewing convergence

The local cells `gamma_p` are exact, but their raw infinite product or sum need not converge. The global observer requires normalized cells `\widehat\gamma_p` satisfying

$$
\sum_p\sup_{s\in K}
\left|d\log\widehat\gamma_p(s)\right|<\infty
$$

on every compact zero-free set `K`, together with basepoint normalization

$$
\widehat\gamma_p(s_0)=1.
$$

Under this majorant, the ordered product converges locally uniformly and logarithmic differentiation commutes with the prime limit. The finite mixed sewing squares then pass to the infinite family.

This is a convergence criterion, not an assertion that raw `gamma_p` already satisfies it. The required normalization must come from the source completion convention.

Status: infinite sewing gate precisely formulated; source normalization remains the missing input.
