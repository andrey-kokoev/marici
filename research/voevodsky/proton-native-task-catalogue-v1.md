# What the tetrahedral seed's native relationships can resolve

## Result and exact task boundary

The actual 1,836-transfer realization admits an exact classification of its
**linear stage-readout tasks**, including a sharp reconstruction theorem and
an explicit ambiguity invisible at both original seed faces.

This is a first bounded catalogue, not a classification of every problem that
could be posed on the geometric seed. Inputs here are arbitrary complex
coefficient assignments on the existing twelve-triangle realization. We do not
claim every such preparation is generated from the six bare source arrows, nor
that an exact complex-amplitude probe is already a physical instrument.

The active SCC obligation is forward realization of the native typed schedule,
then readout descent on its explicit observer kernels. The stratum is the fixed
36-complex-dimensional carrier with its supplied tetrahedral coordinates,
cyclic sector and inherited axis frame. There is no physical-time parameter.

## Source, types and permitted operations

The unchanged source frontend reconstructs the two cycles ABC and ADB from
`research/nima/inputs/proton-six-arrows.json`. Its generated list matches every
endpoint and exact coefficient in
`research/nima/results/twelve-triangle-1836-arrows.json`.

The three 36-coordinate stage spaces have distinct port types:

    raw --L--> local --G--> aligned --N--> raw.

The supported coefficient counts are 108, 432 and 1296. Matrix equality gives
GL=LG=N and NGL=N. Therefore the records generated from raw input x are

    x, Lx, Nx, Nx.

They are **not** x,Lx,Gx,Nx. Applying G directly to raw input would add an operation
not present in this schedule. We retain this distinction throughout. Repetition
gives Nx at every subsequent stage because LN=GN=NN=N.

Allowed observations are exact complex-coordinate readings of these retained
stage records, with offline linear comparisons. All coordinate identifications
between stage copies refer to their explicit (triangle,axis) labels. No
inverse projector, extra dynamics, face-flux norm or energy law is introduced.

## Task catalogue

| Task | Required data/access | Answer and retained freedom |
|---|---|---|
| Diagnose failed local selection versus failed collective agreement | Full raw, local and aligned records | Orthogonal components of dimensions 24, 11 and 1 |
| Decide whether twelve admitted local modes form one coherent assembly | Twelve local mode amplitudes in transported source frames | Exactly eleven independent equality conditions |
| Complete a globally coherent coefficient assignment | One specified nonzero coordinate and the promise x is in im N | Unique completion; other prescribed coordinates must agree with it |
| Find raw inputs producing a prescribed local record y | Full y | No solution unless Ly=y; otherwise y+ker L, a 24-dimensional affine family |
| Find raw inputs producing a prescribed terminal record y | Full y | No solution unless Ny=y; otherwise y+ker N, a 35-dimensional affine family |
| Recover an arbitrary input from selected coordinate addresses across stages | Same address set available at raw/local/aligned copies | Exact all-mask rank formula below; full recovery iff at least two coordinates per triangle are observed |
| Recover a locally admitted input from both original seed faces plus complete return | All six seed-face triangle records and Nx | Five independent hidden local-mode directions remain |
| Recover extra information by repeating the native return | Arbitrarily many repetitions of the same schedule | No new input information: the terminal map is idempotent |

These are mathematical tasks using the actual coefficients. An assumed coherent
input is not a procedure for forcing arbitrary inputs to remain recoverable.

## 1. The network separates three distinct questions

Define readout residuals, not new native primitive stages:

    q_local = (I-L)x,
    q_agreement = (L-N)x,
    q_collective = Nx.

Exact matrix multiplication verifies that I-L, L-N and N are mutually
orthogonal Hermitian projectors, sum to I, and have ranks 24, 11 and 1.
Consequently

    x = q_local + q_agreement + q_collective,
    ||x||^2 = ||q_local||^2 + ||q_agreement||^2 + ||q_collective||^2.

The 24-dimensional component violates local eigenline selection. The next
11-dimensional component satisfies every local selection but disagrees with
the collective mode. Only the last component survives the complete return.

This makes an actual diagnostic possible: a failed return can be localized to
local incompatibility, inter-triangle disagreement, or both. A terminal record
alone cannot recover those discarded components.

The decomposition follows from known projector identities. The new contribution
here is its task/readout classification and the source-checked decoding and
ambiguity certificates below, not a claim to discover these projector ranks.

## 2. Source-derived local coordinates and eleven compatibility conditions

Take a nonzero column of the actual N and normalize its first coordinate to
one, obtaining b. No separately supplied collective target is used. Split b
into its twelve three-coordinate blocks b_t. Every entry is nonzero; every
block has squared norm 15 in this normalization.

Let B place amplitude a_t on b_t in triangle t, and define

    (Cx)_t = b_t^dagger x_t / (b_t^dagger b_t).

The checker establishes

    CB=I12, BC=L,
    GB=BJ, NB=BJ, N=BJC,
    J=(1/12) 1 1^T.

Thus locally admitted inputs are precisely x=Ba. The native alignment stage
averages their **transported** amplitudes. It does not compare ambient spatial
vectors as if their frames were identical.

A global completion requires a_1=...=a_12. The eleven differences a_t-a_1 form
a full-rank test. A connected spanning tree of comparisons suffices; all 66
unordered pair comparisons are redundant for this exact equality task. These
are derived comparison readouts, not 66 newly admitted primitive transfers.

For an input promised to lie on the collective line, x=alpha b. Since every
b_j is nonzero, alpha=x_j/b_j is determined by any one coordinate. If multiple
coordinates are prescribed, consistency requires the same ratio at each one.
Without the collective-line promise this does not reconstruct arbitrary x.

## 3. A sharp observation/reconstruction theorem

An **address** is one (triangle,axis) pair read at its raw, local and aligned
stage copies. It is not one of the 1,836 transfers and not a derived physical
detector. Let S be the chosen address set and k_t the number of selected axes
in triangle t. Let n_0 count triangles with k_t=0. For the observation map

    O_S x = ((x_j)_(j in S), ((Lx)_j)_(j in S), ((Nx)_j)_(j in S)),

the exact complex rank is

    rank O_S = sum_t d(k_t) + indicator(0<n_0<12),
    d(0)=0, d(1)=2, d(2)=3, d(3)=3.

### Proof for every address subset

Within triangle t, the observed raw rows are coordinate rows. Every nonzero
observed L row is proportional to b_t^dagger. Because all three coordinates
of b_t are nonzero, their combined row space has dimension d(k_t). Distinct
triangles have disjoint support, so these dimensions add.

Every observed N row is proportional to b^dagger. If all triangles have at
least one selected address, that row is already in the local row spaces. If
some but not all triangles are unobserved, its nonzero restriction to an empty
triangle makes it one additional independent row. With no addresses there is
no observation. This proves the formula for all 2^36 address subsets, not by
extrapolating the sampled regressions.

Consequences:

- One address across the complete schedule has rank 3 and hides 33 complex
  input directions. Its dense connections do not make it an all-state probe.
- Full recovery is possible **iff every triangle has at least two chosen
  coordinates**. The minimum is therefore 24 addresses.
- A second proof of the lower bound uses ker L: it has dimension 24, and every
  downstream reading vanishes there. Fewer than 24 raw coordinate readings
  cannot distinguish that subspace.
- The threshold depends on this native coordinate/probe grammar. It is not a
  basis-independent minimum for all possible instruments.

### Explicit decoder, not just an observability rank

Choose two raw coordinates per triangle. Also read one local-stage output at
one of those addresses. If k is the missing coordinate and j is the chosen
local output, then

    x_k = [(Lx)_j - sum_(i!=k) L_ji x_i] / L_jk.

All denominators are nonzero in the actual source. The stored decoder uses
24 raw readings plus 12 local readings: 36 independent complex scalars. Its
matrix D satisfies DO=I36 exactly. All three choices of missing coordinate in
each triangle are checked independently, proving every one of the 3^12 such
layouts works. Deleting any address from the displayed minimal layout leaves
a nonzero explicitly stored invisible direction.

This is input reconstruction from retained intermediate data. It is not an
inverse of the terminal rank-one projector.

## 4. A problem the two original seed faces cannot resolve

The original faces ABC and ABD contain the six generated triangle labels

    AB, BC, CA, AD, DB, BA.

Read all their raw, local and aligned coordinates and, if desired, the entire
terminal record. For arbitrary raw inputs this observation has rank 19 and
hides 17 dimensions. On locally admitted x=Ba it has rank 7 and hides **five**
local-mode dimensions.

The reason is constructive: the six observed amplitudes are known; the global
return supplies only the sum of the remaining six. Their five independent
zero-sum differences remain invisible.

### Equal-norm counterexample

Set all twelve transported local amplitudes to one, except at the generated
triangles AC and BD, which lie outside the two seed faces:

| Input | a_AC | a_BD | All other amplitudes |
|---|---:|---:|---:|
| x | 2 | 0 | 1 |
| y | 0 | 2 | 1 |

Then x and y are different, both satisfy Lx=x and Ly=y, and

    Nx=Ny=b,
    O_seed x=O_seed y,
    ||x||^2=||y||^2=210.

They remain indistinguishable after every further native return. A common
normalization by sqrt(210) gives the same counterexample at unit norm. The
receipt stores every complex coordinate and a full basis for the five hidden
local-amplitude directions.

This does **not** say a known total norm can never certify coherence. In fact
||x||^2=||Nx||^2 would force x=Nx by orthogonal projection. Our pair has equal
norms to each other, not equality with its collective projection norm; both
have collective disagreement. Total norm can detect a disagreement budget
without locating how it is distributed.

## 5. A stage-type error that changes the answer

At a single coordinate address, the true schedule gives the three rows

    e_j^T, e_j^T L, e_j^T N.

Their rank is 3. Adding e_j^T G acting on raw input makes the rank 4 in the
source fixture. That extra information is real mathematically, but requires
an additional access/operation permission. We reject it as evidence about
the original schedule. The checker explicitly detects this tempting shortcut.

## Prior results used, not rebranded

- `research/nima/twelve-triangle-positive-geometry.md`: source construction,
  local/global phase distinction, native ranks and return.
- `research/nima/1836-constituent-gluing.md`: four face sectors of 135 internal
  arrows and six 216-arrow bridges; not independently normalized constituents.
- `research/nima/1836-pair-face-factorization.md`: each directed bridge has
  rank-three alignment plus rank-one feedback, and ordinary face-plane
  restriction loses a normal channel. This supplies the existing interface
  compression task; it is not freshly reverified by this checker.
- `research/strominger/arrow-anchored-local-collective-response.md`: a distinct
  declared field-response model. Its remote shielding result is not transferred
  to the native L/G/N schedule without an adapter.

## Prospective test and disposition

The input contract froze the task, rivals and hostiles before the first run.
SCC fingerprint: `40e67aae29c46c33723d1015ce293fbc2a5c4d802c3a3f9609785f1c57532eb2`.
The classification survived its frozen challenge. Eleven check groups pass:
source reconstruction, typed composition, diagnostic decomposition, local mode
transport, every local mask, 60 global masks, decoder identities and deletions,
seed-face ambiguity, preimage fibers, and corrupted-source controls.

An independent verifier does not import the producer. It realifies the exact
field to rational matrices using

    A + sqrt(-3) B  ->  [[A,-3B],[B,A]],

then checks all 60 global mask ranks, all 24 deletion witnesses, the decoder
on all 72 rational basis vectors, the source hashes and the equal-norm pair.
Both implementations pass. Shared sources and stores remain unchanged.

The general rank and decoder-layout conclusions follow from the proofs above
plus exact structural identities, not merely from the 60 examples. These are
exact finite-carrier linear-algebra theorems, not a new formal proof-assistant
closure or an experimentally realized tomography protocol.

## Reproduction and source-generated continuation

    python research/voevodsky/checkers/check_proton_native_task_catalogue.py
    python research/voevodsky/checkers/verify_proton_native_task_catalogue.py

Artifacts:

- `inputs/proton-native-task-catalogue-v1.json`: task and operation contract.
- `results/proton-native-task-catalogue-v1.json`: full exact certificate.
- `results/proton-native-task-catalogue-v1-independent-audit.json`: independent audit.
- `scc-models/proton-native-task-catalogue-v1.json`: bounded SCC registration.

The source-generated continuation now answers the next discrimination task:
`proton-seed-rotation-readout-repair-v1.md` constructs the word ABC, ABC, ADB,
whose coefficient action exchanges the observed and complementary face pairs.
Five additional independent readings then recover every locally admitted input.
This explicitly extends the probe grammar before the lossy return. Passive
relabelling and rotation of an already projected state still add no information.
