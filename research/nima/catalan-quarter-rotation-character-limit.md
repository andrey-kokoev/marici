# Catalan quarter-rotation character limit

For `n` divisible by four, rotate the labelled `n`-gon by `n/4` vertices. This induces an order-four operator `q_n` on the Catalan triangulation module `H_n`, with

\[
q_n^4=1.
\]

Direct enumeration at `n=4,8,12` gives

\[
\operatorname{Tr}(q_n)=\operatorname{Tr}(q_n^3)=0,
\qquad
\operatorname{Tr}(q_n^2)=\binom{n-2}{(n-2)/2}.
\]

The second formula counts centrally symmetric triangulations. The first reflects the absence of a triangulation fixed by a genuine quarter turn.

The four character-projector ranks are therefore

\[
\dim H_n^{(0)}=\dim H_n^{(2)}
=\frac14\left(C_{n-2}+\binom{n-2}{(n-2)/2}\right),
\]

\[
\dim H_n^{(1)}=\dim H_n^{(3)}
=\frac14\left(C_{n-2}-\binom{n-2}{(n-2)/2}\right).
\]

Since the central binomial correction grows like `2^(n-2)` while `C_(n-2)` grows like `4^(n-2)` up to a polynomial factor,

\[
\frac{\operatorname{Tr}(q_n^k)}{\dim H_n}\to0
\quad(k=1,2,3),
\]

and every character weight tends exponentially to

\[
\frac14.
\]

At `n=12` the four normalized weights are approximately

\[
(0.2537509,\ 0.2462491,\ 0.2537509,\ 0.2462491).
\]

This supplies an actual finite-degree order-four operator whose normalized character sectors converge to one quarter. The remaining comparison is to intertwine polygon rotation `q_n` with the analytic four-chart rotation on the realized Catalan module.
