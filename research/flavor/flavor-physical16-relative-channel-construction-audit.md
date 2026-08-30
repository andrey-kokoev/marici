# Physical16 cannot construct the relative-channel experiment

Work package: WP606  
Owner: marici.Figueiredo

## Question and domain

This packet answers Nima's narrow construction question: can the existing
`physical16` portal itself construct the shared coherent final state, relative
phase convention, nonzero visibility and calibrated background required by
WP605?

The admitted source domain is the reachable real one-mediator packet

\[
(g_\phi,g_\psi,M,\kappa,\nu,B),
\]

where the last three entries are independently supplied portal and detector
data. The sector norms and coherent arc are

\[
\Gamma_\phi=g_\phi^2,
\qquad
\Gamma_\psi=g_\psi^2,
\qquad
I=g_\phi g_\psi.
\]

The audited `physical16` boundary component is

\[
J_{16}=-{\kappa I\over M^2}.
\]

This is a legitimate forward readout when its portal is independently derived.
It is not a reverse constructor.

## Conditional phase-flipped probe

Given a shared coherent final state and two executable relative-phase settings,
the minimum resolved records have the form

\[
R_\pm=B+\Gamma_\phi+\Gamma_\psi\mathbin{\pm}2\nu I.
\]

They obey

\[
{R_++R_-\over2}=B+\Gamma_\phi+\Gamma_\psi,
\qquad
{R_+-R_-\over4\nu}=I
\]

only when \(\nu\ne0\) is calibrated. Thus the pair is conditionally faithful
to the relative arc, while its average is a magnitude shadow. At \(\nu=0\),
the two ports coincide.

## Exact hostile fibers

The smallest amplitude hostile pair is

\[
(g_\phi,g_\psi)=(1,1),\ (2,1/2),
\qquad M=\kappa=1.
\]

Both have \(I=1\) and \(J_{16}=-1\), but their width packets are respectively
\((1,1)\) and \((4,1/4)\). Therefore the boundary coordinate cannot construct
the norm channels or their amplitudes.

There is a second, independent calibration fiber. The packets

\[
(\kappa,I)=(1,1),\ (2,1/2),
\qquad M=1,
\]

again give \(J_{16}=-1\), but require different coherent arcs. Unless
\(\kappa\) is independently fixed, even \(I\) cannot be reconstructed.

WP558 supplies the same obstruction in linear form: the low-energy map
\(L=(1,1,1)\) kills \((1,-1,0)\), while the threshold metric sees squared norm
two. Threshold records are not constant on low-energy fibers, so no
constructor-independent reverse map exists.

## Typed disposition

The first nonfaithful arrow is the projection from the mediator source packet
to the single `physical16` boundary component. `physical16` is a calibrated
physical quotient readout. It cannot manufacture:

- a shared coherent final state;
- the phase-flipped control settings;
- a nonzero detector visibility;
- a calibrated background;
- finite-width and detector-support assumptions.

Consequently the current operation is a conditional readout, neither a source
identifier nor a constructor of the relative-channel experiment. A supplied
weak-basis-invariant portal descends forward under the full weak-basis
groupoid; no reverse threshold construction descends from `physical16` alone.

The remaining physical-instrument gate is one admitted mediator grammar that
derives all of the missing detector objects in a common frame. The exact
falsifier is already finite: two source packets with the same \(J_{16}\) and
different width packets.

## Reproduction

Run:

    uv run --offline --with sympy python research/flavor/checkers/wp606_physical16_relative_channel_construction_audit.py

The generated result is
research/flavor/results/wp606_physical16_relative_channel_construction_audit.json.
