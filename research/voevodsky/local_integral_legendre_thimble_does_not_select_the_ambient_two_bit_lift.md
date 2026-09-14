# The local integral Legendre thimble does not select the ambient two-bit lift

## Question

Construct the local integral Picard–Lefschetz thimble at the source-defined total-energy cusp and compute the parity of twice an elliptic coinvariant lift in the full rank-nine lattice.

## Local thimble construction

Let

\[
H_1(E_t;\mathbb Z)=\mathbb Z\langle\delta,\beta\rangle,
\qquad
\langle\delta,\beta\rangle=1,
\]

where \(\delta\) is the primitive vanishing cycle of the nodal Legendre fiber and \(\beta\) is a primitive transverse cycle. The local Lefschetz thimble \(\mathcal T_\delta\) is the relative two-chain swept out by \(\delta\) along a radial path from a nearby smooth fiber to the node. Its oriented boundary is

\[
\partial\mathcal T_\delta=\delta.
\]

The source-normalized total-energy monodromy is

\[
T_{\rm src}=
\begin{pmatrix}1&2\\0&1\end{pmatrix}
\]

in the column basis \((\delta,\beta)\). Hence

\[
T_{\rm src}(\delta)=\delta,
\qquad
T_{\rm src}(\beta)=\beta+2\delta.
\]

This is the square of the primitive Picard–Lefschetz transvection, reflecting the source-defined level-two cusp width. Therefore

\[
(T_{\rm src}-I)H_1=2\mathbb Z\delta
\]

and

\[
H_1/(T_{\rm src}-I)H_1
\cong
\mathbb Z\langle[\beta]\rangle
\oplus
(\mathbb Z/2)\langle[\delta]\rangle.
\]

The local integral thimble thus canonically identifies the elliptic torsion class as the boundary class \([\delta]\).

## Attempted ambient lift

Let

\[
\mathcal A_{--}=\mathbb Z\langle e_6,v_{\rm alg}\rangle
\]

be the source-supported algebraic plane. An ambient lift \(m\) of \([\delta]\) must obey

\[
2m=a e_6+bv_{\rm alg},
\qquad
(a,b)\in(\mathbb Z/2)^2.
\]

The four candidate extension lattices are therefore

\[
L_{a,b}
=
\frac{
\mathcal A_{--}\oplus\mathbb Z\langle m\rangle
}{
\langle2m-ae_6-bv_{\rm alg}\rangle
}.
\]

Every \(L_{a,b}\) has the same local elliptic quotient, the same primitive thimble boundary \(\delta\), the same width-two monodromy, and the same rational splitting. The four values

\[
(a,b)=(0,0),(1,0),(0,1),(1,1)
\]

remain distinct integrally.

## Why the requested parity is not computable locally

The local thimble determines \(\delta\) and the relation \(N\beta=2\delta\). It does not specify an integral lift of \(\delta\) through the primitive infinity-Gysin sequence. Equivalently, it supplies no chain-level intersection numbers with the two algebraic generators \(e_6\) and \(v_{\rm alg}\).

The known physical Cut pairing cannot fill this gap: prior work proves that it maps to zero in the elliptic coinvariants before taking the extension.

Consequently the parity of twice the ambient lift is not a function of the local Legendre thimble. Any asserted value would choose one of four extension lattices without source evidence.

## Exact missing constructor

To compute \((a,b)\), one needs a source-normalized relative chain

\[
\widetilde{\mathcal T}_\delta
\]

inside the degree-two del Pezzo complement whose Gysin boundary is \(\delta\), together with integral intersection pairings against duals to \(e_6\) and \(v_{\rm alg}\). Reducing those two pairings modulo two gives \((a,b)\).

No existing artifact supplies this chain-level embedding. The local thimble is constructed; the requested ambient parity remains underdetermined by exactly two bits.

## Disposition

Constructed: the primitive vanishing cycle, local Lefschetz thimble, width-two transvection, and elliptic coinvariant torsion generator.

Not computed: the parity of twice an ambient elliptic lift. Its value remains one of the four predeclared classes because the integral del Pezzo thimble embedding is absent.
