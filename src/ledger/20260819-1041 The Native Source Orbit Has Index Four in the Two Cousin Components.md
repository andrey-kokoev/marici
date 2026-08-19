# 1041 — The Native Source Orbit Has Index Four in the Two Cousin Components

Entry 1030 orders the six source occurrences as

\[
(P_1Q_2,\ P_2Q_2,\ P_3Q_4,\ P_4Q_4,\ P_2Q_1,\ P_4Q_3).
\]

Entry 1037 puts occurrences \(0,1,4\) in component \(h_L\), and occurrences
\(2,3,5\) in component \(h_R\). Applying this augmentation to Entry 945's
primitive two-seed \((\mathbb Z/2)^2\)-orbit gives

\[
A_{H_0}=
\begin{pmatrix}
2&0&0&2&1&-1&-1&1\\
2&0&0&-2&3&1&1&-1
\end{pmatrix}.
\]

The gcd of its entries is \(1\), and the gcd of its \(2\times2\) minors is
\(4\). Therefore

\[
\boxed{\operatorname{SNF}(A_{H_0})=(1,4)},
\qquad
\operatorname{coker}(A_{H_0})\cong\mathbb Z/4.
\]

Both components are reached over \(\mathbb Q\), but the native orbit has
index four in their integral augmentation lattice. This is a
source-presentation statement, not a physical torsion theorem.

Artifacts: research/benincasa/marici-gm/src/bin/string_six_point_loaded_cousin_integral_h0.rs and research/benincasa/string-six-point-loaded-cousin-integral-h0.json.

Epistemic event: ev-000000000660-53aa5647-523f-4831-8b9a-1ee7058e4c36.
