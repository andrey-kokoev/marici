# qRB finite loading witness: definition

We define the first witness packet using primes

$$
F_2=\{2,3\},
$$

one regular source point

$$
s_0=2,
$$

and the normalized local feature coordinates

$$
Y_p=C_pX_p(s_0).
$$

The target normalization is defined by the completed mixed source convention

$$
\mathcal B_{\rm mix}(s_0)
=\sum_{p\in F_2}\frac12p^{-3/2}Y_p.
$$

The competing Euler-to-theta convention is

$$
\mathcal B_{\theta}(s_0)
=\sum_{p\in F_2}c_pY_p,
\qquad
c_p=2(\log p)\sum_{k\ge1}p^{-k/2}\Phi'(k\log p).
$$

For each candidate, record the three residuals:

$$
\Delta_{\rm wall},
\qquad
\Delta_{\rm sew},
\qquad
\Delta_{\rm comp}.
$$

The witness is noncircular only if the target wall, sewing, and completion coordinates are independently specified—not defined by the candidate being tested.

This file defines the packet and normalization slots but does not assign numerical `Y_p` or target values. Such assignments require the source-derived local feature formula.
