# Flavor mixed-quartic repair DPC

## Decisive problem condition

Find a source-derived finite symmetry or representation law for two Flavor doublets satisfying all four conditions:

1. It preserves the opposite-sign relation between the two renormalizable D4 anisotropies.
2. It forbids the allowed mixed quartic \(\operatorname{Re}(z_1^2z_2^2)\).
3. The full generated group has no generalized-CP stabilizer on any selected vacuum.
4. The resulting degree-four source action is closed under the declared symmetry and renormalization.

A proposal fails if any one condition fails. Conditions one and two concern the invariant ring. Condition three concerns the full symmetry group after adjoining the repair. Condition four prevents a truncated potential from carrying source authority.

## First complete candidate class

The smallest obvious repairs are diagonal rephasings

\[
U_{p,q}:(z_1,z_2)
\longmapsto
\left(e^{ip\pi/4}z_1,e^{iq\pi/4}z_2\right).
\]

Preserving each individual quartic anisotropy requires even \(p\) and \(q\). Making the mixed quartic odd requires

\[
p+q=2\pmod4.
\]

There are exactly eight candidates modulo 8.

## Exact audit

For each of the eight candidates, the checker:

- verifies preservation of both individual anisotropies;
- verifies rejection of the mixed quartic;
- generates the full group from common D4 rotation, bare CP, twisted exchange, and \(U_{p,q}\);
- enumerates every CP-odd element;
- tests every CP-odd element against all 16 selected vacua.

Every candidate generates a 64-element group. Every selected vacuum has exactly two generalized-CP stabilizers.

Therefore no candidate passes the DPC.

## Interpretation

The minimal repair is self-defeating. Relative rephasing forbids the dangerous mixed operator by distinguishing the two phase sectors, but that same additional phase authority supplies generalized-CP transformations that fix the misaligned vacua.

This closes the entire diagonal-rephasing repair class, not merely one guessed symmetry.

## Surviving directions

A surviving construction must leave this candidate class. Plausible possibilities are:

- inequivalent representations whose tensor product excludes the mixed quartic;
- a gauge selection rule rather than a global rephasing;
- a nontrivial mediator sector whose full invariant ring produces a protected effective relation;
- more than two multiplets with collective CP breaking and no pairwise generalized stabilizer.

Each proposal must be checked against the same four-part DPC before numerical fitting or vacuum minimization.
