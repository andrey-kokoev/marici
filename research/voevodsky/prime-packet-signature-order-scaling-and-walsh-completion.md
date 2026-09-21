# Prime packet pressure test: signature order, state cost, and Walsh completion

## Results

For full routes through a d-prime Boolean cube, retain endpoints and the ordered-edge signature through degree k. The source has d! route coefficients.

Exact integer ranks are:

| primes d | routes | degree ≤1 | degree ≤2 | degree ≤3 |
|---:|---:|---:|---:|---:|
| 4 | 24 | 18 | 24 | — |
| 5 | 120 | 50 | 120 | — |
| 6 | 720 | 130 | 630 | 720 |

The pressure test yields two general theorems:

1. Full-route reconstruction requires and is supplied by signature order floor(d/2), for d≥2.
2. For d=2m, the kernel at order m−1 consists exactly of the highest block-parity modes on the (2m)!/2^m ordered pair blocks. Consequently its dimension is (2m)!/2^m.

For six primes the ninety missing channels are ordinary Walsh characters on ninety disjoint three-bit cubes of internal pair orientations. We implement their streaming readout and construct a ninety-output completion with a proved conditioning bound.

## 1. Measurement contract

Vertices are subsets of {0,…,d−1}. An edge (S,j) adds j∉S. Each full path starts at the empty set and adds all d indices in some order. The numerical prime values do not affect this combinatorial test.

Let E(p)=(e₁,…,e_d) be the edge word of a full route. An edge carries both its source subset and its added index. For r≥1 define

\[
S_r(p)=\sum_{i_1<\cdots<i_r}e_{i_1}\otimes\cdots\otimes e_{i_r}.
\]

Every tensor coordinate is an ordered-edge occurrence indicator. Extend these observations linearly to complex route coefficients. The cumulative measurement A_k stacks S₁,…,S_k. At degree zero retain total coefficient mass; for k≥1 it is already recoverable by summing first-edge coordinates.

All rank statements refer to this edge-labelled signature, including its endpoint masks. A signature retaining only the added prime name is a different measurement.

The source counting metric makes route basis vectors orthonormal. Unless otherwise stated, each retained signature coordinate has unit output weight.

## 2. Exact rank computation

For each signature coordinate, the checker enumerates the full routes on which it is one. It constructs the integer Gram matrix

\[
G_k=A_k^T A_k
\]

by summing the rank-one incidence contributions. Since the entries are real and the counting metric is positive,

\[
\ker G_k=\ker A_k.
\]

FLINT integer-matrix rank therefore certifies the displayed ranks over Q, R, and C. Floating eigenvalues are computed separately and used only as finite spectral diagnostics.

The first-order formula is

\[
\operatorname{rank}A_1=d2^{d-1}-2^d+2.
\tag{1}
\]

Proof: an edge response has boundary λ(e_top−e_bottom). The corresponding space has dimension |E|−|V|+2. A positive average of all full paths lies in the relative interior of the nonnegative unit-flow polytope. Every nonnegative unit flow in an acyclic graph decomposes into full paths. Thus their affine span is the full unit-flow affine space, giving (1).

The degree-r raw coordinate counts in the tests are:

| d | degree 1 | degree 2 | degree 3 |
|---:|---:|---:|---:|
| 4 | 32 | 108 | — |
| 5 | 80 | 540 | — |
| 6 | 192 | 2430 | 7680 |

These are measurement counts; their independent ranks are the smaller numbers in the first table.

## 3. Minimum signature order for every packet size

### Upper bound

Set m=floor(d/2). Observe the edges at positions

\[
2,4,\ldots,2m.
\tag{2}
\]

Their labels identify the selected steps. The source masks identify the unique unobserved step between successive selected edges, as well as the first step. For odd d the terminal complement identifies the final unobserved step.

Therefore the tuple of selected edges determines the whole route. The corresponding d! degree-m signature coordinates form a permutation matrix on the route basis. Degree m reconstructs every coefficient.

### Lower bound

Consider the signed route combination

\[
h=\sum_{\sigma\in S_d}\operatorname{sgn}(\sigma)\,p_\sigma.
\]

Fix a degree-r coordinate. Its observed edges determine r selected steps and r+1 unobserved gaps. There are d−r unobserved steps. If r<m, then

\[
d-r>r+1.
\]

At least one gap has length at least two. Swapping two positions inside that gap preserves every selected edge label, including its source mask, and reverses the sign. This is a fixed-point-free pairing of the contributing routes. Hence the coordinate annihilates h.

The even and odd route sums are two positive mixtures of equal mass d!/2 with identical observations through every order r<m. Their degree-m observations differ.

Thus

\[
\boxed{k_{\min}(d)=\lfloor d/2\rfloor,\qquad d\ge2.}
\tag{3}
\]

This is a statement about arbitrary linear combinations of full routes. An individual route can be recovered from its edge set; mixture reconstruction is the stronger requirement driving (3).

## 4. The complete penultimate-order kernel for even packets

Let d=2m. Divide the positional slots into consecutive pairs

\[
(1,2),(3,4),\ldots,(2m-1,2m).
\]

An ordered tuple of unordered label pairs defines a block of 2^m routes: independently reverse the order inside each pair. There are

\[
N=\frac{(2m)!}{2^m}
\]

disjoint blocks. Inside block B let ε∈{0,1}^m record those reversals, and define

\[
h_B=\sum_{\epsilon\in\{0,1\}^m}
(-1)^{\epsilon_1+\cdots+\epsilon_m}p_{B,\epsilon}.
\tag{4}
\]

### Every h_B is invisible through degree m−1

A signature coordinate observing at most m−1 edges leaves at least one positional pair untouched. Reversing that pair preserves all observed edge labels: earlier edges precede both entries, and later source masks include both entries. The corresponding signs in (4) cancel. Thus A_(m−1)h_B=0.

The blocks are disjoint and

\[
\langle h_B,h_C\rangle=2^m\delta_{BC}.
\]

They give N independent kernel vectors.

### There are exactly N kernel dimensions

Fix a block and one of its pair reversals, at pair j. Choose observed positions

\[
2,4,\ldots,2j-2,\quad 2j+1,2j+3,\ldots,2m-1.
\tag{5}
\]

There are m−1 selected edges. The only unobserved gap of length two is the j-th pair; all other gaps contain at most one step. Therefore this coordinate is supported on exactly the two routes differing by that pair reversal.

As the block and j vary, these coordinates contain the unsigned edge-incidence rows of the m-dimensional hypercube on each block's 2^m route vertices. A connected bipartite graph's unsigned incidence matrix has a one-dimensional kernel, generated by its alternating sign vector: x_v+x_w=0 on each edge determines every x from one chosen vertex.

Hence each block contributes exactly one kernel dimension. Combining this lower-rank certificate with the already constructed h_B gives

\[
\boxed{\ker A_{m-1}=\bigoplus_B\mathbb C h_B,
\quad
\operatorname{rank}A_{m-1}=(2m)!\left(1-2^{-m}\right).}
\tag{6}
\]

At m=1 this statement uses the mass coordinate S₀. For the tested d=4 and d=6 it gives ranks 18 and 630 respectively.

This proves the six-prime rank result conceptually, independently of the matrix rank calculation.

## 5. A local eight-route collision

For six primes, take the block of label pairs ((0,1),(2,3),(4,5)). Its eight routes carry coefficients according to the parity of the three independent reversals:

\[
h_B=\sum_{\epsilon\in\{0,1\}^3}(-1)^{|\epsilon|}p_{B,\epsilon}.
\]

The positive and negative parts each contain four routes. All first- and second-order observations agree on these two mixtures. Third-order observation distinguishes them.

The checker constructs all ninety such vectors as columns of K and certifies

\[
K^T K=8I_{90},\qquad A_2K=0.
\tag{7}
\]

It also verifies the presence of every pair-swap-sum row used in the proof of (6). Thus the ninety-column basis exhausts the exact missing subspace.

## 6. Minimal completions

### Five primes

The edge observation has rank 50 on 120 routes. It needs at least seventy extra scalar linear measurements.

Choose fifty independent columns of the edge Gram matrix by exact row reduction. Retain route-indicator measurements for the seventy complementary columns. On the edge kernel, these seventy coordinates determine the whole vector: if they vanish, the remaining vector is supported on independent edge columns and must vanish as well.

Each indicator is a second-order probe using positions (2,4), by (2). Thus seventy second-order probes attain the lower bound. The checker selects them deterministically and verifies exact rank 120.

### Six primes, point-coordinate completion

The degree-two observation has rank 630. Select one canonical route from each of the ninety pair blocks. Its indicator is a third-order coordinate using positions (2,4,6). These ninety probes pair with the kernel columns K by the identity matrix, so they complete reconstruction and attain the lower bound.

### Six primes, Walsh completion

A more balanced completion measures

\[
b=\frac12K^T x.
\tag{8}
\]

Each output is a signed half-sum of the eight routes in one block. These are degree-three signature readouts, obtained by taking the corresponding signed combinations of route-indicator coordinates.

Since K^TK=8I, the kernel component is reconstructed directly:

\[
x_{ker}=\frac14K b.
\tag{9}
\]

The degree-two channel reconstructs the component perpendicular to the kernel. Let A=A₂ and G=A^TA. The joint Gram operator is

\[
G_{joint}=G+\frac14KK^T.
\tag{10}
\]

It is invertible, so an explicit joint reconstruction is

\[
x=G_{joint}^{-1}\left(A^Ty+\frac12K b\right).
\tag{11}
\]

The checker certifies exact rank 720 of 4G+KK^T and executes an exact rational solve from measured signature and parity outputs for a nontrivial 720-coefficient test packet. Equations (7)–(11) prove the reconstruction for arbitrary complex coefficients.

### Fourier interpretation

Within each eight-route block, the reversals form the group (Z/2)^3. The function

\[
\epsilon\longmapsto(-1)^{\epsilon_1+\epsilon_2+\epsilon_3}
\]

is its highest-order Walsh character. Degree-two measurements retain the other seven modes in each block. The ninety missing components are exactly ninety copies of this one character.

The Fourier viewpoint therefore supplies an explicit source-adapted basis for the lost information and a minimal additional measurement.

## 7. Conditioning: proved bound and numerical diagnostics

All statements here use the route-counting metric and the declared coordinate weights. They are separate from any independently weighted analytical source metric.

### Proved six-prime Walsh bound

The degree-two rows include the unsigned edge-incidence rows of a three-cube on each block. Their Gram is the signless cube Laplacian, with spectrum 0,2,4,6 and alternating kernel. Therefore

\[
G\ge2P_{ker^\perp}.
\]

From (7), KK^T/4=2P_ker. Consequently

\[
G_{joint}\ge2I.
\tag{12}
\]

Every row sum of G is 438. This follows directly by counting the number of routes sharing each selected edge tuple with a fixed route:

\[
\sum_{a=1}^6(a-1)!(6-a)!=312,
\]

\[
\sum_{1\le a<b\le6}(a-1)!(b-a-1)!(6-b)!=126.
\]

G has nonnegative entries, so its largest eigenvalue is its constant row sum, 438. The extra term acts as 2 on ker G and vanishes on its orthogonal complement. Hence

\[
\boxed{2I\le G_{joint}\le438I,
\qquad \kappa_2(O_{joint})\le\sqrt{219}\approx14.80.}
\tag{13}
\]

The inverse observation has norm at most 1/sqrt(2). This is an analytic finite-dimensional bound; the checker verifies its combinatorial premises exactly. Numerical eigenvalues agree with both endpoints.

### Numerical comparison

| packet and output choice | condition number |
|---|---:|
| five primes, all degree-one and degree-two rows | 9.75 |
| five primes, edge rows plus seventy selected indicators | 34.37 |
| six primes, all rows through degree three | 11.07 |
| six primes, rows through degree two plus ninety indicators | 66.92 |
| six primes, rows through degree two plus ninety half-parity outputs | ≤14.80, proved |

The completion counts refer to additional outputs beyond the stated base channels. The base itself retains redundant rows. Choosing a smaller base or changing weights changes these conditioning comparisons.

## 8. Observer state cost

State minimality is tested under a fixed contract: start at the empty vertex, follow valid cube paths, retain the current endpoint externally, and read the selected output vector at the terminal vertex. Existing edge/signature-channel storage is additional.

At each vertex v form the typed Hankel matrix with prefixes ending at v as columns and suffix/output pairs as rows. Its rank lower-bounds every linear state fiber at v.

### Selected route-indicator outputs

For distinct route-indicator outputs, two different active prefixes have disjoint nonempty suffix/output supports. Choosing one matching suffix and output per prefix gives an identity minor. A prefix-trie realization supplies the matching upper bound.

The exact results for the chosen minimal completions are:

| outputs | total fiber dimension | peak fiber dimension | total dimensions by layer |
|---|---:|---:|---|
| five-prime seventy indicators | 215 | 70 | 1,5,19,50,70,70 |
| six-prime ninety indicators | 336 | 90 | 1,5,15,45,90,90,90 |

These are minima for the selected output functions under this contract. Optimizing over all possible minimal probe selections is a separate problem.

### Signed Walsh outputs

For each route, group successive indices into pairs. The state records:

- the ordered list of completed unordered pairs;
- the pending first element of the next pair, when present;
- a signed amplitude.

Completing a pair multiplies the amplitude by +1 or −1 according to its internal order. Endpoint-typed transitions are signed maps between the basis states labelled by these descriptors. At termination the descriptor selects one of the ninety outputs, with coefficient sign/2.

Prefixes that differ only by completed internal pair reversals have proportional future-output columns, so their amplitude can be combined. The checker constructs each typed Hankel matrix exactly and verifies that its rank equals the number of compressed descriptors.

For six primes the minimal state bundle has:

\[
\text{total dimension }442,\qquad
\text{peak dimension }90,
\]

with layer totals

\[
1,6,15,60,90,180,90.
\]

This reveals a concrete design tradeoff: the balanced Walsh outputs improve conditioning while requiring more intermediate state than the selected point outputs. Both have the same minimal number of terminal output channels.

The reusable implementation `prime_packet_block_parity_observer.py` evaluates this signed sparse realization and its linear extension to mixtures. Its output is checked against K^T/2 on all 720 routes, and against the local eight-route collision.

## 9. Scaling consequences

The required signature order grows as floor(d/2). A fixed low order eventually loses route-mixture information. At each even packet size d=2m, the last missing layer has exactly (2m)!/2^m independent block-parity channels.

Low signature order and low storage cost are different constraints. Each observed edge already carries a subset mask, and complete route reconstruction has d! independent coefficients. A small number of factors in a tensor coordinate can still specify one of factorially many routes.

The pressure test now supports a concrete choice for six-prime work: retain the degree-two base, append the ninety Walsh outputs, and use the proved bounded inverse (11)–(13). The new outputs must be read from retained route data before the lower-order aggregation, exactly as in the four-prime observer.

## 10. Verification and provenance

Run:

```
uv run --with python-flint --with numpy python research/voevodsky/checkers/check_prime_packet_signature_scaling.py
```

Outputs:

- `research/voevodsky/results/prime-packet-signature-scaling.json`
- `research/voevodsky/prime_packet_block_parity_observer.py`

The result contains exact ranks, explicit minimal probe selections, all ninety kernel blocks through their construction and a recorded witness, typed Hankel certificates, streaming implementation tests, and separately labelled numerical conditioning data.

The minimum-order theorem, even-packet kernel theorem, reconstruction formulas, and six-prime conditioning bound are proved above. The finite calculations verify their four-, five-, and six-prime instances. These are source-path results; no new theta measurement or cutoff-uniform analytical estimate is asserted.
