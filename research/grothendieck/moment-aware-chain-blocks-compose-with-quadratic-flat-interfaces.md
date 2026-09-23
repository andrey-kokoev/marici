# Moment-aware chain blocks compose with quadratic flat interfaces

## Result

There is an exact, source-relative moment-aware interface theorem for a
cap-redundant class of balanced-gain chains. A block exposes its two endpoint
atoms and its contributions to the ORIGINAL U,V moments.

The theorem has two complementary conclusions:

1. A block of m>=4 atoms has exactly **(m-1)(m-2)+2 facets** in its
   four-dimensional endpoint-plus-moment image. Its raw endpoint image alone
   has only four facets. Small raw separators do not preserve bounded flat
   interface complexity after moments are added.
2. Blocks still compose exactly through shared endpoint values and local
   moment allocations. Keeping those allocations as internal variables gives
   a lifted interface whose finite separating dictionary is the UNION of the
   block dictionaries, rather than a materialized global projected boundary.

A prototype implements both global-block certified access and a genuinely
modular two-block optimizer that searches the unknown moment allocations.
Independent verification checks its answers against the global model.

## 1. Declared owning-source subclass

Use the owning source caps 0<=t_j<=100+2j and slopes r_j=128^-j. Fix the
shared positive chart s_j=1+(j mod 3), and write z_j=t_j/s_j. The admitted
chain evidence is

    0<=z_0<=1,
    1/8<=z_j-z_(j-1)<=1/4.

These are balanced-gain inequalities in raw atoms. They are deliberately a
cap-redundant subclass, not all balanced-gain systems from the parent work.
Indeed

    0<=t_j<=s_j*(1+j/4)<=3+3j/4<=100+2j.

Thus every assignment satisfying this chain evidence already obeys the
original source caps. No cap constraint secretly couples the independent
increments used below.

For a block [l,r], use the inherited base interval

    l/8<=z_l<=1+l/4

and the same increment bounds internally. These base bounds include every
restriction of a global chain assignment, and are implied at later block
starts by earlier chain blocks when shared endpoints are identified.

This construction extends to positive scales and nondegenerate increment
intervals whenever source-cap redundancy is separately certified. Active
caps, additional chords and general gain cycles can destroy the independent
increment box. The facet formula and algorithm below do not cover those
cases without further proof.

## 2. Exact product geometry of one moment-aware block

Relabel a block's local indices 0,...,m-1 for this derivation, while retaining
its global slopes r_j. Put ell=1/8 and write

    z_i=z_0+i*ell+sum_(k=1)^i delta_k,
    0<=delta_k<=1/8.

The base z_0 ranges independently in its inherited interval. Let

    S_i=sum_(j=i)^(m-1) s_j,
    R_i=sum_(j=i)^(m-1) s_j*r_j.

The displayed observations are the raw left/right endpoints and block U,V.
An invertible affine change of these four coordinates gives

    z_0,
    D=z_(m-1)-z_0-(m-1)*ell,
    U'=U-S_0*z_0-ell*sum_j j*s_j,
    V'=V-R_0*z_0-ell*sum_j j*s_j*r_j.

Their image is exactly

    [base_low,base_high] x sum_(i=1)^(m-1) [0,1/8]*(1,S_i,R_i).

Both directions follow by assembling the independent increments. This is a
one-dimensional interval times a THREE-dimensional zonotope, unlike the
ordinary two-moment planar residual image.

No block renormalizes the weighted observation. R_i uses the global r_j,
not a slope reindexed to start at one in each block. The affine change is a
geometry argument, not a change to the declared observation accuracy norm.

## 3. Exact quadratic facet count

For i<j, the secant slope of the points (S_i,R_i),(S_j,R_j) is

    (R_i-R_j)/(S_i-S_j)
      = (sum_(k=i)^(j-1) s_k*r_k)/(sum_(k=i)^(j-1) s_k).

For i<j<k, this weighted average is strictly larger than the average on the
next segment j,...,k-1, because every earlier r is strictly larger than every
later one. Consequently no three points (S_i,R_i) are collinear, and every
three generators (1,S_i,R_i) are independent.

Let n=m-1. For every pair of generators, their cross product is normal to
exactly their two-generator plane. The corresponding support face of the
three-dimensional zonotope is a nondegenerate parallelogram. Its opposite
normal gives the opposite facet. Every zonotope facet must have generators
spanning its two-dimensional direction space, so these exhaust the facets:
there are 2*binomial(n,2)=n(n-1).

Taking the product with the base interval adds two facets. The affine change
preserves faces, proving

    F_m=(m-1)(m-2)+2.

The raw endpoint image is instead the parallelogram determined by the base
interval and (m-1)/8<=z_right-z_left<=(m-1)/4, with four facets. Thus the
quadratic growth is intrinsic to the enlarged observation, not merely an
inefficient elimination trace. The count is a flat original-coordinate
halfspace lower bound, not a lower bound on every generator or lifted model.

## 4. Certified access without persistent boundary materialization

The source is an affine image of a box of m increments, including the base
increment. For any objective in endpoint/moment coordinates, pull it back to
these increments. Taking each increment at the appropriate cap computes
exact support and an admitted source witness with O(m) sign/sum work once
the block data are available.

A fixed finite dictionary consists of:

- two base-interval inequalities;
- both orientations of each pair-generator cross-product support, pulled
  back through the affine coordinate change.

The dictionary has exactly F_m rows and is independent of retained evidence
or queried moment values. It can be streamed rather than persistently stored.
The independent verifier checks its support values directly and verifies that
each pair normal annihilates the base column and exactly its two increment
columns. Opposite orientations and full pair coverage are checked.

Membership first scans for a violated facet. If none exists, the prototype
asks an exact bounded increment-space LP for a lift and checks its source
caps, chain differences and all four observations. Mathematical completeness
follows from the exact facet description and rational box-fiber feasibility;
unchecked solver output is not an admission certificate.

With retained rational linear endpoint/moment frames, bounded outer LP plus
this dictionary supplies a finite lazy procedure: every rejected optimizing
point adds a new facet, so at most F_m cuts are added. A source lift and dual
bound certify the optimum; a checked Farkas combination certifies emptiness.

The exact LP backend is a certificate proposer, not a proved implementation
of all rational LP instances. An initial proposal failed to supply a checked
Farkas ray on a contradictory-history control. The implementation now directly
recognizes opposite rows with negative summed bound and returns their exact
nonnegative contradiction combination. It does not infer emptiness from the
exception or claim the general solver has been repaired.

## 5. Moment-aware block composition and source gluing

Take adjacent blocks [0,s] and [s,m-1]. Their exact relations expose

    (t_0,h,U_L,V_L),   (h,t_(m-1),U_R,V_R),  h=t_s.

They compose through the exact accounting equations

    U=U_L+U_R-h,
    V=V_L+V_R-r_s*h.

The shared atom occurs in both local sums, so its contribution MUST be
subtracted once. Merely adding block moments describes the wrong source.

Every global source restricts to two admitted block points obeying these
identities. Conversely, fix compatible endpoints AND moment allocations,
obtain an admitted lift in each block, and concatenate them at their equal
shared atom. Every chain edge and source cap belongs to a block; the union
therefore satisfies all global constraints. The accounting identities give
exactly the requested moments.

The two local lifts need not be the restrictions of an earlier chosen global
witness. They glue because the common interface value was fixed before each
local membership query. This is not a claim that arbitrary selected section
points agree.

The same argument works for a chain of blocks with disjoint interiors, shared
charts and every shared endpoint retained. Additional declared local linear
frames remain valid in their blocks; global public frames pull back through
the accounting map. No hidden shared variable may be discarded prematurely.

## 6. Lifted dictionary and the representation tradeoff

For B blocks, retain B+1 raw boundary values and two local moments per block.
There are 3B+1 internal coordinates; the global two moments are linear
functions of them after subtracting the B-1 overlaps. They need not be stored
as two additional variables.

Each block inequality pulls back to a row involving just its two endpoints
and two local moments. The union of these dictionaries, together with retained
frames, describes the exact lifted relation. At a candidate allocation, either
a block returns a violated fixed dictionary row, or all blocks return lifts
that glue. This is a complete source-relative oracle under the checked block
LP hypotheses. Finite-separation closure applies in this enlarged dimension.

The progress dictionary has size

    sum_b F_(m_b).

For blocks of at most L atoms, with one shared endpoint between neighbors,

    sum_b F_(m_b) <= (L-2)*(m-1)+2B = O(mL).

Thus fixed-length blocks permit a linear-size lifted dictionary, even though
the flat four-coordinate global image has quadratically many facets. Internal
moment allocations and the larger outer LP dimension have not disappeared.
This is a representation tradeoff, not an elimination of the original source
information or an extension-complexity lower bound.

The theorem supplies the B-block construction. The executable modular backend
currently implements TWO blocks, using seven allocation variables. Its LP
actually chooses the shared value and local moments; they are not supplied
from a known global witness. Candidate rejection streams a cut from a block,
and successful local lifts produce a verified global source.

## 7. Executable evidence

For m=4,5,8,16,32, the global facet counts are respectively

    8, 14, 44, 212, 932.

The verifier checks all 1,210 facet rows, plus 40 support controls, 20
membership/separation controls and nine retained-history query certificates.
The histories include a moment-coupled U+V bound and a direct contradiction.

Two-block controls at m=8,16,32 supply nine glued witnesses and twelve exact
composed support bounds. For objectives +/-U and +/-V, block support bounds
with the shared-atom correction sum to the global support, and the supplied
global source attains both block bounds.

Two additional m=8 optimization requests use the seven-variable MODULAR
backend with unknown allocations. Both agree with independently verified
four-variable global optima. Their combined block dictionary has 22 rows,
compared with 44 global facets. The runs add 10 and 11 cuts respectively,
retaining 27 and 29 rows including initial bounds and evidence. These are
finite workload measurements, not worst-case time claims.

Six mutations are rejected: missing facet coverage, a changed source support,
a dropped expected frame, a mismatched shared witness, doubled shared moment
mass and an omitted shared-objective correction.

New files:

- `checkers/moment_chain_interface.py`
- `checkers/composed_moment_chain.py`
- `checkers/check_moment_chain_interface.py`
- `checkers/verify_moment_chain_interface.py`
- `results/moment-chain-contract.json`
- `results/moment-chain-interface.json.gz`

Reproduce:

    uv run --with sympy python research/grothendieck/checkers/check_moment_chain_interface.py
    python research/grothendieck/checkers/verify_moment_chain_interface.py

The independent verifier imports no constructor, source query engine or LP
solver. It reconstructs source increments, charts, expected histories and
accounting maps, checks linear certificates and validates all source witnesses.
Assertions must remain enabled.

## 8. Cost, admission and continuation limits

The source subclass, observer and increment evidence are frozen explicitly.
The original cap formula is checked directly. This is not a fresh upstream
analytical-admission proof, prime-realizable source claim, or authenticated
observation acquisition.

The prototype materializes O(m) block generator data; its current tail-sum
preparation uses straightforward summation. Facets are streamed by runtime
queries but materialized in the verification workload. A full scan can take
O(m^3) rational work with the current support evaluation per pair. Lift LPs
also materialize increment constraints. These costs are separate from the
O(m) unrestricted support operation and the finite cut-count bound.

The modular method trades a smaller source dictionary for a larger allocation
LP and retained block metadata. Rational slope encodings, lift vectors,
verification tables and proof archives remain charged. No constant-bit,
constant-work or total-storage claim follows from keeping the raw interface
small. No conditioning comparison is made after a chart change.

An exact projected public interface preserves public-only refinements.
Re-exposing hidden atoms still requires retained fine information or an
explicitly changed continuation contract. Source lifts are witnesses of
possibility, not the actual source or arbitrary audit-preserving transport.

## Synthesis

The balanced-gain raw-interface theorem does not extend with the same bounded
flat row count when moments are added. On a certified chain subclass the
increase is exactly quadratic, yet additive moment allocations support a
compositional lifted alternative with controlled dictionary growth.

The remaining structural boundary is active source caps or more general
balanced-gain graph evidence: their increments are no longer an independent
box. Extending the moment-aware representation theorem there requires a new
complete block relation, not an assumption that raw shortest-path summaries
already encode the moments.

Related notes:

- `../voevodsky/difference-constraint-blocks-have-controlled-certified-interfaces.md`
- `../voevodsky/balanced-gain-evidence-inherits-controlled-block-elimination.md`
- `../voevodsky/certified-gain-block-summaries-compose-with-source-lifts.md`
- `existential-audit-certificates-transport-sparsely-without-resolving.md`
