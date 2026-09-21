# All-state Clark sewing is a balanced counit with derived seam data

## Result of the bounded test

There is a source-derived all-state composition interface, but it is **not** a natural transformation of the two original independent right-creation receivers.

It requires:

- a right-action input and an oppositely typed **prefix-action** input;
- one declared packet-wide memory capacity;
- the derived balanced tensor, including its degree-minus-one seam data.

The joining map is a counit from that derived tensor to the memory algebra. It agrees with the existing sewing on emitted records, has the prescribed split-and-copy Green mate, and is associative at the memory-algebra level. It is generally **not a derived equivalence**.

The smallest diamond already has a nonzero seam class made entirely from forgotten arrows. It remains after restricting to a common total-degree budget. Thus retaining only terminal memory would lose source data even after the action/variance issue has been repaired.

## 1. Source and memory are different algebras

Use the finite acyclic typed analytical path algebra A constructed in `three-prime-cut-duality-locates-the-ghosts-in-the-marginal-cofiber.md`:

`A=T_B(K)`, `B=direct_sum_x C e_x`,

`K_e=C Omega_e direct-sum W_e`.

Here W is the prescribed finite sheet-reduced J-invariant feature envelope. The marked source embeds by e^0 -> Omega_e and e^1 -> g_e. Omega_e is an event of retained degree zero, not a vertex identity. All parallel paths remain distinct.

Fix a packet-wide capacity N and put

`R=T_(<=N)(W)`.

This is the existing finite memory vector space, now equipped with its truncated chronological product: concatenate words, and set products of total degree greater than N to zero. It is a finite-dimensional associative algebra. Its Hilbert weights remain tau^(2r), and its signed operator remains direct_sum J^(tensor r). No new metric is selected.

For k=z Omega_e+w, set r_e(k)=z 1+w in R. The physical marked generators retain exactly their previous memory values 1 and g_e.

## 2. The compatible all-state actions

Let P be the row module with one copy of R at each vertex. It is a left R-module by multiplication on the left. Its right A-action sends

`p_x · k_(x->y) = (p_x r_e(k))_y`.

Let Q be the column module with one copy of R at each vertex. It is a right R-module by multiplication on the right. Its left A-action sends

`k_(x->y) · q_y = (r_e(k) q_y)_x`.

On the prepared source lines the accompanying transports are respectively T_e and T_e^(-1); after their given unitary trivializations these are the displayed formulas. The left action is an opposite-category action. It does not add inverse arithmetic arrows to the original source.

This defines an (R,A)-bimodule P and an (A,R)-bimodule Q. The free path algebra supplies their extension from generators. Associativity of R verifies the commuting outer actions.

There is a precise algebraic dual description:

`Q=Hom_R(P,R)`

for the finite free left R-module P. Evaluation is row times column. This is an **R-linear module dual**, not the scalar conjugate dual defined by the Green pairing.

The ordinary joining map on the vertex-balanced tensor is

`mu:P tensor_B Q -> R`,

`mu(p_x tensor q_x)=p_x q_x`, summed over vertices.

For an arrow x->y and arbitrary memories p in P_x and q in Q_y,

`mu((p k) tensor q)= (p r_e(k)) q
                  = p (r_e(k) q)
                  = mu(p tensor (k q))`.

Thus joining is balanced over A. This is the requested action/variance equation on all admitted memories.

## 3. What changed from the original pointed interface

On a vacuum, prefix creation by a segment path produces the same ordered word as forward right creation by that path: the operators act in the opposite compositional order on the left module. Consequently mu reproduces the previously proved record(p) record(q) identity, when N is at least the total source event count.

On an arbitrary memory, prefix and right creation are different. They cannot be identified by this vacuum agreement.

There is a second issue: capacities must be declared consistently. The original map

`F_a tensor F_b -> F_(a+b)`

is valid as a bounded linear concatenation map, but its individually truncated actions are not all-state module actions for that target. For example, with a=b=1,

`mu(c_L^1(a) a tensor vacuum)=0`,

whereas `c_L^2(a) mu(a tensor vacuum)=aa`.

Here both segment modules instead have the common capacity N, and the target multiplication also truncates at N. This preserves all vacuum-emitted records of an N-event packet. It does **not** preserve the arbitrary-state action at the boundary of each earlier, smaller capacity. That is an explicit interface change, not a hidden naturality assertion.

## 4. The finite derived composition complex

Because A is a free path algebra on a finite acyclic graph and B is semisimple, the standard length-one relative projective resolution computes the derived balanced tensor as

`C^(-1)=P tensor_B K tensor_B Q`,

`C^0=P tensor_B Q`,

`d(p tensor k tensor q)=p k tensor q - p tensor k q`.

One way to prove this is to resolve the left A-module Q by

`0 -> A tensor_B K tensor_B Q
   -> A tensor_B Q -> Q -> 0`.

The two left terms are projective, since finite B-modules are projective. Exactness follows by splitting a nonempty tensor word at its first letter, or by the usual tensor-algebra resolution. Tensoring with P gives the displayed complex. No flatness of P over A is assumed.

Balancing is precisely `mu d=0`, so mu is a chain map

`P tensor_A^L Q -> R[0]`.

Moreover, P is finite free over R. The adjunction between derived tensor with P and derived Hom_R(P,-) therefore has right adjoint Q tensor_R^L -. Its counit is this mu. On these finite perfect categories the adjunction restricts: the acyclic path algebra makes the finite left A-module Q perfect, while P is finite free over R.

This gives an actual composition correspondence with defined source actions. It does not make the counit invertible.

### Degree-zero output

For a connected source graph with at least one edge, H^0(C)=R in this analytical refinement. The Omega_e relations first identify the vertex copies of R tensor R. The W_e relations then impose `(p w) tensor q=p tensor (w q)` for every w in W. Since W generates R, the quotient is R tensor_R R, hence R.

This argument uses the full K_e= C Omega_e + W_e refinement. For the original two-mark space, only the particular g_e directions are supplied; the same conclusion must not be assumed unless those directions generate the required memory algebra.

## 5. The counit is not a derived equivalence

The two-term complex has

`H^(-1)(C)=ker d`.

Its nonzero elements are real derived seam data, not removable by an assertion about H^0.

### Overflow classes

For one edge, two memory letters, and N=2, the exact complex has dimensions

`147 -> 98`, with `rank d=91`.

Therefore H^0 has dimension 7, equal to R, while H^(-1) has dimension 56. An explicit cycle is a full degree-two memory on both sides of a retained degree-one seam letter: both actions overflow and vanish. There is no degree-minus-two term in this projective model, so this basis cycle represents a nonzero class.

Restricting to total retained degree at most N defines a subcomplex. In this one-edge fixture its dimensions are 27 -> 34, and its H^(-1) is zero. This restriction removes the overflow classes, but is a declared smaller complex, not the entire derived tensor of the original independent modules.

### A forgotten diamond cycle survives the total-budget restriction

In the diamond 2->4->12 and 2->6->12, let t_e be the seam generator with both memories vacuum and the edge coordinate Omega_e. Then

`d t_(x->y)=vacuum_y tensor vacuum_y - vacuum_x tensor vacuum_x`.

Consequently

`t_(2->4)+t_(4->12)-t_(2->6)-t_(6->12)`

is a nonzero cycle of retained degree zero. It survives every nonnegative total-degree budget. Its nonzero status uses the admitted free source: the four edge summands are distinct, and this projective resolution has no preceding boundary group.

For the two-letter N=1 fixture, the whole complex has dimensions 108 -> 36 and cohomology dimensions 75 and 3 in degrees -1 and 0. Its total-budget subcomplex still has H^(-1) dimension 11. The displayed forgotten cycle is one explicit class there.

This is a seam-complex class, not an asserted identification with the earlier 48-path marginal ghosts. It shows independently that the derived composition cannot simply be replaced by terminal memory. Declaring the two source routes equal would change the source algebra and its resolution; it is not an allowed repair.

### Its image in an explicit source boundary closure

The degree-zero seam complex has a direct source interpretation. Restrict to the forgotten-arrow subgraph and its prepared vacuum lines. Every transport is the identity after the prescribed unitary trivialization. Its graph-shaped stable colimit is the cofiber of the edge-incidence map

`C^(edges) -> C^(vertices)`.

For the free diamond, decompose the graph into its two directed path pieces. Each piece has colimit C. Their intersection is the **two discrete endpoint objects**, not a single terminal object: the two composite arrows 2->12 are distinct in the admitted free source. The common boundary is therefore C direct-sum C, and both attaching maps are (id,id).

The resulting stable pushout is represented by

`C^2 --[[1,1],[-1,-1]]--> C^2`

in degrees -1 and 0. It has one-dimensional cohomology in each degree, so is equivalent to C direct-sum C[1]. The checker constructs an explicit chain deformation retract from the four-edge incidence complex to this boundary-pushout complex. The forgotten diamond cycle maps to the difference of the two endpoint basis vectors in its degree-minus-one kernel.

Thus this particular source closure **retains**, rather than kills, the seam class. Replacing its two-component boundary by one line removes that class. No metric fitting or new route relation is involved. This is a concrete binary stable boundary realization; it is not yet an Agda instantiation of the native closure library or an identification with an additional physical spatial interface.

## 6. Green mates on the composition complex

Give P and Q their existing orthogonal vertex sums of the signed memory form. Give K_e the prescribed form on C Omega_e direct-sum W_e, including the degree-one weight. Tensor over the matching vertex blocks to obtain nondegenerate forms on C^(-1) and C^0.

These produce unique scalar Green mates d^sharp and mu^sharp. For mu, the formula is exactly the finite split-and-copy rule: split a word at every position and copy it to each allowed cut vertex. Products exceeding N have no corresponding output word and contribute nothing to the mate.

The balancing equation dualizes to

`d^sharp mu^sharp=0`.

The cochain conjugate dual has differential -d^sharp from degree zero to one. Thus mu^sharp is the dual chain map, with the required sign convention. The checker verifies all these matrix identities and rejects the claim that the mate is an inverse.

Do not identify Q=Hom_R(P,R) with the scalar Green-dual representation of P. Q uses **prefix creation**; the scalar mate of right creation uses **contraction**. On the vacuum the former is nonzero for a nonzero feature, while the latter is zero. The distinction remains exact even though both constructions are called duality.

Hence the all-state balanced interface and the Green comparison coexist through the dual seam complex; they are not obtained by equating their second-input representations.

## 7. The original hostile remains visible

At one memory seam,

`delta=vacuum tensor b - b tensor vacuum`

lies in the kernel of ordinary concatenation. Right insertion of a on the first factor gives

`mu((c_R(a) tensor I) delta)=ab-ba`,

which is nonzero for independent letters and sufficient capacity. Thus the original first-factor right action does not descend to joined memory. The new construction does not erase this test: it replaces the incompatible independent action by the typed right/left balancing relation, with the seam differential recording that relation.

Associativity of truncated multiplication is checked on every basis triple in the finite memory fixture. Derived associativity is the ordinary associativity of bimodule tensor product; it is not an assertion that a counit with nonzero H^(-1) becomes an equivalence after repeated joining.

## 8. Verification

`uv run --with sympy python research/nima/checkers/check_typed_seam_composition.py`

Certificate: `results/typed-seam-composition.json`.

Passed exact checks:

- all-state balancing as mu d=0;
- ranks and cohomology dimensions in the one-edge and diamond fixtures;
- explicit overflow and forgotten-diamond classes;
- a chain deformation retract identifying the forgotten cycle with the two-endpoint stable boundary pushout, plus the one-endpoint compression hostile;
- total-degree subcomplexes and their residual cohomology;
- signed Green mates and the dual-complex sign;
- common-capacity associativity on all basis triples;
- the non-descending internal-action commutator;
- the independent-capacity hostile;
- the prefix-versus-contraction distinction.

The derived-resolution identification and adjunction are mathematical arguments above, not consequences of numerical ranks. The two-letter matrices are signed-coordinate fixtures, not a sampled model of all analytical shell features. The forgotten cycle uses only prescribed vacuum transports and is independent of the feature dimension.

## Disposition

The all-state question is now localized:

- with unchanged independent right actions and separate capacities, the proposed promotion fails;
- with the explicit opposite prefix input and common capacity, it is a valid finite balanced counit;
- the full derived seam complex must remain unless a further admissible comparison is supplied;
- scalar Green duality is carried by the dual complex, not by identifying prefix creation with contraction.

For the free forgotten diamond, the source boundary comparison is now explicit: its two endpoint attachments retain the cycle as C[1]. The next formal target is this exact incidence-to-boundary deformation retract and its dual, before generalizing to more seam stages. Any further claim that a physical or higher source attachment kills the class must supply that attachment; equality of terminal transports is not enough.

No physical inverse event, monoidal shortcut, positive full-history functional, infinite topological completion, or terminal invariant metric is asserted.
