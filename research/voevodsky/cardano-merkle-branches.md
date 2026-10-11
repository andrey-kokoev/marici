# Branch-sensitive Cardano reassembly in an exact algebraic field

## Question

Can witness-preserving Merkle reassembly handle an irreducible cubic whose real roots require complex Cardano contributions, while distinguishing a valid change of presentation from a lost branch constraint?

The test is x cubed minus three x minus one equals zero. Its rational-root candidates plus or minus one fail, so the cubic is irreducible over the rationals. Its Cardano discriminant is minus three quarters. The active obligations are attachment transport and route/coherencer compatibility. No floating-point root approximation is used.

## Exact endpoints and compatibility

Work in the cyclotomic field Q[t]/(t^6-t^3+1), with t a primitive eighteenth root of unity. The checker verifies t has order 18. For k=0,1,2 define

\[
u_k=t^{1+6k},
\]

\[
v_k=t^{-1-6k},
\]

\[
s_k=(u_k^3-v_k^3)/2.
\]

Each ordered boundary carries the equations

\[
s_k^2=-3/4,
\]

\[
u_k^3=1/2+s_k,
\]

\[
v_k^3=1/2-s_k,
\]

\[
u_kv_k=1.
\]

The paired-root construction is explicit rather than a global branch-selection algorithm. Its assembled root is x_k=u_k+v_k. The standard cubic identity then gives x_k^3-3x_k-1=0.

## Reassembly into the real cubic field

Let h map to t+t inverse. The output admits the real representation Q[h]/(h^3-3h-1). All three roots become

\[
x_0=h,
\]

\[
x_1=2-h^2,
\]

\[
x_2=h^2-h-2.
\]

The checker verifies these are distinct, satisfy the cubic, agree with the paired complex branches, and are fixed by complex conjugation. In the six-coordinate cyclotomic basis, h maps to t+t squared minus t to the fifth power.

The three basis images of the real algebra have exact rank three. The embedding preserves the unit and all nine basis products; rational bilinearity then establishes multiplicative compatibility throughout the real algebra. The output thus moves from a six-dimensional rational field representation to its three-dimensional real subfield. This is not a claim that total artifact storage halves: the complex endpoint and branch witnesses remain retained.

## What hashes preserve

Each package contains its ordered endpoint boundary, root expression, and attached RootAndAssemblyWitness. Verification checks both the Cardano constraints and the equality of the output with the endpoint sum. The normalized expression uses an explicit typed embedding of the real normal form into the cyclotomic field. A branch-preserving equivalence certificate binds source and normalized package hashes and rechecks those equations.

Swapping u and v and negating s preserves the root but changes the ordered boundary and package hash. A boundary-preserving certificate correctly refuses to merge these presentations silently. A separate EndpointSwapEquivalence verifies the precise endpoint exchange and sign transport. Applying that exchange twice recovers the original boundary. Thus the two presentations are not declared inequivalent; their equivalence requires the explicit attachment transport.

There are three root values and six ordered branch presentations. Six normalization certificates and three endpoint-swap certificates are stored with 59 valid reachable objects.

## Falsifiers

Multiply v by t to the sixth power without changing u or s. This leaves v cubed unchanged, so both individual cube equations still hold. Nevertheless uv ceases to be one, and the assembled sum fails the cubic. A faithfully hashed but mathematically false branch is rejected.

Deleting the product constraint is rejected. Substituting a different valid cubic root under the original endpoint attachment is also rejected: being a root does not establish that it is the sum of those endpoints. The artifact is serialized and all retained normalization and swap certificates reverified from the serialized store.

## Disposition and reproduction

All 24 exact checks passed. This goes beyond CRT's finite residue table: it uses exact algebraic-number identities, an injective real-subfield realization, and nontrivial branch-dependent attachments. It demonstrates neither automatic discovery of the field model and normal forms nor globally minimal circuits, arbitrary radical-branch selection, or a geometric 2-Segal theorem.

Run `python research/voevodsky/checkers/check_cardano_merkle_branches.py` from the repository root. Only the Python standard library is required.

- Checker: `research/voevodsky/checkers/check_cardano_merkle_branches.py`.
- Receipt: `research/voevodsky/results/cardano_merkle_branches.json`.
- Content-addressed branch packages and certificates: `research/voevodsky/results/cardano_merkle_store.json`.
- Preceding fixed-domain experiment: `research/voevodsky/crt-merkle-reassembly.md`.
