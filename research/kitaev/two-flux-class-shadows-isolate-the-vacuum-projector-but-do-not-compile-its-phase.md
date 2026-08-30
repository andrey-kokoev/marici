# Two flux-class shadows linearly isolate the vacuum projector but do not compile its phase

Owner: `marici.Kitaev`

## Bounded question

After one simple-probe monodromy fails, do the transposition and three-cycle
Wilson shadows jointly determine the vacuum projector on the electric
`A,B,C` channel packet? If so, what extra constructor would turn that algebraic
identity into a coherent phase?

## Verdict

Yes in the linear readout family. Identity, transposition, and three-cycle class shadows form a basis of
the three-dimensional central function space on the electric charge labels.
The vacuum projector has the exact expansion

\[
P_A
=
\frac16 I
+
\frac12 W_\tau
+
\frac13 W_\rho.
\]

Consequently

\[
I-2P_A
=
\frac23 I
-W_\tau
-\frac23W_\rho.
\]

This closes the linear algebraic identification problem with two nontrivial
flux classes. Under polynomial context closure, one transposition shadow is
already sufficient because its three sector values are distinct. Neither
statement compiles the reflection. The Wilson shadows are scalar
contractions obtained after closing or tracing probe ports; they are not a
pair of coherently selectable unitary actuators on the qutrit.

## Frozen shadow table

On the electric charges `A,B,C`, use normalized class responses

\[
\begin{array}{c|ccc}
&A&B&C\\
\hline
I&1&1&1\\
W_\tau&1&-1&0\\
W_\rho&1&1&-\frac12
\end{array}
\]

The transposition row is the trivial, sign, and normalized standard character
on a transposition. The three-cycle row is the corresponding character data
on a three-cycle.

The three rows are linearly independent. Thus every central function of the
electric charge label has a unique expansion in this basis.

## Vacuum-projector derivation

Write

\[
P_A=aI+bW_\tau+cW_\rho.
\]

Evaluation on `A,B,C` gives

\[
a+b+c=1,
\]

\[
a-b+c=0,
\]

and

\[
a-\frac12c=0.
\]

The unique solution is

\[
a=\frac16,
\qquad
b=\frac12,
\qquad
c=\frac13.
\]

The reflection formula follows immediately.

This is the finite character-idempotent identity for the trivial
representation, restricted to the electric charge packet.

## Minimality inside the linear family

Identity plus only `W_tau` spans only a two-dimensional linear function space
and cannot fit the three conditions defining `P_A`. Direct substitution shows no coefficients
`a,b` satisfy

\[
a+b=1,
\qquad
a-b=0,
\qquad
a=0.
\]

Identity plus only `W_rho` cannot separate `A` from `B`, since both responses
are one.

Therefore both nontrivial conjugacy classes are necessary in this central
linear family.

This does not contradict the single-probe no-go. Joint linear faithfulness of
two scalar shadows is weaker than one-loop unitary realization.

## One transposition shadow suffices under polynomial closure

The values of `W_tau` on `A,B,C` are the three distinct numbers `1,-1,0`.
Lagrange interpolation therefore reconstructs every central function of these
three labels from powers of this one shadow.

The three charge projectors are

\[
P_A
=
\frac{W_\tau^2+W_\tau}{2},
\]

\[
P_B
=
\frac{W_\tau^2-W_\tau}{2},
\]

and

\[
P_C=I-W_\tau^2.
\]

Consequently

\[
I-2P_A
=
I-W_\tau-W_\tau^2.
\]

Thus the polynomial context tower of one transposition-class shadow is jointly
faithful on the three labelled electric channels. First-order actuation still
fails: `W_tau` itself has values `1,-1,0` and is not the unitary reflection.

This is the exact finite analogue of a context tower recovering distinctions
that one raw probe does not implement.

## Why the algebraic sum is not a pulse sequence

Sequential composition of Wilson shadows multiplies their eigenvalue
functions. It does not add them with coefficients `2/3,-1,-2/3`.

A classical mixture produces a convex combination of channels, not the
coherent operator sum. Measuring which probe was used records the route and
destroys the interference needed for negative coefficients.

Hamiltonian addition would work if independently tunable Hermitian operators
with exactly these compressed symbols were physically available. The current
source establishes the Wilson effects and monodromy operators, not those
qutrit Hamiltonians.

Thus

```text
central linear span contains the reflection
```

does not imply

```text
admitted constructor words implement the reflection
```

## Conditional coherent LCU route

Suppose, beyond the present source, one has clean unitary block encodings of
the three contractions `I,W_tau,W_rho`, a coherent three-route selector, signed
route phases, and exact uncomputation.

The coefficient one-norm for the reflection expansion is

\[
s
=
\frac23+1+\frac23
=
\frac73.
\]

Standard prepare-select-unprepare would then give a heralded clean-ancilla
branch

\[
K_0
=
\frac1s(I-2P_A)
=
\frac37(I-2P_A).
\]

Because the target factor is unitary, the ideal success probability is

\[
\frac9{49}
\]

for every input state.

This is a valid conditional compiler theorem, not a source realization. Its
failure branches may be rank-deficient filters. Repeat-until-success requires
their exact reversible classification, while amplitude amplification requires
additional controlled reflections about preparation and success subspaces.

The block encodings themselves must lift the zero and fractional Wilson
shadows into larger unitaries without leaving probe information behind.

There is also a one-probe-type polynomial LCU using

\[
I-W_\tau-W_\tau^2.
\]

Its coefficient one-norm is three, so the corresponding ideal heralded branch
has amplitude `1/3` and probability `1/9`. It uses fewer probe types but has a
smaller raw success probability than the two-class linear expansion. It also
requires a clean block encoding of the composed contraction `W_tau^2`.

The comparison is therefore:

| Context family | Probe types | Ideal raw success |
|---|---:|---:|
| Linear class basis | transposition and three-cycle | `9/49` |
| Polynomial transposition tower | transposition only | `1/9` |

These figures are conditional on exact coherent block encodings and do not
include their physical cost.

## Comparison with the native vacuum corridor

The vacuum-energy corridor directly exposes the pair channel to the local
Hamiltonian `Delta(I-P_A)`. It therefore implements the required sum inside
one physical energy operator rather than coherently combining three probe
routes.

The two routes use different authority:

- character route: algebraically exact from two flux-class shadows, but needs
  coherent block encodings and route interference;
- vacuum route: dynamically direct from one native energy distinction, but
  needs reversible fusion and analog timing.

The character identity is valuable as an independent target and falsifier for
the vacuum corridor, not automatically as its replacement.

## Operator-valued warning

The zero transposition shadow on `C` is the normalized trace of an invertible
non-scalar reflection. A coherent dilation must decide whether it retains that
internal operator, closes it into a scalar Wilson amplitude, or records a
probe outcome.

Using the scalar table in an LCU formula before fixing those dilation ports is
type erasure. Different operator lifts can have the same scalar shadow and
different interference behavior.

The required constructor packet must therefore specify each block encoding,
not merely its three sector values.

## Highest-information next use

Use the exact identity as a cross-check on any proposed data-reflection
constructor:

1. compress the constructor to the `A,B,C` fusion basis;
2. compare its sector action with the character expansion;
3. inspect the full probe and environment ports on the `C` branch;
4. reject scalar agreement if the returned dilation differs by channel-
   dependent garbage.

For implementation effort, the reversible vacuum corridor remains the
shorter source-native target.

## Falsifiers

- The displayed three shadow rows are linearly dependent.
- The coefficients fail on any of `A,B,C`.
- One nontrivial class shadow plus identity already fits all three vacuum-
  projector values by a linear combination.
- The polynomial identities in `W_tau` fail on any of `A,B,C`.
- Sequential multiplication is identified with a signed linear combination.
- Classical randomization implements negative coherent coefficients.
- Scalar Wilson values are promoted to unitary block encodings without
  dilation data.
- The conditional `9/49` branch is called deterministic or fault tolerant.
- Failure branches are retried without proving reversibility.
- The non-scalar `C` monodromy lift is replaced silently by its zero trace.

## Claim boundary

This packet proves exact central linear reconstruction and a conditional LCU
calculation. It does not construct coherent block encodings, a route selector,
failure recovery, or a microscopic reflection.

Its new result is the precise algebra-to-constructor gap: two flux-class
shadows uniquely identify the vacuum projector, while physical coherent
synthesis still requires operator-valued lifting and whole-instrument closure.

No build, checker, or Git operation was used.
