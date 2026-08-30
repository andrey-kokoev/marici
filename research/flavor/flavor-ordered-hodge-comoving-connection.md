# Ordered Hodge Portal Has a Co-moving Connection but No RG Selector

## Question

Does WP878's ordered Hodge portal (H=P_v-P_u) admit a source-derived
transport law through a moving singlet frame, and does that law determine the
portal magnitude or RG trajectory?

## Exact two-plane transport

Choose an oriented orthonormal source frame ((e_u,e_v)) and define

\[
J=e_ve_u^T-e_ue_v^T,
\qquad H=P_v-P_u.
\]

For a differentiable rotation (R(t)=\exp(\theta(t)J)),

\[
H(t)=R(t)H(0)R(t)^T,
\qquad \Omega(t)=\dot R(t)R(t)^T=\dot\theta J.
\]

Direct differentiation gives

\[
\dot H=[\Omega,H].
\]

Therefore the covariant derivative

\[
D_tH=\dot H-[\Omega,H]
\]

vanishes. The angular velocity is reconstructible from the ordered projector
germ:

\[
\dot\theta=\frac14\operatorname{tr}(JH\dot H).
\]

This is a kinematic connection supplied by the moving ordered source frame.
It is not obtainable from eigenvalues or other conjugation-invariant scalar
RG data alone.

## Descent under moving weak bases

Under a time-dependent weak-basis transformation (U(t)),

\[
H'=UHU^{-1},
\qquad
\Omega'=U\Omega U^{-1}+\dot U U^{-1}.
\]

Then (D_tH) transforms covariantly:

\[
D_t'H'=U(D_tH)U^{-1}.
\]

Freezing the connection to zero in every chart fails this test. Even a
constant physical (H) acquires

\[
\dot H'=[\dot U U^{-1},H']
\]

in a moving presentation. Thus a zero-connection comparison is chart data,
not a weak-basis-descended physical statement.

## What the connection does not select

For the portal (G=gH),

\[
D_tG=\dot g\,H+gD_tH=\dot g\,H.
\]

Parallel transport of the ordered frame removes spurious angular motion but
leaves the scalar beta function (dot g=\beta_g) completely untouched. It
also does not choose the anomaly-free matter completion, threshold masses,
or detector response. The connection therefore rigidifies comparison across
moving presentations; it is not a numerical selector.

## Contextual partition

On differentiable ordered-projector histories, two presentations are
contextually equivalent when related by a moving weak basis together with
the inhomogeneous connection transformation above. Scalar-only RG histories
form a coarser partition because they forget the projector germ and hence
the reconstructed (dot\theta).

The smallest hostile pair consists of two histories with identical constant
projector spectra and scalar RG records:

- (H_1(t)=H_0), with (Omega_1=0);
- (H_2(t)=R(t)H_0R(t)^T), with (Omega_2=dot R R^T).

They are the same physical history only when the connection is transported.
A frozen-coordinate derivative falsely distinguishes them.

## Aspect classification

- Realization: exact on a declared differentiable ordered-projector source
  history.
- Tester: covariance and reconstruction are exact.
- Falsifier: frozen (Omega=0) fails under any nontrivial moving basis.
- Ontology: threshold discontinuities and projector degeneracies require
  separate matching data.
- Governance: the connection is admitted only where the source provides the
  ordered projector path; scalar RG output cannot synthesize it.
- Portfolio: no new detector port follows from this transport theorem.

## Claim boundary

The theorem repairs descent for smooth ordered-frame transport. It does not
construct a dynamical source law for the frame, cross a degeneracy, fix
(g), or supply an experimental instrument. At a threshold jump, the left
and right projector frames require an independently derived matching
intertwiner.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp882_ordered_hodge_comoving_connection.py
~~~
