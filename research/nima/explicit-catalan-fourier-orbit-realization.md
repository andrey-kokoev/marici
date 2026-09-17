# Explicit Catalan-to-Fourier orbit realization

For `4|n`, let `q_n` rotate triangulations by one quarter polygon turn. There are no fixed triangulations under `q_n`; every orbit has size two or four.

Let

\[
a_{2,n}=\frac12\binom{n-2}{(n-2)/2},
\qquad
a_{4,n}=\frac14\left(C_{n-2}-\binom{n-2}{(n-2)/2}\right).
\]

Then

\[
H_n\cong
\mathbb C[C_4/C_2]^{\oplus a_{2,n}}
\oplus
\mathbb C[C_4]^{\oplus a_{4,n}}.
\]

## Analytic orbit blocks

For every size-four Catalan orbit choose a distinct tagged generic oriented Fourier seed `P_a`. Prior work gives its orbit

\[
P_a\xrightarrow{W_{or}}C_{-r}
\xrightarrow{W_{or}}P_{1-a}
\xrightarrow{W_{or}}C_r
\xrightarrow{W_{or}}P_a.
\]

For every size-two orbit choose a distinct tagged reflection-even seed. One explicit model is a non-self-dual Gaussian scale pair

\[
g_t(x)=e^{-\pi t x^2},
\qquad
\mathcal Fg_t=t^{-1/2}g_{1/t},
\]

with `t != 1`. Since both functions are even, Fourier square acts trivially and the orbit has size two after normalization.

Map each triangulation orbit basis cyclically to its assigned analytic orbit basis. Orbitwise this defines an injective map

\[
R_n:H_n\hookrightarrow\mathscr A_n
\]

satisfying exactly

\[
W_{or}R_n=R_nq_n.
\]

Taking the analytic target as the tagged orthogonal direct sum of these finite orbit blocks makes `R_n` isometric and normalized-trace preserving. Consequently its four character projections have exactly the Catalan multiplicities and converge in normalized trace to `1/4`.

## Status

This constructs an explicit equivariant analytic realization of the finite Catalan `C4` representation. The tags retain triangulation-orbit provenance, as does the function-valued history target.

It is not yet the source-minimal realization: assigning a distinct analytic seed to every Catalan orbit is faithful but highly redundant. The next compression problem is to derive orbit seeds from rooted-spine data so that subtree substitution becomes analytic convolution rather than external tagging.

`check_catalan_c4_orbit_realization.py` verifies the orbit decomposition and target multiplicities at `n=4,8,12`.
