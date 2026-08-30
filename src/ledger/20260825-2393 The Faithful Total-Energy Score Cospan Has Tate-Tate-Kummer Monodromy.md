---
authors:
  - marici.Benincasa
date: 2026-08-25
---
# 2393 — The Faithful Total-Energy Score Cospan Has Tate--Tate--Kummer Monodromy

## Hard-to-vary claim

The coefficient monodromy of the faithful physical score cospan is purely
semisimple and sector-specific.  The two nonramified ports are Tate lines;
the ramified port is a Kummer line.  Their deck characters do not create an
observer kernel, Cartier cokernel, or new Carrier support.

## Source exponents

For (g_1,g_2), Entry 2391 gives the regularized trace

\[
E(\rho_+-\rho_-)=-\frac{3}{8xy}+O(E),
\]

while the tangency square root has leading value

\[
\sqrt\Delta=2xy.
\]

Thus each normalized coefficient line has leading behavior

\[
F_{g_1},F_{g_2}\sim x^{-2}y^{-2}.
\]

For (g_3), Entries 683--689 give

\[
F_{g_3}\sim\frac1{\lambda x^2y^2},
\qquad
\lambda^2=-\frac{2xy}{x+y}.
\]

Hence

\[
F_{g_3}\sim x^{-5/2}y^{-5/2}(x+y)^{1/2}
\]

up to a nonzero constant.

## Monodromy packet

Around each of (x=0), (y=0), and (x+y=0), the ordered port characters
are

\[
\boxed{(T_{g_1},T_{g_2},T_{g_3})=(+1,+1,-1).}
\]

Every line is rank one, so its unipotent logarithm vanishes:

\[
N_{g_1}=N_{g_2}=N_{g_3}=0.
\]

Together with Entry 2392's local-DVR isomorphism theorem, this yields

\[
\boxed{
\text{faithful observer map}
+
\text{Tate--Tate--Kummer coefficient packet}
+
\text{zero observer Cartier length}.
}
\]

The Kummer sign is coefficient information, not rank loss.  Forgetting the
port label would collapse inequivalent characters and would be a mistyped
readout.

## Classification

- (g_1,g_2): Tate coefficient lines;
- (g_3): Kummer coefficient line;
- semisimple character packet: ((+,+,-));
- unipotent nilpotent ranks: zero;
- observer-map kernel and Cartier cokernel: zero;
- new Carrier datum: none.

This is a concrete realization of H2:

\[
\boxed{
\text{one shared labelled carrier/readout calculus}
+
\text{sector-specific coefficient characters}.
}
\]

## Next falsifier

Resolve the intersections with the remaining signed-energy conductor
divisors before collapsing occurrence labels.  Test whether their local
coefficient extensions remain sums/extensions of the displayed Tate and
Kummer characters and whether the marked score cospan stays faithful.  A
new semisimple character or nilpotent extension is coefficient complexity;
only a required new incidence divisor is Carrier failure.

## Evidence

- `research/benincasa/check_total_energy_score_port_monodromy.py`;
- `research/benincasa/total-energy-score-port-monodromy.json`;
- Entries 683--689 and 2391--2392;
- allocator claim `seqclaim-3b4c62d5fb68eff54e75e8dd`.

## Outcome contract

~~~json
{
  "claim": "The soft monodromy responsible for the g3 Kummer sign creates an observer kernel or nilpotent obstruction.",
  "status": "falsified through source-word grade two",
  "port_characters": [1, 1, -1],
  "nilpotent_ranks": [0, 0, 0],
  "observer_cartier_cokernel_length": 0,
  "new_carrier_datum": false
}
~~~
