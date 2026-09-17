# qRB microstep 57: wall-norm summability criterion

Write the sieve difference as the positive tail

$$
S_S-\phi_1=\sum_{n\in A_S}\phi_n,
$$

where `A_S` consists of labels removed by the finite prime set. A sufficient condition for wall-norm convergence is absolute summability of the source cells in the wall norm:

$$
\sum_{n\ge2}\|\phi_n\|_{\rm wall}<\infty.
$$

Then

$$
\|S_S-\phi_1\|_{\rm wall}
\le
\sum_{n\in A_S}\|\phi_n\|_{\rm wall}
\longrightarrow0.
$$

Combined with the weighted trace bound, this gives convergence of the prime boundary observer.

The criterion is deliberately stronger than necessary. The current source record establishes rapid decay for local feature seminorms, but does not yet state this exact global wall-norm sum for all labels.

Status: wall convergence reduced to a concrete summability estimate.
