# The Normalized Euler Vacuum Is a Calkin Corona State

## Input from the two-port completion theorem

Let

\[
\mathcal H=\ell^2(\mathbb P)
\]

with prime basis \((e_p)\).  For a cutoff \(X\), put

\[
H_X=\sum_{p\le X}\frac1p,
\qquad
v_X=\frac1{\sqrt{H_X}}
\sum_{p\le X}\frac{e_p}{\sqrt p}.
\]

Nima's two-port theorem proves that \(v_X\) is the normalized arithmetic
vacuum inside the ordinary packet space and that every fixed labelled or
cross-prime coefficient disappears as \(X\) grows.  Operator-theoretically,

\[
\|v_X\|=1
\]

while every fixed coordinate tends to zero.

## Weak escape

The vectors converge weakly to zero in \(\mathcal H\):

\[
v_X\rightharpoonup0.
\]

Indeed, convergence holds against every finite-support vector because all
fixed coordinates vanish, and finite-support vectors are dense while the
\(v_X\) are uniformly bounded.

Consequently, for every compact operator \(K\) on \(\mathcal H\),

\[
\|Kv_X\|\longrightarrow0.
\]

Define the vector states

\[
\omega_X(A)=\langle v_X,Av_X\rangle,
\qquad A\in\mathcal B(\mathcal H).
\]

Then

\[
\omega_X(I)=1
\]

at every cutoff, but

\[
\omega_X(K)\longrightarrow0
\]

for every compact \(K\).

## Corona theorem

The state space of \(\mathcal B(\mathcal H)\) is weak-* compact.  Hence every
subnet cluster \(\omega_\infty\) of \((\omega_X)\) is a state satisfying

\[
\omega_\infty(I)=1,
\qquad
\omega_\infty|_{\mathcal K(\mathcal H)}=0.
\]

It therefore factors through the Calkin algebra

\[
\mathcal Q(\mathcal H)
=\mathcal B(\mathcal H)/\mathcal K(\mathcal H).
\]

The escaped prime-harmonic mass is thus literally a corona state.  It is not
merely an informal boundary contribution.

Existence is canonical, but uniqueness is not yet proved.  Different subnets
may select different singular states.  A source-derived Mertens finite-part or
theta--Tate normalization would have to select a distinguished state or prove
that every admissible completion observable has the same corona value.

## Two incompatible completions

Let

\[
K_X=|v_X\rangle\langle v_X|.
\]

As trace-class functionals tested only against compact operators,

\[
K_X\longrightarrow0.
\]

As states tested against all bounded operators, cluster points retain

\[
\omega_\infty(I)=1.
\]

Therefore compact-port completion and unital operator completion do not
commute.  The former loses the entire arithmetic vacuum; the latter retains it
as a singular quotient state.

This is the exact completion-at-infinity obstruction sought in the preceding
programme.  Every finite-rank and compact observation can converge to zero
while a unit of relationship mass survives in the quotient.

## Consequence for the RH completion map

Any completed theta--Tate observable \(A\) intended to detect the normalized
Euler vacuum must have a nontrivial Calkin symbol

\[
\pi(A)\in\mathcal Q(\mathcal H).
\]

If \(A\) is compact, every corona state annihilates it and it cannot carry the
missing completion anomaly.  Thus the RH-bearing completion object cannot be
built solely from trace-class tails and compact boundary repairs.  Its
primitive channel must survive modulo compact operators.

This matches the earlier three-level filtration:

- the connected \(k\ge3\) tail is trace class and invisible in the corona;
- the \(k=2\) seam image is controlled at Hilbert level but is insufficient;
- the primitive \(k=1\) mass supplies the noncompact quotient state.

The new operator target is not an arbitrary boundary functional.  It is a
source-authorized state on the Calkin image of the completed comparison
algebra.

## Falsifier and next gate

The finite falsifier is already exact:

\[
\operatorname{Tr}K_X=1,
\qquad
\langle e_p,K_Xe_q\rangle\longrightarrow0
\]

for every fixed \(p,q\).  Any completion declaring \(K_X\to0\) while claiming
to preserve total arithmetic mass is unfaithful.

The next gate is to identify the completion observable algebra
\(\mathcal A_{\mathrm{comp}}\subseteq\mathcal B(\mathcal H)\), compute its
Calkin image, and test whether the cutoff states have a unique restriction to
that image.  Uniqueness on the full Calkin algebra is unnecessary; uniqueness
on the source-authorized comparison algebra would suffice.

Source transfer:
`research/nima/the-two-port-seam-observer-completes-b2-packets-but-not-the-euler-vacuum.md`
