# Value and flux seam lines have opposite reflection parity

## Trace transformation

Let reflection act by

\[
(Jf)(t)=f(-t).
\]

A seam at \(b\) moves to \(-b\). Since reflection exchanges the two sides,

\[
(Jf)(-b+)=f(b-),
\qquad
(Jf)(-b-)=f(b+).
\]

Therefore the value jump transforms as

\[
J_{-b}^0(Jf)=-J_b^0(f).
\]

For derivatives, the chain-rule sign cancels the side-exchange sign:

\[
J_{-b}^1(Jf)=J_b^1(f).
\]

Thus reflection acts on the two-channel seam type by

\[
\begin{pmatrix}J^0\\J^1\end{pmatrix}
\longmapsto
\begin{pmatrix}-1&0\\0&1\end{pmatrix}
\begin{pmatrix}J^0\\J^1\end{pmatrix}.
\]

Translation moves the seam location and preserves both channel coefficients.

## Distributional compatibility

The massive operator decomposition is

\[
(1-\partial^2)f
=(1-\partial_{\rm pw}^2)f
-J^1\delta_b-J^0\delta_b'.
\]

Under reflection, \(\delta_b\) is transported evenly to \(\delta_{-b}\), while \(\delta_b'\) is transported oddly. This agrees exactly with flux-even and value-odd seam parity.

## Green subrepresentation

Green kernel sections have zero value jump and nonzero flux jump. Hence the Green innovation line is the reflection-even summand

\[
\mathbb C_b^{\rm flux}
\subset
\mathbb C_b^{\rm value}\oplus\mathbb C_b^{\rm flux}.
\]

The value-jump line is a distinct reflection-odd summand. Symmetry therefore prevents an equivariant identification between the two one-dimensional quotient cells even before topology is considered.

## Constructor update

The varying-fiber graph protocol should type every seam as

```text
Seam(b) = ValueOdd(b) plus FluxEven(b)
```

with translation transporting \(b\) and reflection transporting \(b\mapsto-b\) while acting diagonally by \((-1,+1)\).

This two-channel parity is different from the incoming/outgoing hyperbolic double, where reflection swaps the two lines. The two rank-two carriers must not be identified merely because their dimensions agree.

## Verification

```text
python research/coherence/check_value_flux_seam_symmetry.py
```

The checker verifies the trace transformation and reflection involution on 100 exact rational trace quadruples.

Artifacts:

- `check_value_flux_seam_symmetry.py`
- `value-flux-seam-symmetry.v1.json`
