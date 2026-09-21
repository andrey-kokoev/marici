# The bounded filtered limit recovers the source and its faithful Fox jets

## Result

The completed filtered source is exactly the uniformly seminorm-bounded part of its filtration inverse limit, when that part is given the corresponding supremum seminorms. It has a continuous faithful multiplicative realization by its full ordered Fox-jet family. The jet action retains the extension data that an associated graded direct sum would lose.

An unrestricted compatible family need not be summable. The proof identifies the precise boundedness condition instead of asserting automatic inverse-limit noncollapse.

## 1. Source and quotient seminorms

Use the common-path Frechet ideal X=J_1 with seminorms

    p_b(x)=sum_c (1+n(c))^p (b a)^(n(c)) ||x_c||_path,

for integer b>=1, fixed p>=0, and the admitted a>=1. Its closed subideals J_(m+1) give E_m=X/J_(m+1). Write p_(b,m) for the actual common-path quotient seminorms. The earlier simultaneous finite-corner lifts identify these quotient spaces and prove strict exactness.

The Fox factorization theorem transfers each fixed finite quotient to its presentation-scale version. Uniformity in m below is stated in these COMMON path seminorms, not in independently rescaled seminorms chosen separately at every depth.

## 2. Characterize realizable compatible families

For x in X, the family x_m=x mod J_(m+1) is compatible. Conversely, let (x_m) be a compatible family with x_m in E_m. Fix an endpoint c of event length n. Since a relation consumes at least two events, the ideal power I^(m+1) vanishes in that corner for 2(m+1)>n. The corner of x_m therefore stabilizes to an actual vector x_c in I_c.

For a fixed b, the corner quotient norms increase monotonically to the path norm of x_c. Monotone convergence for the countable sum over endpoint corners gives the exact equality, allowing infinity,

    sup_m p_(b,m)(x_m)
      = sum_c (1+n(c))^p (b a)^(n(c)) ||x_c||_path.

Thus (x_m) comes from a UNIQUE x in X exactly when the left side is finite for every b. Give this bounded part of the inverse limit seminorms

    P_b((x_m))=sup_m p_(b,m)(x_m).

Reconstruction is then an isometry for every seminorm. This proves completeness and noncollapse of the bounded realization. It does not use a bounded inverse to the Clark map.

The ordinary product topology on the whole inverse limit is weaker. The statement is NOT a topological identification with the subspace topology inherited from that product.

## 3. A compatible family excluded by the criterion

For each r choose the forgotten product of r consecutive diamond relations in its minimal 2r-event root corner. It has 2^r nonzero path coefficients, belongs to I^r, and survives because I^(r+1)=0 there. Rescale it to have p_1 norm one and call it z_r. Use distinct terminal endpoints for different r.

Define x_m=sum_(r<=m) z_r mod J_(m+1). Every x_m has finite endpoint support, hence belongs to every radius scale. The family is compatible: terms with r>m vanish in E_m. But

    p_(1,m)(x_m)=m.

It has no summable source preimage. This is a genuine inverse-limit family, not a nonzero element in the kernel of the faithful completed receiver.

Similarly a single unit vector z_r at increasing r converges to zero in every fixed filtration quotient but not in p_1. This explains why the supremum topology cannot be replaced by the inverse-limit product topology.

## 4. Ordered Fox jets of the recovered source

Let D_0=rho. For k>=1 let D_k mark k ordered distinct event positions and retain the actual marked seam edges with the k+1 intervening coefficient buffers. Its target here is the normal-form record space in bottom seam degree, not an assertion that its value on every source path is a cycle.

On paths the exact convolution law is

    D_k(uv)=sum_(i+j=k) D_i(u) tensor_balanced D_j(v).

It is the partition of selected event positions into those lying in u and v. No factor permutation occurs. Regarding k as jet order gives an ordinary convolution product of these record families. Comparison to shifted cochain presentations uses the existing suspension normalization, rather than inserting new signs into this path identity.

For each fixed k, the number of terms is binomial(n,k). Any required polynomial n^k and fixed feature-radius factor are absorbed by a larger path radius in X. Thus D_k extends continuously to X in the forcing-resolved and normalized analytical record spaces. For fixed k, the convolution sum is finite; continuity and density extend its identity to completed sources.

The family D=(D_0,D_1,...) is therefore a continuous algebra map to the product-topology jet algebra. On X=J_1, D_0=0, but the higher convolution terms retain nontrivial multiplication.

## 5. Faithful finite jets and extension-sensitive action

D_k kills J_(k+1). On I^k its induced map on I^k/I^(k+1) is the finite faithful balanced layer map. Induction therefore gives, for a finite source corner,

    ker(D_1,...,D_m) on I = I^(m+1).

The same statement holds on the completed source by continuous endpoint projections. Thus the first m jets faithfully detect E_m, and the full family separates the reconstructed X. Equivalently, on a fixed finite corner the top path-order jet records the entire marked path with empty intervening buffers.

For two relations a,c,

    D_0(a)=D_0(c)=0,
    D_1(ac)=0,
    D_2(ac)=D_1(a) tensor_balanced D_1(c),

which is nonzero for the diamond witness. The source action is therefore triangular in jet order: it is NOT an action factoring through B on every coordinate independently. This retains the nonsplit filtered extension, rather than merely listing its associated layers.

D_k on the whole ideal is not claimed to be source-equivariant as an isolated map into an I-annihilated target. Source equivariance of the full family is expressed by the convolution law. Only its restriction to the kth associated layer has the earlier isolated equivariance and cycle property.

## 6. What the result does not assert

The product-topology jet realization is faithful but no continuous inverse from its image is claimed. The earlier inverse-instability witnesses remain valid. The bounded inverse-limit realization uses source quotient seminorms, not a metric inferred from the output jets.

Current identities and separate-channel convergence apply to every fixed finite jet packet on its forcing-resolved domain. An additional sum over ALL jet orders requires the previously declared depth/feature summability scales; it is not supplied merely by a product-topology family.

No completed projectivity, completed tensor-Hom duality, or equality with an independently specified arithmetic Green operator has been inferred.

## Verification

- `uv run python research/voevodsky/checkers/check_bounded_filtered_inverse_limit.py`: actual forgotten ideal products through depth eight, the compatible non-summable family, and a summable positive control.
- `uv run python research/voevodsky/checkers/check_filtered_fox_jet_product.py`: 80 ordered derivative convolution identities, the nontrivial second-jet relation action, and highest-jet marked-path retention.

The full inverse-limit criterion and continuity arguments are the proofs above, not conclusions from finite rank tests.
