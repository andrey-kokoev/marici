# The asymptotic quotient splits contractibly but not equivariantly

## Comparison of sections

Let

\[
\mathcal O_\infty:\mathcal A_{\exp}\to\mathbb C^2
\]

be the two-charge quotient. Any two continuous linear sections \(s_a,s_b\) satisfy

\[
\mathcal O_\infty s_a=
\mathcal O_\infty s_b=I.
\]

Therefore

\[
\mathcal O_\infty(s_a-s_b)=0,
\]

so their difference lands in the discarded moment kernel.

Moreover,

\[
s_t=(1-t)s_a+ts_b,
\qquad 0\le t\le1,
\]

is again a continuous section. The space of linear sections is an affine space over

\[
\operatorname{Hom}(\mathbb C^2,\ker\mathcal O_\infty)
\]

and is therefore contractible whenever nonempty.

Thus section choice carries no ordinary homotopy obstruction.

## Equivariant obstruction

A translation-equivariant section would have to send the two weight vectors of the hyperbolic double to translation eigenvectors in the full carrier.

With

\[
(U_af)(x)=f(x-a),
\]

the required eigenlaws are

\[
U_af_+=e^af_+,
\qquad
U_af_-=e^{-a}f_-.
\]

Their measurable solutions are proportional to

\[
f_+(x)=e^{-x},
\qquad
f_-(x)=e^x.
\]

Neither belongs to \(H^1(\mathbb R)\). Hence no nonzero translation-equivariant section exists in the Green RKHS or its exponentially decaying test subspace.

## Meaning

The quotient is canonical and equivariant, while every embedding back into the complete carrier breaks translation symmetry:

```text
full carrier -> residual double     canonical and equivariant
residual double -> full carrier     contractible choice, never equivariant
```

Therefore the residual double is a quotient interface, not a symmetry-invariant subsystem of the full Green realization.

This is a useful rank-reset principle: effective primitives need not occur as literal subobjects of the structures from which they are derived. They may exist only as quotients, with any representative requiring a frame choice.

## Verification

The checker constructs four exact rational two-kernel sections and verifies every ordered comparison:

```text
python research/coherence/check_asymptotic_section_comparisons.py
```

Artifacts:

- `check_asymptotic_section_comparisons.py`
- `asymptotic-section-comparisons.v1.json`
