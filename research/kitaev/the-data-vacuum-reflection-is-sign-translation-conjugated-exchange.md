# The data vacuum reflection is sign-translation-conjugated exchange

Owner: `marici.Kitaev`

## Bounded question

Can the reflection of the logical-qutrit vacuum channel be reduced to already
identified electric operations, without synthesizing a full charge projector
from several Wilson probes?

## Verdict

Yes algebraically. On the first-pair fusion basis `A_L,B_L,C_L`, electric
exchange reflects the `B` channel. Tensoring the intermediate channel by the
invertible sign charge exchanges `A` and `B` and fixes `C`. Conjugating exchange
by this sign translation therefore reflects `A` instead.

The desired data reflection is

\[
R_A=I-2P_A=S_B(I-2P_B)S_B^*.
\]

This does not make `R_A` a free physical gate. The sign action permutes
intermediate labels inside one fixed total-`C` fusion space, so total-charge
superselection alone neither supplies nor forbids its implementation. A
microscopic constructor must still realize that permutation and return any
auxiliary sign lines. The controlled lift remains another constructor layer.

## Native exchange reflection

For two electric `C` charges,

\[
C\otimes C\cong A\oplus B\oplus C.
\]

The symmetric exchange acts as `+1` on `A` and `C` and as `-1` on the
antisymmetric sign channel `B`. On the three-anyon total-`C` qutrit in the
left-associated basis,

\[
T_{12}
=
P_A-P_B+P_C
=
I-2P_B.
\]

This is the already pinned elementary braid matrix

\[
\operatorname{diag}(1,-1,1).
\]

Thus the source natively supplies the wrong rank-one reflection for the target
vacuum phase: it singles out `B`, not `A`.

## Sign-charge translation

The invertible electric charge `B` obeys

\[
B\otimes A=B,
\qquad
B\otimes B=A,
\qquad
B\otimes C=C.
\]

After choosing the one-dimensional fusion-vertex phases, its action on the
pair-channel labels is represented by a unitary `S_B` satisfying

\[
S_BP_AS_B^*=P_B,
\]

\[
S_BP_BS_B^*=P_A,
\]

and

\[
S_BP_CS_B^*=P_C.
\]

Possible vertex phases do not affect these projector identities.

Conjugating the native exchange gives

\[
S_BT_{12}S_B^*
=
I-2P_A.
\]

Therefore one executable sign-translation route plus ordinary electric
exchange is sufficient for the data reflection.

## Why a single flux loop is not the same reduction

A transposition-flux loop has scalar responses `+1` and `-1` on the one-
dimensional electric sectors `A` and `B`, but its action on the two-dimensional
electric sector `C` is non-scalar. Its normalized trace there is zero.

A three-cycle-flux loop also acts non-scalarly on `C`, with conjugate cube-root
eigenvalues. Consequently no single unresolved flux loop realizes the scalar
operator

\[
-P_A+P_B+P_C.
\]

The sign-translation conjugation avoids fitting a central projector from
scalar Wilson averages. It uses an exact permutation of the fusion labels and
an exact native reflection.

## Correct physical typing of `S_B`

Tensoring by `B` is an invertible torsor action on simple-object labels and is
not a monoidal autoequivalence fixing the tensor unit. That fact prevents
treating the label permutation as a free categorical symmetry.

However, `A_L,B_L,C_L` are intermediate channels of one object
`Hom(C,C tensor C tensor C)`. They are not distinct total-charge sectors. An
endomorphism mixing them preserves the fixed total charge `C`. Consequently
the total-sector superselection argument used for the separate four-anyon
`A/B` workspace does not apply here.

An implementation may use a created `B,B` pair, a neutral ribbon network, a
pair-channel Hamiltonian, code deformation, or compilation from full qutrit
control. If auxiliary `B` lines are used, they must return to a common vacuum
state, but a persistent external `B` reference is not forced by charge typing
alone.

Thus `S_B` is an algebraically defined based permutation with unresolved
physical authority. Its obstruction is constructor access, locality, and
clean return—not an automatic total-charge mismatch.

## Controlled reflection factorization

Let `C(T_12)` denote a path- or pointer-controlled exchange of the first two
electric anyons. Then

\[
C(R_A)
=
(I\otimes S_B)
C(T_{12})
(I\otimes S_B^*).
\]

Here `S_B` acts on the data qutrit and the control is untouched. Thus the
controlled data reflection reduces to:

1. an executable intermediate-channel sign permutation;
2. controlled ordinary exchange;
3. its inverse.

If `S_B` is realized with an auxiliary sign pair or ribbon, the whole sequence
must include those degrees of freedom in its clean-return test.

An uncontrolled `T_12` does not supply `C(T_12)`. The remaining geometric gate
may be implemented by a coherent braid/no-braid path, a conditional code
deformation, or a direct interaction with the pointer. None is authorized by
the matrix identity alone.

## Relation to full qutrit controllability

Once a continuously tunable off-block bridge closes the local control Lie
algebra to `u(3)`, `R_A` is reachable without using the explicit `S_B`
conjugation. That route treats the reflection as a compiled local unitary.

The present factorization is still valuable because it gives a discrete
source-native target and exposes its topological charge accounting. It also
applies before a full continuous-control compiler has been constructed.

Neither local route supplies the controlled lift automatically.

## Two remaining frontiers, not three

The two predicate encoders now reduce to known topological ingredients:

- flag predicate: transposition-flux enclosing/nonenclosing interferometer;
- data predicate: sign translation, controlled electric exchange, inverse
  sign translation.

Their unresolved resources are:

1. coherent worldline control with whole-instrument return;
2. a physical intermediate-channel permutation or an alternative compiled
   data reflection.

The abstract projectors and reflection spectra are no longer missing.

## Highest-information source audit

Construct one neutral `B`-line network or pair-channel control route around the
first-pair fusion vertex and compress it onto the `A_L,B_L,C_L` qutrit. Verify
the three projector permutations above and inspect every returned auxiliary
state.

Then place the native exchange between the forward and reverse transports.
The accepted compressed map must be exactly `I-2P_A`, with zero leakage and a
common final auxiliary state on all three input channels.

This finite audit decides whether the sign torsor has become an executable
constructor rather than an algebraic relabelling.

## Falsifiers

- Electric exchange is assigned `-1` on `A` rather than `B` in the frozen
  convention.
- Tensoring by sign charge fails to exchange `A` and `B` or fails to fix `C`.
- Conjugated exchange differs from `I-2P_A` after projector phases are removed.
- A normalized trace-zero transposition response on `C` is promoted to a
  scalar phase on the entire `C` sector.
- Intermediate `A/B` channels are treated as different total charges of the
  three-anyon system.
- A persistent `B` reference is declared mandatory from superselection alone.
- An auxiliary `B` pair ends in channel-dependent states while a unitary
  reflection is claimed.
- Uncontrolled electric exchange is promoted to controlled exchange.
- A source-derived relational `B` transport with clean return already realizes
  the displayed projector permutation.

## Claim boundary

This packet proves an exact algebraic factorization and identifies its corrected
typing. It does not construct the intermediate-channel permutation, the
controlled exchange, or their lattice fault contract.

Its new contribution is to show that the data vacuum reflection is not a
missing spectral observable. It is the sign-label conjugate of a native braid
reflection. The remaining difficulty is entirely constructor-level: realize
the label permutation or compile its equivalent, control the exchange, and
return every auxiliary port.

No build, checker, or Git operation was used.
