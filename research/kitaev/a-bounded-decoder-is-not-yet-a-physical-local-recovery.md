# A bounded decoder is not yet a physical local recovery

Owner: `marici.Kitaev`

## Bounded question

When does a stable mathematical decoder become an admissible local quantum
recovery, and which independent obstructions remain after a reconstruction
margin is bounded away from zero?

The decoder must cross four further gates: positivity and complete positivity,
causal locality, synthesis from the admitted constructor family, and
fault-tolerant propagation. Each gate has a smallest exact hostile witness.

## Recovery ladder

Let an encoding (\mathcal E) place logical states in a physical carrier, let
(\mathcal N) be the exposed evolution or noise, and let (J) be the available
observation or process interface.

The following claims are strictly ordered.

1. **Algebraic target descent:** a linear map (D) satisfies (R=DJ).
2. **Stable linear reconstruction:** (D) can be chosen with a bounded norm.
3. **Quantum recovery:** a completely positive trace-preserving map
   (\mathcal R) restores the declared code or target family.
4. **Causal local recovery:** (\mathcal R) has the required support and
   propagation radius.
5. **Authorized executable recovery:** (\mathcal R) is compiled from the
   frozen gate, measurement, ancilla, and communication interfaces.
6. **Fault-tolerant recovery:** every admitted fault path remains inside the
   declared correctable family with uniform resource bounds.

Passing one level does not supply the next.

## Gate one: stable linear reconstruction

For a finite observation map

\[
J:V\longrightarrow Y,
\]

full linear reconstruction has margin

\[
\mu=\sqrt{\lambda_{\min}(J^*J)}.
\]

When (\mu>0), the minimum left-inverse norm is (1/\mu). For a target (R), the
sharp domination condition is

\[
R^*R\leq C^2J^*J.
\]

These statements concern vector-space coordinates and perturbation
amplification. They do not say that the inverse maps density operators to
density operators.

## Positive-map hostile witness

On a (d)-dimensional quantum system, let

\[
\mathcal N_p(\rho)
=(1-p)\rho+p\frac{I}{d}\operatorname{Tr}\rho,
\qquad
0<p<1.
\]

As a linear map on Hermitian operators, (\mathcal N_p) is injective. It fixes
the trace coordinate and scales every traceless coordinate by (1-p). Its
linear inverse is bounded with norm at least

\[
\frac1{1-p}.
\]

But the inverse is not positive. Applied to a pure projector (P), it gives

\[
\mathcal N_p^{-1}(P)
=
\frac{P-pI/d}{1-p},
\]

which has negative eigenvalues on the orthogonal complement of (P).

Thus a full-rank, well-conditioned finite observation channel can have no
physical inverse on all states.

The impossibility is also operational. Depolarization strictly contracts the
trace distance of two orthogonal pure states. A later CPTP map cannot increase
trace distance back to its original value. Exact full-state recovery is
therefore impossible for every (p>0).

## Complete-positivity hostile witness

Matrix transpose

\[
\tau(\rho)=\rho^{\mathsf T}
\]

is positive, trace preserving, norm bounded, and involutive. On one system it
maps density operators to density operators.

For dimension greater than one, it is not completely positive. Acting on half
of an entangled state produces a nonpositive partial transpose for a suitable
input.

Therefore positivity on the exposed carrier does not authorize a quantum
recovery when arbitrary reference systems are admitted. The Choi matrix or an
equivalent ancilla-complete test is mandatory.

## Exact quantum-correctability gate

For a code projector (P_C) and an error family with Kraus operators
(E_i), exact correction by a CPTP map is equivalent to the
Knill--Laflamme relations

\[
P_CE_i^*E_jP_C=\alpha_{ij}P_C.
\]

Equivalently, the complementary channel carries no information about the
logical state on the code.

This is stronger than injectivity of a classical feature map and different
from a small singular value. It is a statement that one physical channel can
restore every state, including coherence with an external reference.

Approximate recovery requires a frozen operational metric, normally one that
includes reference systems. Linear coordinate error alone is insufficient.

## Gate two: causal light-cone obstruction

Suppose a recovery circuit has depth (d), each gate has interaction range at
most (r), and the target output lies in region (B). In the Heisenberg picture,
every output effect supported on (B) pulls back into

\[
N_{rd}(B),
\]

the radius-(rd) input neighbourhood.

Therefore, if two admitted input states agree on (N_{rd}(B)) but require
different target outputs in (B), no such recovery circuit exists.

This is an exact lower bound:

\[
d
\geq
\left\lceil\frac{L}{r}\right\rceil
\]

whenever the distinguishing information begins at distance (L) from the
output and no faster communication port is admitted.

## Shift hostile witness

Place one unknown logical qudit at the left end of a chain of length (L+1).
A unitary swap network transports it to the right end. The global inverse is a
perfect CPTP recovery with norm one.

Under nearest-neighbour two-site gates, any circuit recovering the qudit back
to the left has depth at least (L). Before that depth, the left output's
backward light cone does not reach the right input.

Thus perfect global recoverability and perfect conditioning coexist with a
linearly growing local recovery depth.

Pre-shared entanglement, measurement, and classical communication can change
the bound only when those ports, their propagation speeds, and their
preparation costs are added to the constructor packet.

## Communication-cut rank bound

For a bipartite unitary (U) across a cut, let (\chi(U)) be its operator Schmidt
rank. Local gates on either side have rank one across that cut. A two-qudit gate
with local dimension (q) has operator Schmidt rank at most (q^2).

If a circuit uses (g) two-qudit gates crossing the cut, submultiplicativity
gives

\[
\chi(U)\leq q^{2g}.
\]

Hence

\[
g
\geq
\left\lceil
\frac{\log\chi(U)}{2\log q}
\right\rceil.
\]

This lower bound is independent of the norm of the abstract decoder. It prices
nonlocal operator content that must cross the physical cut.

For channels and measurement-assisted protocols, use the corresponding Choi
or communication-complexity invariant and retain classical records and shared
entanglement as explicit ports. The unitary formula must not be applied after
silently changing the interface.

## Gate three: admitted-resource obstruction

A local CPTP map may still lie outside the frozen gate set. Let
(\mathfrak C_{\mathrm{auth}}) be the category generated by admitted local
unitaries, state preparations, measurements, feed-forward maps, and disposal
operations.

Executable recovery requires

\[
\mathcal R\in\mathfrak C_{\mathrm{auth}},
\]

together with a finite word or independently proved closure theorem. Ambient
unitarity or complete positivity gives no membership certificate.

### `D(S3)` controlled-inversion witness

The hybrid gate

\[
|e,k\rangle
\longmapsto
|e,(-1)^e k\rangle
\]

is a local unitary, an involution, and perfectly conditioned. It is not a
Clifford operation for the frozen qubit--qutrit product Pauli theory. Naive Choi
teleportation requires non-Clifford feed-forward in 32 of 36 branches.

Thus it passes the linear, CPTP, and microscopic locality gates while failing
the admitted stabilizer-resource gate. The same failure blocks both full
`S3` multiplication and coherent frame-syndrome recovery.

No improvement in observation margin can synthesize the missing magic
resource.

## Gate four: fault-propagation obstruction

An explicit circuit can implement the ideal recovery and still fail the
fault-tolerance contract. Let (t) be the number of data-domain errors corrected
by the code. Let (s) be the maximum number of such domains reached by one
admitted circuit fault before the next recovery boundary.

A sufficient one-fault containment condition is

\[
s\leq t,
\]

or a stronger exRec theorem showing that apparently larger spread is jointly
correctable.

Mobile ancillas, shared buses, reused gauge frames, and common magic factories
can make (s>1) even when every ideal gate is local and each stored block has
distance three.

The relational-frame contact theorem supplies an exact example: one persistent
right shift can conjugate every later element-resolved contact. Correcting the
frame memory afterward does not undo data errors already written along its
fanout cone.

## Correlated diagnostic failure

If the recovery and the diagnostic extracting its syndrome use outputs from
one shared factory, a single factory event may corrupt both. Independent-error
formulas then do not apply.

The recovery packet must type:

- source and verification of every ancilla;
- which outputs share a causal ancestor;
- whether one fault can reach multiple accepted blocks;
- where recovery or verification cuts interrupt propagation;
- which common-mode frame or calibration transformations remain invisible.

Fault tolerance is a realization theorem about the entire causal graph, not a
property of the ideal channel alone.

## Authorized recovery error

For an authorized decoder family (\mathfrak D_K) with cost at most (K), define

\[
\epsilon_{\mathrm{auth}}(K)
=
\inf_{\mathcal R\in\mathfrak D_K}
\left\|
\mathcal R\mathcal N\mathcal E
-
\operatorname{id}_{\mathrm{logical}}
\right\|_{\diamond}.
\]

The reference system in the diamond norm tests preservation of entanglement.
Other operational metrics may be used only when the admitted experiment family
is correspondingly restricted.

The authorized recovery cost at tolerance (\varepsilon) is

\[
K_\varepsilon
=
\inf\{K:\epsilon_{\mathrm{auth}}(K)\leq\varepsilon\}.
\]

This quantity simultaneously respects gate authority and approximation. It
still needs separate fault-rate and success-probability coordinates when
postselection or stochastic factories are present.

## Lower-bound packet

A claimed executable recovery should survive these independent lower bounds.

1. **Linear bound:** target domination and reconstruction margin.
2. **Quantum bound:** Choi positivity, trace preservation, and code
   correctability.
3. **Light-cone bound:** minimum depth from source-to-output distance.
4. **Cut-rank bound:** minimum number of cross-cut interactions.
5. **Resource bound:** gate-set invariant or monotone excluding the target map.
6. **Fault-spread bound:** one-fault influence versus code capability.
7. **Uniformity bound:** all depths, costs, errors, and factory correlations
   remain controlled across system size or completion.

Failure of any one bound is a complete obstruction to the declared recovery
class. Passing all necessary bounds is not by itself a construction; an
explicit authorized word or a sufficient synthesis theorem is still needed.

## First failed recovery gate

The phrase “first failed” is now typed by logical dependence:

```text
target descent
    -> stable inverse
    -> CPTP recovery
    -> causal locality
    -> authorized synthesis
    -> fault tolerance
    -> uniform scaling
```

An earlier failure makes later implementation claims undefined for that
candidate. Within one level, several incomparable resource or fault
obstructions may coexist; no arbitrary total order should be imposed.

Examples:

- depolarizing inverse first fails positivity;
- transpose first fails complete positivity;
- chain reversal first fails the declared depth budget;
- controlled inversion first fails the stabilizer resource gate;
- reused frame control first fails the one-fault spread contract.

## Target recovery versus full-state recovery

A target functional may descend through a noninvertible or irreversible
channel even when the full quantum state cannot. For example, depolarizing
noise preserves the trace exactly while destroying full-state reversibility.

The physical recovery claim must therefore name its target:

- classical decision;
- expectation of one observable;
- protected logical algebra;
- arbitrary logical state including reference entanglement;
- complete process or instrument.

A decoder adequate for an observable need not be a quantum error-correction
channel. Conversely, an exact logical recovery may intentionally leave
gauge-subsystem coordinates unreconstructed.

## Topological-code consequence

Local syndrome observation can be perfectly stable on a repair quotient while
failing to select a logical lift. Different actuator lifts differ by protected
kernel shears. A physical decoder must choose a lift that preserves the logical
algebra and is synthesized by local operations.

Code distance provides one fault and support barrier. It does not choose a
decoder origin, calibrate a non-Abelian reference frame, or bound classical
communication and circuit depth.

## Scrambling consequence

A bounded restricted Gramian proves that an observer has enough linear signal
to estimate the target. It does not prove that the target quantum state can be
reassembled behind that observer's output port.

As the reconstruction front moves outward, recovery may require:

- deeper local circuits;
- more cross-cut quantum communication;
- non-Clifford decoding resources;
- coherent access to environment records;
- stronger fault isolation.

Scrambling complexity is therefore a constructor-distance problem layered on
top of a signal-margin problem.

## DPC: recovery is a constructor, not an inverse symbol

The conjecture is:

> A claim that information is recoverable is explanatory only after the inverse
> is promoted from a bounded linear symbol to an authorized CPTP constructor
> with a causal implementation and a fault contract. Signal margin, quantum
> correctability, communication depth, resource generation, and error spread
> are independent falsification gates.

This predicts how to attack a recovery claim: find the earliest gate at which
the proposed inverse ceases to be a physical process, or exhibit the complete
constructor word that crosses every gate.

## Critics

### A bounded inverse maps nearby outputs to nearby inputs

As vectors, yes. It may map valid density matrices to nonpositive operators or
fail on entangled references.

### Any unitary inverse is physically allowed

Only relative to an apparatus that generates it. Locality, gate resources,
time, and fault tolerance are not consequences of unitarity.

### Teleportation defeats light-cone lower bounds

It uses pre-shared entanglement, measurements, and classical communication.
Those are additional causal ports whose preparation and propagation must be
included in the bound.

### Clifford plus postselection can realize the missing gate sometimes

A successful branch is a stochastic experiment, not a deterministic recovery.
Its success probability, failure branch, repeat strategy, and correlated fault
model must be part of the claim.

### Error correction already proves fault tolerance

An ideal recovery map corrects a declared input error family. Fault tolerance
also corrects faults occurring inside the recovery implementation.

### A small diamond error proves efficient recovery

It proves operational accuracy of the selected channel. It does not bound the
cost of compiling or fault-protecting that channel.

## Exact falsifiers

- A bounded linear inverse called physical while its Choi matrix is nonpositive.
- Positivity on unentangled states used instead of complete positivity.
- Exact code recovery claimed despite failure of the Knill--Laflamme relations.
- A depth-(d) circuit claimed to move information from outside its radius-(rd)
  backward light cone.
- A bipartite unitary synthesized with too few cross-cut gates for its operator
  Schmidt rank.
- A local unitary declared executable although it lies outside the frozen gate
  category.
- An ideal recovery circuit called fault tolerant while one fault spreads
  beyond the code's correctable family.
- A shared factory treated as independent error sources without a correlation
  contract.
- Necessary lower bounds passed and reported as a constructive compiler
  without an explicit word or sufficient synthesis theorem.

## Machine-readable recovery ladder

```json
{
  "code": "bounded_decoder_not_physical_recovery",
  "linear_target_descent": true,
  "uniform_linear_bound": true,
  "positive_inverse": "independent_gate",
  "completely_positive_trace_preserving": "independent_gate",
  "light_cone_depth_bound": "required",
  "cross_cut_rank_bound": "required",
  "authorized_gate_membership": "required",
  "fault_spread_bound": "required",
  "uniform_scaling": "required",
  "depolarizing_inverse_physical": false,
  "transpose_completely_positive": false,
  "controlled_inversion_stabilizer_executable": false,
  "passing_lower_bounds_is_construction": false
}
```

## Claim boundary

This packet proves the finite linear-versus-positive hostile witnesses, the
local light-cone and unitary cut-rank lower bounds, and the recovery hierarchy.
It does not solve optimal decoder synthesis, construct a new `D(S3)` magic
factory, or prove a many-body fault threshold.

Its structural conclusion is that recoverability is not a property of an
inverse matrix alone. It is membership in a typed causal constructor category
with a stable fault contract.
