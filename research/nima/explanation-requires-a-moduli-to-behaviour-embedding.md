# Explanation requires a moduli-to-behaviour embedding

## Why the raw margin is insufficient

The numerical margin

\[
\mu(E)
=
\inf_{\|\delta E\|=1}
\|D\Sigma_E(\delta E)\|
\]

depends on the chosen parameter and output norms. A nonlinear
reparameterization can change it without changing the realization or any
experiment. The margin is a useful conditioning statistic only after the
source supplies the relevant uniform structures.

The invariant core is topological and geometric: the admissible realization
moduli must embed into complete intervention behaviour.

## Realization moduli

Let \(\mathcal M_{\mathrm{src}}\) be the hostile-closed space of
source-admissible realizations, and let \(\mathcal G_{\mathrm{auth}}\) be the
independently authorized realization groupoid. Form the moduli object

\[
\mathcal Q
=
\mathcal M_{\mathrm{src}}/\mathcal G_{\mathrm{auth}}.
\]

Let \(\mathcal Y\) be the space of complete declared intervention behaviours.
The observation map descends only when authorized equivalent realizations
have the same behaviour:

\[
\overline\Sigma:\mathcal Q\longrightarrow\mathcal Y.
\]

This separates four gates.

1. **Adequacy:** the observed behaviour lies in the image.
2. **Structural identifiability:** \(\overline\Sigma\) is injective.
3. **Local identifiability:** \(\overline\Sigma\) is an immersion or has the
   appropriate infinitesimal monomorphism property.
4. **Stable identifiability:** \(\overline\Sigma\) is a topological embedding,
   so reconstruction is continuous on its image.

When locally compact Hausdorff hypotheses apply, properness of
\(\overline\Sigma\) supplies a useful sufficient condition for stable
identifiability.

## Completion escape as failure of embedding

Injectivity alone permits a sequence of inequivalent realizations \(q_N\) to
remain separated at every finite stage while their behaviours converge:

\[
\overline\Sigma(q_N)\longrightarrow y.
\]

If \(q_N\) has no corresponding convergence to the unique realization of
\(y\), the inverse on the image is discontinuous. Finite identification then
fails to survive completion.

This is the coordinate-free form of a collapsing observability constant. A
metric lower bound is one certificate for embedding stability, not its
definition.

## Gauge and duality

Behavioural equality does not itself authorize a gauge identification. A
duality belongs to \(\mathcal G_{\mathrm{auth}}\) only when the source
constructs its action on states, interventions, probes, and composition.

Conversely, two presentations related by an authorized similarity or unitary
port transformation should not count as rival explanations. The explanatory
object is the moduli point together with its source typing, not one coordinate
matrix.

## Positive finite control pilot

Consider a discrete-time SISO system

\[
x_{k+1}=Ax_k+Bu_k,
\qquad
y_k=Cx_k,
\]

of known finite state dimension \(n\). Its Markov parameters are

\[
h_k=CA^kB.
\]

Construct the Hankel matrices

\[
H_0=(h_{i+j})_{0\le i,j<n},
\qquad
H_1=(h_{i+j+1})_{0\le i,j<n}.
\]

If

\[
\operatorname{rank}H_0=n,
\]

the realization is controllable and observable on its generated state space.
The shift induced by \(H_1\) relative to \(H_0\) reconstructs the internal
dynamics in a Hankel realization. Any two minimal realizations with the same
Markov sequence are similar.

Thus the complete impulse-response behaviour embeds the moduli of minimal
order-\(n\) realizations into behaviour space. In this bounded rational class,
finitely many Markov parameters determine the two Hankel matrices and hence a
realization gauge class.

This is a genuine positive example of lower-lens observations reconstructing
an Endo model because the following were fixed independently:

- system class;
- state-order bound;
- input and output ports;
- minimality rank;
- realization gauge;
- intervention protocol.

## Why this is still not a source explanation

Ho--Kalman reconstruction explains the minimal linear state machine realizing
an impulse response. It does not prove that the physical source is linear,
has the declared state dimension, or uses the reconstructed coordinates as
physical variables.

Accordingly there are two explanatory levels: behaviour-relative realization
and source-mechanism realization.

The first is earned by the embedding theorem. The second additionally requires
the source to derive the state types and transition constructors.

## Hostile tests

- Same behaviour from two inequivalent points of \(\mathcal Q\): failure of
  structural identifiability.
- Injective map with discontinuous inverse: completion instability.
- A similarity declared unauthorized despite preserving the frozen ports:
  overspecified presentation.
- A physical duality declared gauge without a source action on interventions:
  authority by behavioural equality.
- Hankel rank below the claimed state order: dark or redundant state.
- Reconstruction requires an order bound chosen after examining the data:
  hostile class not predeclared.
- A nonlinear or switched realization matches the same finite samples but was
  excluded without source authority.

## Revised hard-to-vary criterion

An explanation is hard to vary when the hostile-closed moduli-to-behaviour map
is an embedding and the source-derived realization law determines its moduli
point. Quantitative margins refine this statement only after invariant norms
or uniformities are supplied.
