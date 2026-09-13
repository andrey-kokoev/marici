# Movable-cutoff observers give a linear-time local codec

## Tail encoding

For ordered state coefficients \(u_1,\ldots,u_n\), define right-tail observations

\[
B_i
=
\sum_{j=i}^n
\left(\prod_{r=i}^{j-1}\rho_r\right)u_j.
\]

They satisfy the backward recurrence

\[
B_n=u_n,
\]

\[
B_i=u_i+\rho_iB_{i+1}.
\]

Thus the complete observer bank is computed by one right-to-left scan.

## Local decoding

The inverse is bidiagonal:

\[
u_n=B_n,
\]

\[
u_i=B_i-\rho_iB_{i+1}.
\]

Encoding and decoding both require \(O(n)\) arithmetic operations and constant-width local memory.

## Noise locality

If the measured tails are

\[
\widetilde B_i=B_i+\eta_i,
\]

then reconstructed error is

\[
\widetilde u_i-u_i
=
\eta_i-\rho_i\eta_{i+1}.
\]

Each observer error affects only two neighboring reconstructed states. There is no global Vandermonde error propagation.

For \(0<\rho_i<1\), the local absolute amplification is bounded by

\[
|\eta_i|+|\eta_{i+1}|.
\]

## Architecture

```text
encoder:
  backward exponential accumulation

decoder:
  nearest-neighbor differencing

state storage:
  one tail value per labelled cutoff
```

The same bidiagonal matrix is the Markov innovation operator. Stable observation and local state dynamics are exact duals.

## Continuous limit

The discrete equations converge to

\[
B'(x)=B(x)-u(x),
\]

or

\[
u(x)=B(x)-B'(x).
\]

Thus the moving-boundary observation field obeys a first-order local codec even though its integrated value contains the entire future tail.

## Significance

This is a concrete mechanism by which global contextual memory can be both:

- completely observable;
- encoded and decoded locally;
- linearly scalable;
- robust against global error spreading.

The cost is not algebraic order but one independently addressable cutoff for each retained context.

## Verification

```text
python research/coherence/check_tail_observer_encoder_decoder.py
```

The checker verifies exact encoding, direct tail summation, and decoding for 600 rational packets through thirty contexts.

Artifacts:

- `check_tail_observer_encoder_decoder.py`
- `tail-observer-encoder-decoder.v1.json`
