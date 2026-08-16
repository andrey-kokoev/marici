---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Q Is Invisible Through Regular Connection Order

## Correction to the frontier

The algebraic quartic cannot first be detected in the regular
\(E^0\) coefficient of the total-energy connection. Its first varying
signature occurs at connection order \(E^1\), equivalently at second
ordinary/Rees order in the coefficient object.

Therefore computing only the regular term after Entry 293 is insufficient
to locate \(\mathcal Q\). The next reduction must retain one additional
normal order.

## Exact expansion

Use
\[
p=xy,\qquad s=x+y,
\]
and the source-independent identity
\[
\mathcal Q(E)=-16p^2-8pE^2+8sE^3-5E^4.
\]
Away from soft support \(p=0\),
\[
\frac{-\mathcal Q(E)}{16p^2}
=
1+\frac{E^2}{2p}
-\frac{sE^3}{2p^2}
+\frac{5E^4}{16p^2}.
\]
Hence
\[
\log(-\mathcal Q)
=
\log(16p^2)
+\frac{E^2}{2p}
-\frac{sE^3}{2p^2}
+\frac{3E^4}{16p^2}
+O(E^5),
\]
and
\[
\boxed{
\partial_E\log(-\mathcal Q)
=
\frac Ep
-\frac{3s}{2p^2}E^2
+\frac{3}{4p^2}E^3
+O(E^4).
}
\]
For a square-root Kummer normalization,
\[
\boxed{
\frac12\partial_E\log(-\mathcal Q)
=
\frac{E}{2p}
-\frac{3s}{4p^2}E^2
+\frac{3}{8p^2}E^3
+O(E^4).
}
\]

In particular,
\[
\left.\partial_E\log(-\mathcal Q)\right|_{E=0}=0.
\]

## Consequence

A regular \(E^0\) connection calculation may be required to complete the
relative connection, but it cannot distinguish a genuine \(\mathcal Q\)
deformation from its generic boundary unit
\[
\mathcal Q(0)=-16p^2.
\]
The first discriminating datum is
\[
\boxed{
[E^1]\,\partial_E\log(-\mathcal Q)=\frac1p,
}
\]
or \(1/(2p)\) for the half-log Kummer character.

Thus the correct provenance test is not
\[
\text{compute through }E^0,
\]
but
\[
\boxed{
\text{compute the Rees-regularized connection through }E^1.
}
\]

## Architectural status

This is a normal-order constraint, not evidence that \(\mathcal Q\)
actually is a Kummer factor. It applies to every proposed realization whose
\(\mathcal Q\)-dependence is analytic or logarithmic at generic
\(E=0\).

It sharpens the alternatives:

1. an \(E^1/p\) term on the existing algebraic plane can realize the first
   \(\mathcal Q\) deformation as coefficient data;
2. absence of that term excludes a local logarithmic/Kummer home there;
3. a different \(E^1\) term may place \(\mathcal Q\) in a nontrivial
   extension rather than a rank-one factor;
4. none of these outcomes requires a new carrier stratum unless the frozen
   relative geometry cannot generate the term.

## Next finite falsifier

After proving the universal logarithmic residue, compute both the regular
\(E^0\) and linear \(E^1\) coefficients of the Rees-shifted primitive
column. Project the \(E^1\) term to
\[
\mathcal A_{--}=\langle e_6,v_{\rm alg}\rangle
\]
and test for the source-fixed \(1/p\) signature. Do not assign
\(\mathcal Q\) a home from the \(E^0\) term alone.
