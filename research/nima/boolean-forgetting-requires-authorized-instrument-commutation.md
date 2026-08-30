# Boolean forgetting requires authorized instrument commutation

## Question

Does every pair of labelled occurrences generate a Boolean forgetting square, or does sequential continuation force an ordered partial structure?

## Exact finite gate

Represent forgetting a measurement outcome by its nonselective instrument channel. Two deletions form a Boolean square on an admitted state family only if their channels commute there.

For one qubit, take the initial state

\[
\rho=|0\rangle\langle0|
\]

and dephasing measurements along the (Z) axis and the rational Bloch axis

\[
N=\frac45 Z+\frac35 X.
\]

Writing the corresponding channels as (D_Z) and (D_N), exact rational arithmetic gives

\[
D_ZD_N(\rho)-D_ND_Z(\rho)
=
\begin{pmatrix}
0 & -6/25\\
-6/25 & 0
\end{pmatrix}.
\]

The residual is nonzero. Forgetting the two sequential same-carrier occurrences in opposite orders therefore does not reach one common continuation. The proposed Boolean square is absent.

For independent tensor ports, the lifted channels are (D_Z\otimes 1) and (1\otimes D_N). They commute on every matrix unit and hence on every two-qubit operator. That pair does generate the expected Boolean square.

## Theorem

Independent labelled ports generate a Boolean forgetting cube only when the associated instrument channels are authorized to commute on the admitted continuation space. Without that witness, occurrence deletion belongs to an ordered partial category. A nonzero channel commutator is a finite falsifier of the free Boolean claim.

The distinction is not cosmetic. A static outcome table forgets the continuation maps and can make both cases look like deletion of two labels. The instrument semantics preserves whether one occurrence changes the state consumed by the next.

## Consequence for the closure programme

The Boolean incidence conjecture survives for genuinely independent ports. It does not survive as a theorem about arbitrary labelled occurrences. The more general object is cubical only along authorized commuting faces; sequential faces retain order.

This also sharpens the capability-coalgebra proposal. Source and task cannot generally be reconstructed from an untyped carrier or one immediate capability fiber. They are reconstructible from the process semantics only when the admitted contexts and continuations are jointly conservative: two source-task presentations may be quotiented precisely when every authorized future context gives equivalent continuation behavior. Otherwise the source/task boundary remains observable and cannot be erased as presentation data.

## Verification

The dependency-free checker uses exact rational arithmetic. It verifies a nonzero same-carrier residual, commutation on all sixteen matrix units for independent ports, and the commuting same-observable hostile.
