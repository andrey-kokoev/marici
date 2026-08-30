# Spin(5) Bell setting-seed hostile (WP914)

## Question

Does WP913's Bell reference port explain independent event-key acquisition, or
does it move the same independence assumption into the Bell setting seed?

## Exact measurement-dependence hostile

In the CHSH game, settings (x,yin\{0,1\}) and outputs (a,bin\{0,1\})
win when

\[
a\oplus b=xy.
\]

With settings independent of the devices, every deterministic local strategy
has the form (a=A(x)), (b=B(y)), and wins at most three of the four setting
pairs.

Now let the hidden device state contain the future settings:

\[
\lambda=(x,y).
\]

The settings remain marginally uniform. Alice outputs (a=0); Bob uses the
shared hidden state and outputs (b=xy). The CHSH condition is satisfied on
all four setting pairs, but the outputs have zero entropy conditional on
(lambda). The apparent perfect Bell score therefore certifies no fresh
randomness.

This does not exploit detector inefficiency, signalling during the trial, or
extractor failure. It attacks only measurement independence: the setting
choices were already present in the device's past state.

## Consequence for WP913

Device-independent randomness expansion is expansion, not creation from no
premise. The cited experiment explicitly uses independently and randomly
chosen measurement settings. Its soundness theorem is conditional on the
protocol's setting-source and isolation assumptions.

WP913 remains a valid conditional reference-port design, but its private
setting-seed preparation is an upstream source port. A public beacon pulse is
not automatically sufficient: the devices must be unable to predict or learn
the chosen future pulse before producing the relevant outputs, and beacon
operator correlation must be inside the threat model.

The admissible repairs are explicitly different:

1. a trusted private seed whose independence from both Bell devices is an
   admitted preparation fact;
2. a randomness-amplification protocol with a declared weak-source model and
   separated devices;
3. multiple independent reference sources combined under a theorem that one
   remains outside the device common cause.

None removes every assumption. Each states a physical causal separation that
forbids the hostile.

## Deutschian status

The explanation must name what prevents (lambda) from containing the future
settings. A high Bell score, extractor transcript, or marginally uniform seed
does not answer that question. The smallest exact falsifier is one setting bit
predictable to both devices before the trial.

This is a reference-port source-support obstruction. It changes no flavor
selector or texture-rigidifier conclusion.

Run:

~~~text
uv run python research/flavor/checkers/wp914_spin5_bell_setting_seed_hostile.py
~~~
