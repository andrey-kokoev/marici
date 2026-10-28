# Central belt junction trial: retained common and contrast modes

The six three-input destinations in the central exchange are tagged with `retained-common-contrast-v1`. Existing arrows, positions and all 74 links are unchanged. There is no new UI text, animation or automatic time evolution. The law is executable in `research/realization-tower/belt-fiber-junction.mjs`.

For three equal-width real reference fibers a,b,c, apply coordinatewise:

- common s = (a+b+c)/sqrt(3)
- contrast u = (a-b)/sqrt(2)
- contrast v = (a+b-2c)/sqrt(6)

Store all three modes at the destination. The inverse reconstructs all three input fibers. A trial step fixes s and rotates (u,v) by 120 degrees. The declared metric is the Euclidean sum of squared reference coordinates; it is not identified with a native field metric or physical energy.

## Result

The transform is orthogonal, invertible and norm-preserving. Three steps return the complete input. A 3000-step numerical regression preserves the common mode, total norm and contrast norm within tolerance. A nonzero contrast state with zero common mode explicitly demonstrates the information lost by retaining only the common output.

Crucially, transforming the 120-degree step back to the input basis gives exactly `(a,b,c) -> (c,a,b)`. Thus this trial supplies bounded cyclic circulation, not attenuation of mismatch or cross-source amplitude mixing. The orthogonality and cyclic-permutation identities establish the ideal boundedness; the finite run is only a numerical regression. No feedback or dissipative stabilization is established.

`tests/belt-fiber-junction.test.mjs` checks reconstruction, reversibility, norm preservation, common-mode retention, lack of contrast decay, the cyclic identity and attachment to the six actual central junctions. Layout, wiring and browser regressions also pass.
