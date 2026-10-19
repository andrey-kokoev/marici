# Testing an M/C torus in simplicial realization space

## Existing geometry

Exact rational simplicial homology was computed from the three supplied reader
facets, the full glued 4-simplex and its boundary. Boundary matrices satisfy
d squared = 0.

| Complex | Betti numbers |
|---|---|
| Union of P/N/E tetrahedral facets | (1,0,0,0) |
| Full T 4-simplex | (1,0,0,0,0) |
| Boundary of T | (1,0,0,1) |
| Link of the common C1/M1 edge within reader-facet union | (1,1) |
| Link of that edge in full T | (1,0,0) |

The three selected facets provide one transverse circle: their common-edge
link is the triangle boundary. The common edge itself is still an interval.
There are not yet two independent closed directions. The entire reader-facet
union has no first homology; the link circle should not be confused with a
noncontractible loop of the whole union. Filling T fills the triangle link.

## Two explicit closure prototypes

If the longitudinal interval is made periodic while retaining a transverse
circle, the resulting surface depends on the seam:

- Identity gluing of the transverse circle gives a torus, Betti (1,2,1).
- Reflection gluing gives a Klein bottle, rational Betti (1,1,0).

Both were constructed as 3x3 triangulated strip closures. All edges belong to
two faces and every vertex link is a circle. These are checked closed-surface
prototypes, not identifications already present in the isotope geometry.

The prior reference reversal exchanges u/v (the core endpoints) and b/c in the
triangle link while fixing a, so its action on that link is orientation
reversing. If that action is chosen as the longitudinal closure monodromy,
the prototype is the Klein-bottle case. The physical/configuration closure law
has not yet been supplied; its choice determines which prototype applies.

## Native two-axis transport

The separate electron spin-axis dictionary gives -I for the commutator
A B A^-1 B^-1 in all 12 signed distinct-axis cases. Projectively the commutator
is identity, while full spinor amplitudes retain the sign.

Those generators therefore cannot themselves be the two commuting holonomies
of an ordinary flat full-spinor torus representation. They could motivate a
projective/twisted transport model. They have not yet been identified with the
geometric M/C cycles, and their phase behavior does not establish torus or
Klein-bottle topology by itself.

## Disposition

The current simplicial data supplies one transverse cycle. A second cycle
requires an additional longitudinal boundary identification. Its action on the
first cycle is the next decisive datum: preserving orientation gives the torus
prototype; reversing it gives the Klein-bottle prototype.

Production and viewer unchanged.

```sh
python research/strominger/checkers/check_T_torus_hypothesis.py
```

Evidence: `results/T-torus-hypothesis/verification.json`.
