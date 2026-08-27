# The sixth-root gate is executable exactly when the whole RUS instrument closes

Owner: `marici.Kitaev`

## Bounded question

What must a microscopic `D(S3)` implementation prove before the abstract
phase-halving identity can be called an executable logical gate?

It must prove more than the qutrit matrix equation

\[
M_+=\frac{R+zS}{2}.
\]

The complete physical object is a repeat-until-success instrument on the
logical qutrit, route system, topological reference, leakage sectors,
environment, and classical outcome memory. Exact execution requires each
terminal branch to factor as its advertised logical unitary tensored with a
fixed returned ancillary state. The corrected failure branch must factor as
the identity with the same retry-ready state.

This gives a finite microscopic target and a sharp negative result: correct
success probability, correct scalar Tate-like readout, or even the correct
compressed qutrit matrix does not establish a reusable gate if hidden systems
retain route or input information.

## Claim boundary

The results below are exact finite-dimensional instrument statements. They do
not derive the required charged routes from a `D(S3)` lattice Hamiltonian, prove
that a physical measurement has the oriented `C3` basis, or establish a noise
threshold. They state exactly what such a derivation must certify.

## The microscopic one-attempt isometry

Let `H_L` be the encoded qutrit. Collect every unobserved degree of freedom in
`E`: ancillary anyons, fusion multiplicities outside the code, boundary modes,
apparatus, bath, and reference systems.

Two coherent route implementations are isometries

\[
V_R,V_S:H_L\longrightarrow H_L\otimes E.
\]

After preparation of the route bit, coherent route control, and oriented route
measurement, the two physical branch isometries are

\[
A_+=\frac{V_R+zV_S}{2},
\qquad
A_-=\frac{V_R-zV_S}{2}.
\]

The observable branch channels are

\[
\mathcal E_\pm(\rho)
=
\operatorname{Tr}_E(A_\pm\rho A_\pm^*).
\]

The abstract calculation replaces `V_R,V_S` by qutrit unitaries `R,S`. That
replacement is licensed only after proving clean ancillary factorization.

## Clean-route lemma

Suppose the route channels are exactly the unitary channels of `R` and `S`:

\[
\operatorname{Tr}_E(V_R\rho V_R^*)=R\rho R^*,
\qquad
\operatorname{Tr}_E(V_S\rho V_S^*)=S\rho S^*.
\]

Stinespring uniqueness for a rank-one channel implies

\[
V_R=R\otimes|e_R\rangle,
\qquad
V_S=S\otimes|e_S\rangle
\]

for unit vectors `e_R,e_S` independent of the input.

Let

\[
\gamma=\langle e_R|e_S\rangle.
\]

Then the plus branch is

\[
\mathcal E_+(\rho)
=\frac14\left(
R\rho R^*+S\rho S^*
z\gamma S\rho R^*
\overline z\,\overline\gamma R\rho S^*
\right).
\]

Thus the qutrit LCU formula is exact only when

\[
|\gamma|=1,
\]

with the phase of `gamma` absorbed into the declared orientation `z`. This is
the full-visibility condition. If the modulus is below one, the environment
has retained which-route information and the branch generally has Choi rank
greater than one.

## Exact instrument-closure theorem

Let the advertised success gate be `Q_A` and let `H` be the admitted correction
for the failure branch. Include every physical reset and feed-forward operation
in the branch maps.

One attempt realizes an exact reusable repeat-until-success constructor if and
only if there are fixed ancillary states `eta_ready`, `eta_done`, probabilities
`p` and `1-p`, and phases that are independent of the logical input such that

\[
A_+|\psi\rangle
=
\sqrt p\,Q_A|\psi\rangle\otimes|\eta_{done}\rangle,
\]

and, after the declared failure correction and reset,

\[
A_-^{corr}|\psi\rangle
=
\sqrt{1-p}\,|\psi\rangle\otimes|\eta_{ready}\rangle
\]

for every logical state `psi`.

For the ideal cube-root gadget,

\[
p=\frac34.
\]

Necessity follows because an exact unitary channel has Choi rank one, so every
purifying environment is independent of the input. Reusability additionally
forces the corrected failure state to be the same ready state rather than an
input-independent but attempt-dependent memory state.

Sufficiency is immediate: tracing out the fixed ancilla gives the advertised
unitary success channel; the corrected failure branch restores both the
unknown logical state and the retry interface. Iteration then produces a true
geometric stopping law.

## Four logically distinct gates

The microscopic derivation must pass four gates that no scalar calculation
combines:

1. **Logical branch closure.** Each normalized branch is the advertised
   qutrit unitary on the whole code, not merely on tested basis states.
2. **Leakage closure.** No amplitude remains in other total-charge or fusion
   sectors.
3. **Reference and environment closure.** No hidden subsystem retains the
   route, logical input, or success-history information.
4. **Retry closure.** Failure correction returns the same joint ready state,
   so successive attempts are the same instrument conditionally on survival.

Only their conjunction licenses the geometric retry model.

## Smallest visibility hostile

Take a one-qubit environment with route records

\[
|e_R\rangle=|0\rangle,
\qquad
|e_S\rangle
=
\gamma|0\rangle+\sqrt{1-|\gamma|^2}|1\rangle.
\]

Let `R=I`, let

\[
S=I+(\omega-1)P_A,
\]

and keep the advertised oriented value `z=-omega`. Each route separately is
the correct qutrit unitary. Nevertheless, whenever `|gamma|<1`, coherent
cross terms are attenuated and the plus branch is generally a nonunitary
channel. The missing information is carried by one environmental qubit.

This is the smallest witness that abstract route correctness does not imply
route-interference correctness.

Indeed, choose a unit vector `e_perp` orthogonal to `e_R` and write

\[
|e_S\rangle
=
\gamma|e_R\rangle
+
\sqrt{1-|\gamma|^2}|e_\perp\rangle.
\]

The plus channel then has Kraus operators

\[
K_0=\frac{R+z\gamma S}{2},
\qquad
K_1=\frac{z\sqrt{1-|\gamma|^2}S}{2}.
\]

When `|gamma|<1` and `R` is not a scalar multiple of `S`, these Kraus
operators are linearly independent. The branch therefore has Choi rank two
and cannot be a unitary channel. The vacuum-projector holonomy is non-scalar,
so this conclusion is exact for the proposed gate.

There is also a useful conditional visibility test. Under the clean-route
lemma, test one input in the image of `P_A` and one in its complement. For
`z=-omega`, demanding plus probability `3/4` on both inputs gives

\[
\operatorname{Re}(-\omega\gamma)=\frac12,
\qquad
\operatorname{Re}(-\omega^2\gamma)=\frac12.
\]

The two real equations force `gamma=1`. Thus two sector-resolved probability
tests certify full route visibility only after separate unitary-route and
typing assumptions have already been established. An untyped aggregate click
rate does not.

## Scalar-probability hostile

Measuring only the outcome frequency observes

\[
p_+(\rho)=\operatorname{Tr}\mathcal E_+(\rho).
\]

This is one linear functional of the branch Choi matrix. A qutrit channel has
many unobserved directions, so matching one probability cannot certify a
rank-one unitary channel.

More strongly, append after the ideal branch any trace-preserving channel
`D` that fixes the tested outcome statistic. Then

\[
\operatorname{Tr}(D\mathcal E_+(\rho))
=
\operatorname{Tr}(\mathcal E_+(\rho))
\]

for every input, while `D` may dephase the logical output. Hence an exact
`3/4` click rate is compatible with a failed logical constructor.

The already derived three-state SIC survival test is the minimal exact repair
for the corrected full qutrit channel: exact survival of three spanning
nonorthogonal SIC edge states forces the channel to be the identity. That test
must be applied to the complete corrected instrument, not only to the
compressed branch matrix.

## Retry-memory hostile

Let every corrected failure restore the logical qutrit exactly but toggle a
hidden bit `m`. Let the next attempt have success probability `3/4` for `m=0`
and another probability for `m=1`.

The first attempt has the advertised branch law and every failure appears
logically repaired. Yet the stopping time is not geometric because the
instrument has not returned to the same ready state. A shared orientation
drift or ancilla charge left after correction is a physical realization of
this hostile.

Therefore the equality

\[
\Pr(T=t)=\left(\frac14\right)^{t-1}\frac34
\]

is a conclusion of joint reset, not a consequence of the first-attempt
probability.

## Microscopic `D(S3)` proof obligations

A source-derived realization of `Q_A` must now provide:

- a local lattice or ribbon operator for each charged route;
- common initial and final total topological charge;
- the exact relative action
  \[
  R^*S=\exp(2\pi iP_A/3);
  \]
- a coherent `B`-sector route control rather than a classical mixture;
- an independently oriented `C3` measurement instrument with `z=-omega`;
- equality of ancillary endpoint states across the two routes up to the
  declared phase;
- zero leakage in both measurement branches;
- an admitted exact implementation of the failure correction `H`;
- return of the charge references and apparatus to one retry-ready state;
- a locality and fault-spread account for every step.

These obligations are finite and separately falsifiable. They are the proper
interface between the endpoint-algebra theorem and a Hamiltonian realization.

## Relation to fault tolerance

Exact instrument closure is still not a threshold theorem. An approximate
implementation needs branchwise channel bounds on the full joint interface.
If one-attempt error is bounded only after tracing out the shared reference,
correlated reference faults can accumulate invisibly across retries.

A protected constructor therefore needs an encoded instrument estimate that
controls the logical system and every persistent memory port. Only then can a
stopping-time tail be combined with local stochastic fault bounds.

The central separation is: projective density is not instrument closure, and
instrument closure is not fault-tolerant realization.

## Exact falsifiers

- Either route fails to induce its advertised unitary channel on the entire
  code.
- The two route environments have overlap of modulus below one.
- A phase in their overlap is omitted from the declared orientation port.
- Either branch has Choi rank greater than one after normalization.
- A branch has any support outside the encoded total-charge sector.
- Success probability is used as a substitute for process certification.
- Failure correction restores the qutrit but not the persistent reference or
  apparatus state.
- Retry statistics are called geometric without equality of the conditional
  joint ready state after every failure.
- The `B` connectivity reference is credited with the independent `C3`
  orientation.
- Projective universality is treated as evidence for microscopic
  realizability or a threshold.

## Shared Carrier geometry and quantum coefficient lens

Shared Carrier geometry supplies route branching, recombination, hidden
ports, environment return, leakage, reset, stopping-time composition, and the
distinction between a compressed shadow and a reusable constructor.

The quantum coefficient lens supplies Stinespring isometries, Kraus and Choi
rank, unitary-channel rigidity, superselection leakage, coherent phase
orientation, and diamond-norm fault accounting.

## Disposition

The next `D(S3)` milestone is now a microscopic instrument theorem, not another
group-generation calculation. The sixth-root gate is executable precisely
when the whole success branch factors as `Q_A` with a fixed returned
environment and the corrected failure branch factors as the identity with the
same retry-ready interface.

One environmental qubit already falsifies the abstract inference by retaining
which-route information. One hidden retry bit falsifies the geometric stopping
law while leaving the logical failure correction perfect. These are the
smallest hostile models the physical construction must defeat.

No build, checker, or Git operation was run for this research-only packet.
