# Archimedean gamma filter bank

## Architecture correction

The archimedean countercurrent is not a sixth linear boundary current. The
canonical linear candidate, Gaussian heat degree, is already identical to the
completed prime-power incidence degree.

The genuinely new operation is quadratic: a source-fixed energy gate applied
after the five linear currents have been reconstructed.

## Exact optical compilation

The completed gamma weight decomposes into channels with rates

`a_n = 2n + 1/2`.

For each rate, a two-sided exponential kernel has spectral transfer

`K_n(tau) = 2 a_n / (a_n^2 + tau^2)`.

Interfere that filtered arm against a direct arm of gain `2/a_n`. The
complementary transfer is exactly

`2/a_n - K_n(tau) = 2 tau^2 / (a_n(a_n^2+tau^2))`.

This is Nima's gamma-channel multiplier. It is nonnegative, vanishes only at
zero frequency, and has no fitted coefficient. Forty-four parallel channels
implement the first source-positive truncation. Balanced coherent detection
retains the subtraction sign; square-law integration then measures the summed
quadratic energy.

The endpoint contribution is a separate rank-two coupler in the even and odd
hyperbolic modes. It must be combined before the energy decision, not appended
as a post-hoc offset.

## Tower meaning

The completed local architecture is therefore:

1. five independent linear boundary-current records;
2. one arithmetic--archimedean coherence check identifying heat degree with
   completed prime-power degree;
3. one 44-channel archimedean energy gate testing the supported boundary
   domain.

The third item is the next rung, not a sixth coordinate on the first rung.
This resolves the earlier rank-six pressure: the missing operation changes
type from linear observation to quadratic admissibility.

## Falsification boundary

The finite filter-bank identity is exact. It does not yet prove positivity of
the continuum support-compressed operator. The decisive remaining calculation
is directed interval propagation of the 44-channel boundary-value system,
with a certified zero count for both parity determinants on nonpositive
spectral parameter.

Failure of that certificate kills this countercurrent architecture. Success
establishes the first source-complete archimedean gate and leaves only its
sewing to the five-current totalization law.

## Verification

```text
uv run --with sympy python research/aspect/checkers/check_archimedean_gamma_filter_bank.py
```
