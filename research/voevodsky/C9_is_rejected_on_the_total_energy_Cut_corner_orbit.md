# C9 is rejected on the total-energy/Cut corner orbit

The Cut-nearby source basis is

\[
(g_{101},g_{110},g_{111}^{\sim}),
\]

with ambient coordinates

\[
(e_2,e_3,e_4,e_5,e_6,v_0).
\]

At the sign-labelled corner

\[
(a,b)=(\sigma_a y,\sigma_b x),
\qquad \sigma_a,\sigma_b\in\{\pm1\},
\]

the scaled integral columns are

\[
\begin{aligned}
g_{101}&\longmapsto2\sigma_a e_3,\\
g_{110}&\longmapsto2\sigma_b e_5,\\
g_{111}^{\sim}&\longmapsto
\sigma_a e_3+\sigma_b e_5+e_6.
\end{aligned}
\]

Projecting to the final algebraic plane \((e_6,v_0)\) gives

\[
\begin{aligned}
\operatorname{pr}(g_{101})&=(0,0),\\
\operatorname{pr}(g_{110})&=(0,0),\\
\operatorname{pr}(g_{111}^{\sim})&=(1,0).
\end{aligned}
\]

The result is identical at all four sign corners. The three cyclic sector profiles repeat the same support pattern. Sign and deck transport alter the \(e_3,e_5\) coefficients while preserving zero \(v_0\) support.

Hence C9 is rejected for the complete total-energy/Cut corner orbit: the mixed physical generators activate the \(e_3\) and \(e_5\) directions and contribute zero to \(v_{\rm alg}\).

The top generator continues to select the \(e_6\) direction at every corner.

The prescribed next step is now triggered: stack every sourced corner projection and compute its integral rank and Smith invariants as a rejection-first test of C10.

Certificate:

- `research/voevodsky/checkers/attack_C9_mixed_corner_packets.py`;
- `research/voevodsky/results/C9_mixed_corner_packet_attack.json`.
