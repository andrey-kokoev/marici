# Joint audit images have a uniform finite separation dictionary

## Result

For the owning tail family, the variable-audit image is an invertible shear
of an audit box times a residual two-moment zonotope. This yields a positive
schema-relative representation theorem, not just membership at fixed pins.

For every finite audit schema A:

- the joint image has exactly **2m relative facets**;
- its displayed dimension is |A|+2 and its intrinsic dimension is
  |A|+min(2,m-|A|);
- a fixed, streamed separating dictionary has at most **2m+4 inequalities**,
  independent of the VALUES of the audits;
- finite rational joint moment/audit refinements admit complete lazy exact
  optimization or inconsistency certification, assuming a total exact
  bounded LP backend.

A new prototype implements this construction with checked rational LP
certificates and a separate verifier. It does not modify Nima's public API.

## 1. The source-relative product theorem

Let b_j=100+2j, r_j=128^-j and

    P_m = product_j [0,b_j],
    L_A(t) = (sum_j t_j, sum_j r_j t_j, (t_j)_(j in A)).

A is a fixed, canonically ordered schema. Its coordinates h_j remain
VARIABLES. Merely declaring A supplies no observed values.

Write I={0,...,m-1}\A, k=|A| and q=|I|. On the displayed joint coordinates,
apply the invertible linear shear

    u = U-sum_(j in A) h_j,
    v = V-sum_(j in A) r_j h_j,
    h = h.

Then, exactly,

    shear(L_A(P_m)) = Z_I x product_(j in A) [0,b_j],
    Z_I = { (sum_(j in I) t_j, sum_(j in I) r_j t_j) : 0<=t_j<=b_j }.

Proof: each source point splits into its independent audited and free
coordinates. Conversely, any point in the right-hand product has admissible
audited coordinates and an admissible free lift; their concatenation is a
source lift of the inverse shear. No extra compatibility constraint remains.

This depends substantively on the owning source being a box. Arbitrary hidden
source constraints need not survive this factorization.

## 2. Exact facet and dimension accounting

If q>=2, distinct slopes make Z_I a full-dimensional planar zonotope with
exactly 2q edges. The product with the k-dimensional audit box has dimension
k+2 and exactly 2q+2k=2m facets. Each residual edge times the audit box and
each audit-box facet times the residual polygon is a facet; these exhaust
the product's facets.

If q=1, Z_I is a nondegenerate segment. The product has dimension k+1=m,
with 2+2k=2m relative facets and one affine equality in the displayed space.

If q=0, Z_I is a point. The product is the m-dimensional audit box with
2m relative facets and two displayed affine equalities.

The shear preserves these counts. Thus adding raw-coordinate audits does NOT
cause a source-facet explosion in this family. It instead increases dimension
and the width of joint-coordinate rows. These are different resource accounts.
The same 2m is also a lower bound for an irredundant original-coordinate
relative halfspace presentation; it is not a state-storage lower bound for a
generator program.

## 3. A finite dictionary uniform over audit values

For a residual normal (a,b), define its pulled-back joint normal

    n_A(a,b) = (a,b,(-a-b*r_j)_(j in A)).

Its exact source support is

    H_I(a,b) = sum_(j in I) b_j * max(0,a+b*r_j).

Hence the joint inequality

    n_A(a,b) dot (U,V,h) <= H_I(a,b)

is valid for ALL audit values simultaneously. An apparent pin-dependent
right-hand side has become a fixed row in the enlarged coordinate space.
This is the missing finite-progress guarantee for variable pins.

The declared dictionary is:

- Always: both cap bounds on every audit coordinate (2k rows).
- q>=2: residual normals +/-( -r_i,1 ) for i in I (2q facet rows),
  plus +/- (1,0) residual mass bounds (two auxiliary support rows).
- q=1: the two residual mass bounds and the paired equality
  v-r_i*u=0 (four rows).
- q=0: paired equalities u=0 and v=0 (four rows).

Thus its size is 2m+2 when q>=1 and 2m+4 when q=0. For q>=2 the two mass
bounds are redundant but useful for simple outside-mass cases. Equality rows
are not counted as relative facets.

Each row has a fixed schema-relative identifier and exact rational encoding.
Rescaling a row does not create progress. Dictionary size and facet count
must not be conflated.

## 4. Total exact separation and source lifts

At a rational joint point, first check audit caps and subtract the audit
contributions. Greedy free-coordinate filling in decreasing and increasing
slope order computes the extreme possible residual v values at fixed u.
Interpolate their source profiles when the point is admitted. Append the
supplied audit coordinates to get a complete source lift.

For zero or one free coordinate, the same rule reduces to the declared point
or segment equalities and caps; no division by a zero vertical width occurs.

If no lift exists, at least one row of the dictionary is strictly violated,
because its intersection is exactly the product image under the inverse
shear. Scanning the streamed dictionary therefore finds a certified cut.
This is a deliberately simple complete separator, not an optimal search
algorithm. It need not hold a full facet table in persistent state.

Each candidate uses its own audit values to construct a possible lift. Those
values do not change the dictionary. This is precisely what permits
optimization over variable pins rather than merely reconstruction conditional
on previously fixed pins.

## 5. Closure under retained linear evidence

A state retains the source binding, m, A and a complete finite tuple E of
rational joint-coordinate halfspaces. It denotes

    C_(A,E) = {t in P_m : E(L_A(t))}.

Start an outer LP from certified coordinate bounds and every frame in E.
At each optimum, either return an admitted source lift and matching dual
bound, or add a strictly violated dictionary row. A rejected candidate obeys
all earlier rows, so its cut has not already been added. There are at most
2m+4 rejected candidates. An empty outer LP returns a Farkas certificate.

This is an instance of Voevodsky's finite-separation refinement theorem with
its previously missing joint-audit dictionary now supplied. Additional
rational frames may couple audit coordinates with moments or with each other;
they need not be exact pins or axis-aligned boxes.

An unrestricted support witness that already satisfies E is an optional fast
path. Its exact source support bound proves optimality directly. Such a
terminal support row need not belong to the finite PROGRESS dictionary: it
is not used to justify an unbounded sequence of cuts.

State-relative membership checks all expected frames, then base membership.
A violated frame or source cut excludes that POINT. It does not by itself
certify that the whole state is empty.

The mathematical closure theorem uses a total exact rational LP procedure.
The prototype uses SymPy's rational LP backend, then checks its candidates
and linear certificates. An unexpected solver failure is an operational
failure, not mathematical ambiguity or permission to emit an unchecked
inconsistency claim. Finite replay is not a proof of the third-party solver's
implementation for every rational input.

## 6. Independent certificate contract

The verifier obtains m, the ordered schema, retained frames and objective
from a separately retained frozen experimental contract. It reconstructs
source supports directly by pulling each joint normal back to source
coordinates and summing positive contributions over the caps.

It imports neither the joint engine nor an optimizer nor a greedy lift
constructor. It checks:

- every expected frame in its expected position;
- exact source box bounds and schema-specific dictionary rows;
- strict separation, prior-row satisfaction and unique cut identities;
- source caps, both moments and every audit coordinate of a returned lift;
- nonnegative dual or Farkas multipliers and their exact arithmetic identities;
- correspondence to the independently expected state and query.

The LP variables are nonnegative joint coordinates, a valid source property.
For an optimum, a nonnegative combination of rows with normal >= objective
componentwise and matching bound suffices. For inconsistency, normal >=0
and negative bound contradict nonnegative coordinates. The explicit lower
coordinate bounds are also present in the retained row packet.

A hash binds artifact versions; it does not authenticate external observations
or an unknown past history. The experiments' expected state is independently
retained relative to the answer, not independently authenticated field data.
Copying a value from a selected lift is still not observational justification
for a new audit.

## 7. Executable evidence

New files:

- `checkers/joint_audit_tail_interface.py`: streamed dictionary, joint
  membership, retained-frame membership and lazy joint optimization.
- `checkers/check_joint_audit_tail_interface.py`: frozen producer controls.
- `checkers/verify_joint_audit_tail_interface.py`: independent replay.
- `results/joint-audit-tail-interface-contract.json`: expected schema/history/query.
- `results/joint-audit-tail-interface.json.gz`: exact answer packets.

The producer freshly replays the upstream two-moment tail admission verifier
and Nima's audited-section verifier. It then tests 19 schemas, including every
schema at m=2 and m=3, selected schemas at m=4,8,16, and all residual ranks.

Passed workload:

- 76 retained-frame optimization/inconsistency queries;
- 271 joint membership/separation cases;
- 228 state-relative membership cases;
- 19 feasible reset histories whose complete retained prefixes are inconsistent;
- seven deliberate rejection controls: dropped history, corrupted lift,
  wrong schema, wrong query, wrong optimum value, negative multiplier and
  altered dictionary row.

The maximum observed cut count was 15, displayed dimension 6, row count 25,
nonzero optimum multiplier count 5, and rational numerator/denominator bit
length 189. These are workload observations, not asymptotic bounds.

    uv run --with python-flint --with sympy python research/grothendieck/checkers/check_joint_audit_tail_interface.py
    python research/grothendieck/checkers/verify_joint_audit_tail_interface.py

## 8. Cost ledger and limits

| Account | What this result establishes |
| --- | --- |
| Source geometry | Exactly 2m relative facets for every audit schema |
| Separation progress | At most 2m+4 rejected candidates per query |
| Displayed dimension | k+2; rank is k+min(2,q) |
| Persistent evidence | Full audit schema and full retained frame tuple must be charged |
| Prototype source data | Materializes O(m) caps/slopes/free indices; no claim of a constant-field implementation |
| Dictionary | Streamed rows; no complete persistent facet table; current scanning and row support computation still cost arithmetic work |
| Query-local storage | Coordinate bounds, every frame, discovered cuts and proof data; dense joint rows have k+2 coefficients |
| LP work | Dimension grows with k; the old planar vertex enumerator is not reused |
| Proof arithmetic | Ambient conic bounds allow d nonzero optimum or d+1 Farkas multipliers; the prototype does not promise a minimal-support packet |
| Precision | Exact rational coefficients and outputs can grow; facet/cut counts do not bound bit complexity |

Exact fixed-pin conditioning and finite-precision margin gates remain separate
accuracy results. Linear error boxes can be represented as frames, but their
observational justification, physical noise model and actual-source meaning
are not supplied by the LP interface. Nonlinear/discrete predicates and
non-box hidden constraints remain outside this theorem.

## 9. Synthesis

The rich positive object is now explicit:

    source box decomposition
      -> schema-relative sheared product image
      -> finite uniform separating dictionary
      -> certified access closed under rational linear refinement.

The audit-extension gap is not a geometric obstruction in this source family.
It is resolved by retaining audit coordinates as variables and pulling back
residual cuts before optimization. Dimension, retained information and
accuracy costs remain real even though the source facet count stays fixed.

This construction promises certified access to a family of possibilities,
not the actual source and not audit-preserving witness interchange. Those
identity obligations are neither needed nor silently solved.

Related notes:

- `../voevodsky/finite-separation-makes-certified-query-presentations-closed-under-refinement.md`
- `../voevodsky/a-certified-query-presentation-of-source-relative-filling-families.md`
- `../voevodsky/finite-precision-tail-queries-have-sharp-margin-gates.md`
- `audit-placement-controls-residual-conditioning.md`
