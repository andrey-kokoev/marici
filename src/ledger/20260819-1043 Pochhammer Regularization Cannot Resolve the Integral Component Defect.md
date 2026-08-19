# 1043 — Pochhammer Regularization Cannot Resolve the Integral Component Defect

Section 4.1 of Mizera, *Combinatorics and Topology of
Kawai–Lewellen–Tye Relations* (arXiv:1706.08527), defines

\[
\operatorname{reg}\overrightarrow{(0,1)}
=
\frac{S(\varepsilon,0)}{e^{2\pi i s}-1}
+\overrightarrow{(\varepsilon,1-\varepsilon)}
-\frac{S(1-\varepsilon,1)}{e^{2\pi i t}-1}.
\]

Thus each boundary circle carries \((M_F-1)^{-1}\). In

\[
R_{\mathbb Z}=\mathbb Z[M_F^{\pm1}],
\]

\(M_F-1\) is not a unit: evaluating a hypothetical identity
\((M_F-1)f=1\) at \(M_F=1\) gives \(0=1\).

Therefore regularization is defined only over

\[
R_{\mathbb Z}[(M_F-1)^{-1}],
\]

and does not supply integral columns in Entry 1041's constant component
lattice.

\[
\boxed{\text{Pochhammer regularization cannot canonically saturate the
Entry 1041 quotient over the unlocalized integral group ring.}}
\]

This does not prove that the \(\mathbb Z/4\) is physical torsion.
Localization at \(M_F-1\) also does not automatically kill it; Entry 1044
provides the correction certificate.

Artifacts: research/benincasa/marici-gm/src/bin/string_six_point_pochhammer_integral_type_gate.rs and research/benincasa/string-six-point-pochhammer-integral-type-gate.json.

Epistemic event: ev-000000000661-0cbaf05e-6141-46be-a717-360acaf3b9e2.
