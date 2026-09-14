# Reversal-parity folding propagates negativity to lower dimension

## Descent lemma

Let \(G\) be a Hermitian rank-\(n\) observation matrix and let \(J\) be the reversal involution. Assume

\[
JG=GJ.
\]

Every vector splits orthogonally into reversal parity components

\[
v=v_++v_-,
\qquad
v_\pm=\frac{v\pm Jv}{2}.
\]

Because \(G\) preserves the two parity sectors,

\[
v^*Gv
=
v_+^*Gv_++v_-^*Gv_-.
\]

Therefore, if \(v^*Gv<0\), at least one parity component is negative.

The even and odd sectors have dimensions

\[
\left\lceil\frac n2\right\rceil
\quad\text{and}\quad
\left\lfloor\frac n2\right\rfloor.
\]

Thus reversal sends every negative observation to a negative folded observation of at most half-scale dimension.

## Why this is stronger than deletion

A reversal-invariant rank-three hostile can have every ordinary rank-two principal face positive while its reversal-even rank-two compression is negative.

For

\[
G=
\begin{pmatrix}
1&9/10&-9/10\\
9/10&1&9/10\\
-9/10&9/10&1
\end{pmatrix},
\]

every deleted-coordinate rank-two determinant is \(19/100>0\). Yet folding by

\[
F(x,y)=(x,y,x)
\]

gives

\[
F^*GF
=
\begin{pmatrix}
1/5&9/5\\
9/5&1
\end{pmatrix},
\]

whose determinant is \(-76/25\).

So reverse-plane folding really does propagate negativity toward lower dimension even when ordinary restriction cannot.

## The remaining incidence requirement

This does not yet produce a contradiction. The folded parity observation is a new compression, not automatically the same object as the previously admitted rung-\(\lceil n/2\rceil\) forward observation.

The decisive missing equation is a source-derived identification

\[
F_n^*G_nF_n
=
T_n^*G_{\lceil n/2\rceil}T_n

after the declared scale and channel transport.
\]

If such a positivity-preserving incidence map exists for both parity sectors, then any negative rank-\(n\) witness descends to a negative earlier-rung witness. Iterating parity folding reaches rank one. A positive base rung would then make negativity impossible.

## Proposed RH mechanism

The desired proof structure is:

1. assume a negative finite Weil observation;
2. split it by reversal parity;
3. retain a negative parity component;
4. identify its folded compression with an earlier forward-plane observation;
5. iterate until rank one;
6. contradict base positivity.

The algebraic descent in steps 2–3 is proved. Step 4 is the substantive arithmetic incidence theorem still required. Reversal symmetry alone does not imply it.

## Verification

```text
python research/voevodsky/checkers/check_reversal_parity_negative_descent.py
```

Artifacts:

- `research/voevodsky/checkers/check_reversal_parity_negative_descent.py`
- `research/voevodsky/results/reversal_parity_negative_descent.json`
