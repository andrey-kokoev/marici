# qRB microstep 125: projective endpoint pair channel

The away-from-endpoint pair estimate is not uniform as `a` tends to zero. The endpoint must therefore be retained as a separate projective coordinate:

$$
\rho_{nm}^{[0,b]}(0)
=\int_0^b e^{-\pi(n^2+m^2)x^2}\,dx.
$$

For every finite pair packet this endpoint row is finite and continuous in `b`. The global endpoint object is the projective family of these finite rows, not an unweighted sum over all pairs.

Thus the pair-response construction has two compatible strata:

- interior shells: absolutely summable Gaussian pair channel;
- endpoint shell: finite-rung/projective boundary channel.

No uniform endpoint Hilbert bound is asserted.

Status: endpoint typing aligned with the relative qRB category; global endpoint pair summability remains open.
