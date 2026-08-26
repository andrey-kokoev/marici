# Theta log-moment flatness and band-asymptotic flatness are distinct quotients

## Status

Typing theorem and completion gate. Two different constructions in the current
RH programme produce remainders described as invisible to every algebraic
order:

- packets invisible to every logarithmic label moment;
- boundaryless band remainders invisible to every inverse-scale asymptotic
  coefficient.

These are kernels of different jet functors on different filtered objects.
They cannot be identified without a source-derived bonding map that
intertwines the two filtrations.

## Logarithmic-moment flat sector

Let \(\mathcal C_{\mathrm{arith}}\) be a completion of the finite labelled
arithmetic module on which the relevant powers of logarithmic degree are
defined. Its algebraic observation map is

\[
J_{\log}v
=
(\varepsilon v,\varepsilon Lv,\varepsilon L^2v,\ldots).
\]

Define

\[
\mathcal F_{\log}=\ker J_{\log}
=\bigcap_{k\geq0}\ker(\varepsilon L^k).
\]

On every finite packet, Vandermonde separation gives

\[
\mathcal F_{\log}\cap\mathcal C_{\mathrm{fin}}=\{0\}.
\]

The completed flat sector can nevertheless be nontrivial if the chosen
topology admits a nonzero limit invisible to every fixed moment.

Prime transport preserves this sector because its action on moments is
triangular. Reciprocal reflection preserves it because it only changes moment
parity.

## Band-asymptotic flat sector

Let \(\mathcal C_{\mathrm{band}}\) carry the macroscopic band parameter (M),
or its inverse (h=M^{-1}). The algebraic asymptotic jet records the
coefficients

\[
J_{\mathrm{band}}x
=(b_0(x),b_1(x),b_2(x),\ldots)
\]

in an expansion

\[
x(h)\sim\sum_{j\geq0}b_j(x)h^j.
\]

Its flat sector is

\[
\mathcal F_{\mathrm{band}}=\ker J_{\mathrm{band}}.
\]

An element of this kernel is smaller than every algebraic power of (h), but
may remain nonzero through exponential or other nonperturbative scale.

Grothendieck's boundaryless band theorem places the surviving modular current
in this second kind of flat remainder. It does not, by itself, place that
current in \(\mathcal F_{\log}\).

## Required bridge

To identify the two flat sectors, one needs a source-derived map

\[
B:\mathcal C_{\mathrm{arith}}
\longrightarrow
\mathcal C_{\mathrm{band}}
\]

and a map of jet targets

\[
\beta:operatorname{Im}J_{\log}
\longrightarrow
\operatorname{Im}J_{\mathrm{band}}
\]

such that

\[
J_{\mathrm{band}}B=\beta J_{\log}.
\]

Only then does

\[
B(\mathcal F_{\log})\subseteq\mathcal F_{\mathrm{band}}
\]

follow. Equality, injectivity on flat sectors, or reconstruction of one sector
from the other requires additional theorems.

Formula resemblance between logarithmic moments and band coefficients does not
supply this square.

## Independent nonperturbative observable

Let \(\mathcal B\) be a proposed modular boundary current on
\(\mathcal C_{\mathrm{band}}\). It is genuinely beyond the band jet if there is
an element (x) with

\[
J_{\mathrm{band}}x=0,
\qquad
\mathcal Bx\neq0.
\]

Likewise, its pullback would be genuinely new relative to logarithmic moments
only if there were (v) satisfying

\[
J_{\log}v=0,
\qquad
\mathcal B(Bv)\neq0.
\]

This witness proves that the boundary current does not factor through the
algebraic jet quotient. Without such a witness or an equivalent dual-space
separation theorem, calling the current nonperturbative is only asymptotic
terminology.

## Domination falsifier

At finite order (K), define the algebraic observation energy

\[
Q_K(v)=\sum_{k=0}^K|\varepsilon L^kv|^2.
\]

If a proposed boundary current satisfies, for one fixed (K) and a
cutoff-independent constant (C),

\[
|\mathcal B(Bv)|^2\leq C Q_K(v),
\]

then it is controlled by finitely many algebraic moments and is not the missing
beyond-all-orders port.

Conversely, failure of every finite-(K) domination is necessary but not
sufficient for a continuous nonperturbative observable. Its own graph topology
and completion domain still must be source-derived.

## Compiler object

The minimal typed object is a square of filtered modules:

\[
\begin{array}{ccc}
\mathcal C_{\mathrm{arith}}&\overset{B}{\longrightarrow}&
\mathcal C_{\mathrm{band}}\\
\downarrow J_{\log}&&\downarrow J_{\mathrm{band}}\\
\mathcal J_{\log}&\overset{\beta}{\longrightarrow}&
\mathcal J_{\mathrm{band}}.
\end{array}
\]

The compiler must reject:

- a missing bonding map (B);
- cutoff-dependent choices of (B);
- a noncommuting jet square;
- erasure of either flat kernel;
- a boundary current that is only a fitted functional on the quotient;
- claims that finite-packet moment separation proves completed separation.

## Consequence for the RH lane

The algebraic arithmetic programme and the nonperturbative modular programme
now meet at one exact construction problem: derive the filtered bonding square
from the labelled theta source.

If the square exists and the modular boundary current detects a log-moment-flat
state with a controlled orientation, it supplies genuinely new information.
If every modular current factors through the logarithmic jet tower, then it
cannot evade the divisor-preservation no-go already proved for prime transport.
