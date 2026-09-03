# Affine-simplex modular naturality

## Question

Which modular or reciprocal actions preserve the ordinary Mellin affine fillers strictly?

## Claim boundary

The result covers actions affine on the underlying real spectral space and preserving the admitted convex domain. It does not classify every modular action used elsewhere in the programme.

## Affine law

For an affine map \(g(v)=Lv+b\) and simplex barycentric coordinates \(\lambda_i\),

\[
g\left(\sum_i\lambda_i v_i\right)=\sum_i\lambda_i g(v_i).
\]

Therefore the induced chain map preserves every affine simplex and commutes strictly with its boundary.

## Declared reciprocal action

The fixture reciprocal action is negation

\[
\rho(v)=-v.
\]

It is linear, preserves the reflection-closed fixture, and sends each admitted triangle to its reciprocal triangle. Thus reciprocal naturality of the ordinary-domain affine filler is strict.

Complex conjugate-linear actions are real-linear and satisfy the same result when their domains are invariant.

## Nonlinear boundary

Nonlinear inversion does not preserve straight simplices. For \(x=1\) and \(y=2\),

\[
\iota\left(\frac{x+y}{2}\right)=\frac23,
\qquad
\frac{\iota(x)+\iota(y)}2=\frac34.
\]

Hence a genuinely nonlinear modular action requires a source-derived comparison homotopy; affine naturality cannot be transported to it.

## Disposition

The reciprocal-negation naturality gate is closed on the ordinary affine domain. Remaining work is to enumerate actual modular and basis actions, classify each as affine or nonlinear, and then test cutoff compatibility and completed descent.

## Verification

- `research/voevodsky/affine-simplex-naturality-contract-v1.json`
- `research/voevodsky/checkers/check_affine_simplex_naturality.py`
- `research/voevodsky/results/affine_simplex_naturality.json`
