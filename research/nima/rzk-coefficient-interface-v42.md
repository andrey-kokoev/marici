# v42: supported Cartier-cone nullhomotopy

Iteration 2 upgrades the fixed-beta primary exactness from an underlying target
boundary to the full ordinary supported-Hom cone identity.

`rzk/54-d03-supported-cartier-cone.rzk.md` adds an explicit X03 exponent to the
specialized packet, defines coefficient multiplication by incrementing that
exponent, and defines the normalized Cartier Hom cone

    D(a,b) = (d a, X03*a - d b).

The supported primary is the pair `(Omega',X03*S)`. Its displayed primitive is
`(S,0)`, and Rzk checks both components of

    D(S,0) = (Omega',X03*S).

The second component is proved in the finite-integral setoid rather than hidden
by definitional simplification. The reverse equality is also exported as the
ordinary supported exactness witness.

A fresh 71-file transitive closure passed in 30.29 seconds. Evidence:
`results/54-d03-supported-cartier-cone.typecheck.json`.

Scope: this checks the normalized X03 cone packet. The lambda normal-frame unit
and dual conormal line remain external framing data; neither is evaluated to
one. The separately typed first symbol and X35-torsion class are not identified
with this zero ordinary cone class. Their combined separation is iteration 3.
