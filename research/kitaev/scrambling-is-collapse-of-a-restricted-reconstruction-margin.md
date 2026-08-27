# Scrambling is collapse of a restricted reconstruction margin

Owner: `marici.Kitaev`

## Bounded question

How should the programme distinguish information that remains globally present
under unitary evolution from information that becomes unstably recoverable
through an authorized family of local, shallow, or otherwise restricted
contexts?

The exact finite answer is the smallest singular value of the restricted
observation map after source and tester norms are frozen. Scrambling relative
to an interface is collapse of this reconstruction margin, not destruction of
the global state.

## Encoded target and global evolution

Let (V) be the finite-dimensional space of source-normalized target
coordinates. Let

\[
W_t:V\longrightarrow\mathcal H_{\mathrm{op}}
\]

be an isometry into a Hilbert space of operators, states, or process
coordinates after time (t):

\[
W_t^*W_t=I_V.
\]

For Heisenberg operator evolution, (\mathcal H_{\mathrm{op}}) may carry the
Hilbert--Schmidt inner product and (W_t) may consist of encoding followed by
unitary conjugation. Global information is preserved because (W_t) is
isometric.

Let (\mathcal K) label an authorized context budget: spatial radius, circuit
depth, operator weight, time window, number of probes, or a typed combination
of these. The corresponding normalized observation map is

\[
M_{\mathcal K}:\mathcal H_{\mathrm{op}}\longrightarrow Y_{\mathcal K}.
\]

The restricted source-to-observation map is

\[
J_{\mathcal K,t}=M_{\mathcal K}W_t.
\]

## Restricted observation Gramian

Define

\[
G_{\mathcal K,t}
=
J_{\mathcal K,t}^*J_{\mathcal K,t}.
\]

For every target vector (v),

\[
\langle v,G_{\mathcal K,t}v\rangle
=
\|J_{\mathcal K,t}v\|^2.
\]

The exact invisible subspace is

\[
\ker G_{\mathcal K,t}=\ker J_{\mathcal K,t}.
\]

Full algebraic reconstruction through the restricted interface holds exactly
when

\[
G_{\mathcal K,t}>0.
\]

## Reconstruction margin

Define

\[
\mu(\mathcal K,t)
=
\inf_{\|v\|=1}\|J_{\mathcal K,t}v\|
=
\sqrt{\lambda_{\min}(G_{\mathcal K,t})}.
\]

When (\mu>0), the sharp norm of a linear left inverse on the observed range is

\[
\|D_{\min}\|=\frac1\mu.
\]

Thus:

- (\mu=0) means an exact restricted-context kernel;
- (0<\mu\ll1) means algebraic recovery with large noise amplification;
- a uniform lower bound (\mu\geq\mu_0>0) means stable linear reconstruction;
- (\mu\to0) along size, time, or cutoff means completion-unstable recovery.

The margin is meaningful only with source and tester norms fixed before the
audit. Rescaling a weak tester by an arbitrarily large gain changes its cost
rather than repairing the physical interface for free.

## Orthogonal-cut conservation law

Suppose the authorized observation is orthogonal projection onto an accessible
operator subspace:

\[
M_{\mathcal K}=P_{\mathcal K}.
\]

Let

\[
Q_{\mathcal K}=I-P_{\mathcal K}
\]

be the complementary port. Define

\[
G_P=W_t^*P_{\mathcal K}W_t,
\qquad
G_Q=W_t^*Q_{\mathcal K}W_t.
\]

Because (W_t) is isometric,

\[
G_P+G_Q=I_V.
\]

For every normalized target direction,

\[
\|P_{\mathcal K}W_tv\|^2
+
\|Q_{\mathcal K}W_tv\|^2
=1.
\]

When the restricted margin collapses, there is a moving normalized direction
(v_t) whose signal approaches the complementary port. Information has not
vanished; it has crossed the admitted observation cut.

This identity requires an orthogonal decomposition in the frozen operator
metric. For overlapping sensors or general instruments, use their joint
Gramian and do not interpret a sum of squared outputs as conserved without a
frame normalization.

## Local operator-growth instance

Choose an orthonormal Pauli or local-operator basis. Let
(P_{A,k}) project onto operators accessible in region (A) with declared weight
or circuit complexity at most (k).

For one evolved target operator (O(t)) of unit norm, the maximum normalized
linear signal available to that subspace is

\[
\|P_{A,k}O(t)\|.
\]

For a target subspace with orthonormal initial basis
(O_1,\ldots,O_r), the restricted Gram matrix is

\[
(G_{A,k,t})_{ij}
=
\langle P_{A,k}O_i(t),P_{A,k}O_j(t)\rangle.
\]

Its smallest eigenvalue tests whether every target combination retains a
stable accessible component. Average operator weight or one out-of-time-order
correlator can show spreading while missing a nearly invisible linear
combination. Full subspace recovery requires the Gramian.

## Reconstruction front

Order context budgets by inclusion or increasing cost. For a required margin
(\varepsilon>0), define the reconstruction front

\[
\kappa_\varepsilon(t)
=
\inf\{\mathcal K:\mu(\mathcal K,t)\geq\varepsilon\}.
\]

This is the smallest authorized context complexity that stably recovers the
declared target space at time (t).

If context (\mathcal K') contains (\mathcal K) with compatible normalization,
the joint observation Gramian satisfies

\[
G_{\mathcal K',t}\geq G_{\mathcal K,t}.
\]

Hence the margin cannot decrease when a genuinely additional normalized port
is admitted. The reconstruction front can move outward as operators spread.

Calling this motion scrambling is explicitly interface-relative. A different
region, a deeper decoder, or an opened environment port can have a different
front.

## Time-extended contexts

Observations at several times can be stacked. With nonnegative weights
(w_j) satisfying (\sum_jw_j=1), define

\[
G_{\mathcal K,T}
=
\sum_jw_j
W_{t_j}^*M_{\mathcal K}^*M_{\mathcal K}W_{t_j}.
\]

The time family may observe a direction invisible at one instant. This is the
dynamical-observability Gramian for repeated source preparations or a declared
nondemolition observation protocol.

If the measurements act sequentially on one quantum copy, their state updates
must instead be modeled as an instrument or process tensor. Stacking scalar
rows while ignoring measurement disturbance is not an authorized time
Gramian.

## Target-relative reconstruction

Full recovery may be stronger than the theorem requires. Let

\[
R:V\longrightarrow Z
\]

be a frozen target map. It is algebraically computable from the restricted
observation exactly when

\[
\ker J_{\mathcal K,t}\subseteq\ker R.
\]

It is stably computable with decoder norm at most (C) exactly when

\[
R^*R\leq C^2G_{\mathcal K,t}.
\]

The sharp target decoder constant is

\[
C_*
=
\sup_{Jv\neq0}
\frac{\|Rv\|}{\|Jv\|}.
\]

Full-state reconstruction is the case (R=I_V), where (C_*=1/\mu).

A direction may therefore be scrambled for full tomography while remaining
irrelevant to a fixed target. The target must be frozen before the collapsing
direction is found and closed under every future constructor used by the
claim.

## Smallest exact hostile family

Let

\[
V=\mathbb R^2,
\qquad
\mathcal H_{\mathrm{op}}=\mathbb R^3.
\]

For (N\geq1), define

\[
\varepsilon_N=\frac{2N}{N^2+1},
\qquad
\beta_N=\frac{N^2-1}{N^2+1}.
\]

Then

\[
\varepsilon_N^2+\beta_N^2=1.
\]

Encode the two target directions as the first two coordinate vectors and apply
the orthogonal evolution

\[
U_N=
\begin{pmatrix}
1&0&0\\
0&\varepsilon_N&-\beta_N\\
0&\beta_N&\varepsilon_N
\end{pmatrix}.
\]

Let the authorized interface observe only the first two output coordinates.
The restricted map is

\[
J_N=
\begin{pmatrix}
1&0\\
0&\varepsilon_N
\end{pmatrix}.
\]

Every finite (J_N) is injective, but

\[
\mu_N=\varepsilon_N
\longrightarrow0,
\]

and

\[
\|D_{\min,N}\|
=
\frac{N^2+1}{2N}
\longrightarrow\infty.
\]

The second source coordinate has not been destroyed. Its complementary output
amplitude is (\beta_N), which tends to one.

Opening the third-coordinate port gives the full observation map

\[
\widetilde J_N=
\begin{pmatrix}
1&0\\
0&\varepsilon_N\\
0&\beta_N
\end{pmatrix},
\]

with

\[
\widetilde J_N^*\widetilde J_N=I_2.
\]

The full margin is exactly one at every cutoff. This is the smallest rational
orthogonal witness separating global preservation, finite restricted
injectivity, collapsing local stability, and complete repair by one
complementary port.

## Target split in the hostile family

For the first target coordinate,

\[
R_0=(1,0),
\]

the sharp decoder norm remains one. For the second,

\[
R_1=(0,1),
\]

the sharp decoder norm is (1/\varepsilon_N) and diverges.

The same scrambled interface can therefore stably answer one question and
unstably answer another. “The information is recoverable” is incomplete until
the target and norm are named.

## Causal-cut interpretation

If the authorized future contexts all factor through one side of a causal cut,
their observation range cannot see a target component transported entirely to
the other side. At exact separation the margin is zero.

Before exact separation, a small leakage across the cut gives a positive but
collapsing margin. More terminal samples can estimate the small signal at
increasing cost; they do not change which port carries most of the operator.

Stable recovery requires at least one of:

- a port crossing the complementary cut;
- a larger causal region;
- a deeper authorized decoding circuit;
- a time-extended nondisturbing context;
- a frozen target quotient that annihilates the escaping direction.

The source theory must authorize the added context. The Gramian can identify
the missing direction but cannot manufacture its physical port.

## Linear decoder versus quantum recovery

A bounded left inverse proves stable linear tomography of the declared target
coordinates. It need not be a completely positive trace-preserving recovery
channel.

Quantum state recovery additionally requires an admissible channel and the
appropriate error-correction or information-disturbance condition, such as
decoupling of the complementary channel on the code. Approximate recovery
should be measured in a frozen operational norm, often including reference
systems.

Similarly, a small-norm linear decoder may still have prohibitive circuit
depth or require nonlocal gates. Reconstruction margin, physical channel
admissibility, and executable decoder complexity are three distinct gates.

## Record and reference consequence

Opening the complementary port can restore the margin while also exposing an
environment record or reference coordinate. Recovery may then require coherent
erasure of that record, not merely reading another scalar.

In the `S3` frame example, a raw syndrome environment carries the reflection
sheet. It improves access to that coordinate by destroying its system
coherence. A reconstruction theorem must specify whether the task is classical
estimation of the sheet or coherent recovery of the frame.

## Topological-code consequence

Local syndrome can have perfect margin on the local repair quotient while
having an exact kernel on logical loop sectors. Adding noncontractible probes
opens the missing topological ports.

Under growing size, exact logical distinction is still not a signal-strength
theorem. Measurement noise, path length, decoder locality, and reference-frame
faults determine the physical reconstruction margin. Code distance and
restricted observation margin are different invariants.

## DPC: scrambling is a moving decoder obstruction

The conjecture is:

> Information is operationally scrambled relative to a frozen context family
> when globally isometric source directions acquire a collapsing restricted
> reconstruction margin, forcing every decoder through that interface to
> amplify perturbations without bound or to exceed the authorized context
> complexity. The missing information is localized by the complementary
> Gramian, not declared destroyed.

This is explanatory because it predicts the exact repair: enlarge the causal
port, context depth, time family, or target quotient, and then test whether the
margin returns.

## Critics

### Unitary evolution preserves information, so reconstruction is automatic

It preserves the global norm. It does not place a bounded inverse behind a
restricted observer's interface.

### Full rank at every size proves recoverability

It proves finite algebraic injectivity. The hostile family has full rank at
every (N) and a diverging optimal decoder norm.

### More measurements can overcome any small singular value

They can reduce statistical error at increasing sample cost. The tester norm
or sample budget must be charged. Unlimited duplicate rows make an unnormalized
Gramian arbitrary.

### Operator growth already measures scrambling

It measures distribution in a chosen operator basis. Stable recovery of a
multi-operator target depends on the smallest eigenvalue of their accessible
Gram matrix and on the authorized decoder family.

### Opening the environment always recovers the quantum state

It restores global information access in the ideal isometric model. A physical
quantum recovery still needs coherent control, a CPTP decoder, and compatible
reference systems.

### A good singular margin implies an efficient decoder

No. It bounds linear noise amplification. Circuit size, locality, magic,
communication, and fault tolerance remain implementation coordinates.

## Exact falsifiers

- A claimed restricted kernel when (G_{\mathcal K,t}) is positive definite.
- Stable full recovery claimed while (\lambda_{\min}G_{\mathcal K,t}) tends to
  zero in the frozen norm.
- Loss of global information claimed despite isometric (W_t).
- Orthogonal complementary ports whose Gramians fail to sum to identity on the
  encoded target space.
- A larger normalized context family producing a smaller joint Gramian.
- A time-stacked Gramian applied to sequential measurements while their state
  updates are omitted.
- A bounded linear inverse promoted to a physical quantum recovery channel
  without complete positivity and causality.
- A singular gap reported after uncharged tester rescaling or unlimited row
  duplication.
- A target quotient chosen only after the escaping mode is observed.

## Machine-readable reconstruction margin

```json
{
  "code": "restricted_scrambling_reconstruction_margin",
  "global_evolution_isometric": true,
  "restricted_observation": "J_K_t",
  "gramian": "J_star_J",
  "reconstruction_margin": "sqrt(lambda_min(gramian))",
  "finite_injectivity": true,
  "uniform_margin": false,
  "optimal_decoder_norm": "1/margin",
  "complementary_gramian_sum": "identity_for_orthogonal_ports",
  "hostile_margin": "2N/(N^2+1)",
  "hostile_decoder_norm": "(N^2+1)/(2N)",
  "full_port_margin": 1,
  "physical_quantum_decoder_proved": false,
  "executable_decoder_complexity_bounded": false
}
```

## Claim boundary

This packet proves the finite restricted-Gramian, decoder-norm, complementary
port, and rational hostile-family statements. It does not derive a scrambling
Hamiltonian, establish experimental tester norms, prove a CPTP recovery map,
or bound decoder circuit complexity for a many-body model.

Its structural conclusion is that scrambling is not disappearance of
information but collapse of stable reconstructibility relative to a declared
causal and computational interface.
