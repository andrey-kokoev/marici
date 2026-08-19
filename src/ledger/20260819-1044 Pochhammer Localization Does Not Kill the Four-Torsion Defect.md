# 1044 — Pochhammer Localization Does Not Kill the Four-Torsion Defect

Entry 1043 originally stated that the finite quotient disappears after
Pochhammer localization. That statement was false and is withdrawn.

Let

\[
R=\mathbb Z[M^{\pm1},(M-1)^{-1}].
\]

Take

\[
\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)
\]

and specialize \(M\mapsto\alpha\). Both \(M\) and \(M-1=\alpha+1\) are
invertible, since

\[
\alpha(\alpha+1)=1.
\]

Hence there is a nonzero map

\[
\mathbb F_2[M^{\pm1},(M-1)^{-1}]
\longrightarrow\mathbb F_4,
\]

so \(R/2R\neq0\), and therefore \(R/4R\neq0\).

\[
\boxed{\text{Pochhammer localization neither canonically saturates nor
automatically kills Entry 1041's }\mathbb Z/4.}
\]

Entry 1043's type gate survives: primary regularization lands in localized
twisted homology and cannot serve as an unlocalized integral lift. Whether
the order-four quotient persists under a correctly typed comparison remains
open.

Next, construct the component augmentation over the universal monodromy
Laurent ring before specializing characters to signs, then compute its
determinantal support after Pochhammer localization.

Artifacts: research/benincasa/marici-gm/src/bin/string_six_point_pochhammer_four_torsion_survival.rs and research/benincasa/string-six-point-pochhammer-four-torsion-survival.json.

Epistemic event: ev-000000000663-642128a6-a93b-4236-aaf6-0e205245ff3b.
