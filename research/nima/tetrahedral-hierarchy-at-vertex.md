# The filled tetrahedral constructor retains four arity levels

## Question and source

Does each witnessing return contain unary, binary, ternary and quaternary structure, and feed that complete structure back into the starting vertex?

The actual source examined is `agda/RetainedTetrahedralPackage.agda`. Its `Cells.Full` package contains the following named slots:

| Arity level | Retained data | Cell dimension |
|---|---|---:|
| Unary | Four marked vertex values | 0 |
| Binary | Six shared edge paths | 1 |
| Ternary | Four triangle witnesses | 2 |
| Quaternary | One tetrahedral coherence witness | 3 |

These are arities and simplex cells, not powers of an energy variable. “Unary” here does not assert unitarity. The table describes this filled tetrahedral constructor; it is not a proof that every WG operation must have exactly these four levels or that each contribution is nonzero.

`Cells.build` starts from a supplied marked horn (vertices, edges and three triangle witnesses) and completes the fourth face with its tetrahedral coherence. It retains the lower inputs. It does not obtain the entire hierarchy from a bare four-edge loop: the seed-to-filled-tetrahedron interpretation remains a separate obligation.

## New formal check

`agda/TetrahedralHierarchyAtVertex.agda` imports this existing package and projects its vertices, edges, complete face-bearing surface and tetrahedral filler. Exact reassembly is proved. Thus all four levels survive in the full constructor's output.

The existing `Cells.vertex` operation only projects the chosen vertex value. The new module specializes an existing counterexample: two different packages have the same four fixed vertices (and even the same diagonal), but differ in edge witnesses. Their selected vertex values agree. It follows that there is no vertex-value-only decoder recovering every fixed-boundary package. Therefore the bare vertex projection cannot be called lossless conversion of the whole hierarchy.

## Retaining the complete hierarchy at the mark

A new, explicit view adapter is defined by

    View(mark) = (x : X, p : Full, vertex(p,mark) = x).

It places the full package beside its marked active value, with an agreement witness. Both round-trip laws are proved, and all tiers are recovered. This is a lossless marked presentation, not an assertion that the old vertex projection already retained those fields.

The active value is provably unchanged by this adapter. No next-step update consumes the attached package yet. Thus we can retain the complete hierarchy **at** a marked vertex, but have not shown that it changes that vertex's subsequent dynamics. The construction introduces no scalar coefficients or polynomial action.

## Disposition

The proposed four-level organization is already present in the actual filled tetrahedral carrier. The useful correction is that its bare vertex readout does not carry that hierarchy back; an explicitly retained marked view does. A back-reaction mechanism would need to use the attached hierarchy in its next update, rather than discard it or call its unchanged projection a response.

This does not establish a universal four-term law, a quartic physical interaction, or a gravitational constant. It also does not supply the missing face and edge interpretations that turn our free seed cycle into a filled tetrahedron.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module TetrahedralHierarchyAtVertex -Fresh

Fresh safe Cubical/guardedness closure passed on the first run, with ignored interfaces and stable inputs. Receipt: `results/agda-TetrahedralHierarchyAtVertex.json`. Finished 2026-10-05T20:19:00.3113811Z. Source SHA-256: `47dc77b572d3cae39d475a87777967f609e2c703fe6cd6569f29815ca9f958d4`.

No postulates or unresolved holes were added. No ledger entry, commit or publication is claimed.
