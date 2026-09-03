# Preconditioned spline finite explicit-formula theorem

## Question

What is the strongest theorem established by the repaired preconditioned-spline computation, before any comparison with the proposed radial–G4 carrier?

## Claim boundary

Let

\[
k_7(u)=\frac1{7!}\sum_{j=0}^{8}(-1)^j\binom8j(u+4-j)_+^7,
\qquad a=2\log 2,
\]

and define the five-shift preconditioned spline

\[
f(x)=k_7(x/2+2a)-5k_7(x/2+a)+\frac{33}{4}k_7(x/2)-5k_7(x/2-a)+k_7(x/2-2a).
\]

Use the kernel shift `b=n+1/4` and the prime-power sign implemented in `research/nima/checkers/preconditioned_spline_weil.py`. Enumerate every prime power within the compact support; the checker proves that prime powers above its enumerated cutoff contribute zero. The earlier results field `c=5/4` had no bound role in the computation and is retracted as inert metadata.

For the archimedean integral, split the series at `N=3`. For `n=0,1,2`, integrate every truncated-power piece exactly as a rational interval, using

\[
2\exp\bigl(2b(s+4-j)\bigr),\qquad b=n+\frac14,
\]

including the knot factor that was absent in the retracted computation. For the remaining series, use the exact zero jets, the signed atomic measure `d f^(7)`, and the one-sided Euler–Maclaurin bounds audited in `research/nima/euler-maclaurin-tail-audit.md`.

Under those definitions, the explicit-formula Gram quantity lies in

\[
[1.1790450740162717\times10^{-5},\;1.1906013635010338\times10^{-5}],
\]

and is therefore strictly positive.

The certified archimedean contribution lies in

\[
[-4.193076879324755,\;-4.1930767637618604].
\]

The checker also verifies that its signed atomic-tail interval is contained in the coarser interval obtained from total variation `81/2`. It retains deliberate failures for reversing the prime sign, omitting shifts, omitting the `D_N` component, setting the Stieltjes variation to zero, and reversing the `B4` orientation.

## Scope

This is a finite explicit-formula theorem for one declared test function and normalization. It does not prove RH, positivity for all admissible test functions, a canonical radial–G4 identification, a physical readout theorem, or an unbounded/colimit result. No arrow from this positive instance to those claims is supplied.

The earlier exact-moment intervals that omitted `exp(2b(4-j))` remain retracted. The theorem uses only the repaired formula and regenerated artifact.

## Durable verification

- Checker: `research/nima/checkers/preconditioned_spline_weil.py`
- Results: `research/nima/results/preconditioned_spline_weil.json`
- Remainder audit: `research/nima/euler-maclaurin-tail-audit.md`
- Full successful execution: `structured_command_execution:e_4616_1788287225919610300_22`
- Prefactor repair admission: `ev-000000012214-b072fea6-71f7-449b-9ba8-aca3449c2f11`
- Positive certificate admission: `ev-000000012264-2993630d-15bc-4d5f-88c3-9878a9a8d872`
- Remainder audit admission: `ev-000000012275-c436b57a-5279-4bca-8449-a52d3ed949e7`

## Disposition

The finite positive interval is frozen at the demonstrated strength. Any promotion requires a separately proved comparison or quantification arrow.
