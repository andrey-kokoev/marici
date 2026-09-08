# v41: explicit D03 packet specialization map

Iteration 1 internalizes the transition from the module-47 resonance packet to
the fixed-beta packets in modules 51 and 52.

`rzk/53-d03-specialization-map.rzk.md` defines the principal-factor evaluation
on every pre-specialization basis monomial:

    Omega |-> Omega'
    Wu    |-> S
    Wmu   |-> Hmu

where `dS=dHmu=Omega'` and `Z=Hmu-S`. Rzk checks the chain-map equation on all
three source basis families and computes

    Theta = u03 Wmu - mu Wu |-> Hmu-S = Z.

A second chain map kills `Omega'` and `S`, sends `Hmu` to the bottom generator
of the strict X35 occurrence summand, and therefore sends `Z` and the evaluated
`Theta` to its primitive exponent-zero class.

To make this map exact, module 51 was strengthened: `Hmu` is now represented as
the second specialized primitive and `Z` is definitionally their difference,
rather than an unrelated formal cycle symbol.

A fresh 73-file transitive closure passed in 38.60 seconds. Evidence:
`results/53-d03-specialization-map.typecheck.json`.

Scope: this is the normalized principal-factor evaluation, not a claim that raw
homology commutes with the nonflat graph. Explicit X03/lambda coefficient
factors and the supported cone are the next iteration.
