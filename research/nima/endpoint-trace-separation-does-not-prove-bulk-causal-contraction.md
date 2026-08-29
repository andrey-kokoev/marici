# Endpoint trace separation does not prove bulk causal contraction

## Canonical even energy

The closed twisted history pair

\[
\mathcal H_-\oplus\mathcal H_+
\]

already carries a positive graph energy

\[
S=
\begin{pmatrix}
S_-&0\\
0&S_+
\end{pmatrix},
\]

where each diagonal form is the transported relative Sobolev graph norm. On reduced support, \(S>0\) by construction.

This supplies the even auxiliary block without fitting an additional energy.

## General reciprocal-odd coupling

A Hermitian reciprocal-odd perturbation has the form

\[
iT=
\begin{pmatrix}
0&iJ\\
-iJ^{*}&0
\end{pmatrix}.
\]

The complete auxiliary form

\[
D=S+iT
\]

is positive precisely when the normalized coupling

\[
K
=
S_-^{-1/2}J S_+^{-1/2}
\]

satisfies

\[
\|K\|\le1,
\]

and it is strictly coercive when

\[
\|K\|<1.
\]

Thus the local auxiliary margin is

\[
\delta_{\mathrm{aux}}
=
1-\|K\|.
\]

## What the exact trace columns prove

The theta trace vectors

\[
\left(\frac12,\frac12\right),
\qquad
\left(\frac14,-\frac14\right)
\]

prove exact rank-two endpoint observability. They determine the action of any proposed \(J\) only after compression to the two-dimensional trace quotient.

A strict contraction of the compressed matrix does not imply

\[
\|S_-^{-1/2}JS_+^{-1/2}\|<1
\]

on the full history graph. A hidden bulk direction may saturate or exceed the even energy while all endpoint traces remain correct.

Conversely, the endpoint odd/even ratio \(1/2\) is not itself the bulk contraction constant. Treating it as \(\|K\|=1/2\) would repeat scalar-shadow reasoning.

## Minimal hostile

Let the history space split as

\[
mathcal H_{\mathrm{trace}}
\oplus
\mathcal H_{\mathrm{dark}}.
\]

Choose \(K\) to agree with the desired factor \(1/2\) on the trace plane but act isometrically on the dark subspace. Then every Wronskian and Euler endpoint normalization passes, while

\[
\|K\|=1
\]

and the auxiliary form loses strict coercivity.

## Exact missing constructor

The source must now define the bulk odd operator \(J\), not merely its endpoint compression. The theorem must establish:

1. \(J\) comes from causal versus anti-causal twisted history;
2. it acts on the common reduced graph domain;
3. reflection gives the required odd character;
4. it intertwines valuation labels;
5. its normalized bulk norm is strictly below one;
6. its trace compression equals the fixed odd Wronskian value.

Until \(J\) is extracted, the positive even form is available but the oriented auxiliary energy is not.

## Consequence

The earliest missing arrow has contracted to one operator:

\[
J:
\mathcal H_+
\longrightarrow
\mathcal H_-.
\]

All current finite trace data constrain its boundary symbol, but do not determine or bound its interior action.
