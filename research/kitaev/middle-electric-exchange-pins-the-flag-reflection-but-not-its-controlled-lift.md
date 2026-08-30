# Middle electric exchange pins the flag reflection but not its controlled lift

Owner: `marici.Kitaev`

## Bounded question

Does the four-anyon fusion-qubit construction already contain either of the
controlled reflections required by the reusable bus compiler?

## Verdict

It contains the flag reflection itself. Exchanging the two middle electric
`C` anyons acts as `+1` on their trivial-charge channel `A` and `-1` on their
sign-charge channel `B`. On the vacuum-compatible fusion qubit this is exactly
the reflection of one `A/B` outcome projector.

It does not contain the controlled lift of that reflection merely by virtue of
containing the exchange. Nor does it supply the reflection of the data-qutrit
vacuum projector. The two predicates must remain separately typed.

The new reduction is therefore asymmetric:

- the flag-side reflection has a native braid word;
- the data-side reflection is only algebraically compilable after full qutrit
  control;
- both controlled incidences remain physical obligations.

## Electric exchange on the middle pair

The middle electric charges obey

\[
C\otimes C\cong A\oplus B\oplus C.
\]

Because the electric subcategory is `Rep(S3)` with symmetric exchange, the
flip of the two tensor factors acts by `+1` on the symmetric summands and by
`-1` on the antisymmetric sign channel. In the cross-character subspace used
by the four-anyon vacuum sector,

\[
|A\rangle
=
\frac{|+-\rangle+|-+\rangle}{\sqrt2},
\]

and

\[
|B\rangle
=
\frac{|+-\rangle-|-+\rangle}{\sqrt2}.
\]

Hence middle exchange `T_mid` satisfies

\[
T_{mid}|A\rangle=|A\rangle,
\qquad
T_{mid}|B\rangle=-|B\rangle.
\]

On the vacuum-compatible recoupled states `A_F,B_F`,

\[
T_{mid}=P_{A_F}-P_{B_F}=I-2P_{B_F}.
\]

Up to a global minus sign it is also the reflection `I-2P_{A_F}`. Thus the
binary `A/B` flag has an exact source-derived reflection target.

## Action in the route basis

The route basis and charge basis are related by the real Hadamard recoupling:

\[
|0_F\rangle
=
\frac{|A_F\rangle+|B_F\rangle}{\sqrt2},
\]

\[
|1_F\rangle
=
\frac{|A_F\rangle-|B_F\rangle}{\sqrt2}.
\]

Therefore the same exchange swaps the two route channels:

\[
T_{mid}|0_F\rangle=|1_F\rangle,
\qquad
T_{mid}|1_F\rangle=|0_F\rangle.
\]

It is a logical Pauli `X` in the route basis and logical Pauli `Z` in the
`A_F/B_F` charge basis. This is exactly the reflection needed to distinguish
the complementary recombination outcomes coherently.

## What is and is not executable

An unconditional physical exchange applies `T_mid` to the fusion qubit. A
coherent encoder for the flag into another port requires

\[
C(T_{mid})
=
|0\rangle\langle0|\otimes I
+
|1\rangle\langle1|\otimes T_{mid}.
\]

The first operation does not imply the second. A classical command choosing
whether to exchange produces a mixture when the command is not retained
coherently. A superposition of worldline commands requires an additional
path, framing, or interaction degree of freedom and exact environment return.

There is one possible architectural simplification: use the fusion qubit
itself as the common actuator control port. Then no separate encoder for `Q`
is needed. But this requires the reusable port-to-bus Hamiltonian to couple
directly to `P_{B_F}` while preserving the four-anyon total-vacuum workspace.
That coupling has not been derived.

## Do not confuse the two projectors named A

The flag charge projector `P_{A_F}` acts on the two-dimensional four-anyon
fusion space. The data projector `P_A` acts on the vacuum line of the logical
qutrit on which the sixth-root gate is desired.

They have different domains and different roles:

| Projector | Domain | Role |
|---|---|---|
| `P_{A_F}` or `P_{B_F}` | four-anyon fusion qubit | recombination flag |
| `P_A` | logical qutrit | target joint phase |

Middle electric exchange realizes a reflection of the first kind. It says
nothing directly about the second.

After a physical off-block bridge gives full local `U(3)` control, the
data-side reflection `I-2P_A` is reachable as a bus-local or data-local unitary
under the continuous-control assumptions. Its controlled lift relative to the
common port remains separate.

## Constructor inventory after the reduction

The finite programme now has:

1. a native flag reflection `T_mid`;
2. a deterministic monodromy giving the flag's cube-root phase;
3. exact real Hadamard recoupling between route and charge bases;
4. an abstract data reflection `I-2P_A`;
5. a route-to-fusion incidence isometry `J` as a mathematical target.

It still lacks:

1. a lattice realization of `J`;
2. a coherent controlled lift of the needed reflection or an equivalent
   direct flag-to-bus interaction;
3. a controlled data-predicate incidence;
4. a whole-instrument return and fault audit.

The flag-side spectral observable is therefore no longer missing. Its
actuator incidence is.

## Highest-information next test

Project a candidate localized middle-pair interaction onto the two-dimensional
vacuum-compatible fusion space and ask whether it produces

\[
P_{B_F}\otimes h_B
\]

with a non-scalar bus operator `h_B`, while preserving total charge. If yes,
the fusion qubit can serve directly as the shared control port and its separate
`Q` encoder disappears.

This is more informative than another charge measurement calculation. The
measurement basis and reflection are already fixed; only coherent actuator
incidence remains open.

## Falsifiers

- Middle electric exchange has the same sign on the `A` and `B` channels.
- The route-to-charge recoupling is not Hadamard in the frozen convention up
  to vertex phases.
- `T_mid` does not swap `0_F` and `1_F`.
- An unconditional exchange is promoted to a controlled exchange without an
  added coherent control degree of freedom.
- The fusion-qubit `A_F` projector is identified with the data-qutrit vacuum
  projector `P_A`.
- A localized interaction already couples the middle-pair charge projector
  nontrivially to the qutrit bus with clean return and bounded leakage.

## Claim boundary

This packet identifies an existing braid word with the exact flag reflection
on the protected four-anyon subspace. It does not derive a controlled braid,
a direct fusion-to-bus coupling, or the data-side controlled reflection.

Its new contribution is to close the flag-observable question and leave only
the typed actuator-incidence question. The reflection exists natively; its
conditional use does not yet.

No build, checker, or Git operation was used.
