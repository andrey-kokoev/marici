# Many-many labelled Koszul extension gate

Use the block differential

$$
D(s)=
\begin{pmatrix}
d_{\rm ret}(s)&0\\
\beta(s)&\tau(s)
\end{pmatrix}.
$$

The source equations require

$$
D(s)^2=0,
$$

which expands to

$$
 d_{\rm ret}(s)^2=0,
\qquad
\beta(s)d_{\rm ret}(s)+\tau(s)\beta_1(s)=0
$$

when the next labelled degree and comparison block `beta_1` are retained. The reduced two-block truncation has the special condition `tau beta=0`.

The labelled return operator is first realized as the block-diagonal Gram return `U^*U`; its radical descends labelwise before any common-history codiagonalization. A separate chain differential is required if an acyclic labelled return complex is desired. Its determinant contribution is then a holomorphic unit, preserving the Koszul determinant section.

The extension must also commute with reciprocal transport, prime restriction, and the four-block Hadamard projection.

Status: full square-zero conditions exposed; labelled return and comparison blocks remain to be supplied by source construction.
