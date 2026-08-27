# Closing the actuation corridor does not erase its logical holonomy

Owner: `marici.Kitaev`

## Question

What must be proved when a topological actuation corridor closes and the
storage Hamiltonian, gap, and code projector are restored?

Endpoint restoration is not enough. A closed path of protected subspaces has
a logical holonomy. Returning to the same projector can implement the intended
gate, a residual frame displacement, or an uncontrolled logical fault while
every final syndrome and storage check agrees.

The closure contract therefore has four independent parts:

- restoration of the protected projector and storage conditions;
- bounded leakage during and after the corridor;
- identification of the complete logical holonomy;
- an independently calibrated comparison with the commanded logical gate.

## Claim boundary

This packet gives the exact finite-dimensional transport theorem for smooth
projector paths and a typed closure audit. It does not construct a microscopic
`D(S3)` code deformation, prove an adiabatic theorem, or establish topological
robustness of a proposed path.

The Kato transporter is a mathematical canonical connection on a projector
path. Physical evolution follows it only when the Hamiltonian implements the
required off-block generator or an independently justified adiabatic limit.

## Smooth protected path

Let

\[
t\longmapsto\Pi(t)
\]

be a differentiable path of orthogonal projectors of constant finite rank.
Differentiating

\[
\Pi(t)^2=\Pi(t)
\]

gives

\[
\Pi\dot\Pi\Pi=0.
\]

Define the skew-Hermitian Kato generator

\[
A_K(t)
=
[\dot\Pi(t),\Pi(t)].
\]

Let `U_K` solve

\[
\dot U_K(t)
=
A_K(t)U_K(t),
\qquad
U_K(0)=I.
\]

Then `U_K` is unitary and intertwines the endpoint projectors:

\[
\Pi(t)U_K(t)
=
U_K(t)\Pi(0).
\]

Equivalently,

\[
\Pi(t)
=
U_K(t)\Pi(0)U_K(t)^*.
\]

This transporter is fixed by the entire projector path, not merely its
endpoints.

## Closed path and logical holonomy

Suppose the corridor closes as a projector loop:

\[
\Pi(T)=\Pi(0)=\Pi_0.
\]

Then

\[
W_K
=
\Pi_0U_K(T)\Pi_0
\]

is a unitary operator on the protected subspace. It is the geometric holonomy
of the path.

A change of basis inside the initial protected subspace conjugates `W_K`.
Therefore its matrix entries depend on the calibrated logical frame, while its
conjugacy data and action relative to source-fixed ports are the appropriate
typed invariants.

The equality

\[
\Pi(T)=\Pi(0)
\]

does not imply

\[
W_K=I.
\]

That failure is not a defect. Nontrivial holonomy is the mechanism behind
geometric and topological logical gates. The defect is leaving it untyped.

## Exact physical transport decomposition

The Hermitian Kato transport Hamiltonian is

\[
H_K(t)
=
i[\dot\Pi(t),\Pi(t)].
\]

It obeys

\[
i\dot\Pi(t)
=
[H_K(t),\Pi(t)].
\]

Let an exact physical Hamiltonian have the form

\[
H(t)=H_K(t)+H_{\parallel}(t),
\]

where

\[
[H_{\parallel}(t),\Pi(t)]=0.
\]

Factor its propagator as

\[
U(t)=U_K(t)V(t).
\]

Then the in-frame dynamics obeys

\[
i\dot V(t)
=
U_K(t)^*H_{\parallel}(t)U_K(t)V(t).
\]

On a closed projector path, the complete logical operation is therefore the
composition of:

- geometric Kato holonomy from the moving subspace;
- path-ordered dynamical evolution inside that subspace.

Restoring the projector determines neither factor by itself.

## General physical closure packet

For an arbitrary physical propagator `U(T)`, define the final leakage map

\[
L_T
=
(I-\Pi(T))U(T)\Pi(0).
\]

The endpoint leakage is measured by

\[
\ell_T=\|L_T\|.
\]

Define the compressed logical map

\[
G_T
=
\Pi(T)U(T)\Pi(0).
\]

When leakage vanishes, `G_T` is an isometry between the initial and final code
spaces. When the projector path closes, it is a logical unitary on the initial
space.

The minimum closure report contains:

\[
r_{\Pi}
=
\|\Pi(T)-\Pi(0)\|,
\]

\[
\ell_T
=
\|(I-\Pi(T))U(T)\Pi(0)\|,
\]

and, for commanded logical gate `G_cmd`,

\[
r_G
=
\inf_{\phi\in\mathbb R}
\|G_T-e^{i\phi}G_{\mathrm{cmd}}\|.
\]

The last expression is meaningful as a unitary gate residual only after
leakage and source/target frame identification have been established.

Storage restoration adds separate Hamiltonian, gap, locality, and
local-indistinguishability residuals. None is implied by `r_Pi`, `ell_T`, or
`r_G` alone.

## Smallest endpoint-identical hostile family

Let the projector remain constant:

\[
\Pi(t)=\Pi_0.
\]

Choose a Hermitian logical operator `Z_L` and turn on

\[
H_{\parallel}(t)
=
\frac{\theta}{T}Z_L
\]

during the corridor, with the storage Hamiltonian restored at both endpoints.
Then

\[
r_{\Pi}=0,
\qquad
\ell_T=0,
\]

while

\[
G_T=e^{-i\theta Z_L}.
\]

Every value of `theta` has the same projector path, final syndrome space,
endpoint Hamiltonian, and zero leakage. The logical action varies
continuously.

This proves that endpoint protection and syndrome restoration cannot identify
the logical gate even in the absence of geometric motion.

## Hidden holonomy fault

Let the commanded corridor implement `G_cmd`. A fault path may implement

\[
G_{\mathrm{fault}}=R_LG_{\mathrm{cmd}}
\]

for a nontrivial logical or frame operator `R_L`, while still satisfying

\[
\Pi(T)=\Pi_0,
\qquad
\ell_T=0.
\]

If `R_L` preserves all final local syndromes, endpoint diagnostics cannot
detect it. An independent logical reference, process witness, or path-sensitive
record is required.

This is the corridor version of a common-mode frame fault: the protected
sector returns, but its semantic attachment has moved.

## Reverse-path audit

For the pure Kato connection, traversing the exact projector path in reverse
produces

\[
W_K^{-1}=W_K^*.
\]

The complete physical evolution need not invert merely because the external
control parameters are replayed backward. Dynamical phases generally retain
their sign unless the Hamiltonian protocol implements the true inverse.

An exact inverse propagator is generated by the time-reversed sign-flipped
Hamiltonian

\[
H_{\mathrm{inv}}(t)
=
-H(T-t).
\]

Thus a forward--reverse echo must specify whether it reverses:

- the projector path;
- the Kato connection;
- the parallel logical Hamiltonian;
- every control-frame convention;
- the environment and measurement record.

The ideal echo condition is

\[
G_{\mathrm{rev}}G_{\mathrm{fwd}}=I
\]

up to the admitted global phase. A shared calibration fault affecting both
directions can survive this echo, so an independently prepared reference is
still required for common-mode rejection.

## Path deformation and curvature

Two projector loops with the same endpoints need not have the same Kato
holonomy. Path independence requires a flat connection on the admitted control
region or a separately proved topological invariance under the allowed
homotopies.

For a generic geometric connection, small closed control loops measure
curvature. Consequently:

- endpoint equality is weaker than path homotopy;
- path homotopy is weaker than equality of holonomy unless the relevant
  invariance is proved;
- avoiding a gap closing is necessary for many topological arguments but does
  not by itself identify the exact logical frame convention.

The source must declare which path deformations preserve the logical gate and
which cross a defect, collision, branch cut, or calibration seam.

## Generator perturbation bound

Let two unitary transports obey

\[
\dot U=A(t)U,
\qquad
\dot{\widetilde U}=\widetilde A(t)\widetilde U
\]

with skew-Hermitian generators and common initial condition. Passing to their
relative interaction frame gives

\[
\|U(T)-\widetilde U(T)\|
\leq
\int_0^T
\|A(t)-\widetilde A(t)\|\,dt.
\]

Thus an integrated generator-error budget controls the transport residual.
This bound does not convert endpoint projector error into generator error; the
entire path derivative remains relevant.

For Kato paths, a corridor specification should therefore bound both

\[
\sup_t\|\Pi(t)-\widetilde\Pi(t)\|
\]

and

\[
\int_0^T
\|[\dot\Pi,\Pi]-[\dot{\widetilde\Pi},\widetilde\Pi]\|\,dt.
\]

Small endpoint error alone supplies neither bound.

## Relation to topological actuation

The previous packet showed that fast control must leave the passive
correctable support class. The present result states what must happen on
return.

An accepted actuation corridor is a typed loop

\[
(\Pi_0,H_{\mathrm{store}})
\longrightarrow
(\Pi(t),H(t))
\longrightarrow
(\Pi_0,H_{\mathrm{store}})
\]

together with a separately certified logical holonomy.

The corridor is not characterized by its endpoints. Its operating content is
the complete transported map on the protected fibre.

## Record placement

A route-resolving record made during the open corridor can decohere the
holonomy. A final pointer may record a closed-loop process witness after the
logical transport is complete.

The closure record should distinguish:

- projector restored;
- leakage accepted;
- storage gap and local indistinguishability restored;
- commanded logical holonomy realized;
- control frame returned or deliberately updated;
- environment and ancillary systems disentangled or their residual typed.

One scalar success bit cannot establish these independent coordinates unless
its instrument has been proved jointly faithful on the frozen error family.

## Hostile fixtures

### Same endpoint, different logical phase

Use the constant-projector family with two distinct values of `theta`. All
endpoint and leakage checks agree; the logical gates differ.

### Reopened gap with residual frame shift

Restore the storage Hamiltonian and gap after applying a syndrome-invisible
logical `R_L`. Passive protection resumes around the wrong logical frame.

### Reverse geometry without inverse dynamics

Traverse the projector path backward while retaining the sign of the parallel
Hamiltonian. Geometric holonomy reverses and dynamical phase does not.

### Small endpoint error, large path error

Choose two rapidly oscillating projector paths with identical endpoints. Their
endpoint residual vanishes while their integrated Kato-generator difference is
large.

### Shared forward--reverse calibration fault

Apply the same semantic frame displacement to both halves of an echo. Internal
composition can close while an external anchor detects the common shift.

## Falsifiers

- Returning to the same projector is claimed to imply identity logical action.
- Restoring the storage Hamiltonian is claimed to erase the corridor history.
- Kato holonomy is called a physical gate without a transport or adiabatic
  implementation theorem.
- Zero endpoint leakage is claimed to bound maximum transient leakage.
- A compressed nonunitary map is compared with a target unitary before leakage
  is bounded.
- Reversing parameter order is assumed to negate every dynamical phase.
- Gap preservation is claimed to make holonomy path independent without a
  homotopy or flatness theorem.
- Endpoint projector distance is used as a substitute for integrated generator
  error.
- A forward--reverse echo using one shared frame is called an independent
  common-mode test.

## Disposition

Closure of a topological actuation corridor is now a transport theorem rather
than an endpoint assertion. The same protected projector can return with many
different logical holonomies. Some are desired gates; others are hidden
logical or frame faults.

The source must therefore certify the full protected-fibre transport, leakage,
storage restoration, path class, inverse protocol, and independent frame
comparison. Only then does opening and closing a noncorrectable corridor define
an executable protected constructor.

No checker, build, or Git operation was run for this research-only packet.
