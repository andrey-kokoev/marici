# Consumer-Relative Phase-Port Compiler

Let (w\in\mathbf C^m) be a frozen vector of continuous invariant features,
such as edge magnitudes and unnormalized cycle products. Let the declared
downstream consumers be

\[
y=Lw,
\qquad
L\in\mathbf C^{r\times m},
\]

and let a selected family of source-authorized ports have observation matrix

\[
x=R_Sw.
\]

The consumers factor through the selected ports exactly when

\[
\ker R_S\subseteq\ker L.
\]

In finite dimension this is equivalent to

\[
\operatorname{row}(L)\subseteq\operatorname{row}(R_S),
\]

or to the existence of a decoder (D) satisfying

\[
L=DR_S.
\]

This is the precise consumer-relative replacement for full orbit
reconstruction.

## Two different minima

If arbitrary linear mixtures of invariant features are authorized, the
information-theoretic minimum is

\[
\operatorname{rank}L.
\]

A row basis of (L) attains it. But this statement supplies no source
authority for those mixtures.

For a frozen candidate vocabulary

\[
\mathcal R=\{r_1,\ldots,r_k\},
\]

the actual compiler must solve

\[
\min |S|
\quad\text{subject to}\quad
\operatorname{row}(L)
\subseteq
\operatorname{span}\{r_i:i\in S\}.
\]

Its optimum can exceed \(\operatorname{rank}L\). Rank is therefore a lower
bound, not an executable port count.

## Exact separation witness

Take four invariant coordinates and consumers

\[
L=
\begin{pmatrix}
1&1&0&0\\
0&1&1&0
\end{pmatrix}.
\]

The consumer rank is two. If the only authorized ports are individual
coordinates, all of (w_1,w_2,w_3) are required, so the minimum is three.
For example, omitting (w_2) leaves the invisible state

\[
v=(0,1,0,0)^T,
\qquad
Lv=(1,1)^T.
\]

If the two consumer mixtures themselves are independently authorized as
ports, the minimum drops to two. The algebra did not create this repair; the
expanded source vocabulary did.

## Continuity gate

The row-space theorem is pointwise and finite. For a pro-Gram completion,
every selected row and decoder must also obey a cutoff-independent domination
bound. A sequence of exact decoders (D_N) with

\[
\|D_N\|\to\infty
\]

does not give a continuous completed compiler. Thus the complete verdict has
three gates:

1. source authorization of every selected port;
2. finite factorization (L_N=D_NR_{S,N});
3. one fixed subset (S) and uniformly bounded decoder/domination constants.

Full feature reconstruction is sufficient but often unnecessarily costly.
Consumer-relative compilation asks only that the invisible subspace of the
ports lie inside the invisible subspace of every declared consumer.

## Support strata

If admissible supports vary, the same fixed selected family must satisfy the
kernel condition on every admitted stratum. A subset optimal on the generic
support can fail after some cycle products vanish. Allowing a different
subset on each stratum creates a switching compiler and requires an
independently observable support-type signal.

## Authority boundary and falsifiers

The theorem optimizes only over a frozen authorized port list. It neither
invents theta currents nor declares every invariant feature operative.

Falsifiers are:

- reporting \(\operatorname{rank}L\) as executable cost without authorized
  row mixtures;
- checking only that (R_S) has high rank rather than that its row space
  contains the consumer rows;
- using cutoff-dependent subsets without a typed switching signal;
- accepting exact finite decoders whose norms diverge;
- adding an unauthorized mixture because it attains the rank lower bound;
- compiling nonlinear consumers through this linear theorem.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to turn consumer-relative compression into a decidable
finite kernel theorem.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Rank gives the abstract minimum, while the authorized vocabulary and
uniform decoder bound determine the executable minimum.
