# Odd endpoint completion is nonnegative and injective but not coercive

Let the completed labelled odd endpoint carrier be the Hilbert direct sum of finite interval fibers with lengths `L_n`, where every `L_n` is finite and `L_n->infinity`. The normalized leverage values are

$$
\kappa(L)
=\frac{\sinh L-L}{2\sinh^2(L/2)}.
$$

For every finite `L>0`,

$$
0<\kappa(L)<1,
$$

while

$$
\kappa(L)\longrightarrow1
$$

as `L->infinity`.

Define the diagonal leverage operator

$$
K_{\rm odd}=\bigoplus_n\kappa(L_n).
$$

Then

$$
0\le K_{\rm odd}\le I,
\qquad
\|K_{\rm odd}\|=1.
$$

Nevertheless,

$$
\ker(I-K_{\rm odd})=\{0\},
$$

because no diagonal entry equals one. Thus the residual form

$$
R_{\rm odd}=I-K_{\rm odd}
$$

is nonnegative and injective.

It is not coercive: normalized basis vectors in shells with `L_n->infinity` satisfy

$$
\langle R_{\rm odd}e_n,e_n\rangle
=1-\kappa(L_n)\longrightarrow0.
$$

Accordingly, `ran(R_odd)` is not closed and zero belongs to its continuous/essential spectral boundary, but not to its point spectrum.

This distinction is sufficient for exact finite-shell zero exclusion and for completed injectivity. It is insufficient for a uniform inverse, a resolvent annulus, or stable reconstruction. Any RH argument needing only absence of an actual null vector may use transversality; arguments requiring compact-uniform coercivity need an additional margin from another observer.

Status: limiting semidefinite transversality closed on the labelled direct sum; uniform coercivity remains open.
