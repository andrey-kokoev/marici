# Erratum: The Reflection Response Is a Nonsplit Gauge Extension

Ledger 3865 correctly identified an invariant gauge line and a
three-dimensional relational quotient, but incorrectly described them as a
split \(3+1\) response.

The quotient response has Smith form

\[
\operatorname{diag}(384,12288,0),
\]

so it has rank two. Its primitive kernel direction

\[
(27447202735341,20222796908424,-11491475072005)
\]

lifts to a vector whose full response is

\[
505222245120(1,1,1,1).
\]

Thus the quotient-fixed direction shears into the gauge line. The correct
object is a nonsplit filtered extension, not a direct sum. The total-blindness
criterion \(n\mid96\) remains unchanged.

Evidence:

- `research/strominger/the-reflection-response-is-a-nonsplit-gauge-extension.md`
- `research/strominger/checkers/eta_squared_faithful_artin_action_checks.py`
- `research/strominger/results/eta_squared_faithful_artin_action_checks.json`
- aggregate gates: 26/26
- checker SHA-256: `f25540cdeade79e57f6f55e18c25e1bb7b6315e97228048e093cb5c81cdf9cae`
