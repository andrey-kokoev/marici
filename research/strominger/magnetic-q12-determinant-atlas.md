# A one-row chart transition repairs the q=12 scalar failure

Companion to checkers/magnetic_q12_atlas_checks.py (7/7, exit 0) and
results/magnetic_q12_atlas.json.

For \((g,q)=(2,12)\), the primary nested maximal minor is nonzero through
\(k=4\) and vanishes from \(k=5\) onward. A neighboring chart repairs it by
the single target-row exchange

\[
1\longmapsto3.
\]

The replacement row sets remain nested through every tested cutoff
\(k\le20\). Their maximal minors are nonzero, while the primary minors remain
zero. Thus the two charts cover the full interval:

\[
\mathcal U_0:\ 0\le k\le4,\qquad
\mathcal U_1:\ 5\le k\le20.
\]

At the transition, the replacement determinant relative to its preceding
value is

\[
-\frac{809600}{3}\ne0.
\]

From the stable threshold \(k=8\) onward, the replacement determinant ratios
recover the uniform even-\(q\) character

\[
\left|\,\frac{D_k^{(1)}}{D_{k-1}^{(1)}}\,\right|
=
12\cdot2\cdot5\,
(2k)^{\overline2}(2k)^{\overline1}(2k+13).
\]

The sign difference is the fixed orientation of the new row chart.

This proves in finite range that the first scalar-minor failure is removable
by one local coordinate change. The underlying determinant line remains
nonzero, and the parity transport character resumes after the transient.

The next global object should encode several neighboring maximal minors as
homogeneous Plucker coordinates. Kernel birth occurs only when all coordinates
vanish simultaneously; a chart transition occurs when one coordinate
vanishes and another does not.

