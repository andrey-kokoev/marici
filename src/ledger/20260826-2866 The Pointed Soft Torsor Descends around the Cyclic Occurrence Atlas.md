# 2866 — The Pointed Soft Torsor Descends around the Cyclic Occurrence Atlas

## Cyclic chart packet

For each labelled soft normal \(X_i=0\), the source supplies the corresponding marked wall \(q_{gi}\) and normalized exceptional coordinate

\[
t_i=\frac{q_{gi}}{X_i}.
\]

The physical chain has

\[
t_i\in[0,2],
\]

with marked endpoint \(t_i=0\) and pointing endpoint \(t_i=2\).

The cyclic source action sends

\[
(X_i,q_{gi},t_i)
\longmapsto
(X_{i+1},q_{g,i+1},t_{i+1}).
\]

Because the numerator and normal are transported together, the normalized coordinate has transition unit one:

\[
t_i\longmapsto t_{i+1}.
\]

## Pointing naturality

The condition

\[
F_i(2)=0
\]

therefore transports to

\[
F_{i+1}(2)=0.
\]

The positive physical chamber and its occurrence covector

\[
V_{\rm phys}=(1,0)
\]

are preserved by cyclic relabelling. After three transitions, the chart, pointing, and orientation all return identically. The three-cycle has source-orientation sign \(+1\).

## Result

The chain-pointed logarithmic torsor passes cyclic occurrence naturality. No cyclic transition unit shifts its affine origin.

This establishes descent around the \(C_3\) occurrence atlas only. It does not establish:

- noncyclic residue-chart naturality;
- compatibility with the complete \(a\)-dependent relative cycle;
- regulator invariance;
- logarithmic residue/Leray-tube compatibility.

Those remain independent gates before the pointed finite part becomes a physical renormalized bulk readout.

## Durable artifacts

- research/benincasa/check_soft_endpoint_pointing_cyclic_naturality.py
- research/benincasa/soft-endpoint-pointing-cyclic-naturality.json

