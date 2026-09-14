# Zero versus nonzero is central versus outer D4 incidence

The \(D_4\) resolution lattice gives a precise geometric test for whether the cusp class vanishes.

Order the exceptional curves by one central node followed by the three outer nodes. The Cartan matrix is

\[
C=
\begin{pmatrix}
2&-1&-1&-1\\
-1&2&0&0\\
-1&0&2&0\\
-1&0&0&2
\end{pmatrix}.
\]

A relative thimble meeting an exceptional component once represents the corresponding fundamental weight, namely the associated column of \(C^{-1}\), modulo the root lattice.

The calculation gives:

- the central fundamental weight is integral in the root basis and hence represents zero in \(D_4^\vee/D_4\);
- each outer fundamental weight is half-integral and has order two;
- the three outer weights are the three distinct nonzero classes;
- the sum of any two outer classes is the third.

Therefore

\[
\boxed{
\text{zero parity}\iff\text{central-node incidence},
}
\]

whereas

\[
\boxed{
\text{nonzero parity}\iff\text{single outer-node incidence}.
}
\]

This reframes the remaining question without parity coordinates. We do not need to calculate two fitted bits. We need to resolve the strict transform of the oriented physical thimble and see which exceptional component it meets.

If it meets an outer component, the class is automatically nonzero; site-exchange triality then forces the unique fixed outer class, corresponding to the diagonal matching

\[
(++,--)\mid(+-, -+).
\]

If it meets the central component, the class is zero despite the local width-two monodromy.

The next operation is thus the first explicit blow-up of the physical branch in

\[
XY=E q_2,
\]

retaining its orientation and strict transform.

Certificate:

- `research/voevodsky/checkers/d4_thimble_incidence_discriminant.py`;
- `research/voevodsky/results/d4_thimble_incidence.json`.
