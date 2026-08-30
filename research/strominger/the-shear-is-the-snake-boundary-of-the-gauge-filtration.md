# The Shear Is the Snake Boundary of the Gauge Filtration

## Result

Let \(V=\mathbb Z^4\), let \(G=\mathbb Z(1,1,1,1)\), and put \(Q=V/G\).
For the response operator \(\Delta=R-I\), simultaneous translation is fixed,
so \(\Delta|_G=0\). The invariant filtration gives a commuting diagram with
exact rows:

\[
\begin{array}{ccccccccc}
0&\to&G&\to&V&\to&Q&\to&0\\
 &&\downarrow 0&&\downarrow\Delta&&\downarrow\overline\Delta\\
0&\to&G&\to&V&\to&Q&\to&0.
\end{array}
\]

The snake lemma supplies the connecting morphism

\[
\partial:\ker\overline\Delta\longrightarrow
\operatorname{coker}(\Delta|_G)=G.
\]

Both source and target are infinite cyclic on their primitive generators. The
explicit computation gives

\[
\partial=\times505222245120.
\]

Thus the previously observed gauge shear is the canonical snake boundary of
the filtration.

## Exact sequence

Since the full response has only the gauge fixed line, the relevant part of
the snake sequence is

\[
0\longrightarrow G
\longrightarrow\ker\Delta
\longrightarrow\ker\overline\Delta
\xrightarrow{\ \partial\ }G
\longrightarrow\operatorname{coker}\Delta
\longrightarrow\operatorname{coker}\overline\Delta
\longrightarrow0.
\]

The first map \(G\to\ker\Delta\) is an isomorphism. Hence the map from the full
kernel to the extra quotient kernel is zero, and \(\partial\) is injective.
This proves invariantly that the extra quotient-fixed relationship has no
integral fixed lift.

## Torsion checksum

The Smith packets are

\[
\operatorname{coker}\Delta
\cong
\mathbb Z\oplus\mathbb Z/96\oplus\mathbb Z/1536
\oplus\mathbb Z/16167111843840,
\]

and

\[
\operatorname{coker}\overline\Delta
\cong
\mathbb Z\oplus\mathbb Z/384\oplus\mathbb Z/12288.
\]

Exactness predicts

\[
|\operatorname{Tor}\operatorname{coker}\Delta|
=505222245120\,
|\operatorname{Tor}\operatorname{coker}\overline\Delta|.
\]

The checker verifies this equality exactly. It is an independent arithmetic
checksum on the connecting morphism.

## Categorical meaning

The missing coherence datum is not another object or port. It is a boundary
map generated when kernels and cokernels are compared across the invariant
gauge filtration.

This explains why quotient coherence can coexist with failure of full
coherence: the quotient class is closed, but its connecting image is a nonzero
gauge class. Modulo \(n\), that boundary vanishes precisely when
\(n\mid505222245120\).

## Replay

```powershell
uv run python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py
```
