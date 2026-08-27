# Noncentral flux control quantitatively consumes an invariant six-state frame

## Bounded question

The exact catalytic no-go says that an invariant relational gauge frame cannot
be returned unchanged and uncorrelated after inducing a noncentral data-only
operation through symmetric dynamics. How much is the finite six-state frame
disturbed by one explicit relational flux pulse?

This packet answers only the one-use finite question. It does not assume that
return probability alone controls repeated use, because correlations and
coherences carried between uses also matter.

## Relational pulse

Let the reference have basis

\[
\{|r\rangle:r\in S_3\},
\]

and let \(B^g\) denote the orthogonal projector onto data flux \(g\). For a
fixed noncentral element \(q\), define

\[
P_q=\sum_{r\in S_3}B^{rqr^{-1}}\otimes |r\rangle\langle r|.
\]

The gauge-invariant relational pulse is

\[
V_q(\theta)=e^{-i\theta P_q}
=\sum_{r\in S_3}W_r(\theta)\otimes |r\rangle\langle r|,
\]

where

\[
W_r(\theta)
=I+(e^{-i\theta}-1)B^{rqr^{-1}}.
\]

Each \(W_r\) is unitary. The joint pulse is controlled by the reference
orientation rather than by an absolute gauge label.

## Exact return-probability theorem

Prepare a pure reference

\[
|\eta\rangle=\sum_r c_r|r\rangle,
\qquad
p_r=|c_r|^2,
\]

and an arbitrary data density operator \(\rho\). After applying \(V_q\) and
tracing out the data, let the reference state be \(\sigma_R'\). Its probability
of passing the sharp return test \(|\eta\rangle\langle\eta|\) is

\[
f_\eta(\rho)
=\langle\eta|\sigma_R'|\eta\rangle
=\operatorname{Tr}(\rho M_\eta^\dagger M_\eta),
\]

with

\[
M_\eta=\sum_r p_rW_r.
\]

Indeed, the reduced reference matrix elements are

\[
\langle r|\sigma_R'|s\rangle
=c_r\overline{c_s}\operatorname{Tr}(W_r\rho W_s^\dagger),
\]

and contraction with \(|\eta\rangle\) gives the stated expression.

The worst-case return probability over all data states is therefore

\[
f_{\min}(\eta)
=\lambda_{\min}(M_\eta^\dagger M_\eta)
=s_{\min}(M_\eta)^2.
\]

This is an exact finite theorem. It converts reference consumption into a
smallest-singular-value calculation.

## Uniform invariant frame

For the invariant reference

\[
|+\rangle=\frac1{\sqrt6}\sum_{r\in S_3}|r\rangle,
\]

all probabilities are \(p_r=1/6\). Let \(C_q\) be the conjugacy class of
\(q\), and set \(k=|C_q|\). Every conjugate occurs \(|Z(q)|\) times as \(r\)
runs through the group, so

\[
M_+
=I+\frac{e^{-i\theta}-1}{k}B^{C_q},
\qquad
B^{C_q}=\sum_{g\in C_q}B^g.
\]

On flux sectors outside \(C_q\), the eigenvalue is one. On flux sectors in
\(C_q\), it is

\[
\frac{k-1+e^{-i\theta}}{k}.
\]

Consequently,

\[
f_{\min}^{(q)}(\theta)
=1-\frac{4(k-1)}{k^2}\sin^2\frac\theta2.
\]

The disturbance is zero precisely for a trivial pulse, a central singleton
class, or an input excluded from the addressed class. Noncentral pulse strength
and invariant-frame return cannot both remain exact in the worst case.

## The three classes of S3

For the identity class, \(k=1\), and

\[
f_{\min}^{(e)}(\theta)=1.
\]

This agrees with the catalytic theorem: central control does not require an
orientation resource.

For a transposition, \(k=3\), and

\[
f_{\min}^{(t)}(\theta)
=1-\frac89\sin^2\frac\theta2.
\]

At \(\theta=\pi\), the return probability is \(1/9\).

For a three-cycle, \(k=2\), and

\[
f_{\min}^{(c)}(\theta)=\cos^2\frac\theta2.
\]

At \(\theta=\pi\), the return probability is zero. A worst-case cycle-flux
input drives the frame to a state orthogonal to its invariant preparation in a
single use.

## Direct witness on a sharp flux input

Take a data flux basis state \(|g\rangle\) with \(g\in C_q\). Exactly
\(|Z(q)|\) of the six reference orientations satisfy

\[
rqr^{-1}=g.
\]

Those amplitudes acquire phase \(e^{-i\theta}\); the remaining amplitudes do
not. The overlap amplitude with the initial invariant frame is therefore

\[
\frac{k-1+e^{-i\theta}}{k}.
\]

This flux-basis witness attains the worst-case bound. No optimization or
asymptotic argument is hidden in the result.

## Sharp frame contrast

For a sharp boundary frame \(|r_0\rangle\), the probability distribution is a
delta function and

\[
M_\eta=W_{r_0}.
\]

Since \(W_{r_0}\) is unitary, the frame returns exactly and the final joint
state remains a product for every data input. This does not violate the
catalytic no-go: a sharp frame is not gauge invariant. It is a boundary
condition or an asymmetric apparatus resource.

The distinction is therefore exact:

- the invariant frame is source-symmetric but can be consumed by noncentral
  relational use;
- the sharp frame is exactly reusable for the based pulse but supplies an
  external orientation;
- a gauge-averaged pulse needs neither resource but loses element resolution.

## What the data sees when the frame is forgotten

Tracing out the reference gives

\[
\Lambda_p(\rho)=\sum_r p_rW_r\rho W_r^\dagger.
\]

For the uniform invariant frame this is a conjugacy-twirled random-unitary
channel. The data does not receive one based element pulse. It receives an
average over all conjugate pulses.

The information missing from the data has not disappeared. It has been written
into the reference coherence and, for general inputs, into data-reference
correlation. The frame is therefore an output port of the constructor, not
clean workspace that may be silently discarded.

## Repeated use is a dynamical resource problem

The one-use return probability is not a scalar budget that can simply be
multiplied across uses. After one pulse:

- the reference may be mixed;
- it may remain correlated with earlier data;
- its orientation coherences may depend on the addressed flux;
- a later pulse may encounter a different effective distribution and phase
  matrix.

An exact repeated-use analysis must propagate the complete reference channel,
not reset it by assumption. Restoration of the invariant frame must export the
which-orientation record to another system or erase it dissipatively. Either
route introduces a new physical port and fault domain.

## Compiler consequence

The abstract endpoint algebra does not reveal this cost. The algebra says which
operators generate the endpoint block algebra. The executable compiler must
also specify the reference carrier and its state transition.

Thus a physical noncentral gate should be typed as

\[
(\rho,\sigma_R)\longmapsto
V_q(\theta)(\rho\otimes\sigma_R)V_q(\theta)^\dagger,
\]

not merely as a data operator \(W_q(\theta)\). Projecting this constructor to a
data-only channel or to a scalar charge record loses the resource transition.

The correct equivalence notion for two implementations must therefore preserve
at least:

- the induced logical channel;
- the reference output state and correlations;
- covariance under the gauge action;
- the admitted reset or replenishment constructor;
- the fault locality of the reference path.

Equality of endpoint matrices on a frozen sharp frame is too weak.

## Fault implications

A noncentral relational pulse makes the frame a record of the addressed flux
class. This creates three distinct failure modes.

1. Frame dephasing turns coherent relational control into an incoherent
   conjugacy average.
2. A frame displacement conjugates all subsequent element-resolved ports and
   acts as a common-mode compiler fault.
3. An assumed reset can inject an unmodelled external orientation or erase a
   correlated record into the environment.

Checking only the data syndrome cannot diagnose all three. A fault-tolerant
compiler needs an independent relational reference check or a source-authorized
replenishment mechanism.

## General finite-group law

For any finite group \(G\), the uniform regular reference and a relational
phase addressed to an element whose conjugacy class has size \(k\) obey

\[
f_{\min}^{(q)}(\theta)
=1-\frac{4(k-1)}{k^2}\sin^2\frac\theta2.
\]

The result depends on the class size, not directly on \(|G|\). The group order
determines the reference dimension and multiplicities; conjugacy geometry
determines the one-use worst-case return.

## Exact falsifiers

- A noncentral pulse on the invariant regular frame claimed to have unit
  worst-case return probability at generic \(\theta\).
- A three-cycle \(\pi\)-pulse claimed to leave nonzero worst-case overlap with
  the initial invariant frame.
- A transposition \(\pi\)-pulse assigned return probability other than
  \(1/9\).
- A sharp boundary frame described as invariant under the left-regular action.
- The conjugacy-twirled data channel identified with one based element pulse.
- Repeated-use performance inferred solely from the one-use return number.
- Reference reset treated as free without an environment or replenishment port.
- Two compilers called equivalent from data-only scalar outputs while their
  reference transitions differ.

## Machine-readable result

```json
{
  "code": "invariant_relational_frame_one_use_cost",
  "group": "S3",
  "reference_dimension": 6,
  "return_test": "initial_pure_reference_projector",
  "general_class_formula": "1 - 4*(k-1)/k^2*sin(theta/2)^2",
  "identity": {"class_size": 1, "minimum_at_pi": 1},
  "transposition": {"class_size": 3, "minimum_at_pi": "1/9"},
  "three_cycle": {"class_size": 2, "minimum_at_pi": 0},
  "sharp_frame_exactly_reusable": true,
  "sharp_frame_gauge_invariant": false,
  "uniform_frame_gauge_invariant": true,
  "uniform_frame_exactly_catalytic_for_noncentral_control": false,
  "repeated_use_determined_by_one_use_return": false
}
```

## Deutschian explanation

The invariant frame contains every orientation with equal amplitude, but it
does not contain a freely reusable hidden orientation. A noncentral operation
must act differently in different orientation branches. Those differences
write a record into their relative phases. The reference has performed real
work and no longer has its original operational state.

The class size fixes how the record is distributed. For a three-cycle, half of
the orientations receive the phase and half do not, so a \(\pi\)-pulse makes
the two halves cancel completely against the original invariant state. For a
transposition, one third receive the phase, leaving incomplete cancellation.

The resource is not mysterious asymmetry hidden inside a symmetric state. It
is the reference coherence consumed by making an element-level distinction.

## Shared Carrier geometry and coefficient lens

The shared Carrier statement is that a constructor resolving a quotient label
must retain the reference port across which that label is defined. Forgetting
the port performs a quotient and can turn controlled transport into an
averaged channel.

The quantum coefficient lens supplies the specifically quantum content:

- coherent orientation amplitudes;
- controlled unitaries;
- entanglement with the data;
- return probability as a singular-value problem;
- and phase cancellation between reference branches.

An additive scalar lens can record averaged class weights but cannot represent
the consumed coherence. An ordered noncommutative lens is required for the
actual compiler transition.

## Claim boundary

This packet proves the exact one-use return law for the explicit relational
flux pulse and evaluates it for every conjugacy class of \(S_3\). It does not
construct a local Hamiltonian implementing the pulse, derive a multi-use
capacity, design a replenishment protocol, or prove fault-tolerant physical
control of the full endpoint algebra.

## Process calibration

Excitement is 10/10. Confidence in the finite theorem is 10/10. The information
gain is high because the earlier qualitative catalytic obstruction now has an
exact resource curve and a saturating witness. The next question is whether a
fault-tolerant compiler can replenish or encode this relational frame without
reintroducing an undetectable common-mode orientation fault.
