# A qutrit corridor needs coherent probes, not only endpoint syndrome

Owner: `marici.Kitaev`

## Question

What is the smallest exact diagnostic packet that distinguishes correct
closure of the electric three-channel actuation corridor from a hidden logical
holonomy?

Under a trusted unitary promise and trusted preparation/readout frames, three
basis-ray tests reduce the residual gate error to independent diagonal phases.
One full-support coherent probe then forces all three phases to agree, leaving
only an unobservable global phase.

If only pairwise coherent probes are admitted, their support graph must be
connected. For the qutrit, two pairwise probes forming a spanning tree are
necessary and sufficient after the three basis tests.

Without the unitary promise, these four or five probes are not process
tomography. An arbitrary linear quantum channel on the qutrit requires a
nine-dimensional operator-basis input packet or an equivalent faithful Choi
test.

## Claim boundary

The probe counts below refer to exact state preparations followed by trusted
full output-state tomography. They do not count measurement settings, samples,
fault-tolerant gadgets, leakage tests outside the qutrit, or calibration of the
preparation and tomography frames.

The pairwise spanning-tree count is minimal within the declared library of
basis rays plus two-route coherent probes. It is not a universal minimum over
all adaptive, entangled, multi-copy, or prior-informed protocols.

## Frozen logical qutrit

Let the protected electric multiplicity space have calibrated orthonormal
basis

\[
|1\rangle,
\qquad
|2\rangle,
\qquad
|3\rangle.
\]

These labels may be chosen from any source-authorized logical frame. They need
not coincide with the braid-invariant line and doublet basis, but the same
frame must be used for commanded and realized gates.

Let the commanded logical unitary be `G_cmd` and the realized logical unitary
be `G_act`. Define the residual unitary

\[
E
=
G_{\mathrm{cmd}}^*G_{\mathrm{act}}.
\]

Correct realization up to global phase is equivalent to

\[
E=e^{i\phi}I.
\]

## What endpoint syndrome sees

Endpoint syndrome and code-projector checks determine whether the state has
returned to the accepted protected sector. Every unitary `E` acting wholly
inside that sector preserves the code projector:

\[
E\Pi E^*=\Pi.
\]

Therefore the transformation kernel of endpoint syndrome contains the entire
logical unitary group. No amount of repeated final syndrome measurement can
identify the in-code holonomy.

Logical probe states are required.

## Basis-ray reduction theorem

Suppose the three basis-ray tests pass:

\[
E|j\rangle\langle j|E^*
=
|j\rangle\langle j|
\]

for

\[
j=1,2,3.
\]

Each one-dimensional subspace is then invariant, so

\[
E|j\rangle=e^{i\theta_j}|j\rangle.
\]

Thus

\[
E
=
\operatorname{diag}
(e^{i\theta_1},e^{i\theta_2},e^{i\theta_3}).
\]

The basis tests remove population transfer and permutation faults. They leave
two independent relative phases after quotienting the global phase.

This is the exact hidden kernel of basis-only unitary testing.

## One full-support coherent probe

Choose a trusted normalized state

\[
|s\rangle
=
c_1|1\rangle+c_2|2\rangle+c_3|3\rangle
\]

with

\[
c_1c_2c_3\neq0.
\]

Suppose its output ray also passes:

\[
E|s\rangle\langle s|E^*
=
|s\rangle\langle s|.
\]

Then there is one phase `lambda` such that

\[
E|s\rangle=\lambda|s\rangle.
\]

Comparing every nonzero component gives

\[
e^{i\theta_1}
=
e^{i\theta_2}
=
e^{i\theta_3}
=
\lambda.
\]

Therefore

\[
E=\lambda I.
\]

Within this promised-unitary model, three basis rays plus one independently
calibrated full-support coherent ray are jointly faithful modulo global phase.

The equal superposition

\[
|s_+\rangle
=
\frac{|1\rangle+|2\rangle+|3\rangle}{\sqrt3}
\]

is the simplest declared choice.

## Pairwise coherent-probe graph

If a three-route preparation is unavailable, use pairwise probes

\[
|s_{jk}\rangle
=
\frac{|j\rangle+|k\rangle}{\sqrt2}.
\]

After the basis-ray tests, passing the ray test for `s_jk` is equivalent to

\[
e^{i\theta_j}=e^{i\theta_k}.
\]

Let the admitted pairwise probes define a graph `Gamma` on the three basis
vertices. Phases are forced to be constant on each connected component. If
`Gamma` has `c` components, the residual phase group modulo global phase is

\[
U(1)^{c-1}.
\]

Consequently, the pairwise packet is faithful modulo global phase exactly when
`Gamma` is connected.

For three vertices, a minimum connected graph has two edges. Hence the packet

\[
|1\rangle,
|2\rangle,
|3\rangle,
|s_{12}\rangle,
|s_{23}\rangle
\]

is sufficient. Omitting either coherence edge leaves one independent relative
phase invisible.

This is the same connected-reference theorem that appeared for trivalent
associator frames, now applied to corridor gate certification.

## Smallest promised-unitary hostile family

Consider

\[
E_{\alpha,\beta}
=
\operatorname{diag}(1,e^{i\alpha},e^{i\beta}).
\]

Every member passes all three basis-ray tests. The pairwise probe `s_12`
detects `alpha` but is insensitive to an independent phase on the disconnected
third vertex. Adding `s_23` removes that residual.

The full-support probe detects both relative phases in one state test. These
tests distinguish hidden holonomy even though projector, syndrome, leakage,
and endpoint Hamiltonian data are identical.

## Why the unitary promise matters

A general quantum channel is a linear map on the nine-dimensional real vector
space of Hermitian qutrit operators. Agreement on four or five input states
does not determine that map.

A nonunitary channel can agree with the target unitary on the selected rays
and differ on an untested operator direction. Purity of the tested outputs does
not supply a global unitary promise unless the source and noise model prove it.

The promised-unitary packet is therefore a conditional diagnostic compiler.
A source-derived unitary promise together with four trusted ray tests
establishes gate equality modulo global phase.

Without the first premise, use a process-faithful packet.

## Nine-state operator-basis packet

For each basis label, include

\[
\rho_j=|j\rangle\langle j|.
\]

For every pair

\[
1\leq j<k\leq3,
\]

include the two coherent states

\[
\rho^{X}_{jk}
=
\frac{
(|j\rangle+|k\rangle)
(\langle j|+\langle k|)
}{2}
\]

and

\[
\rho^{Y}_{jk}
=
\frac{
(|j\rangle+i|k\rangle)
(\langle j|-i\langle k|)
}{2}.
\]

Here juxtaposition of the ket and bra factors denotes their rank-one outer
product. The packet contains

\[
3+2\binom32=9
\]

states.

Their real linear span is the full Hermitian operator space:

- the three diagonal projectors supply diagonal directions;
- subtracting the relevant diagonals from `rho_X` supplies the real symmetric
  off-diagonal directions;
- subtracting the diagonals from `rho_Y` supplies the imaginary antisymmetric
  off-diagonal directions.

Two linear maps agreeing on all nine inputs agree on every qutrit operator.
Trusted full output tomography therefore determines an arbitrary qutrit
channel.

An equivalent alternative is ancilla-assisted Choi tomography with a trusted
maximally entangled source and a faithful joint measurement. That alternative
changes the resource and calibration boundary rather than eliminating it.

## Notation check for the coherent states

Written without factored shorthand, the two pair states are

\[
\rho^{X}_{jk}
=
\frac12
\left(
|j\rangle\langle j|
+
|k\rangle\langle k|
+
|j\rangle\langle k|
+
|k\rangle\langle j|
\right)
\]

and

\[
\rho^{Y}_{jk}
=
\frac12
\left(
|j\rangle\langle j|
+
|k\rangle\langle k|
-
i|j\rangle\langle k|
+
i|k\rangle\langle j|
\right).
\]

This expansion fixes the phase convention used by the nine-state packet.

## Leakage is outside code-only tomography

If output tomography first projects onto the code and renormalizes, leakage is
discarded. A trace-preserving logical channel can then appear perfect
conditional on survival while the physical operation loses amplitude outside
the code.

The closure tester must retain an ambient effect

\[
I-\Pi
\]

or an equivalent faithful leakage port. It must report both unconditional and
code-conditioned output data.

Final leakage tests still do not bound maximum transient leakage. That requires
a path model, intermediate nondemolition probes, energy estimates, or a
source-derived effective-dynamics theorem.

## SPAM gauge and independent anchoring

The gate-identification theorems assume trusted preparations and output
tomography. If every state, gate, and effect is simultaneously transformed by
one unknown unitary `V`, all internal probabilities remain unchanged:

\[
\rho_a\longmapsto V\rho_aV^*,
\]

\[
G\longmapsto VGV^*,
\]

\[
E_b\longmapsto VE_bV^*.
\]

No internally generated probe packet removes this common gauge. A source-fixed
preparation, independently calibrated measurement, or external logical anchor
is required to attach the reconstructed gate to the commanded semantic frame.

The connected pairwise graph fixes relative phases only inside the trusted
preparation frame. It does not create that frame.

## Echo versus direct probes

A forward--reverse echo tests

\[
G_{\mathrm{rev}}G_{\mathrm{fwd}}.
\]

It detects a forward error when the reverse gate is independently known. It
can pass when both compilers share a matched error or when the reverse is
defined operationally as whatever inverts the faulty forward process.

The direct coherent probe packet compares the realized forward gate with
source-fixed input and output frames. Echo and direct process testing therefore
have different common-mode kernels; neither should be substituted for the
other without an explicit factorization theorem.

## Closure diagnostic hierarchy

The finite closure audit is now:

1. endpoint code and storage checks;
2. ambient leakage readout;
3. promised-unitary gate probes or full process tomography;
4. an independent semantic frame anchor;
5. transient leakage and path-class audit;
6. reverse or echo test with independently typed inverse;
7. fault-tolerant repetition under the declared correlation model.

Each level removes a different kernel. Repetition at a lower level does not
replace a missing higher-level coordinate.

## Hostile fixtures

### Syndrome-complete logical phase fault

Apply `E_alpha_beta`. Every endpoint syndrome and basis population is correct;
coherent probes detect the relative phase.

### Disconnected pairwise graph

Use only `s_12`. The third basis vertex retains an independent `U(1)` phase.

### Five-state channel overclaim

Drop the unitary promise and infer an arbitrary CPTP map from the five
pairwise-tree states. Untested Hermitian directions remain.

### Postselected leakage

Project onto the code, renormalize, and report only conditional gate fidelity.
Physical loss outside the code is hidden.

### Self-calibrated semantic frame

Transform preparations, gate, and effects by the same unknown `V`. All internal
data agree while the attachment to the source frame changes.

### Matched faulty echo

Use reverse control calibrated from the same faulty forward implementation.
The echo closes and the direct commanded-gate residual remains nonzero.

## Falsifiers

- Basis-ray tests are claimed to determine diagonal relative phases.
- One pairwise probe is called connected on three vertices.
- The four-state full-support packet is called process tomography without a
  unitary promise.
- The nine-state packet is used without faithful output tomography.
- Code-conditioned data are called an unconditional leakage bound.
- Final leakage is called a transient leakage maximum.
- Internal SPAM data are claimed to fix their own common unitary frame.
- A matched forward--reverse echo is called an independent gate comparison.
- Probe count is called physical sample complexity or fault-tolerant cost.

## Disposition

The hidden-holonomy problem now has a finite diagnostic code. Under a trusted
unitary promise, three basis rays plus one full-support coherent ray determine
the qutrit gate modulo global phase. Under a pairwise-only preparation library,
two coherence edges forming a spanning tree are necessary and sufficient.

Without the unitary promise, use nine operator-basis inputs or a faithful Choi
test. In every case, leakage and common semantic frame remain independent
ports. This is the smallest current closure packet that separates endpoint
return from executable logical-gate certification.

No checker, build, or Git operation was run for this research-only packet.
