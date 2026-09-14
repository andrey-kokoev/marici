# v192: exact ramified ringed Q-algebra map

The ramified conductor transport now has an exact algebraic realization. Write
the qg2-restricted exceptional kernel as `A xi^2+B xi+C`, with `A=16p^4`, and
let `Delta=B^2-4AC`. Over the localized Q-base, adjoin `d` with `d^2=Delta`.
The two conductor branches are

`xi_plus=(-B+d)/(2A)` and `xi_minus=(-B-d)/(2A)`.

Exact polynomial reduction verifies that both annihilate the restricted kernel.
The deck involution `d -> -d` exchanges them, so their difference is an odd
orientation line candidate. Since Delta has x-order one, d has half x-order;
the base change `x=h^2` converts this to an integral h-filtration.

This constructs the local ramified ringed filtered Q map rather than only its
Puiseux leading term. The remaining comparison is functorial: identify its odd
branch-difference module with the literal physical filtered Q target and prove
that the target road-boundary functor sends it to the selected Cech class v.

Evidence is `results/qg2-ramified-ringed-Q-map.json`.
`rzk/220-qg2-ramified-ringed-Q-map.rzk.md` passes all eight declarations without
assumptions.
