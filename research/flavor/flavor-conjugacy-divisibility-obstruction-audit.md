# WP151 — conjugacy-divisibility obstruction

## Bounded question

Does equivariance of WP149's natural order-96 flavor group force WP150's
fixed-point correction \(F\) to vanish modulo 96?

## Exact group audit

The group is

\[
G=((\mathbb Z_2)^3\rtimes S_3)\times\mathbb Z_2^{\rm CP},
\qquad |G|=96.
\]

For a genuine \(G\)-action, fixed-set Euler characteristics are constant on
conjugacy classes. If the nonidentity classes have sizes \(s_i\) and class
fixed-set values \(f_i\), then

\[
F=\sum_i s_i f_i.
\]

The exact checker enumerates all signed permutation matrices, adjoins CP,
computes inverses and conjugation, and obtains 20 conjugacy classes. The center
has four elements:

\[
Z(G)=\{1,\mathrm{CP},-1,-\mathrm{CP}\}.
\]

Hence there are three nonidentity singleton conjugacy classes. The gcd of all
nonidentity class sizes is therefore

\[
\gcd(s_i)=1.
\]

## Consequence

Conjugacy invariance alone imposes no nontrivial divisibility on \(F\). In
particular, a class-invariant packet may assign fixed-set Euler value 24 to the
central CP class and zero to the other nonidentity classes. Then

\[
F=24,
\qquad
k=4\chi(X/G)-1.
\]

At \(\chi(X/G)=1\), this gives \(k=3\), reproducing WP150's smallest exact
modulus-four falsifier without violating conjugacy symmetry.

This does not claim that every integer assignment is realized by a physical
UV manifold. It proves the narrower and decisive statement: group equivariance
and class organization cannot by themselves derive \(F=0\pmod{96}\).

## Typing

- **Admitted domain:** conjugacy-invariant fixed-set Euler packets for the
  canonical order-96 group.
- **Faithful flavor quotient:** `physical16` remains downstream; this audit
  resolves an upstream equivariant source kernel.
- **Source-authorized probes:** group multiplication, conjugation, class size,
  and fixed-set Euler values.
- **Contextual partition:** 20 conjugacy classes, including three nonidentity
  central singleton classes.
- **Separation:** class-resolved probes distinguish fixed-set contributions;
  the aggregate \(F\) forgets their individual origin.
- **Selection:** none. Class symmetry does not select the required residue.
- **Rigidification:** organization into conjugacy classes only.
- **Descent:** conjugacy-class data descend under changes of group
  presentation; the induced flavor packet descends under full weak-basis
  equivalence.
- **Reference port:** a class-resolved fixed-set probe would be an additional
  relational source experiment, not recovery of absolute flavor data.
- **Physical instrument:** absent.

## Smallest exact falsifier

The central CP element forms a singleton conjugacy class. A fixed-set value 24
on that class is already compatible with conjugacy invariance and gives
\(F=24\), hence \(k=3\) at quotient Euler one. No larger group calculation is
needed.

## Reopening condition

Supply a stronger equivariant index, anomaly-cancellation identity, or
supersymmetric pairing theorem that constrains the *values* \(f_i\), especially
on the three central singleton classes, and proves
\(\sum_i s_i f_i=0\pmod{96}\) throughout the admitted source domain. Merely
grouping elements by conjugacy cannot close the gate.

## Verification

```text
python research/flavor/checkers/wp151_conjugacy_divisibility_obstruction.py
```

The dependency-free exact enumeration writes the JSON result and requires
12/12 checks.

## Process calibration

Pre-objective: excitement 8/10, confidence 10/10, expected information gain
8/10. The central elements made the obstruction likely. The confound was that
failure of class-size divisibility does not exclude a stronger geometric index
identity.

Frozen optionality snapshot: 96 exact group elements, 20 expected classes,
three hostile nonidentity central classes, one class-invariant \(F=24\)
packet, 12 checks, and no physical instrument.

Post-objective: excitement 8/10, confidence 10/10, realized information gain
8/10. Conjugacy organization was fully computed; the possible symmetry-only
divisibility was reduced to gcd one; the `F=0 mod 96` branch received no
support; and the next admissible branch was narrowed to identities constraining
fixed-set *values*, not class multiplicities. No physical realization of the
hostile Euler packet or instrument was claimed.

