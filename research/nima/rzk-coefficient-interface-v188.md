# v188: relative-cut orientation supplies the required character twist

The needed sign line has a canonical geometric source if the qg2 conductor
cell is represented by an oriented interval from its endpoint pole to its
conductor pole. Reversal swaps the two boundaries and negates the interval
generator, so its orientation character is -1.

Tensoring this line with the normalized conductor line changes the character
from `(+1)` to `(+1)(-1)=-1`, exactly matching the reflection-odd logarithmic
primitive. After also stripping the inverse-Euler unit from v186, the twisted
conductor generator has both detector value one and odd character.

This constructs the formal orientation repair without choosing a sign from the
target. It remains conditional on constructing the physical relative cut chain
itself and transporting it through the ambient nearby-cycle comparison.

Evidence is `results/qg2-relative-cut-orientation-twist.json`.
`rzk/216-qg2-relative-cut-orientation-twist.rzk.md` passes all eight declarations
without assumptions.
