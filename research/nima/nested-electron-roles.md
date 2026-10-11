# Nested witness roles can coexist with physical electron exchange

## Question

The operator corrected the earlier pair model: the first electron witnesses a proton, while the second witnesses the retained proton-plus-electron composite. Test whether this hierarchy can be preserved under electron-label exchange, rather than imposing equality of construction roles. Active obligation: attachment transport and readout descent. A proton plus two electrons has H-minus composition, not helium.

## Claim boundary

The explicit marked syntax is

    attach(attach(proton,e1),e2).

The parent of the outer attachment is the entire first composite. Relabeling exchanges both electron occurrences, yielding

    attach(attach(proton,e2),e1).

These are different marked terms. Exchange transports the whole tree, preserves its depth, commutes with retrieving its parent, and applied twice returns the original. The attachment constructor itself is supplied: no claim is made that a new physical interaction or old-native rule has been derived.

`agda/NestedWitnessTransport.agda` proves the involution, attachment naturality, parent transport and inequality of the two marked terms. Thus exchange is a structural transport rather than an assertion that distinct construction records are literally identical.

## Physical compatibility fixture

An independent two-mode quantum example uses the symmetric spatial state proportional to

\[
a(1)b(2)+b(1)a(2)
\]

and the antisymmetric spin singlet. The full state changes sign under exchange, while its density is invariant. For orthonormal a,b, both numbered-electron spatial marginals are the same matrix diag(1/2,1/2). Different occupied modes therefore do not imply a permanently identifiable inner electron and outer electron. This is a supplied compatibility example, not a derivation from the marked syntax or a calculation of the H-minus ground state. The label symmetry does not erase the external construction record; making that record physically coupled would require a joint state and interaction model.

A two-particle Hamiltonian that assigns different intrinsic laws to numbered particles fails the exchange test. Applying the same one-body law to both particles permits different mode energies and passes. These are exact rational matrix checks.

## Hierarchical addition energies

Different first and second addition energies are consistent with exchange symmetry. For the declared occupation energy

\[
E(n)=\epsilon n+U\frac{n(n-1)}2,
\]

the two increments are epsilon and epsilon+U. An exact fixture uses epsilon=2 and U=3, giving increments 2 and 5 without referring to numbered electron identities. The constants are illustrative, not fitted or predicted binding energies. The example distinguishes different environments at successive stages from different intrinsic electron species.

Controls reject a partial relabeling that duplicates an electron occurrence and detect particle-label-specific energy terms that violate exchange invariance.

## Disposition and verification

The construction hierarchy should be retained. Exchange symmetry need not identify its roles or erase its parents, and it does not require equal sequential addition energies. Conversely, marked roles alone do not establish a physical role-dependent interaction or select a correlation kernel. The next physical target for this specific core is H-minus binding/electron addition, with a specified coupling between the retained roles and physical state; the helium benchmark cannot substitute for it.

Fresh safe Agda check passed via `structured_command_execution:e_32876_1791225962028820800_33`; receipt: `results/agda-NestedWitnessTransport.json`. Exact executable test `python research/nima/checkers/check_nested_electron_roles.py` passed with the spin-singlet fixture via `structured_command_execution:e_32876_1791226008175906700_35`; output: `results/nested-electron-roles.json`. Python is not verified extraction from Agda. No commit or publication is claimed.
