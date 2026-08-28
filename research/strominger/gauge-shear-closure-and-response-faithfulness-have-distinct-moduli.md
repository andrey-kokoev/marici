# Gauge-Shear Closure and Response Faithfulness Have Distinct Moduli

## Result

The nonsplit reflection response carries two independent arithmetic predicates.

The first is total response blindness:

\[
n\mid96.
\]

The second is whether the primitive quotient-fixed relationship admits a fixed
lift to the full four-port packet. Its integral lift has response

\[
(R-I)\widetilde v
=S(1,1,1,1),
\qquad
S=505222245120.
\]

Because adding any gauge vector to \(\widetilde v\) leaves this response
unchanged, the shear cannot be removed by choosing another lift. Modulo \(n\),
a fixed lift exists exactly when

\[
n\mid S.
\]

The factorization is

\[
S=2^8\cdot3\cdot5\cdot19\cdot193\cdot35879.
\]

## Independence hostile

Take \(n=5\). Then

\[
5\mid S,
\qquad
5\nmid96.
\]

The quotient-fixed relationship lifts without gauge shear, yet the full braid
response is still visible. Thus closure of this extension does not imply
instrument blindness.

Take \(n=7\). Then

\[
7\nmid S,
\qquad
7\nmid96.
\]

The response is visible and the lift remains sheared.

Every totally blind modulus divides 96, and 96 divides \(S\). Therefore total
blindness implies shear closure, but the converse is false.

## Typed interpretation

The two predicates answer different questions:

| invariant | question |
|---|---|
| content 96 | does the complete reflection response vanish? |
| shear \(S\) | does one quotient-fixed relationship possess a fixed full lift? |

The first concerns observation faithfulness. The second concerns attachment
coherence across the gauge extension. Neither may be inferred from the other.

This gives a concrete example of a system that remains observably active while
one higher attachment obstruction has disappeared.

## Replay

```powershell
uv run python research/strominger/checkers/eta_squared_faithful_artin_action_checks.py
```
