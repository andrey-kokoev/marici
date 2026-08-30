# The Reflection Response Is a Nonsplit Gauge Extension

## Correction of the direct-sum picture

The Smith form of the four-port response suggested three relational channels
plus one gauge line. The dimension count is correct, but direct splitting is
false.

Let \(V=\mathbb Z^4\), let \(G=\mathbb Z(1,1,1,1)\), and let \(R\) be the
reflection response. There is an invariant exact sequence

\[
0\longrightarrow G\longrightarrow V\longrightarrow V/G\longrightarrow0.
\]

The induced operator on the relational quotient \(V/G\) has response Smith
form

\[
\operatorname{SNF}(\overline R-I)
=\operatorname{diag}(384,12288,0).
\]

Thus the quotient response has rank two, not three.

## The missing quotient direction

A primitive kernel vector for the quotient response is

\[
v=(27447202735341,\ 20222796908424,\ -11491475072005).
\]

Using the lift \(\widetilde v=(v,0)\in V\), direct computation gives

\[
(R-I)\widetilde v
=505222245120(1,1,1,1).
\]

The quotient regards \(v\) as fixed, but its lift is not fixed: it acquires a
pure gauge displacement. This is the extension shear.

The coefficient factors as

\[
505222245120
=2^8\cdot3\cdot5\cdot19\cdot193\cdot35879.
\]

The largest nonzero Smith factor of the full four-port response is exactly 32
times this shear coefficient.

## Correct categorical object

The response is not

\[
\text{relational object}\oplus\text{gauge line}.
\]

It is an extension in which one quotient-invariant relationship has a
nontrivial gauge-valued attachment. Equivalently, the correct structure is:

```text
invariant gauge line
        -> full four-port response
        -> relational quotient
        -> gauge-valued shear class
```

This distinction is observable. A quotient-only instrument reports the vector
\(v\) as fixed, while an instrument retaining absolute gauge records a shift.

## General and special parts

For any braid acting by affine reflection-label Hurwitz maps, simultaneous
translation is invariant. That gauge line is universal.

What is special to \(W_{\eta^2}\) is:

1. the quotient response has Smith factors \((384,12288,0)\);
2. its primitive fixed quotient direction has nonzero gauge shear;
3. the full response therefore has rank three despite quotient rank two.

This repairs the earlier overstatement without changing the total-blindness
criterion \(n\mid96\).

## Replay

```powershell
uv run python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py
```
