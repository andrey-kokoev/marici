# The magnetic current cokernel forms a finite tower

Let \(M_{g,k,Q}\) be the ordinary target matrix in component \(Q=q+2\),
with pole depths \(0,2,\ldots,2k\). Let \(K_{g,a,q}\) be the current defect
created by branchwise inter-component raising at pole depth \(a\).

The exact census supports

\[
\dim
\frac{
\operatorname{im}M_{g,k,q+2}
+
\operatorname{span}\{K_{g,0,q},\ldots,K_{g,2k,q}\}
}{
\operatorname{im}M_{g,k,q+2}
}
=\min(k+1,D_{g,q}),
\]

where

\[
D_{g,q}
=q+4-
\min\left(
2,
\max\left(0,\left\lfloor\frac{q-g+2}{2}\right\rfloor\right)
\right)
+\epsilon_{g,q},
\]

and

\[
\epsilon_{g,q}=
\begin{cases}
1,&(g,q)=(2,5),\\
0,&\text{otherwise}.
\end{cases}
\]

The formula passed 1,716 exact rational rank comparisons over
\(2\le g\le12\), \(1\le q\le12\), and \(0\le k\le12\).

## Meaning

Each newly admitted pole depth initially contributes an independent current
class. The tower then saturates at a finite width determined by grade and
component.

The exceptional correction occurs at source component \((g,q)=(2,5)\),
whose target is \((g,Q)=(2,7)\). Thus the previously known grade-two
\(Q=7\) circuit reappears as an extra current-cokernel direction. Removing
the exceptional term gives the first falsifier at \((g,q,k)=(2,5,7)\).

This is presently a sharply falsified-and-repaired conjecture, not yet an
unbounded theorem. A proof should triangularize the current columns by their
upper endpoints and identify the final two relations responsible for
saturation. The \((2,7)\) circuit should account for the unique rank recovery.

Replay with: python research/strominger/checkers/magnetic_current_cokernel_tower_checks.py
