# Joint uncertainty commutes with presentations, quotients and admitted history

## Implemented result

The interval adapter is now integrated into the source-presentation and history bridge. This is executable work, not a proposed interpretation of another lane's result.

The integration uses the owning adapter unchanged:

`../grothendieck/certificates/reconstruct_uncertain_forgotten_slice.py`.

It carries the entire joint source set through expansion/regrouping and the actual vacuum-pair quotient with residual retention. It then compares two exact constructions of the history-compatible set:

1. intersect the reconstructed source set with the admitted reachable history;
2. pull all seven reading intervals back through that history and intersect with the earlier evidence.

The resulting parameter domains are equal. Earlier evidence is retained separately from the final terminal check.

## 1. No independent re-boxing

Write the reading evidence as

`y=c+G epsilon`, with `epsilon in [-1,1]^7`.

The source inverse D and interaction transform Z give

`a=Dc+DG epsilon`,

`m=ZDc+ZDG epsilon`.

Expansion back from interactions recovers both the source center and its entire generator matrix. This is a matrix identity for all shared parameters, not a claim based only on endpoint samples.

For the two-vacuum projection P and the owning residual extraction R, retain

`(Py,Ry) = (Pc,Rc) + (PG,RG) epsilon`.

The same seven parameter labels occur in both blocks. The declared section and kernel inclusion reconstruct y exactly. Separate marginal intervals for the visible pair and residuals are not used as replacements.

The tests exhibit why: taking all their marginal upper endpoints can reconstruct a reading outside the original reading box. Likewise, independent upper endpoints of source-coefficient marginals violate the ideal's exact coefficient-sum constraint.

## 2. AST/presentation compatibility for affine coefficients

The presentation test is applied to the constant coefficient and all seven generator coefficients of the affine family. Each is expanded in the actual P/Q and P/H source bases and compared as an ordered marked source.

Because these coefficient maps are linear, the checked affine identity holds on the complete parameter box. All 128 parameter-box vertices are also tested per fixture as an independent regression check; those samples are not the sole justification.

## 3. Exact joint history pullback

The separately admitted deterministic history appends P-Q in each of the last two blocks. Let T map the initial pair q=(a_P,a_Q) to the final eight path coefficients. Actual source multiplication checks T.

Its seven-reading map is J, with

`Jq=(a_P,a_Q,0,0,0,0,0)`.

The forward-intersection equations are

`DG epsilon - Tq = -Dc`.

The backward reading equations are

`G epsilon - Jq = -c`.

Exact rational row reduction verifies equality of their complete affine solution spaces in the SAME nine parameters `(epsilon,q)`. Both sides also retain the identical epsilon bounds and earlier terminal interval on `a_P+a_Q`. Consequently the constrained joint sets agree, including when they are empty.

Eliminating epsilon gives a bounded two-dimensional history polytope. The checker computes its vertices exactly from rational boundary intersections. It handles polygons, line segments, points and empty sets. The complete 13-coordinate history is the image of that polytope under the retained transition map, not the product of separate stage marginals.

## 4. Cases that matter

At each background 2, 3 and 4, the suite checks:

- noisy cubic evidence with an initial zero-terminal constraint;
- a correlated line segment with initial terminal exactly one;
- a genuine six-vertex polygon with interval-valued earlier evidence;
- a final reading incompatible with the declared dynamics;
- earlier evidence incompatible with otherwise valid final intervals;
- the exact zero-width history case.

One nonempty example has a reading-box center outside the reachable subspace, while its joint uncertainty set intersects that subspace. Intersecting only the center would incorrectly reject it.

In the correlated segment, independently combining historical marginal endpoints violates the retained terminal fact. This directly tests cross-stage correlation retention.

## 5. Filtration and conditionality

Every nonempty compatible history in this model has two appended ideal factors, so its final source lies in I^2. If the retained initial terminal is exactly zero, the reachable set is in I^3. These are statements about the whole history-compatible set, not the unconditioned reading-box center.

Empty histories are reported as empty; they are not assigned a fictitious reconstructed source or a vacuous physical filtration conclusion.

The history contract is explicitly admitted by the synthetic caller. It is never inferred from the final readings. The final six-event terminal interval and the earlier first-block terminal interval remain distinct evidence objects.

## 6. Retention and verification

The output retains the entire owning interval-adapter bundle, the earlier evidence, the source/history labels, and all shared generators and constraints. Recovery recomputes the integrated bundle and compares it before returning the incoming evidence.

Corruption checks reject changed shared generators, earlier intervals, derived vertices and history background labels. An absent history admission is rejected. Digests bind these contracts; they do not authenticate physical evidence or prove that the dynamics occurred.

Run:

`python research/nima/checkers/check_uncertain_presentation_history_bridge.py`

Artifacts:

- `research/nima/results/uncertain-presentation-history/tests.json`
- `research/nima/results/uncertain-presentation-history/joint-history-example.json`

This is a repository-local integration checker/adapter, not a newly packaged standalone deployment. Scope is the finite forgotten source, exact rational interval sets, and the prescribed deterministic history. Uncertain dynamics, broader marked sources, actual noisy acquisitions and global source-bimodule extensions remain outside this certificate.
