# v18: complete supported top-cohomology normalization

**Next checkpoint:** [`rzk-coefficient-interface-v19.md`](rzk-coefficient-interface-v19.md)
checks the physical six-point source, primitive cycle, and strict conductor
augmentation.

`rzk/29-supported-top-normalization.rzk.md` closes the finite-polynomial
normalization gap.

For every arbitrary finite integral expression over `(u,s,t)` monomials it
constructs, by recursion:

1. its top cochain in the unique degree-one state;
2. an explicit degree-zero primitive for every positive monomial term;
3. its constant integer coefficient.

Rzk proves the setoid decomposition

    top(p) = d(primitive(p)) + constant(p) * tau.

The recursion handles raw syntax containing sums, negatives, integer scales,
and cancellation among constant terms. It does not assume a pre-normalized
polynomial or invoke polynomial division. In particular Rzk proves

    constant(p)=0  ->  top(p)=d(primitive(p)).

Together with module 27, which proves every boundary has zero residue and tau
has residue one, this establishes the operational setoid classification

    H^1(M_loc) = Z[u,s,t]/(u,s,t) <tau> = Z <tau>

for the minimal coefficient block (spectator coefficients remain omitted as
stated in v15). Since degree one is the terminal rank-one state, every top
cochain is automatically a cycle.

A fresh 74-file headless transitive closure passed in 42.40 seconds. Evidence:
`results/29-supported-top-normalization.typecheck.json`. The Rzk LSP was not
used.

This is a classification by mutually inverse residue/representative behavior
in the existing evaluation setoid; it does not postulate or construct an Rzk
quotient type.
