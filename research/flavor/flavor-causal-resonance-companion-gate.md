# Causal resonance companion-signal gate (WP424)

## Minimal admitted model

The smallest passive causal resonance candidate for enhancing the WP422
response has susceptibility

$$
\chi(\omega)=\frac{A}{\Delta-i\gamma},
\qquad
\Delta=\omega_0-\omega,
$$

with independently normalized pole strength (A>0), linewidth (gamma>0),
and commanded detuning (Delta). Its dispersive and absorptive readouts are

$$
R=\operatorname{Re}\chi=\frac{A\Delta}{\Delta^2+\gamma^2},
\qquad
I=\operatorname{Im}\chi=\frac{A\gamma}{\Delta^2+\gamma^2}.
$$

Causality relates these channels through dispersion relations. It does not
authorize treating (R) as an isolated fitted amplifier.

Primary source: [review of causality, passivity, and dispersion relations](https://arxiv.org/abs/2008.05546).

## Exact ambiguity of a gain-only readout

For a target dispersive gain (R=G>0), real detunings exist only if

$$
A\mathrel{\geq}2G\gamma.
$$

Above threshold there are two solutions,

$$
\Delta_{\pm}=\frac{A\pm\sqrt{A^2-4G^2\gamma^2}}{2G}.
$$

They produce exactly the same quartic-facing gain but different absorption.
Their detunings obey (Delta_+\Delta_-=\gamma^2), while their absorptive
responses obey

$$
I_+I_-=G^2.
$$

Thus one branch has (I\leq G) and the other has (I\geq G). A gain-only
measurement collapses two physically different resonance contexts. Large
same-frequency absorption is not unavoidable, but the complementary linewidth
and absorption profile is unavoidable if resonance is the explanation.

## Hostile pair

The exact packet (A=5), (gamma=1), and (G=1) has

$$
\Delta_{\pm}=\frac{5\pm\sqrt{21}}{2}.
$$

Both yield (R=1), while their absorptive responses are unequal and multiply
to one. This is the smallest explicit witness that a measured quartic gain
does not identify the resonance constructor.

## Instrument and verdict

A resonance proposal passes only if one common experiment measures a bounded
frequency scan containing:

- the dispersive quartic-facing response;
- the absorptive or loss response;
- the linewidth and pole location;
- an independently calibrated command-frequency axis;
- a pole strength fixed without fitting the desired quartic displacement.

The scan must satisfy the causal pole relation, not merely interpolate the
target point. Finite resolution must separate the two allowed branches or
bound the omitted one.

WP424 therefore does not yet supply an enhancement. It converts resonance into
a falsifiable constructor family and identifies its missing physical
instrument. The smallest falsifier is a claimed gain (G) with independently
fixed (A,gamma) for which (A<2Ggamma), or a measured absorption/dispersion
scan inconsistent with the shared pole.

Run `uv run --with sympy python
research/flavor/checkers/wp424_causal_resonance_companion_gate.py` to regenerate
the JSON result.
