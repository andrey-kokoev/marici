# Prior research moves the gate to ordered bulk polarization

Date: 2026-09-08

## Correction to the preceding frontier

The proposed identification of the endpoint Mellin metric with the resolved three-port metric is not required.  `reassembly-conjugation-closes-the-resolved-graph-under-moving-seam-transport.md` proves directly that

\[
\mathcal R_bT_{b\leftarrow a}
=T_{b\leftarrow a}^{\oplus3}\mathcal R_a
\]

and hence

\[
T_{b\leftarrow a}^*
\bigl((1+M_\Phi^2)I+B_b^*B_b\bigr)
T_{b\leftarrow a}
=
(1+M_\Phi^2)I+B_a^*B_a
\]

on the transported graph domain and after closure.  The resolved graph and endpoint observer are separately natural under the same seam transport; they need not share one metric.

## External flux already closed

`anti-diagonal-trace-already-closes-external-flux-not-the-resolved-bulk-polarization.md` records that the completed anti-diagonal zero-trace theorem already gives

\[
\mathfrak b_\partial^+
-
\mathfrak b_\partial^-
+
\mathfrak F_B
=0.
\]

Thus endpoint attachment, external five-cell flux, and their cancellation are not open.

## Actual first residual

Green integration by parts splits into endpoint and bulk terms.  Cancellation of the endpoint term does not determine the ordered bulk polarization

\[
\mathcal C_z(K)=\langle DK,zK\rangle.
\]

Its real part controls the oriented face difference

\[
\|x_+\|^2-\|x_-\|^2
=4\operatorname{Re}\langle DK,zK\rangle.
\]

The resolved positive Gram and endpoint packet retain only diagonal energies unless this ordered pairing is separately included.  A phase rotation of `DK` preserves those diagonal data while changing the bulk polarization.

The first remaining local theorem is therefore:

1. construct `C_z` on the resolved completed source domain;
2. prove compatibility with the direct-sum graph before codiagonalization;
3. prove both polarized radical conditions
   \[
   \mathcal C_z(r,v)=\mathcal C_z(v,r)=0
   \]
   for every radical vector of the even zero-trace bulk form;
4. identify its four endpoint matrix-unit shadows with the source Adams polarization.

## Updated closure chain

Closed by prior research:

- source selection of the resolved saturated order;
- three-port graph covariance under moving seam, including closure;
- endpoint naturality and rank-two faithfulness;
- anti-diagonal cancellation of typed external flux;
- real positive mixed resolved-tail entry;
- Pauli module reduction of the output audit.

Open:

- ordered cross-face bulk polarization;
- its radical descent;
- full analytic--arithmetic pushout closed range;
- prime-uniform coercivity.

## Evidence

- `research/nima/reassembly-conjugation-closes-the-resolved-graph-under-moving-seam-transport.md`
- `research/nima/anti-diagonal-trace-already-closes-external-flux-not-the-resolved-bulk-polarization.md`
- `research/nima/moving-seam-transport-and-complete-endpoint-pushforward-form-an-exact-metric-natural-transformation.md`
