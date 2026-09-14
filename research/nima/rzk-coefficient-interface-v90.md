# v90: supported residue amplitude channel

`rzk/118-supported-residue-amplitude-channel.rzk.md` factors the physical
amplitude through a shifted supported Gysin class and an oriented residue.
This makes the channel choice explicit: the ordinary polynomial return
specializes to zero, whereas the supported local-cohomology channel retains the
primitive class.

The module constructs the residue amplitude both on arbitrary fillings and on
coherent coefficient/physical comparison fillings. Both reduce judgmentally to
`residue (gysin physical)`. It also states the typed reflection-covariance gate
for the odd sheet-exchange orientation and retains the ordered conormal
determinant requirement.

A fresh Rzk check passes all 12 declarations. The symbol closure contains one
file and no `#assume` declarations.

Concrete instantiation still requires the physical Gysin map and oriented
residue map; neither is inferred from the coefficient-only scalar pairing.
