# Probe-context versus source-knob typing (WP404)

## Bounded question

Can an executable collider scan be identified with WP403's common source knob
merely because it changes the measured mediator response?

## Typed maps

Freeze the affine one-mediator source grammar

\[
H(c)=M^2+c,
\qquad
N(c)=J_0+J_1c,
\qquad
A(c,\omega)=\frac{N(c)}{H(c)-\omega^2}.
\]

The source packet is $\theta=(M^2,J_0,J_1)$. Collider energy, reconstructed
mass, cuts, and luminosity act after this packet has been fixed. In particular,

\[
\frac{\partial\theta}{\partial(\omega,\mathcal L)}=0,
\]

although $\partial A/\partial\omega$ is generically nonzero. Response variation
therefore does not establish source intervention authority.

By contrast, the formal knob has source tangent

\[
\frac{\partial(H,N)}{\partial c}=(1,J_1)^T.
\]

It changes both curvature and tadpole when $J_1\ne0$. The joint static readout
$(H,A_\star)$ distinguishes independent curvature and tadpole errors: its
Jacobian determinant with respect to $(M^2,J_0)$ is $1/(M^2+c)$. Displacement
alone has rank one. Thus WP401--WP403 provide the correct calibration shape,
but not the missing physical map into $c$.

## Candidate-operation audit

- Beam energy or reconstructed invariant mass is executable and detector
  calibrated, but it scans $\omega$ in the propagator rather than changing the
  source coefficients.
- Integrated luminosity changes exposure only.
- Analysis cuts change the admitted readout and may change the contextual
  partition, but do not counterfactually change the mediator action.
- Renormalization scale reorganizes a fixed prediction; it is not a laboratory
  source setting.
- A controlled background field or medium could define $c$ only after a named
  coupling, preparation protocol, and common detector calibration are derived.
  No such admitted construction is present in the flavor programme.

None of the currently executable candidates can be promoted to the WP403 knob
by coordinate relabelling. A new background field would define a new
relational experiment and its stabilizer groupoid must be stated explicitly.

## Exact hostile test

At $M^2=3$, $J_0=2$, $J_1=1$, $c=1$, and $\omega=1$, the dynamic readout has
nonzero $\omega$ derivative while the entire source-parameter Jacobian with
respect to $\omega$ is zero. This is the smallest exact counterexample to the
claim that every executable response scan is a source knob.

## Disposition

WP404 closes the collider-coordinate shortcut negative. Existing CMS records
provide an experimentally calibrated probe family and WP237 provides a
conditional trace-adjoint/Higgs mediator architecture. Their composition does
not supply the counterfactual operation required by WP403. The affine $c$ map
is a source-level proposal, not yet an executable physical instrument.

The remaining acceptance gate is a named apparatus map into $c$, independently
calibrated to produce both $H$ and $N$ shifts in the same source/readout frame,
followed by WP403's reserved measurements without refitting.

Run `uv run --with sympy python
research/flavor/checkers/wp404_probe_source_knob_typing.py` to regenerate the
result.
