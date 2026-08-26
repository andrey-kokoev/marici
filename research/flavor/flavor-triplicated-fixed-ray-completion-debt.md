# Triplicated fixed-ray completion debt

Work package: WP593  
Owner: marici.Figueiredo

## Concrete instantiation test

WP592 supplies an isolated fixed-ray architecture. WP593 asks whether the
already declared triplicated messenger theory realizes it after adding the
WP591 common-clock CP modulus.

The answer is no at present. The only computed triplicated fixed-point
component is the gauge-only two-loop truncation. It has

\[
g_*^2=-{104\pi^2\over265},
\]

outside the positive coupling domain. The Yukawa fixed-ray coefficients have
not been derived, and the CP-clock coupling is absent from that action.

## Exact radial closure enlargement

Before the CP modulus is added, the RG-closed quartic basis on the four radial
variables \((F,H,R,\sigma)\) contains ten self and pairwise coordinates.
Adding \(s\) enlarges this to fifteen. The five new coordinates are

\[
s^4,quad s^2\sigma^2,quad
s^2F^2,quad s^2H^2,quad s^2R^2.
\]

The first two occur in the WP591 locking square. The other three cannot be
consistently set to zero: a one-loop bubble joining the
\(s^2\sigma^2\) vertex to each existing leaf-(\sigma\) portal generates
the corresponding \(s^2F^2\), \(s^2H^2\), or \(s^2R^2\) counterterm.
Their support coefficients are nonzero throughout the admitted positive
domain.

WP545 established an 18-coordinate unresolved lower bound before this CP
extension. The five new contractions have distinct field content, so the
extended concrete theory has at least 23 unresolved source coordinates before
a selector-authoritative beta vector field can be formed. This remains a
lower bound; inherited couplings, Standard Model coordinates, masses, scheme
data, and possible higher-loop structures are additional.

## Deutschian consequence

The reduced WP592 coefficients cannot be assigned independently inside this
theory. They must emerge from the complete closed beta system. Omitting even
one generated CP-leaf portal can create a spurious isolated zero and therefore
cannot support explanatory authority.

This is not merely computational inconvenience. Different omitted-coordinate
completions can change or destroy the putative fixed ray while leaving its
reduced \((x,r)\) projection unchanged. A hard-to-vary prediction requires
the full source law.

## Smallest exact falsifier

Omit only \(s^2F^2\). The positive
\(s^2\sigma^2\) and \(F^2\sigma^2\) vertices generate it at one loop.
The truncation is not closed, so any fixed point computed in it lacks selector
authority.

The reopening condition is a scheme-declared beta system over at least the
23-coordinate unresolved packet plus every inherited coupling, followed by a
controlled positive isolated ray and finite-threshold preservation theorem.
Only after that source calculation may the CP/flavor-clock prediction be
compared with an experiment.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp593_triplicated_fixed_ray_completion_debt.py

The generated result is
research/flavor/results/wp593_triplicated_fixed_ray_completion_debt.json.
