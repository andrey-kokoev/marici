# Reciprocal full-interval coercivity covers both open sectors and degenerates at the seam

## Right sector

For `Re(s)=sigma>1/2`, use

\[
\ell_s^+(c)=\sum_{n\ge1}c_n n^{-s}.
\]

On its null space, the full interval energy satisfies

\[
\mathcal E(c)
\ge
\frac{2\log2}{\zeta(2\sigma)}\|c\|_2^2.
\]

## Left sector

Reciprocal transport replaces `s` by `1-s`. For `sigma<1/2`, define

\[
\ell_s^-(c)=\sum_{n\ge1}c_n n^{s-1}.
\]

The coefficient row belongs to `ell^2` because

\[
\sum_{n\ge1}|n^{s-1}|^2
=
\zeta(2-2\sigma)<\infty.
\]

If `ell_s^-(c)=0`, the same vacuum decomposition gives

\[
\mathcal E(c)
\ge
\frac{2\log2}{\zeta(2-2\sigma)}\|c\|_2^2.
\]

## Reciprocal form

Writing

\[
d(s)=\left|\operatorname{Re}s-\frac12\right|,
\]

both sector estimates have the common constant

\[
\kappa(s)
=
\frac{2\log2}{\zeta(1+2d(s))}.
\]

It is positive in either open sector and invariant under `s -> 1-conjugate(s)`.

For every `epsilon>0`,

\[
\inf_{d(s)\ge\varepsilon}\kappa(s)
=
\frac{2\log2}{\zeta(1+2\varepsilon)}>0.
\]

Thus reciprocal sector charts carry uniform full-interval coercivity on compact sets separated from the seam.

## Seam boundary

As `d(s)` tends to zero,

\[
\zeta(1+2d(s))\longrightarrow\infty,
\qquad
\kappa(s)\longrightarrow0.
\]

At the seam neither scalar coefficient row is in `ell^2`. The failure is exactly the transition from a bounded scalar observer to the previously constructed relative anomaly line and exterior boundary functional.

The two open-sector estimates therefore sew as reciprocal inequalities but do not extend as one Hilbert observer through the seam. A seam theorem must use the line-valued boundary carrier rather than the raw scalar Mellin row.
