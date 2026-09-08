# v15: supported local coefficient target

**Next checkpoint:** [`rzk-coefficient-interface-v16.md`](rzk-coefficient-interface-v16.md)
adds a checked constant-term residue, proves all boundaries have residue zero,
and detects the primitive tau class internally.

The first semantic-realization target is now a concrete Rzk coefficient
complex rather than an external matrix description.

`rzk/26-supported-local-coefficient-complex.rzk.md` contains the 16 states of
the retained-normal supported local Hom block, in cohomological ranks

    3, 7, 5, 1.

Its coefficient monomials are typed over the three decisive independent
parameters

    u=u03, s=t04, t=t35.

Spectator parameters act independently and are deliberately omitted from this
minimal block. No inverse of u, s, or t is available.

The generated differential is the exact matrix block

    [-M^T; -u I3],
    [w^T 0; u I4 -M^T],
    (-u,t,s,t,s),

with the ordered conductor signs from the incoming supported-Gysin and
secondary calculations. It has 16 state constructors and 28 signed polynomial
arrows. Rzk checks all generator squares and extends square-zero to every
finite integral polynomial coefficient expression. The named alpha chain and
its differential u-tau are retained at chain level.

A fresh 71-file headless transitive closure passed in 42.46 seconds. Evidence:

- `results/26-supported-local-coefficient-complex.typecheck.json`
- `results/supported-local-generation.json`

The Rzk LSP was not used.

This does not yet prove the cohomology classification H1=D<tau>, construct
principal parts, or identify the physical conductor-Morse class. It supplies
the small receiving coefficient complex on which those next proofs can be
stated without loading the 27,440-column jet matrix.
