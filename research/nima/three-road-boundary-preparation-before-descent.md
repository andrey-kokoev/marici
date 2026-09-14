# The three roads form a rank-three boundary preparation space before descent

The physical pullback matrices already contain the missing three-port object. In the labelled basis

`(conductor+, conductor-, road_D03, road_D25, road_D14)`, let the joint boundary trace be projection to the last three coordinates.

It is surjective even after restricting to cycles. A canonical integral right inverse sends

- `(1,0,0)` to `p_D03=(1,0,1,0,0)`;
- `(0,1,0)` to `p_D25=(1,0,0,1,0)`;
- `(0,0,1)` to `p_D14=(1,0,0,0,1)`.

Each vector is killed by `d1`. The conductor boundary `(1,1,0,0,0)` has zero joint road trace, so the trace descends through the internal conductor quotient.

The other three `d2` columns are exactly

`p_D03-p_D25`, `p_D25-p_D14`, and `p_D14-p_D03`.

They span the rank-two augmentation ideal. Quotienting by road gluing therefore collapses the rank-three boundary preparation module to the previously computed rank-one physical homology. There is no contradiction:

`pre-gluing boundary preparations = Z^3`, while `fully descended physical H1 = Z`.

For an arbitrary road triple `(a,b,c)`, the closed lift

`(a+b+c,0,a,b,c)`

has joint road trace `(a,b,c)`, and full descent retains only `a+b+c`. This establishes a rank-three **road-labelled** boundary space, but it does not identify those labels with the target-typed packet `(s,W,v)`.

Indeed, evaluating the established target rows on the three basis preparations gives

```
       p_D03 p_D25 p_D14
s        1     1     1
W        1     1     1
v        1     1     1
```

The readout has rank one. There is therefore no permutation assigning `D03,D25,D14` separately to `s,W,v`. The roads are one cyclic orbit, whereas `s`, `W`, and `v` are different detector types; in particular `W` is endpoint-supported, not a road projection.

Module 239 is consequently only an abstract boundary-preparation interface. Its scalar residue definition is conditional on a future target-typed preparation and is not inhabited by the three road lifts. A physical symbolic residue still requires three independent target-typed boundary maps, not merely three labelled roads.

Executable evidence: `checkers/check_three_road_boundary_preparation_space.py` and `checkers/check_three_road_to_selected_channel_assignment.py`. Formal interface: module 239.
