# A Source Involution Freezes Port Polarization but Not the Safety Margin

The repair and drift ports require a source-bearing polarization. The minimal
algebraic source is an involution

\[
R^2=I
\]

whose \(+1\) and \(-1\) eigenspaces are the two typed port rays. In a labelled
basis,

\[
R=
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}.
\]

Let an admitted constructor act by

\[
A=
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}.
\]

Then

\[
[A,R]
=
\begin{pmatrix}
0&-2b\\
2c&0
\end{pmatrix}.
\]

Therefore

\[
[A,R]=0
\quad\Longleftrightarrow\quad
b=c=0.
\]

Commutation with the involution is exactly preservation of the ordered
repair–drift polarization.

## Exchange and mixing

Anticommutation gives

\[
\{A,R\}=0
\quad\Longleftrightarrow\quad
a=d=0.
\]

Such a constructor exchanges the two character spaces. A constructor with
both diagonal and off-diagonal parts neither preserves nor purely exchanges
the ports; it mixes their meanings.

With spectral projectors

\[
P_+=\frac{I+R}{2},
\qquad
P_-=\frac{I-R}{2},
\]

the leakage operator is

\[
L_R(A)=P_+AP_-+P_-AP_+.
\]

For the two-dimensional real packet,

\[
\|[A,R]\|_F^2
=4(b^2+c^2)
=4\|L_R(A)\|_F^2.
\]

The commutator is thus an exact quantitative mixing certificate, not merely a
binary test.

## Polarization preservation is insufficient

Suppose \(A\) preserves the rays and has positive gains:

\[
A=\operatorname{diag}(g_+,g_-).
\]

If the repair strength is transported by \(g_+\) and the drift strength by
\(g_-\), the invariant safety factor changes by

\[
M\longmapsto\frac{g_+}{g_-}M.
\]

The relative gain

\[
\gamma(A)=\frac{g_+}{g_-}
\]

is multiplicative:

\[
\gamma(AB)=\gamma(A)\gamma(B).
\]

Hence exact commutation with \(R\) does not prevent completion collapse.

The hostile sequence

\[
A_n=
\begin{pmatrix}
1/2&0\\
0&1
\end{pmatrix}
\]

satisfies \([A_n,R]=0\) at every stage, but after \(N\) stages

\[
M_N=2^{-N}M_0\longrightarrow0.
\]

The port labels survive perfectly while their positivity margin disappears.

## Completion-ready compiler

Two independent audits are required:

1. Polarization leakage:
   \[
   [A_X,R_X]=0
   \]
   exactly, or a cutoff-uniform leakage bound when approximation is genuinely
   source-authorized.

2. Relative-gain cocycle:
   \[
   M_X=M_0\prod_{n\le X}\gamma(A_n)
   \]
   must remain above \(1+\delta\), or the source must provide a normalization
   transport that cancels this cocycle.

The tensor-unit lesson reappears here. A canonical polarization chooses the
rays; it does not construct a norm-preserving transport between stages.

## Source-authority boundary

The Clark sheet involution or Fourier–Tate reflection may supply a candidate
\(R\), but the compiler cannot identify it. Grothendieck must derive:

- which character space is repair and which is drift;
- whether every admitted constructor commutes with or exchanges the
  involution;
- the relative gains on the two characters;
- the normalization cocycle through completion.

## Falsifiers

- A nonzero commutator for a claimed polarization-preserving constructor.
- Counting an exchanging constructor as preserving the ordered ports.
- Vanishing commutator with a relative-gain product tending to zero.
- Renormalizing each cutoff independently without a composition law.
- Inferring safety-margin preservation from sheet-character preservation.
- Choosing the involution after inspecting which ray repairs the sign.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to classify the exact structure needed to make the port
polarization canonical and stable.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. The involution gives a complete no-mixing theorem, while a separate
multiplicative gain cocycle controls completion stability.
