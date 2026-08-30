# Binary branch carrier (WP386)

## Bounded question

Can a source-defined binary carrier preserve WP385's union of factor branches
with a lower-degree positive operation?

## Classical branch-conditioned operation

Augment the source domain by $s\in\{-1,+1\}$ and define

\[
V_s(C,D)=(C-s\beta D)^2.
\]

Each branch penalty has bifundamental field degree 24. Classical elimination
by minimization gives

\[
V_{\min}=C^2+\beta^2D^2-2\beta D|C|.
\]

Its zero set is exactly

The zero set consists of the two branches $C=\beta D$ and $C=-\beta D$,
and hence agrees with $F=0$. The binary carrier therefore preserves the
union while halving the positive operator degree from 48 to 24.

The displayed disjunction is ordinary mathematical content, but the branch
carrier adds physical structure. Under CP, $C$ changes sign and $s$ must also
change sign. Summing over unlabelled branches preserves CP; preparing one
fixed branch selects a CP orientation and defines an augmented experiment.

## Preparation-law obstruction

Classical minimization is not equivalent to finite-temperature summation. At
inverse temperature $\tau$, normalized branch summation gives

\[
V_\tau=-\frac1\tau\log
\left(\frac{e^{-\tau V_+}+e^{-\tau V_-}}2\right).
\]

For nonzero $D$ on the plus branch,

\[
V_\tau=\frac1\tau\log
\left(\frac{2}{1+e^{-4\tau\beta^2D^2}}\right)>0.
\]

Thus finite thermal mixing lifts the original branch shell. Only the
zero-temperature envelope recovers the union. A superselection rule could
also retain branch-conditioned zeros, but that rule must be source-derived.

## Authority and groupoid

The carrier construction descends under weak-basis transformations because
$C$, $D$, and each branch penalty are invariant. The simultaneous flip
$(C,s)\mapsto(-C,-s)$ belongs to the augmented CP groupoid. A labelled branch
port changes the groupoid to its stabilizer; it creates a relational
orientation observable and does not reveal an absolute phase.

The operation is a genuine conditional selector of a proper shell once
$\beta$ and the preparation law are admitted. It does not predict $\beta$,
and finite-temperature source dynamics does not preserve its exact zero set.

## Disposition

WP386 opens the first lower-degree positive branch that preserves WP378's
union: a binary carrier with zero-temperature minimization or superselection.
Its smallest falsifier is the finite-temperature point
$C=\beta=D=\tau=1$, where the classical penalty vanishes but the thermal
effective penalty is positive.

The remaining gate is a source derivation of the binary carrier, its CP law,
$\beta$, and its zero-temperature or superselection preparation, followed by
an executable detector readout.

Run `uv run --with sympy python
research/flavor/checkers/wp386_binary_branch_carrier.py` to regenerate the
result.
