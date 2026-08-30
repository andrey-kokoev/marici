# Spin(7) Exchange Leaves the Three-Family Tensor Shape Free

Work package: WP925

## Question

When WP924's scalar coefficients are promoted to three-family Yukawa tensors,
does exchange-reflection select the spectral shape needed for normalized CP?

## Exact fixed tensor locus

Let (Y_-) and (Y_+) be complex (3\times3) matrices. The exchange acts as

\[
(Y_-,Y_+)\longmapsto(Y_+^*,Y_-^*).
\]

The fixed locus is

\[
Y_+=Y_-^*.
\]

An ordered pair contains (36) real coordinates. The fixed equations have
rank (18), leaving (18) real coordinates: exactly one arbitrary complex
(3\times3) tensor. The symmetry eliminates a duplicate conjugate tensor; it
does not determine the surviving tensor.

## Exact spectral-shape hostile

Choose two real diagonal representatives,

\[
Y_A=\operatorname{diag}(1,2,3),
\qquad
Y_B=\operatorname{diag}(1,2,4),
\]

and pair each with its exchange-required conjugate. Both lie on the exact
fixed locus. For Gram eigenvalues (h_i), define the scale-free cubic gap
record

\[
\widehat\Delta(H)=
\frac{|(h_2-h_1)(h_3-h_1)(h_3-h_2)|}{h_{\max}^3}.
\]

The two values are

\[
\widehat\Delta_A=\frac{40}{243},
\qquad
\widehat\Delta_B=\frac{135}{1024}.
\]

They differ exactly and remain unchanged under a common rescaling of the
Yukawa tensor. Hence the hostile is spectral shape, not clock scale.

## Boundary completion

Exchange-even localized operators may depend on invariants such as
(\operatorname{tr}(Y^\dagger Y)), higher power traces, or their scalar
partners. Exchange symmetry permits these terms because they assign the same
functional to the conjugate copy. Their coefficients and stationary spectra
remain source data unless a further action or fixed point determines them.

## Verdict

The operation is a conjugate-copy selector and tensor-presentation rigidifier.
It is neither a spectral-shape selector nor a physical16 selector. The
four-coordinate shape beta block remains undefined: exchange equivariance
constrains its covariance but does not supply its vector field.

The next calculation should use the most general exchange-equivariant tensor
beta normal form and project it onto singular-value ratios. If symmetry permits
an arbitrary shape vector field or a zero/relevant mode, dynamics—not exchange
alone—must supply the missing selector.

No physical instrument gate opens until a source law selects shape and that
law survives thresholds.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp925_spin7_exchange_fixed_family_tensor_fiber.py
~~~
