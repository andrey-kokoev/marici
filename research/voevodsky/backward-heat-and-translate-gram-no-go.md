# Backward heat and translate-Gram no-go

## Question

Can broad pointwise positivity of the completed heat kernel propagate to narrow probes or imply all-translate Gram positivity?

## Claim boundary

The audit refutes both promotions. It does not test the full arithmetic kernel numerically.

## Heat direction

With

\[
\tau=\frac1{4t},
\]

forward smoothing satisfies

\[
\partial_\tau\Theta=\partial_\xi^2\Theta.
\]

In the width parameter,

\[
\partial_t\Theta=-\frac1{4t^2}\partial_\xi^2\Theta.
\]

At a first spatial zero minimum, \(\partial_\xi^2\Theta\geq0\), hence \(\partial_t\Theta\leq0\). Increasing \(t\) moves backward relative to the positivity-preserving heat direction and permits entry into negativity.

## Exact fixture

Consider the heat mode

\[
k_\tau(x)=1-be^{-\tau}\cos x.
\]

When \(r=be^{-\tau}=1/2\), it is pointwise nonnegative. Yet the translate Gram matrix at \(0\) and \(\pi\) has determinant

\[
(1-r)^2-(1+r)^2=-4r=-2.
\]

Thus pointwise positivity does not imply positive definiteness. Under backward continuation to \(r=3/2\), the value at zero becomes \(-1/2\), so broad positivity also does not propagate to narrower probes.

## Disposition

Two distinct shortcuts are closed:

- forward heat positivity cannot be transported backward by reparameterizing width;
- positivity of \(\Theta(t,\xi)\) as scalar values cannot replace positivity of every finite translate matrix.

The remaining acceptance test is direct positive semidefiniteness of the completed arithmetic translate kernel at every width, followed by a source-family density proof.

## Verification

- `research/voevodsky/backward-heat-and-translate-gram-no-go-v1.json`
- `research/voevodsky/checkers/check_backward_heat_and_translate_gram_no_go.py`
- `research/voevodsky/results/backward_heat_and_translate_gram_no_go.json`
