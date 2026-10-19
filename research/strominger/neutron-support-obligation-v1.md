# What coefficient elimination does—and does not—justify about neutron occupancy

## Restart point

The experimental terminal P/E rule repairs four saved isotope deletions: two N-14 candidates from N-15 and two Ne-21 candidates from Ne-22. It uses six local shortcuts in total. These remain experimental, not native admissions.

The open premise is permission to leave the intermediate neutron body unoccupied while using its reference-mediated transfer. The prior [graded path algebra](graded-path-rules-v1.md) and [coherence cube](contraction-coherence-cube-v1.md) organized that permission but did not derive it.

This audit tests whether eliminating the intermediate coefficient variables supplies the missing justification. **It does not.** It supplies an exact endpoint relation while retaining a uniquely determined, generally nonzero intermediate reference response.

## Exact coefficient calculation

Let A be the actual five-coordinate PN permutation and B the actual NE permutation. In the ambient linear response space, write p,n,e for the three coefficient vectors. The native relations are

```
n = A p,
e = B n.
```

Eliminating n gives

```
e = B A p.
```

The projection from native solutions to endpoint solutions is bijective: the lift is uniquely n=A p. The intermediate variable has been eliminated from the description, **not set to zero**.

The exact checker finds, on every tested local instance:

- native constraint rank 10 on 15 ambient coefficient coordinates: solution dimension 5;
- eliminated endpoint constraint rank 5 on 10 coordinates: solution dimension 5;
- adding n=0 raises the native constraint rank to 15: only the zero solution remains.

These are ambient coefficient-response dimensions, not a count of independent physical particle degrees of freedom. The calculation does not assert that all ambient vectors are physically realized.

The actual permutation maps are invertible and norm preserving. Consequently the implication n=0 => p=e=0 also holds on any restricted source family. All five ambient source basis responses are checked, with inverse recovery and unchanged endpoint composition.

## Two meanings of “unoccupied” must not be conflated

### A. Unoccupied means zero intermediate coefficient response

If that interpretation is imposed while retaining both native transfer equations, nonzero P/E transfer is impossible. A nonzero source fixture has squared PN residual 55 when the middle response is forcibly zeroed.

This is a **conditional obstruction**. The source has not established that an unoccupied neutron cell must be represented by a zero value of these five reference coefficients. We do not adopt that interpretation as physical vacuum theory.

### B. The body is unoccupied but the reference response is retained

Then n=A p remains a nonzero derived reference response, even though N is not counted as an occupied body. Endpoint coefficient elimination is consistent. But the permission to use that reference-mediated relation is an additional occupancy/admission rule.

This is precisely the premise of the experimental shortcut. Calling n a reconstructed or eliminated variable does not itself authorize that rule.

## A support-policy separation on the actual witnesses

The audit compares two explicitly distinct support descriptions:

```
native composition:  required occupied support {P,N,E}
experimental PE:     required occupied support {P,E}
reference support:   {P,N,E} in both descriptions
```

Their endpoint readers, zero grade, marked reference geometry and composed coefficient maps agree after the occupied-support requirement is forgotten. Reversal inverts the same maps and preserves each description's respective support requirement; it therefore cannot choose between them.

On each selected deletion configuration, the native support condition fails and the experimental support condition succeeds. This is a different answer to an occupancy predicate despite identical occupancy-blind transfer data.

The separation establishes only that the listed coefficient/geometry/reversal data do not determine occupied-support permission. It is **not** a pair of equivalent implementations of the unchanged production grammar: that grammar retains the native support obligation. The second policy is the explicitly proposed extension.

The experimental vacancy guard remains essential. The fact that a smaller support set is contained in a larger occupied configuration is not permission to apply the guarded rewrite with N occupied. The prior guard checks are freshly replayed and still reject that case.

## Actual evidence checked

The checker uses the saved native factors, packet permutations, origins and marked coordinate aliases for:

- all 24 hydrogen markings;
- all six shortcut terms in the four passing N-14/Ne-21 deletion configurations.

It freshly replays the separate Python witness audit, which verifies all 20 isotope deletion trials and finds the same four experimental positives. It also replays the graded-support checker and its 24 invalid-contraction controls. It does not run a fresh lattice search or regenerate the saved universe in this audit.

The new checks cover 30 local instances and 150 ambient coefficient basis responses, as well as support-preserving reversal and the zero-middle rank obstruction. All coefficients and ranks use exact rational arithmetic.

## Consequence for constructing isotopes

The experimental repairs remain well specified and finitely checked, but no new native isotope has been admitted by this calculation. Production and viewer status remain unchanged.

The unresolved source obligation can now be stated more narrowly:

> Supply an independently justified observation/admission rule distinguishing an occupied neutron carrier from a retained, possibly nonzero neutron reference response, and show that the grade-zero terminal transfer is available under the latter condition.

The rule would need to preserve the existing whole-assembly contact, phase, rooted-construction and exit checks. Neither invertibility, norm preservation, reconstructed reference data, grade zero nor reversal supplies it alone. An occupancy-sensitive rule or source construction is required; introducing a desired isotope into the positive set is not that derivation.

There are therefore two honest continuation tracks:

1. Keep the native grammar and continue bounded isotope searches, such as the previously untested Ne-21 origin-10 bound.
2. Investigate the explicit reference-only-N extension as a separate grammar, with a stated source-level occupancy semantics and new admission evidence.

Our later compact reconstruction work helps distinguish retained reference information from erased information. It does not turn reference availability into permission to occupy or omit a physical carrier.

## Reproduction

```
python research/strominger/checkers/check_neutron_support_obligation.py
```

Receipt: `research/strominger/results/neutron-support-obligation/verification.json`. No production, viewer, physical binding or stability claim is changed.
