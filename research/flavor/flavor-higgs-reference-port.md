# Higgs relative-tadpole reference port (WP412)

## Gauge-invariant source

The observed Standard Model Higgs is a real scalar candidate, but its doublet
transforms under $SU(2)_L$. The center transformation sends $H$ to $-H$.
Consequently a gauge-invariant source potential is even in the radial
representative and has no absolute linear tadpole at the symmetric origin.
A literal linear doublet source requires a transforming spurion and changes the
physical groupoid.

Consider the gauge-invariant radial potential

\[
V(\phi;c)=\frac{-\mu^2+c}{2}\phi^2+\frac{\lambda}{4}\phi^4.
\]

The operator $cH^\dagger H$ is the candidate context deformation. Freeze the
$c=0$ broken vacuum $v_0$, with $\lambda v_0^2=\mu^2$, as a reference and write
$\phi=v_0+h$. Relative to that port,

\[
H_{mathrm{rel}}(c)=2\mu^2+c,
\qquad
J_{mathrm{rel}}(c)=v_0c.
\]

The same $c$ therefore produces both affine shifts, with tangent $(1,v_0)^T$.
This repairs the algebraic mismatch found in WP411 using an explicit reference
port rather than a coordinate identification.

## Changed groupoid

At the actual $c$-dependent equilibrium

\[
v(c)=\sqrt{\frac{\mu^2-c}{\lambda}},
\]

the tadpole vanishes identically. Hence $J_{\mathrm{rel}}$ is not an absolute
Higgs phase or source. It is the force relative to the retained $c=0$ vacuum.
The experiment is defined over the stabilizer groupoid of that prepared
reference, its gauge convention, and the device implementing $c$.

## Physical boundary

WP412 identifies a real scalar and an exact common-shift architecture, but not
an executable Standard Model knob. Temperature or another background can
generate a mass deformation only after its coupling, preparation, support,
nonequilibrium persistence, and detector calibration are derived. Ordinary
collider energy and luminosity remain probe variables, not $c$.

The next constructor must provide an actual source operation varying the Higgs
quadratic term while the original broken-phase reference remains operational,
then independently read both pole curvature and reference-relative
force/displacement. Without that apparatus, WP412 is a relational source model,
not an experiment.

Run `uv run --with sympy python
research/flavor/checkers/wp412_higgs_reference_port.py` to regenerate the JSON
result.
