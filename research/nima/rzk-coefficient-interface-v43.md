# v43: three-carrier specialization distinction

**Native projection update:** [`rzk-coefficient-interface-v44.md`](rzk-coefficient-interface-v44.md)
adds the two endpoint coordinates, six connector labels, and complete normalized
four-term Q cycle as finite Rzk vectors.

Iteration 3 combines the three post-specialization outcomes without collapsing
their types.

`rzk/55-d03-three-carrier-separation.rzk.md` defines a dependent carrier family:

- the ordinary supported carrier contains the Cartier cone pair;
- the first-normal-symbol carrier contains the retained conormal symbol;
- the X35-torsion carrier contains the strict occurrence summand.

The canonical evidence depends on the carrier. For the ordinary datum it is the
explicit equality to `D(S,0)`. For the first symbol it is unit evaluation. For
the torsion datum it is primitive bottom evaluation together with the checked
boundary for every positive X35 multiple and the contradiction obtained from
an alleged boundary of the exponent-zero class.

No coercion between these carriers is declared. In particular, the nonzero
first symbol cannot be used as a proof that the ordinary supported-Hom class is
nonzero, and ordinary exactness cannot erase the independently retained X35
class.

A fresh 73-file transitive closure passed in 36.31 seconds. Evidence:
`results/55-d03-three-carrier-separation.typecheck.json`.

Scope: this is a typed separation theorem for the current finite packets. The
native endpoint vectors and complete four-term Q projection remain the final
iteration.
