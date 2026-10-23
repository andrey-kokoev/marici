# Explicit analytical-prototype binding on the generated esd7 complex

## Result

The [binding implementation](checkers/esd7_analytical_binding.py) connects all343 source analytical-registry entries to actual generated tetrahedra, and retains all784 face objects with their local analytical roles.

This is an explicit geometric/prototype bridge, not an installation of analytical homotopies or native field operators. **24 checks pass.**

## The indexing gap and its construction

The existing analytical registry names cells by cube indices `(i,j,k)` in `0..6`, whereas the independently generated complex names actual ordered-chamber tetrahedra. Equal counts do not identify these objects, and a positional zip would be arbitrary.

The new bridge takes the fixed-axis unit-cube staircase

    b, b+e0, b+e0+e1, b+(1,1,1)

and sorts the three coordinates of **each vertex separately**. The resulting four vertices identify a generated ordered-chamber tetrahedron. This sorting construction is bijective at scale7; the checker also tests scales1 through6. Registry input order does not affect it, and it is not the positional zip of the two registries.

This is a newly constructed finite bridge, not a claim that the source registry previously specified it. Orientation signs are retained, including negative ones. Each assigned tetrahedron carries its actual four shared face IDs, its source face-prototype labels, and the source H234 cutoff/decay budget.

## Concrete shared-interface frontier

All588 interior faces acquire both local contexts:

| Local role pair | Shared faces |
|---|---:|
| H123 / H234 |294|
| H124 / H124 |147|
| H134 / H134 |147|

The source roles mean:

- H123: naturality/interchange with residual augmentation;
- H124: mate/localized equivalence with endpoint coordinate;
- H134: regulator transport with Hermitian/skew coordinates;
- H234: asymptotic face with finite-part and endpoint residue coordinates.

Thus294 interfaces require an explicit comparison between the H123 and H234 presentations. Their different names do **not** prove incompatibility: a suitable retained comparison may exist. Equally, assigning both names to one geometric face does not prove that comparison.

The294 same-role interfaces also remain obligations: matching prototype names do not establish matching parameters, residual coordinates or maps. Every face's composite and direct edge route has matching endpoints, but that checks typing, not the analytical homotopy equation.

## What is deliberately not promoted

The source registry describes a unique nerve filler after residual augmentation. The bridge retains that statement as source provenance; it does not import it as an evaluated filler on the generated native assembly. No face homotopy or tetrahedral filler is marked installed. No full-complex field/readout transport is claimed.

The114-record convention is still unbound. This work does not regroup the345-record geometric stream to force the desired count, and does not interpret343 prototype assignments as343 time steps.

## Reproduce

```sh
python research/strominger/checkers/check_esd7_analytical_binding.py
```

Artifacts:

- [Explicit assignments and all face contexts](results/esd7-analytical-prototype-binding.json).
- [Verification receipt](results/esd7-analytical-binding-verification.json).

The checker freshly generates the geometric complex, compares it with the prior attachment output, checks the sorting bridge, endpoint types and source decay budgets, and rejects duplicate/missing indices, ID mismatches, unsupported prototype variants, invalid decay budgets and mismatched edge routes. Source inputs are hash-pinned. This is not a fresh proof closure of the source analytical programme.

## Next construction

Take an actual generated H123/H234 shared face and construct the retained residual/endpoint comparison from the owning source prototypes. Test its two boundary reductions and transport, then extend across the294 mixed-role interfaces and the294 same-role interfaces. Keep the114-record producer and the full-complex field binding as separate open gates.
