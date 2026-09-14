# The v_alg form sees all four conductor marks equally

The failure of the naive \(D_4\)-to-source identification can be seen directly in the de Rham numerator.

In the normalized chart

\[
X_1=1,
\qquad E=u,
\qquad X_2=y,
\]

write \(X_2=r\) on the cusp \(E=0\). The source-supported vector

\[
v_{\rm alg}=(0,\alpha,\beta,\gamma)
\]

corresponds in the final scalar block to the numerator

\[
N_v=\alpha+\beta a^2+\gamma b^2,
\]

with

\[
\alpha=(1-r^2)r^2,
\qquad
\beta=2r^2,
\qquad
\gamma=-2r^2.
\]

Hence

\[
N_v=2r^2a^2-2r^2b^2-r^4+r^2.
\]

The four conductor marks are

\[
(a,b)=(\pm r,\pm1).
\]

At every one of them,

\[
N_v=r^2(r^2-1).
\]

Thus \(v_{\rm alg}\) is even in both sign coordinates and evaluates identically on all four \(D_4\) marks. No pointwise rational residue of this numerator can distinguish the three perfect matchings.

This explains the apparent symmetry mismatch:

- the \(D_4\) discriminant group remembers integral paths and pairings among four sign-labelled marks;
- the displayed de Rham frame sees only even polynomial values at those marks;
- consequently its visible site-exchange action is trivial.

The missing comparison cannot be recovered by another rational specialization or by evaluating \(v_{\rm alg}\) more accurately. It must retain oriented Betti transport between the marks. In particular, the desired map

\[
D_4^\vee/D_4\longrightarrow
\langle e_6,v_{\rm alg}\rangle/2
\]

is necessarily a period/intersection map, not point evaluation.

Certificate:

- `research/voevodsky/checkers/evaluate_valg_on_four_conductor_marks.py`;
- `research/voevodsky/results/valg_four_conductor_mark_evaluation.json`.
