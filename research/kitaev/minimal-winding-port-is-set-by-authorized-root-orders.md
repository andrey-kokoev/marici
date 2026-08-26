# The Minimal Winding Port Is Set by Authorized Root Orders

The reciprocal scalar quotient erases the sheet winding \(n\in\mathbb Z\).
The minimal discrete repair depends on which constructors are actually
admitted.

For a global \(k\)-th root of an annular unit, the obstruction is

\[
n\bmod k.
\]

Thus one residue port in \(\mathbb Z/k\mathbb Z\) is necessary and sufficient
to determine the monodromy class of the \(k\)-th-root constructor. For the
two-sheet square-root problem, this is exactly one parity bit.

If the authorized constructor family contains root orders

\[
F=\{k_1,\ldots,k_r\},
\]

then the single cyclic port

\[
n\bmod L,
\qquad
L=\operatorname{lcm}(k_1,ldots,k_r),
\]

is jointly faithful for all branch monodromies. Among cyclic quotient ports,
it is minimal: a quotient \(\mathbb Z/m\mathbb Z\) determines every
\(n\bmod k_i\) only if each \(k_i\) divides \(m\), hence \(L\mid m\).

For example, square- and cube-root constructors require one
\(\mathbb Z/6\mathbb Z\) port. Separate parity and mod-three ports carry the
same information through the Chinese remainder isomorphism.

## A logarithm needs more than every finite residue

A global logarithm requires

\[
n=0,
\]

not merely \(n\equiv0\pmod m\). For every finite modulus \(m\), the winding
classes \(0\) and \(m\) have the same residue but different logarithm status.
Therefore no finite cyclic port decides global-logarithm existence on an
unbounded winding domain. One must retain the integer winding itself or prove
an independent source bound that reduces the admitted values to a finite
set.

## Distinction from amplitude reconstruction

The parity bit determines whether a square-root sheet exists. It does not
reconstruct the integer winding, the holomorphic amplitude \(e^h\), or a
physical sheet actuator. This exactly matches the earlier torsor lesson: one
trusted origin bit resolves one binary ambiguity, not an arbitrary linear
state.

## Compiler rule

Given a frozen source constructor family:

1. list the admitted root orders;
2. retain winding modulo their least common multiple;
3. retain full integer winding only if logarithms, arbitrary root orders, or
   winding-sensitive transport are operative;
4. do not preserve predicates for constructors absent from the source monoid.

The port is synthesized from operative constructor requirements, not from all
imaginable arithmetic predicates.

## Falsifiers

- A parity bit is used to decide whether winding is zero.
- Root orders are added after the port has been optimized.
- A modulus not divisible by every admitted root order is called jointly
  faithful.
- A residue port is claimed to reconstruct the holomorphic normalization.
- Full integer winding is demanded without an operative winding-sensitive
  constructor.

## Process calibration

Pre-objective: excitement 10/10, confidence 10/10, expected information gain
10/10. The aim was to size the missing discrete sheet interface from the
declared constructor family.

Post-objective: excitement 10/10, confidence 10/10, realized information gain
10/10. Root-order ports are classified by a least-common-multiple theorem,
while the logarithm obstruction proves exactly when no finite port suffices.
