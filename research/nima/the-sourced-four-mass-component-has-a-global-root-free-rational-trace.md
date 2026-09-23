# A sourced four-mass component has a global root-free rational trace

## Question

Can the full starred four-mass ψ component be expressed RATIONALLY for general four-dimensional external data, rather than evaluated at one positive nine-point target or at individually chosen quadratic roots?

## Exact construction

Yes, on the nondegenerate open set where the sourced quadratic roots are simple and the five-bracket denominators are invertible. From the primary source's coupled auxiliary equations eliminate `β` to obtain `Q(α)=Aα²+Bα+C`. In the two-dimensional algebra `K=Q(four-brackets)[α]/(Q)`, multiplication by `α` in basis `(1,α)` is the explicit companion matrix

    T=[[0,-C/A],[1,-B/A]],
    β=(n0 I+n1 T)(d0 I+d1 T)^-1.

Replace every auxiliary `A=z7+αz8` and `B=z3+βz4` in the COMPLETE component of `ψ[A,1,2,3,4][B,5,6,7,8]` by these two-by-two matrices. Its `χ_1^4 χ_5^4` coefficient is the matrix product of ψ, BOTH fourth-power five-bracket numerators and ALL TEN cyclic four-bracket denominators. The ordinary matrix trace of that product is a ROOT-FREE RATIONAL EXPRESSION in the external four-brackets. This formula holds on the named open set; it needs neither a choice of real-positive branch nor square roots. The checker verifies `Q(T)=0`, all requisite matrix inverses, and commutation with `T`.

The same generic construction reproduces exactly the independently frozen 290-character trace from the nine-point rational target's quotient four-brackets. On an unrelated eight-point four-dimensional moment-curve input it gives a different nonzero exact rational value; omitting the ψ factor changes that value. Thus the construction is not an interpolation from the first target.

## Disposition

This gives a global rational SOURCE SUPERFUNCTION COMPONENT, in compact matrix form, and fixes the earlier one-target limitation on that side. It does NOT supply the global BOSONIC target eight-form coefficient at arbitrary rank-six positive `Z`, nor its `Y0`-chart regularity, so one may not equate the two numerical traces. The primary-source operation and the previously audited orientation ratio `-1` remain the authorized abstract comparison. Computing the explicit rank-six bosonic trace and testing the required nilpotent pullback are independent outstanding steps; assignment of the embedded nine-point cell to a generalized-R tree history also remains open.

Checker: `research/nima/checkers/check_four_mass_complete_component_companion_trace.py`; result: `research/nima/results/four-mass-complete-component-companion-trace.json`.
