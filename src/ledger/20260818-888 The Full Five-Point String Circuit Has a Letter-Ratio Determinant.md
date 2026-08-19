# 888 — The Full Five-Point String Circuit Has a Letter-Ratio Determinant

## Record

Date: 2026-08-18

Status: exact two-by-two five-point circuit theorem. One row is the primary-source equation (5.4); the second is its source-labelled \(3\leftrightarrow4\) image. This proves a complete cycle-basis change, but not yet the cocycle intersection/period identity.

## Frozen bases

Use target cycles

\[
\mathcal D'=\{12354,12453\}
\]

and source basis

\[
\mathcal C=\{13254,14253\}.
\]

Set

\[
x_{ij}=\pi\alpha's_{ij}.
\]

Entry 886 gives the first circuit row. Applying the labelled involution

\[
3\leftrightarrow4
\]

simultaneously to the target, basis orderings, and kinematics gives the second. Therefore

\[
\boxed{
M_{\mathcal D'\leftarrow\mathcal C}
=
-\frac1{\sin x_{12}}
\begin{pmatrix}
\sin(x_{12}+x_{23})&\sin x_{24}\\
\sin x_{23}&\sin(x_{12}+x_{24})
\end{pmatrix}.
}
\]

No second row is fitted from numerical amplitudes.

## Determinant reduction

Direct expansion gives

\[
\det M
=
\frac{
\sin(x_{12}+x_{23})\sin(x_{12}+x_{24})
-\sin x_{23}\sin x_{24}
}{\sin^2x_{12}}.
\]

The numerator obeys

\[
\sin(a+b)\sin(a+c)-\sin b\sin c
=
\sin a\sin(a+b+c).
\]

Hence

\[
\boxed{
\det M
=
\frac{\sin(x_{12}+x_{23}+x_{24})}{\sin x_{12}}.
}
\]

Momentum conservation at leg \(2\) gives

\[
s_{12}+s_{23}+s_{24}=-s_{25},
\]

so equivalently

\[
\boxed{
\det M=-\frac{\sin(\pi\alpha's_{25})}
                  {\sin(\pi\alpha's_{12})}.
}
\]

The checker also constructs the inverse and verifies both products are the identity at a generic nonresonant point.

## Support classification

The determinant contains no mixed polynomial or new divisor. Its zero and pole are two existing Koba--Nielsen letters:

\[
\alpha's_{25}\in\mathbb Z,
\qquad
\alpha's_{12}\in\mathbb Z.
\]

Thus changing between these two complete cycle bases transports resonance within the frozen boundary-letter arrangement. The basis degenerates when the numerator letter vanishes and its chosen inverse chart degenerates when the denominator letter vanishes.

This sharpens Entry 885:

\[
\boxed{
\text{basis change may move displayed resonance,}
\quad
\text{but introduces no non-letter support.}
}
\]

## Field-theory limit

As \(\alpha'\to0\),

\[
\det M
\longrightarrow
\frac{s_{12}+s_{23}+s_{24}}{s_{12}}
=-\frac{s_{25}}{s_{12}},
\]

the determinant of the corresponding BCJ basis transformation.

## Epistemic update

At five points, the string circuit is now closed at matrix level by

\[
\text{labelled associahedral incidence}
+\text{Koba--Nielsen coefficients}
+\text{occurrence covariance}.
\]

There is still no evidence for a string-specific carrier primitive. What remains untested is whether the Parke--Taylor cocycle basis and its period matrices intertwine with this circuit using the same comparison calculus.

## Next falsifier

Freeze the two Parke--Taylor cocycles \(\operatorname{PT}(12345)\) and \(\operatorname{PT}(13245)\). Construct the period matrices for \(\mathcal C\) and \(\mathcal D'\), then verify

\[
P_{\mathcal D'}=M_{\mathcal D'\leftarrow\mathcal C}P_{\mathcal C}
\]

with source orientations. A failure requiring a non-letter correction would falsify the current circuit architecture.

## Certificate

Run:

```text
cargo run --quiet --bin string_five_point_full_circuit
```

Artifacts:

- `research/benincasa/marici-gm/src/bin/string_five_point_full_circuit.rs`
- `research/benincasa/string-five-point-full-circuit.json`

## Sources

- Sebastian Mizera, *Inverse of the String Theory KLT Kernel*, arXiv:1610.04230, Section 5, equation (5.4).
- Sebastian Mizera, *Combinatorics and Topology of Kawai--Lewellen--Tye Relations*, arXiv:1706.08527, Section 3.4.
