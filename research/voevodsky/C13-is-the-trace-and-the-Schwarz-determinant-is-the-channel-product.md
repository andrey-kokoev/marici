# Conditional ansatz: C13 as trace and the Schwarz determinant as channel product

> **Correction.** The source transcript defines \(C_{13}\) as an independent positive mesh charge, not as a Schwarz trace. Everything below is an abstract candidate dictionary requiring a new source comparison theorem. See `research/voevodsky/erratum-kinematic-C13-is-a-mesh-charge-not-a-proved-Schwarz-trace.md`.

The candidate four-point dictionary does not identify \(C_{13}\) with the Schwarz determinant.

Let

\[
S=
\begin{pmatrix}
a&b\\
\overline b&c
\end{pmatrix}
\]

be the primitive/prime-prime observation square. Define its two spectral channels

\[
X_{13}
=
\frac{a+c+\sqrt{(a-c)^2+4|b|^2}}2,
\]

\[
X_{24}
=
\frac{a+c-\sqrt{(a-c)^2+4|b|^2}}2.
\]

Then

\[
\boxed{C_{13}=\operatorname{tr}S=a+c}
\]

gives exactly the affine four-point relation

\[
X_{13}+X_{24}=C_{13}.
\]

The Schwarz determinant is instead

\[
\boxed{
\det S=X_{13}X_{24}=ac-|b|^2.
}
\]

Therefore

\[
S\succeq0
\iff
X_{13}\geq0
\text{ and }
X_{24}\geq0.
\]

This is algebraically compatible with the shape of the four-point positive geometry: positive channel coordinates inside an affine line of fixed positive source \(C_{13}\). No source identification is presently proved.

## Revised source gate

The desired comparison is now:

1. identify the positive source constant with the trace reading;
2. identify the two positive-geometry channels with the two spectral channels of the observation square;
3. preserve this identification under forward/reverse transport.

If these identifications are source-derived, positivity of the four-point region forces rung-four Schwarz positivity.

The remaining difficulty is the spectral-channel map. It is nonlinear and contains the cross reading \(b\). Defining it from the eigenvalues of \(S\) after the fact is algebraically valid but not source-authorized. The source geometry must independently produce \(X_{13}\) and \(X_{24}\), after which comparison with the trace and determinant can be tested.

## Verification

```text
python research/voevodsky/checkers/check_C13_trace_channel_product_dictionary.py
```

Artifacts:

- `research/voevodsky/checkers/check_C13_trace_channel_product_dictionary.py`
- `research/voevodsky/results/C13_trace_channel_product_dictionary.json`
