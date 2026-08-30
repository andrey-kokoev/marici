# 2875 — The Soft Translation Monodromy Is the Source Leray-Tube Pairing

## Local pushed-forward form

At the labelled soft normal \(t=q_{g1}/X_1=0\), the moving-fiber
pushforward has local form

\[
I(t)\,dt
=
L\frac{dt}{t}
+
\text{holomorphic terms}.
\]

The coefficient \(L\) is the \(q_{g1}\)-residue vanishing period, with the
physical positive \(a=y_{23}\) occurrence selected from the full marked
packet.

## Leray tube

Use the source orientation fixed by

\[
dq_{g1}=dy_{12}
\]

and by the oriented positive Cayley–Menger chain. For a positive Leray loop
\(\tau_\epsilon\) around \(t=0\),

\[
\int_{\tau_\epsilon}I(t)\,dt
=
2\pi iL.
\]

The value is independent of the tube radius. Reversing the residue orientation
reverses both sides.

## Translation monodromy

For the pointed primitive

\[
P(t)=\int_2^t I(s)\,ds,
\]

analytic continuation once around the same positive loop gives

\[
\Delta P=2\pi iL.
\]

Hence

\[
\Delta P
=
\left\langle
\text{source Leray tube},
\text{residue coefficient }L
\right\rangle.
\]

The affine translation of the logarithmic torsor is therefore not an
untyped integration constant. It is exactly the source-normalized tube
pairing.

## Classification

- Carrier: the existing labelled \(q_{g1}\) normal and Cut incidence.
- Coefficient object: the residue vanishing period \(L\).
- Physical readout: the source-oriented Leray tube with the physical
  occurrence covector.
- New carrier datum: none.

Together with Entries 2871 and 2873, this completes the moving-cycle,
regulator, and Leray-pairing gates for the soft logarithmic torsor.

## Durable artifacts

- `research/benincasa/check_soft_endpoint_leray_tube_pairing.py`
- `research/benincasa/soft-endpoint-leray-tube-pairing.json`

