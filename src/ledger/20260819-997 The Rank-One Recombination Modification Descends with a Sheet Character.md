# 997 — The Rank-One Recombination Modification Descends with a Sheet Character

## Object

Entry 995 corrected the effective normal symbol to

\[
n_{s,t}=\delta U+st\,\delta V,
\qquad (U,V)=(s,t),
\]

and showed that the source kernel (K_\chi) is divisible by this normal to first order.  Define the source-derived elementary-modification generator

\[
E_{\chi,s,t}=\frac{K_\chi}{n_{s,t}}.
\]

Test its descent under pair shifts, off-diagonal reflection, and cyclic occurrence transport.

## Pair shifts

In character (++), both the kernel and effective normal are fixed, so

\[
T_{24}E_{++}=T_{34}E_{++}=E_{++}.
\]

In character (--), each corresponding pair shift changes the signs of both numerator and normal:

\[
K_{--}\mapsto-K_{--},
\qquad
n_{s,t}\mapsto-n_{s,t}.
\]

Their quotient is again fixed:

\[
T_{24}E_{--}=T_{34}E_{--}=E_{--}.
\]

## Reflection

Reflection exchanges the two normal coordinates and signed sheets:

\[
(U,V;s,t)\mapsto(V,U;t,s).
\]

The collapse scalar obeys the exact identity

\[
q(X^{-1})=-q(X),
\qquad
q(X)=\frac{1+X^2}{X^2-1}.
\]

Consequently the kernel numerator has reflection unit (-1), while

\[
n_{s,t}\mapsto st\,n_{t,s}.
\]

Therefore

\[
\boxed{
R(E_{\chi,s,t})=-st\,E_{\chi,t,s}.
}
\]

The sheet character is involutive:

\[
(-st)^2=1.
\]

## Cyclic descent

The labelled cycle transports (K_\chi), (U), and (V) to their corresponding objects in the next occurrence chart with unit coefficient.  Hence

\[
\boxed{
\operatorname{Hol}_{C_3}(E_\chi)=1.
}

## Result

\[
\boxed{
\text{the rank-one elementary modification is a global source-derived occurrence line.}
}
\]

Its only nontrivial local datum is the reflection sheet character (-st).  No new carrier cell or fitted coefficient summand is required.

This closes the recombination branch through second normal order at the algebraic coefficient level.  It does not identify the modification line with a physical string integration cycle.

## Next falsifier

Compare the modification line with Entry 979's independent degree-one exceptional chamber complex.  The comparison is now typed only after applying the normal Gysin shift.  Derive that shift from the source wall orientation and test whether the two degree-one lines agree, differ by a character, or remain independent.

## Verification artifacts

- `research/benincasa/marici-gm/src/bin/string_six_point_rank_one_modification_descent.rs`
- `research/benincasa/string-six-point-rank-one-modification-descent.json`

The checker verifies the reflected collapse scalar, all four signed-sheet units, pair-shift cancellation, involutivity, and cyclic return.

Epistemic graph event: `ev-000000000615-896e58ce-e4be-41fd-8c70-ac7f98ab0dad`.
