# Frame-messenger factorization kernel: WP651

## Matching map

Attach one WP435-type vectorlike chain to each of WP650's six complex frame
coefficients. With frozen messenger masses, tree-level elimination gives

\[
c_k=-\frac{x_ky_k}{M_k},
\qquad k=1,\ldots,6.
\]

At the unit benchmark, the complex matching Jacobian from twelve vertex
couplings to six coefficients has rank six and kernel dimension six. The exact
fiber action

\[
x_k\longmapsto t_kx_k,
\qquad
y_k\longmapsto y_k/t_k
\]

preserves every \(c_k\).

## Hostile constructor pair

For one chain, the UV packets

\[
(x,y,M)=(1,1,1),
\qquad
(x,y,M)=(2,1/2,1)
\]

both match to (c=-1), while their left-vertex strengths are one and four.
Thus identical low-energy frame coefficients do not identify the messenger
constructor.

## Classification

The messenger grammar supplies an executable low-energy matching carrier. It
neither selects the scalar coefficients nor identifies their UV source. The
first nonfaithful arrow is vertex couplings to effective coefficients.

Repair requires threshold-sensitive calibrated observations that derive from
the same messenger grammar and include finite widths, mixing, decoupling, and
detector resolution. Formal access to the separate factors is not an
instrument.

## Reproduction

```powershell
uv run --with sympy python research/flavor/checkers/wp651_frame_messenger_factorization_kernel.py
```

Generated result: `results/wp651_frame_messenger_factorization_kernel.json`.
