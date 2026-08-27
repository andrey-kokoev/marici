# Target sufficiency must be closed under future constructors

## Bounded question

When does an observation quotient remain sufficient after future constructors
act, rather than merely computing the target at the present instant?

## Frozen predictive packet

Let \(X\) be a finite-dimensional state space. Let

\[
H:X\longrightarrow Y
\]

be the present observation, let

\[
R:X\longrightarrow Z
\]

be a target, and let the admitted constructor alphabet act through linear maps

\[
A_e:X\longrightarrow X.
\]

For a word \(w\), write \(A_w\) for the ordered constructor product.

The future target after word \(w\) is

\[
R A_wx.
\]

The predictive question is whether this value is determined by the present
observation \(Hx\).

## Contextual factorization theorem

For one word \(w\), a decoder \(D_w\) satisfying

\[
R A_w=D_wH
\]

exists exactly when

\[
\ker H\subseteq\ker(RA_w).
\]

For an admitted word family \(W\), the present observation is target-sufficient
for every future context exactly when

\[
\ker H
\subseteq
\bigcap_{w\in W}\ker(RA_w).
\]

This is the context-closed kernel criterion. Present target factorization is
only the empty-word case.

## Smallest one-step failure

Let

\[
H=
\begin{pmatrix}
1&0
\end{pmatrix},
\qquad
R=H,
\]

and admit the swap constructor

\[
A=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
\]

At the present instant,

\[
R=H,
\]

so the target is perfectly determined by the observation.

After the swap,

\[
RA=
\begin{pmatrix}
0&1
\end{pmatrix}.
\]

The hidden vector \(e_2=(0,1)^{\mathsf T}\) satisfies

\[
He_2=0
\]

but

\[
RAe_2=1.
\]

One admitted future constructor turns a presently irrelevant direction into the
entire target. Static target domination was correct and predictively incomplete.

## Quotient-dynamics theorem

Let

\[
N=\ker H.
\]

The constructor \(A_e\) descends to a well-defined map on the observation
quotient \(X/N\) exactly when

\[
A_eN\subseteq N.
\]

If this invariance holds for every constructor generator, it holds for every
word. The quotient then carries autonomous induced dynamics.

If \(R\) also annihilates \(N\), every future target \(RA_w\) factors through
the quotient automatically.

Kernel invariance is stronger than target-relative context sufficiency. It is
the right condition when the programme claims that the observed quotient is
itself a predictive carrier supporting all admitted dynamics.

## Target closure versus carrier closure

Two claims must remain distinct.

Target closure requires

\[
N\subseteq\ker(RA_w)
\]

for every target and word actually used.

Carrier closure requires

\[
A_eN\subseteq N
\]

for every admitted generator. It supports arbitrary quotient-level future
composition.

A quotient may compute one frozen target family without carrying a closed
dynamics of its own. Conversely, a dynamically closed quotient may still omit
a target that does not annihilate its kernel.

## Quantitative future domination

Stable future decoding requires constants \(C_w\) such that

\[
(RA_w)^*RA_w
\leq
C_w^2H^*H.
\]

For a finite horizon \(W_L\), define the aggregate future-target Gramian

\[
Q_L
=
\sum_{w\in W_L}(RA_w)^*RA_w.
\]

One decoder packet with aggregate bound \(C_L\) exists when

\[
Q_L\leq C_L^2H^*H.
\]

An infinite-horizon claim requires control of \(C_L\) as the word horizon
grows. Every finite horizon may factor while the constants diverge.

Thus context closure has both an algebraic kernel gate and a quantitative
growth gate.

## Single-transition finite closure

For one transition matrix \(A\) on a \(d\)-dimensional state space, future
targets are

\[
R,
RA,
RA^2,
\ldots.
\]

By the Cayley-Hamilton theorem, every higher power is a linear combination of
the first \(d\) powers. Therefore it is enough to test

\[
\ker H
\subseteq
\bigcap_{k=0}^{d-1}\ker(RA^k).
\]

This is a genuine finite closure certificate because the source dimension and
the global polynomial identity are known in advance.

Without a source dimension bound, a finite time horizon does not close the
quantifier.

## Unobservable invariant subspace

When \(R=H\), define

\[
N_\infty
=
\bigcap_{k\geq0}\ker(HA^k).
\]

This is the largest \(A\)-invariant subspace contained in \(\ker H\). Quotienting
by \(N_\infty\) gives the minimal state distinction visible through all future
outputs.

The present kernel \(\ker H\) may be larger than \(N_\infty\). A direction
hidden now can become observable later, as in the swap witness.

This is why predictive equivalence is context closure of present-readout
equivalence.

## Interventions enlarge the future family

Adding a new constructor letter enlarges the word monoid and can shrink the
contextually invisible subspace. The observation hardware need not change; the
ability to intervene can make an old scalar sensor distinguish new state
directions.

This is the algebraic explanation of the third-polarizer phenomenon. The middle
polarizer changes the state before the final intensity measurement, so a
previously hidden polarization distinction can affect the same terminal scalar.

The new information comes from an ordered constructor plus readout, not from the
terminal intensity alone.

## Diagnostic consequence

A diagnostic quotient is adequate only if all mechanisms in one observed block
continue to require the same action after every admitted intervention and
continuation.

If a future test separates two presently colliding mechanisms, they were not
predictively equivalent. The diagnostic partition must be refined before it is
used as a closed control state.

This connects the partition lattice to the Hankel residual space: partition
blocks are discrete future-response equivalence classes, while Hankel rows are
their linear analogue.

## Toric-code instance

Local syndrome quotients Pauli errors by the information exposed through star
and plaquette measurements. Under local stabilizer-preserving repairs, many
same-syndrome errors remain control equivalent.

If admitted future constructors include logical loop probes or logical gates,
homology classes with the same syndrome can produce different future targets.
The syndrome quotient is then not a closed predictive carrier for that larger
constructor family.

Adding loop coordinates refines the quotient. It does not make syndrome alone
more informative; it changes the tester and constructor packet.

## Software instance

Two service states may return the same current response and require the same
immediate action. A later command can expose a hidden difference. Caching only
the current response is then not a sufficient state abstraction.

A valid interface state model must be a congruence under every admitted command:
equivalent states must transition to equivalent states and preserve every future
response. This is the software form of kernel invariance.

## Theta/Tate hostile instance

A current may factor through the completed scalar section at the present stage
while a Fourier, Tate, seam, or Green constructor rotates a hidden source
direction into that current later.

The correct audit is not only

\[
\ker H\subseteq\ker R.
\]

It is the context family

\[
\ker H
\subseteq
\bigcap_{w}\ker(RA_w)
\]

for every source-authorized word used by the completed argument, together with
uniform domination constants.

This makes the missing constructor list mathematically decisive: changing the
admitted monoid changes the predictive quotient.

## DPC: explanations must survive their own continuations

The conjecture is:

> An observation quotient is explanatory only when every distinction it erases
> remains irrelevant under all source-authorized constructors and targets used
> by the explanation. Static sufficiency is not predictive sufficiency. The
> quotient must be a constructor congruence or the narrower target-context
> kernel condition must be proved explicitly.

This states why intervention is part of explanation rather than an optional
extra test.

## Critics

### The future constructor family is unbounded

Then a finite certificate needs a source dimension bound, recurrence, or
generator-invariance theorem. Sampling longer words does not close the family.

### Kernel invariance is stronger than necessary

Correct. It is required for autonomous quotient dynamics. A frozen target family
needs only target-context closure.

### The swap is an artificial intervention

Its role is minimality: one legal constructor suffices to invalidate a static
quotient. In an application, the constructor must be source-authorized.

### Future decoding can be recomputed at each horizon

Yes, but diverging decoder norms still prevent a uniform completion theorem.

### Hidden differences may never matter operationally

Then every admitted continuation should annihilate them, and quotient closure
will prove that claim. No microscopic reconstruction is needed.

## Exact falsifiers

- Present target factorization used to infer all future target factorization.
- A kernel quotient called a predictive carrier although one generator moves
  its kernel outside itself.
- A finite word horizon called complete without a source closure theorem.
- Cutoffwise future decoders used while their norms diverge with horizon.
- A new intervention used in the conclusion but omitted from the target-context
  audit.
- A hidden state direction discarded although an admitted constructor rotates
  it into the target.
- Syndrome-only equivalence used after logical loop constructors are admitted.

## Machine-readable context packet

```json
{
  "code": "target_sufficiency_not_context_closed",
  "present_observation": "H",
  "present_target_factors": true,
  "constructor_word": "w",
  "future_target": "R A_w",
  "kernel_witness": "x",
  "present_output": 0,
  "future_target_output": "nonzero",
  "quotient_kernel_invariant": false,
  "uniform_future_domination": false
}
```

## Deutschian explanation

A hidden distinction is irrelevant only if nothing the programme can do makes
it matter. Present observation cannot establish that by itself. Constructors
probe the hidden state by moving its directions into or away from future
readouts.

A predictive quotient is therefore a state space closed under intervention. It
forgets exactly those distinctions whose entire authorized future is the same.

## Claim boundary

This packet proves the finite context-kernel and quotient-invariance criteria,
including a finite Cayley-Hamilton closure for one known transition. It does not
derive the admitted constructor monoid or uniform infinite-horizon bounds for
any sector.

## Process calibration

Pre-objective ratings were excitement 10/10, confidence 10/10, and expected
information gain 10/10. The target was to close static target sufficiency under
future action.

Post-objective ratings are excitement 10/10, confidence 10/10, and realized
information gain 10/10. Predictive sufficiency is target-context closure, while
autonomous quotient dynamics require constructor-invariant kernel.
