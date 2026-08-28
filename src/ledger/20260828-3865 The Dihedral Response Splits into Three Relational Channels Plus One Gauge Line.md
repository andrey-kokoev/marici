# The Dihedral Response Splits into Three Relational Channels Plus One Gauge Line

Strominger computed the full Smith packet of the integral reflection-response
operator \(\Delta=R-I_4\) for the explicit \(\eta^2\) braid:

\[
\operatorname{SNF}(\Delta)
=\operatorname{diag}(96,1536,16167111843840,0).
\]

The zero factor is the common translation vector \((1,1,1,1)\), representing
simultaneous relabelling of every polygon reflection. Thus the response splits
into three relational channels plus one permanent gauge line.

Over \(\mathbb Z/n\),

\[
|\ker\Delta_n|
=n\gcd(n,96)\gcd(n,1536)\gcd(n,16167111843840).
\]

This recovers total blindness exactly at \(n\mid96\) and classifies every
partial-blindness stratum.

Evidence:

- `research/strominger/the-dihedral-response-splits-into-three-relational-channels-plus-one-gauge-line.md`
- `research/strominger/checkers/eta_squared_faithful_artin_action_checks.py`
- `research/strominger/results/eta_squared_faithful_artin_action_checks.json`
- aggregate gates: 22/22
- checker SHA-256: `3801b1b8ff7dc9716fbef9bb529ce0add4998cb61be3274373384465c691ae50`
