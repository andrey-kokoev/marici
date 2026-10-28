# Five-side oct: whole-depth comparison domain and an axis-grammar obstruction

**Status: native incidence and formal comparison-boundary diagnostics, not a completed coherent wiring.** This advances the [rule-and-obligation specification](five-side-oct-routing-obligations-v1.md) without selecting routes, boundary matches or group counts.

Subsequent [Hopf-hypothesis testing](five-side-oct-hopf-hypothesis-v1.md) identifies these residual diagrams with the 44 interior vertex stars and constructs exact integer sphere-sweep witnesses in their native links. It distinguishes a possible local spinor lift from the unsupported claim that the physical carrier itself is a Hopf total space.

## 1. The old grammar cannot represent the specified entry comparisons

The operator's layer-4 comparisons have a shared charged reference, two incident N occurrences, and a common charged comparison site. The two native two-interface presentations are

```
shared reference → first N → comparison site
shared reference → second N → comparison site
```

For **all four specified comparisons in each of six readings**, the entry and exit faces at each N have **different coordinate normals** and share a native edge. This holds at both edge units three and five.

The old constructor only supplies opposite-face, same-axis N passages. Hence it cannot represent these specified comparison boundaries in that passage grammar. This is a precise representational obstruction, not merely a missing boundary seam or an incorrect tube count. Matching Sulfur's periodic candidate did not check this operator requirement.

One five-edge example, reading `0:-1`, is:

- common P reference: `proton:-1,-1,2,2`;
- E comparison site: `electron:-1,-1,1,1`;
- N alternatives: `neutron:-1,0,2,2` and `neutron:0,-1,2,2`;
- respective entry/exit normals: `(1,0)` and `(0,1)`.

The source-directed comparison is between E directions at the shared P reference. Each pair of N faces shares two actual vertices forming an edge of squared length two.

**Scope:** a comparison presentation is not automatically an individual wire trajectory. This does not authorize turning every wire between arbitrary adjacent faces. It shows that an adequate model must represent these cross-port comparisons and supply their witnesses. The old same-axis paths alone do not do that.

## 2. Enumerate the global incidence domain before supplying comparisons

`../realization-tower/five-side-oct-comparison-domain.mjs` uses only native geometry and the independently enumerated source obligations. It does not import the current fibration matching or routing candidate.

For each reading it constructs the entire directed shared-face graph, ordered by cell-centre height. Every native interface crosses exactly one half-unit layer. It then retains:

1. every two-interface path and every endpoint pair with alternative presentations;
2. every three- and four-interface presentation;
3. every exact replacement of one intermediate presentation by another, with both surrounding contexts retained;
4. the complete presentation graph at each endpoint pair and path length;
5. closed boundaries in that graph, still without maps or fillers.

Only the four entry comparisons in a reading are marked as source-required by the reviewed operator specification. The remaining parallel pairs are a **potential comparison domain**. Their authorization is not inferred merely from having common endpoints.

[Source incidence selects the coherence nerve](source-incidence-selects-the-coherence-nerve.md) explains why this boundary information must precede a choice of filling law. It is a methodological source, not itself a port binding or permission to fill the diagrams below.

## 3. Whole-depth results

The following are **per reading**, not sums of six independent copies of the carrier:

| Diagnostic | Three-edge carrier | Five-edge carrier |
|---|---:|---:|
| Native cells | 51 | 245 |
| Shared interfaces | 104 | 560 |
| Parallel two-interface boundaries | 60 | 360 |
| Three-interface paths | 384 | 3072 |
| Four-interface paths | 656 | 7376 |
| Three-interface presentation graphs | 136 | 1136 |
| Four-interface presentation graphs | 114 | 1576 |
| Presentation-graph cycle rank | 82 | 768 |
| Rank spanned by disjoint-substitution squares | 76 | 724 |
| Residual cycle-space dimension | 6 | 44 |

All six readings have the same diagnostic counts. The three-interface presentation graphs are trees; that alone does **not** establish coherence. Closed boundaries appear at four interfaces.

The rank calculations are over **GF(2) edge sets of finite presentation graphs**. They do not compute nonabelian holonomy, phases, independent field modes, or physical tube counts. In particular, **44 is not a new answer to “how many coherence groups?”**

## 4. The repeated residual diagram

Every residual four-interface diagram has:

- N endpoints;
- 16 native path presentations;
- 20 elementary comparison-context moves;
- graph cycle rank 5;
- four independent squares from disjoint substitutions;
- one remaining cycle-space direction after those squares.

For a fixed reading, all six small-carrier occurrences and all 44 large-carrier occurrences are **exact geometric translates of the same diagram**. The check normalizes full native cell geometry and presentation incidence—not just counts. The same translation-normalized diagram occurs at both sizes.

A five-edge representative has endpoints

```
neutron:-1,-1,3,2  →  neutron:0,0,2,1
```

Its 16 presentations go through the intervening charged, N, and charged layers. The four disjoint squares concern changes in separate parts of the presentation. They do not account for the entire graph cycle space; an overlapping-comparison boundary remains.

This localizes an actual missing problem: give the source-bound comparisons and a compatible filling for this diagram, then check their simultaneous translated occurrences and overlaps. The geometry supports reusing the **incidence template**. Equivariance of any comparison action or filling is a separate obligation, not a consequence of translation-normalized geometry.

The recorded fundamental cycles depend on a diagnostic spanning forest. Their particular lengths are not primitive physical arities. The graph and square span, rather than that basis choice, are the retained evidence.

## 5. What this does not establish

- There is still no signed-pair/port binding or actual comparison map.
- Four-interface enumeration is not a completeness theorem for all path lengths or higher overlaps.
- A GF(2) residual is not a nonabelian obstruction class or proof of an unfillable boundary.
- Empty witness fields are not identity witnesses.
- Native comparison boundaries do not supply a boundary closure law.
- No route, N-channel grouping, target permutation or rendering has been changed by this work.

The [geometric context note](geometric-context-and-extended-coherence-v1.md) also describes a reader with incident faces sharing an edge, but its candidate field binding has its own hypotheses. Similarity to the adjacent N-face geometry found here does not establish an isomorphism of native packets, transport actions or histories.

## 6. Reproduce and inspect

```sh
node --test tests/five-side-oct-comparison-domain.test.mjs
node research/strominger/checkers/check_five_side_oct_comparison_domain.mjs --record
```

The checker verifies all six readings at both sizes. The receipt is
`results/five-side-oct-comparison-domain-v1/verification.json`. It retains source hashes, every residual site's endpoints and geometry digest, every required-prefix axis obstruction, and a full representative diagram at each size. The complete domains are reproducible from the source; a large duplicated geometry dump is not required.

Tests independently check native face ownership, context boundaries, closed cycles, GF(2) ranks using a separate set-based elimination, exact translation normalization, and invariance under arbitrary cell renaming and enumeration order. The result is explicitly `constructionAdmitted: false`.

**Next step:** bind the existing native comparison constructors to the representative diagram's adjacent-face operands, including retained contexts and histories. Evaluate the actual composed boundary maps. Only then can one request a source-authorized filler, transfer it across the carrier, and test simultaneous compatibility. Adding more same-axis tubes or arbitrary seam connections cannot address this obstruction.
