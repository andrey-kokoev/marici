# 3949 — The Rank Jump Lies on a Smooth Orthogonality Locus

## Correction

Entry 3946 is retracted as a carrier-support classification.

Write

\[
F(t)=x^2t^4-h t^2+y^2,
\qquad h=x^2+y^2-z^2.
\]

The branch-collision discriminant is

\[
h^2-4x^2y^2,
\]

not (h). At generic nonsoft (h=0), this discriminant is nonzero. The locus is the orthogonality condition encoded by the vanishing cross coefficient; the elliptic boundary remains smooth.

## Replication

The rank pattern from Entry 3946 persists at two distinct rational points on (h=0):

\[
(3,4,5),\qquad(5,12,13),
\]

and at both primes. In the tested direction,

\[
(\dim R_0,\dim R_{\rm lift},\dim R_{\rm obs},
\operatorname{rank}\beta,\operatorname{rank}(\beta,{\rm mixed}))
=(3,1,2,0,1).
\]

Thus (h=0) is a genuine rank locus of the chosen polynomial relation module, but not an intrinsic branch or Carrier discriminant.

## Inversion-chart gate

Under the source-defined inversion (x\leftrightarrow y), (a\leftrightarrow b), the points ((3,4,5)) and ((4,3,5)) carry the same rank packet. Across both directions and primes, all eight signatures equal ((3,1,2,0,1)).

Thus the rank jump survives the first source-equivalent presentation change. This is signature covariance only; it does not yet identify or transport the individual lifted, obstructed, or mixed classes.

## Class-level transport gate

The naive class map obtained by swapping polynomial monomials

\[
a^i b^j\longmapsto a^j b^i
\]

does not transport the relation subspaces. For both derivative routes

\[
x\longrightarrow y,
\qquad
y\longrightarrow x,
\]

the exact finite-field comparison gives

\[
\begin{array}{c|ccc}
&\operatorname{rank}S&\operatorname{rank}T&
\operatorname{rank}(S+T)\\
\hline
\text{base relations}&3&3&4\\
\text{liftable relations}&1&1&2\\
\text{obstructed relations}&2&2&4
\end{array}
\]

at prime (32009). Hence none of the three source and target subspaces agree under the bare monomial involution.

The source polynomials and both parameter derivatives were then checked directly. They are exactly equivariant under

\[
(x,y;a,b)\longmapsto(y,x;b,a),
\]

with marked-pole permutation

\[
(g_1,g_2,g_3,g_{23},g_{31})
\longmapsto
(g_2,g_1,g_3,g_{31},g_{23}).
\]

The denominator product is invariant and the residue Jacobian contributes only one common sign, so neither can repair a relation subspace.

A direct comparison of independently serialized relation packets initially appeared to leave only the liftable line natural. That diagnosis is retracted after transporting the defining exact presentation itself.

Using the exact truncation of the bidual reducer, the two presentations have

\[
18240
\]

columns and exact-row rank

\[
11521.
\]

Every source pivot row reduces to zero in the target and conversely. No transported term leaves the truncation. All (36) low generators also agree in both quotient directions after the quotient coordinate transition is retained.

Therefore the finite exact reducer is source-natural. The earlier relation-vector mismatch is a post-reduction frame or serialization artifact: it compared independently chosen quotient coordinates without the induced quotient transition. It is not evidence of chart memory, truncation failure, or cosmological support.

## Mixed-class falsifier

Transport through the certified quotient transition gives a sharper result. The Bockstein image is zero in both charts and transports trivially. The extracted mixed line does not:

\[
\operatorname{rank}M_{(3,4,5)}=1,
\qquad
\operatorname{rank}M_{(4,3,5)}=2,
\]

for the paired (x,y) directions, while the transported and target full spans have union rank (3). Direction by direction, each rank-one transported line and target line also span rank (2).

This occurs even after retaining the full ambient representative. The low projection is additionally lossy: each mixed representative has (71) omitted ambient coefficients, and its transported low image develops four coordinates outside the target low quotient.

Thus the rank-one mixed object extracted by the sequential relation solver is not source-natural. It depends on the chosen solver or quotient section. The (h=0) packet does not define an intrinsic Bockstein-horizontal coefficient class.

## Updated conclusion

The exact Carrier-side relative presentation is natural on the smooth orthogonality locus. The proposed coefficient class is not. Therefore this branch is a presentation artifact unless a separately derived functorial class replaces the sequential solver output. The present rank jump cannot support a new cosmological coefficient or physical readout.

## Narrow conclusion

The rank jump is currently presentation/coefficient structure on a smooth physical locus. It cannot be assigned a Gysin costalk merely because a coefficient vanishes. The correct next test is whether the full source-normalized relative module has the same rank jump or whether it disappears after changing the polynomial presentation.

If it disappears, (h=0) is chart memory. If it persists invariantly without period singularity, it is a coefficient-filtration locus. Only independently derived physical support could promote it further.

Artifacts:

- `research/benincasa/checkers/check_rank26_orthogonality_inversion_signature.py`;
- `research/benincasa/checkers/check_rank26_orthogonality_inversion_class_transport.py`.
- `research/benincasa/checkers/check_rank26_orthogonality_ambient_row_transport.py`.

Ledger sequence claim: `seqclaim-22c706a2ae7f91d7746a779d`.
