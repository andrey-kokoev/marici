---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Rees Normalization Line Does Not Exhaust Q

## Narrow result

The source-forced correction
\[
\widehat\Omega_{111}=\Omega_{111}+\frac{e_6}{8E}
\]
has now been expanded through the first \(\mathcal Q\)-sensitive connection
order. Its contribution is
\[
\boxed{
\nabla_E\left(\frac{e_6}{8E}\right)
=
-\frac{e_6}{8E^2}
+\frac{e_6}{8sE}
+\left(\frac1{8s^2}-\frac1{4p}\right)e_6
+E\left(\frac1{8s^3}+\frac{3s}{8p^2}\right)e_6
+O(E^2),
}
\]
where \(s=x+y\) and \(p=xy\).

The linear coefficient is not the source quartic's half-log signature
\[
[E^1]\,\frac12\partial_E\log(-\mathcal Q)=\frac1{2p}.
\]
Therefore the forced \(e_6\) normalization term alone does not realize
\(\mathcal Q\). If \(\mathcal Q\) occurs in the Rees-shifted primitive
column, its missing contribution must come from the regularized raw relative
connection or from mixing with the other algebraic-kernel direction.

## Exact expansion

The invariant line has
\[
\nabla_Ee_6=c(E)e_6,
\qquad
c(E)=-\frac12\partial_E\log H,
\]
with
\[
H=(E-s)^2J,
\qquad
J=p^2+2pE^2-2sE^3+2E^4.
\]
Hence
\[
c(E)
=
\frac1{s-E}
-
\frac{2pE-3sE^2+4E^3}
{p^2+2pE^2-2sE^3+2E^4}.
\]
Coefficient extraction gives
\[
\boxed{
c(E)
=
\frac1s
+
\left(\frac1{s^2}-\frac2p\right)E
+
\left(\frac1{s^3}+\frac{3s}{p^2}\right)E^2
+O(E^3).
}
\]
Substitution into
\[
\nabla_E\left(\frac{e_6}{8E}\right)
=
-\frac{e_6}{8E^2}
+
\frac{c(E)}{8E}e_6
\]
proves the displayed result.

## Comparison with Q

Entry 295 established
\[
\frac12\partial_E\log(-\mathcal Q)
=
\frac{E}{2p}+O(E^2).
\]
The normalization-line coefficient
\[
\frac1{8s^3}+\frac{3s}{8p^2}
\]
is not \(1/(2p)\), nor a source-independent constant multiple of it on
generic \((x,y)\). This comparison is basis-specific only in the declared
source-normalized \(e_6\) line; it does not yet determine the projection of
the full Rees-shifted column.

## Classification

\[
\begin{array}{c|c}
E^{-2}\text{ cancellation}&\text{existing Rees gauge on }\langle e_6\rangle\\
E^{-1},E^0,E^1\text{ correction terms}&\text{Tate/Kummer coefficient data}\\
\mathcal Q\text{ from correction alone}&\text{excluded}\\
\mathcal Q\text{ in full primitive column}&\text{open}\\
\text{new carrier datum}&\text{none}
\end{array}
\]

This removes one candidate home without modifying the frozen carrier.

## Next finite falsifier

Compute the raw two-wall connection after subtracting the universal exact
logarithmic lift, through \(E^1\). Project its fixed part to
\[
\mathcal A_{--}=\langle e_6,v_{\rm alg}\rangle.
\]
Only the sum of that projection and the normalization contribution above may
be compared with \(\frac12d\log(-\mathcal Q)\). Failure of the frozen
relative reduction to generate the missing term is the next finite
falsifier.
