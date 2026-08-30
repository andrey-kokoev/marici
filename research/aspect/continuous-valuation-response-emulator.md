# Continuous valuation-response emulator

## One adelic response law

Let `q=exp(-ell)` and center the spectral coordinate at `s=1/2+z`.  The
normalized finite-place odd response becomes

`rho_ell(z)=-sinh(ell z)/sinh(ell/2)`.

For an actual finite prime, `ell=log p`.  The archimedean response is the
algebraic degeneration

`rho_0(z)=lim_(ell->0) rho_ell(z)=-2z`.

The family retains three exact source features for every nonzero `ell`:

- reciprocal oddness: `rho_ell(-z)=-rho_ell(z)`;
- endpoint normalization: `rho_ell(1/2)=-1`;
- opposite endpoint: `rho_ell(-1/2)=1`.

Thus the real-place coefficient `-2` is forced by the same normalized
valuation-difference constructor as the finite responses.

## Convergence jet

The small-`ell` expansion is

`rho_ell(z)=-2z-[z(4z^2-1)/12]ell^2+O(ell^4)`.

There is no linear error.  A two-scale Richardson combination

`rho_R(ell,z)=[4rho_(ell/2)(z)-rho_ell(z)]/3`

cancels the quadratic defect and approaches `-2z` at order `ell^4`.

## Optical realization

Use a tunable pair of reciprocal log-delay paths with separation `ell`.
Normalize their difference by the same endpoint factor `sinh(ell/2)`.  Sweep
`ell` continuously even though actual prime channels occupy only the samples
`ell=log p`.

Measure the complex response at `ell` and `ell/2`, then form the Richardson
port.  The apparatus must recover `-2z` without an independent
archimedean-gain fit.  This makes the infinite place a limit channel of the
same instrument family rather than a separately calibrated detector.

## Falsifiers

- failure of oddness indicates reciprocal-path imbalance;
- failure at `z=plus/minus 1/2` indicates incorrect quotient normalization;
- an error linear in `ell` indicates asymmetric path transport;
- failure of fourth-order Richardson convergence means the finite and
  archimedean columns do not arise from one deformation family.

The emulator tests adelic coherence, not a sequence of primes tending to
one.  Its continuous `ell` is a laboratory deformation coordinate.

## Use in the boundary Schur apparatus

Insert `rho_ell` as the odd local boundary column and take the Richardson
limit as the archimedean column.  Any full Schur matrix that instead fits the
real-place response independently fails before determinant evaluation.  The
test fixes normalization and orientation but does not impose zero
confinement.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_continuous_valuation_response_emulator.py
```
