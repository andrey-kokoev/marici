# The five-cell pointed Fourier module supplies the linear pair-source refinement without doubling Xi multiplicity

Fresh state contains a superseding construction beyond the naive coproduct
no-go.  The ordinary candidates still fail:

- `v -> v tensor conjugate(v)` is nonlinear and sends `tau` to `|tau|^2`;
- `v -> v tensor v` is nonlinear and sends `tau` to `tau^2`;
- the group-like label diagonal retains only `(n,n)` pairs.

However, the source-labelled five-cell module

\[
M_5=\operatorname{span}(\Phi,1,\delta_0,K,V)
\]

provides fixed anchors in the second tensor leg.  Define the pointed one-leg
map

\[
\Delta_5(v)
=
\bigoplus_{\eta\in\{\Phi,1,\delta_0,K,V\}}v\otimes\eta,
\]

or equivalently `v tensor id_(M_5)` before the fixed representation `rho_5`.
This map is linear and holomorphic in the Evans leg, and

\[
\Delta_5(\tau v)=\tau\Delta_5(v).
\]

Therefore it preserves every Xi multiplicity rather than doubling it.

The five anchors supply distinct required coordinates:

- `Phi`: bulk forcing;
- `1`: normalized wall coordinate;
- `delta_0`: odd endpoint jump;
- `K,V`: the two oriented reciprocal tail coordinates.

Their Fourier action forms an exact order-four module: the endpoint anchors
form the half-cycle and `(K,V)` carries the genuine `+/-i` orbit.  Thus the
source refinement `S -> S_pair` is not wholly unconstructed: its finite linear,
reciprocal, wall, endpoint, and multiplicity data already exist.

What remains is not a source coalgebra from scratch.  It is the analytic
promotion of `Delta_5`:

1. prove completion injectivity and uniform prime/grade closure;
2. map the pointed pair carrier into the Green response domain;
3. identify the four window matrix-unit Green polarization, including real
   cross-correlation and oriented imaginary linking;
4. prove positive relative-cone control after radical descent;
5. construct the induced refinement maps on `X_SA`, `X_SC`, and `X_SG`.

This reopens the pair-source route at a later gate.  The linear
multiplicity-preserving source constructor is present; the unresolved content
is its completed Green polarization and filtration-level naturality.
