# Geometry, dynamics, and access are independent physical axes

## Synthesis

The topological sector now supplies controlled examples separating three
questions:

1. **Constitution:** which capability classes exist in the relevant quotient?
2. **Dynamics:** which operators or syndrome labels are conserved by the
   Hamiltonian?
3. **Access:** which operations and records can the admitted constructors
   realize?

These are not successive approximations to one datum. They can vary
independently.

## Axis 1: constitutive geometry

For the mixed-boundary annulus,

\[
\dim H_1(K)=1,
\qquad
\dim H_1(K,R_{\mathrm{rough}})=0.
\]

The boundary relation changes the quotient in which capability is defined.
The old loop becomes a relative boundary.

## Axis 2: dynamical conservation

For

\[
H'=H_0-X_{e_0},
\]

the cellulation and chain identity remain unchanged, while the two adjacent
plaquette labels cease to commute with the Hamiltonian. The local block has

\[
\det(\lambda I-M)=\lambda^2-5.
\]

Thus a chain-level syndrome remains a well-typed kinematic boundary even when
its corresponding stabilizer eigenvalue is not dynamically conserved.

## Axis 3: operational access

On the same two-logical-qubit quotient, changing the admitted constructor
family changes the accessible operator algebra without changing topology:

\[
\langle Z_1,Z_2\rangle
\quad\leadsto\quad4\text{-element commuting basis},
\]

while

\[
\langle X_1,X_2,Z_1,Z_2\rangle
\quad\leadsto\quad16\text{-element full Pauli basis}.
\]

The former separates a preferred classical basis but not arbitrary quantum
coherences.

## Result

The minimal physical specification is therefore not simply

\[
\text{Carrier}+\text{sector lens}.
\]

It contains at least:

\[
\boxed{
(\text{constitutive complex/quotient},
\text{source dynamics},
\text{constructor algebra},
\text{record/readout}).
}
\]

The same Carrier geometry can support multiple dynamical and operational
realities. Conversely, a boundary change can alter constitution even if a
similar observable formula remains writable.

## Software translation

- Constitution resembles schema plus equivalence/constraint relations.
- Dynamics resembles state-transition semantics and invariants.
- Constructor algebra resembles the implemented command surface.
- Readout resembles queries/materialized views over reachable state.

Two systems can share a schema while implementing different commands. They
can implement the same commands while exposing different readouts. A schema
migration can eliminate a distinction rather than merely hiding it.

## Cross-sector falsifier

For any claimed sector lens, vary one axis while holding the others fixed:

1. change a boundary/support relation while freezing coefficient dynamics;
2. change dynamics while freezing the Carrier complex;
3. change admitted constructors while freezing geometry and Hamiltonian;
4. change readout while freezing all upstream operations.

If a claimed universal datum changes under only one variation, it belongs to
that axis rather than to the common Carrier.

## Verification

- `research/nima/checkers/check_geometry_dynamics_access_axes.py`
- composes the independently exact Kitaev WP7--WP9 audit and Nima accessible-
  algebra audit.

