# Piecewise H2 recollement retains value and flux seam lines

## Maximal local graph domain

Let \(B\subset\mathbb R\) be finite and define the broken massive-operator domain

\[
\mathcal G_B=\bigoplus_{I\in\pi_0(\mathbb R\setminus B)}H^2(I).
\]

At each \(b\in B\), both one-sided values and one-sided derivatives exist. Define

\[
J_b^0(f)=f(b+)-f(b-),
\]

\[
J_b^1(f)=f'(b+)-f'(b-).
\]

These are respectively the value and flux jumps.

## Refinement sequence

If \(c\notin B\), the old domain embeds into \(\mathcal G_{B\cup\{c\}}\) as the simultaneous matching locus

\[
J_c^0(f)=J_c^1(f)=0.
\]

The two-channel jump map is surjective, giving

\[
0\to\mathcal G_B
\to\mathcal G_{B\cup\{c\}}
\xrightarrow{(J_c^0,J_c^1)}
\mathbb C_c^{\rm value}\oplus\mathbb C_c^{\rm flux}
\to0.
\]

Thus maximal second-order graph refinement adds rank two per seam, not rank one.

## Distributional operator

For a piecewise \(H^2\) function,

\[
\partial^2f
=f''_{\rm pw}
+\sum_bJ_b^1(f)\delta_b
+\sum_bJ_b^0(f)\delta_b'.
\]

Hence

\[
(1-\partial^2)f
=(1-\partial_{\rm pw}^2)f
-\sum_bJ_b^1(f)\delta_b
-\sum_bJ_b^0(f)\delta_b'.
\]

The value and flux seam lines are intrinsically distinguished by delta-prime and delta output channels.

## Green subdiagram

For \(k_x(t)=e^{-|t-x|}\),

\[
J_x^0(k_x)=0,
\qquad
J_x^1(k_x)=-2.
\]

Therefore

\[
(1-\partial^2)k_x=2\delta_x.
\]

The Green ind/pro realization lands canonically in the flux summand of the enlarged graph quotient. It has no value-jump component.

This supplies the missing typed comparison:

```text
Green innovation quotient
  -> flux seam line
  -> value/flux graph recollement quotient
```

The original broken \(H^1\) refinement embeds as the complementary value-jump story, but it cannot receive the Green innovation directly.

## Constructor consequence

A universal varying-fiber constructor for a second-order Green law must use the two-channel seam type

```text
Seam = ValueJump plus FluxJump
```

and declare which subprotocol selects either channel. Treating every seam as one untyped scalar conflates domain discontinuity with source insertion.

## Verification

```text
python research/coherence/check_value_flux_graph_recollement.py
```

The checker verifies the rank-two trace quotient and that the Green kernel has jump vector \((0,-2)\), producing delta coefficient \(2\) and zero delta-prime coefficient.

Artifacts:

- `check_value_flux_graph_recollement.py`
- `value-flux-graph-recollement.v1.json`
