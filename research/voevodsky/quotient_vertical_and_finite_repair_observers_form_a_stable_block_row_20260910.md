# Quotient, vertical, and finite-repair observers form a stable block row

## Question

When does an observer on a descended quotient combine with a vertical bulk observer and finite-defect repair to reconstruct the original Hilbert or graph-domain source stably?

## Claim boundary

The theorem below applies to bounded maps between Hilbert spaces, including graph Hilbert spaces of closed operators. It assumes a closed vertical subspace and a descended channel that is bounded below in the quotient norm. It does not require the vertical observer to preserve the orthogonal complement, but the quantitative proof uses the Hilbert projection onto the closed vertical subspace. No Banach-space extension is asserted.

## Setup

Let \(X\) be a Hilbert space and \(V\subseteq X\) a closed subspace. Let

\[
p:X\longrightarrow X/V
\]

be the quotient map, with

\[
\|p x\|_{X/V}=\operatorname{dist}(x,V).
\]

Let

\[
B:X/V\to Y,
\qquad
E:X\to Z
\]

be bounded. Think of \(Bp\) as the descended observer and \(E\) as the assembled vertical observer, possibly \(E=(D,K)^\top\).

Assume constants \(a,d>0\) such that

\[
\|Bpx\|\ge a\,\operatorname{dist}(x,V)
\quad (x\in X)
\]

and

\[
\|Ev\|\ge d\|v\|
\quad (v\in V).
\]

No invariance condition \(E(V^\perp)\subseteq E(V)^\perp\) is imposed.

## The block-row theorem

Define

\[
T:X\longrightarrow Y\oplus Z,
\qquad
Tx=(Bpx,Ex).
\]

Then \(T\) is bounded below. More explicitly, with

\[
M=\|E\|,
\qquad
\kappa=\frac{d+M}{a},
\]

we have

\[
\|Tx\|
\ge
\frac{d}{\sqrt{1+\kappa^2}}\|x\|.
\]

### Proof

Let \(P_V\) be the orthogonal projection onto \(V\), and write

\[
v=P_Vx,
\qquad
h=x-v.
\]

This decomposition is used only for the estimate; neither \(B\) nor \(E\) is assumed block diagonal. Since

\[
\|h\|=\operatorname{dist}(x,V),
\]

the quotient estimate gives

\[
\|h\|\le a^{-1}\|Bpx\|.
\]

The vertical estimate and boundedness of \(E\) give

\[
\begin{aligned}
d\|x\|
&\le d\|v\|+d\|h\|\\
&\le \|Ev\|+d\|h\|\\
&\le \|Ex\|+(d+M)\|h\|\\
&\le \|Ex\|+\kappa\|Bpx\|.
\end{aligned}
\]

Cauchy--Schwarz in \(\mathbb R^2\) yields

\[
\|Ex\|+\kappa\|Bpx\|
\le
\sqrt{1+\kappa^2}\,
\sqrt{\|Ex\|^2+\|Bpx\|^2}.
\]

This proves the stated lower bound.

## Converse on the vertical subspace

If \(T=(Bp,E)^\top\) is bounded below by \(\delta>0\), then for every \(v\in V\),

\[
pv=0
\]

and hence

\[
\|Ev\|=\|Tv\|\ge\delta\|v\|.
\]

Thus vertical stability is necessary, not merely sufficient. The descended channel cannot contribute on directions it erases.

## Essential observer plus finite repair

Now write

\[
E=\binom DK,
\]

with \(D:X\to Z_D\) and \(K:X\to Z_K\).

Assume the restriction

\[
D_V=D|_V:V\to Z_D
\]

has closed range and finite-dimensional kernel

\[
N=\ker D_V.
\]

Assume also that

\[
K|_N:N\to Z_K
\]

is injective.

Then

\[
E|_V=\binom{D_V}{K|_V}
\]

is bounded below.

### Proof of finite repair

Let \(V=N\oplus N^\perp\). Closed range of \(D_V\) gives \(c>0\) with

\[
\|D_Vw\|\ge c\|w\|
\quad (w\in N^\perp).
\]

Since \(N\) is finite dimensional and \(K|_N\) is injective, there is \(b>0\) with

\[
\|Kn\|\ge b\|n\|
\quad(n\in N).
\]

If \(E|_V\) were not bounded below, there would be unit vectors

\[
v_j=n_j+w_j
\]

with \(D_Vv_j\to0\) and \(Kv_j\to0\). Then \(w_j\to0\). Compactness of the unit sphere in \(N\) supplies a subsequence \(n_j\to n\in N\) with \(\|n\|=1\). Continuity gives \(Kn=0\), contradicting injectivity of \(K|_N\).

Combining this result with the block-row theorem proves that

\[
x\longmapsto(Bpx,Dx,Kx)
\]

is bounded below on \(X\).

## Calkin formulation

Suppose \(V\) is infinite dimensional. If

\[
q_V(D_V^*D_V)
\]

is positive and invertible in the Calkin algebra of \(V\), then \(D_V\) is upper semi-Fredholm: its range is closed and \(N=\ker D_V\) is finite dimensional. Any bounded \(K\) injective on \(N\) supplies the finite repair above.

Conversely, if \((Bp,D,K)^\top\) is bounded below and \(K|_V\) is compact, then restriction to \(V\) gives

\[
D_V^*D_V+K_V^*K_V\ge\delta^2I_V.
\]

Passing to the Calkin algebra removes the compact term:

\[
q_V(D_V^*D_V)\ge\delta^2q_V(I_V).
\]

Therefore the essential vertical margin must come from \(D\), not from \(Bp\) or compact repair.

## Four omission tests

### Omit quotient control

Take \(X=V\oplus H\), let \(E\) control \(V\), and set \(B=0\). Unit vectors in \(H\) are invisible. Vertical stability alone does not reconstruct the source.

### Omit the essential vertical observer

Let \(V\) be infinite dimensional and let \(D=0\), while \(K|_V\) is compact. No compact map is bounded below on an infinite-dimensional subspace. Quotient control plus compact repair is insufficient.

### Omit finite repair

Let \(D_V\) be upper semi-Fredholm with nonzero kernel \(N\), and set \(K=0\). Every nonzero vector of \(N\) lies in the kernel of the full row because \(Bp\) vanishes on \(V\).

### Omit separation of objectives

The map \(Bp\) may be a stable embedding of \(X/V\) while having kernel \(V\). It succeeds for \(\mathsf{Quotient}(X/V)\) and fails for \(\mathsf{Source}(X)\). This is not a contradiction; it is a change of reconstruction objective.

## Green--Real radial specialization

Take \(X\) to be the graph Hilbert space of a closed radial differential operator. Let \(V\) denote bulk variations erased by the declared descended or boundary channel. Then:

- \(Bp\) is the channel proved stable on the descended quotient;
- a reciprocal-even, Real, thick multiplier \(D_w^+\) supplies the essential vertical margin;
- the compact analytic channel \(A\) may serve as \(K\) only after its injectivity on the finite residual kernel is proved;
- Green wall maps \(W_u\), Real maps \(J_u\), and phase gauges transport the construction but contribute no lower margin merely by being unitary;
- finite holonomy quadratures belong to the moduli factor and are not part of this bulk theorem.

This specialization preserves the distinction between `green_compatible_observer` and unitary `green_comparison_cell`.

## Constructor-role consequences

The theorem makes the role ordering operational:

1. descent identifies \(V\);
2. quotient observation controls \(X/V\);
3. essential observation controls \(V\) modulo finite defect;
4. finite repair detects the exact kernel left by the essential observer;
5. only then does the assembled row certify source reconstruction.

A scalar response comparison before these gates cannot establish the theorem.

## Disposition

The Phase 2 source-reconstruction theorem is proved for Hilbert and graph Hilbert sources. It does not assume block-diagonal observers, but it does use the Hilbert projection onto the closed vertical subspace to derive a quantitative constant. The Calkin converse shows that compact repair cannot replace vertical essential observation. The unresolved extension is to non-Hilbert quotient geometries, where a uniformly bounded choice of representatives may fail.
