# qRB microstep 55: derivative-observer upgrade

To pass the sieve limit through a source derivative of order `j`, it is sufficient to have

$$
\sum_{n\ge1}\|\partial_u^j\phi_n\|_{L^1}<\infty.
$$

Then the differentiated label series converges absolutely in `L1`, and the finite prime sieve satisfies

$$
\partial_u^j S_S
\longrightarrow
\partial_u^j\phi_1
$$

in `L1`.

This is the correct next layer for observer construction: source derivatives are controlled before endpoint evaluation or boundary traces are attempted.

Status: criterion isolated. Theta decay is expected to provide it for each fixed finite `j`, but the corresponding uniform trace estimate is not claimed here.
