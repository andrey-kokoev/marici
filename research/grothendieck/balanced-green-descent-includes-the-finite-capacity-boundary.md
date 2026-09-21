# Balanced Green descent includes the finite-capacity boundary

## Status

**Finite all-state relative comparison theorem**, for the fixed prescribed carrier and capacity. The source-generated correction already descends through Nima's seven-event balancing presentation. Extending it to arbitrary finite input memories requires one additional, forced channel: the negative pairing of record sectors killed by the capacity cutoff.

With that channel included, the corrected form on the full unbalanced seam complex has radical exactly the kernel of balanced normalization. Its quotient is the prescribed balanced normal-form complex with its existing form. The comparison uses the Green mate, which composes contravariantly and is generally not an inverse.

This does not assert that the original uncorrected tensor form descends, that relation self-pairings are nondegenerate, or that varying the capacity gives a compatible completed receiver.

## 1. What is already closed

Nima's updated factorization-descent note proves

G^r=(I/I^2) tensor_B ... tensor_B (I/I^2)

and its faithful cycle inclusion into the balanced analytical seam complex. At seven events the root-to-terminal presentation has dimensions 55440 -> 35280, with balancing kernel dimension 20160.

The note also applies the collision/tail-flux theorem on admitted source templates, where capacity at least seven prevents overflow. It verifies the all-forgotten balancing relation explicitly: the uncorrected kernel self-pairing is 128 and the collision correction is -128.

The present addition concerns the full finite memory carriers, rather than repeating that source-image calculation.

## 2. The actual normal-form map

Let D be the vertex-idempotent algebra, R the prescribed typed truncated memory algebra, and T_R its two-term analytical seam complex. Put

U_r=T_R tensor_D ... tensor_D T_R,

Y_r=T_R tensor_R ... tensor_R T_R.

The canonical chain map M:U_r->Y_r multiplies adjacent coefficient buffers at each interface. It retains the typed seam edges or cut vertices, their letters, all outer endpoints, and the surviving ordered words. At three seams the bottom normal form has three seam letters and four coefficient buffers.

M is surjective in each cochain degree. In the normal form, insert the appropriate typed units to separate adjacent factors again; this proves surjectivity without selecting a preferred factorization of a source relation.

Both U_r and Y_r have the existing degreewise nondegenerate ambient forms, q_U and q_Y, from the finite signature-closed feature envelope and tensor/vertex assembly. The signature is on the normalized two-sheet carrier; the raw four-port coefficient is not used as an invertible signature.

## 3. Why the no-overflow constructor is not enough for all states

Two input coefficient words can each have length at most N while their concatenation has length greater than N. Their product in R is zero. Such states are legitimate vectors of U_r even though they do not occur in the bounded source templates under discussion.

For example, at capacity two, a two-letter word followed by a one-letter word is killed by multiplication. Its uncorrected diagonal pairing can be nonzero. A constructor that only counts newly matching shapes has no diagonal correction there and therefore cannot satisfy the desired comparison identity.

The cutoff loss is part of the declared source operation. It must be retained as a separate capacity-boundary channel, not mistaken for a null direction of the original form.

## 4. Independent constructor: new matches and killed sectors

Use the same typed record-shape description as in the collision-current theorem. Apply the actual truncated normal-form word map.

Define T_M by two operations:

1. For surviving input shapes, enumerate pairs of distinct fine shapes that become the same normal-form shape. Assign their ordered slot Green kernels, existing weights, and root/source-state factors. These are the previous collision currents.
2. For input shapes killed by overflow, include the negative of their prescribed fine pairing. Its slot kernels are again supplied by the existing tail Green identity. Mark it as a capacity-loss contribution, not a new collision or a new forcing source.

The killed sectors are unions of memory-degree and endpoint blocks. They are orthogonal to the surviving fine sectors under the prescribed graded form. This makes the loss operation well-defined without choosing a basis in the analytical feature space.

Vacuum incidence terms remain separate from non-vacuum tail-current terms. Every retained spectral pair keeps its own denominator. Signature-transformed observers use the already specified sewn positive or signed coefficient, as in the preceding current theorem.

No matrix is fitted and no inverse relation Gram matrix is used.

## 5. Comparison and exact ambient radical

The constructor gives the identity

q_U + T_M = M^* q_Y.

For surviving fine shapes this is the earlier collision proof: concatenation preserves ordered feature pairings and multiplies the memory weights correctly. For killed sectors the right side is zero and the loss channel cancels the original pairing. Mixed surviving/killed fine sectors have zero original pairing by the degree-shape decomposition.

Let q_tilde=q_U+T_M. Then

radical(q_tilde)=kernel(M)

in every cochain degree. One inclusion follows from the displayed identity. Conversely, if u pairs to zero with every v under q_tilde, then M u pairs to zero with all of Y_r, because M is surjective. Nondegeneracy of q_Y gives M u=0.

Since M is a chain map, this radical is a subcomplex. Consequently

(U_r / radical(q_tilde), induced corrected form)

identifies with the actual normal-form complex (Y_r,q_Y), degree by degree and compatibly with the differential.

This is descent of the CORRECTED relative form. It is not descent of the uncorrected q_U. The correction itself can still require the original factorization labels and need not descend separately.

## 6. Nested normalization with losses

For two composable permitted normalizations M_1,M_2, associative truncated multiplication gives M_21=M_2 M_1. The constructor satisfies

T_(M_21)=T_(M_1)+M_1^* T_(M_2).

There are now three cases. A record pair may acquire its common shape at the first merge, at the second merge, or be killed at either stage. If a pairing created at the first merge is killed at the second, the second-stage loss cancels that intermediate contribution. Thus a pair must not be permanently counted as a surviving collision merely because it matched at an earlier cut.

This law is determined by the same typed partial word map, including its zero outputs. No extra triangle parameter is introduced. It specializes to the no-overflow collision law on all admitted seven-event source templates.

The proof concerns compatible finite concatenations at ONE capacity. It does not turn inclusion from cap N into cap N+1 into an algebra or module map.

## 7. Green mate, not inverse

Use the original nondegenerate ambient beta maps. Define

M^sharp=beta_U^(-1) M^vee beta_Y.

Then beta_U M^sharp=M^vee beta_Y. This is the paired observation square. The degenerate corrected form does not supply an inverse beta map and is not used to define this mate.

For composable maps,

(M_2 M_1)^sharp=M_1^sharp M_2^sharp.

With the standard cochain dual signs these are the corresponding maps of Green-dual complexes. Surjectivity of M implies injectivity of the dual observation map and of M^sharp, but generally M M^sharp is not identity.

The checker exhibits the distinction explicitly: several raw decompositions contribute to one normal-form word, and M M^sharp counts those contributions rather than producing an inverse normalization.

## 8. Consequence for the seven-event relation presentation

Let F_r be the unbalanced source factorization presentation, m:F_r->G^r its multiplication/associated-layer map, and j_raw,j_bal the derivative maps. The established equality is

M j_raw=j_bal m.

It follows that

j_raw^*(q_U+T_M)=m^*(j_bal^* q_Y).

Every balancing generator is annihilated in either argument by the corrected source form. This includes the complete 20160-dimensional seven-event presentation kernel, not just the all-forgotten example. No source-generated overflow term is needed at capacity at least seven; the new loss channel controls the larger ambient all-state domain.

Do not infer that this is the entire radical after restricting to the source presentation. The balanced relation image can have additional self-pairing degeneracy. The exact ambient radical statement in section 5 and a restricted relation Gram statement are different claims.

The paired observation j_bal^vee beta_Y is nevertheless surjective onto the conjugate dual of the coefficient layer, by injectivity of j_bal and ambient nondegeneracy. This retains all 35280 root-to-terminal coefficient directions. The full seven-event derived receiver has other endpoint supports; its dimension is not obtained by multiplying 35280 by a root-carrier dimension without the separate module calculation.

Passing from external to balanced carriers may change the restricted product Gram matrix. The old external tensor Gram formula is not silently transferred as an isometry. What remains compatible is the source attachment map and the specified relative paired comparison.

## Verification

`uv run --with sympy python research/grothendieck/checkers/check_balanced_green_capacity_descent.py`

Exact tests:

- 2916 formal spectral-pair checks of nested correction with overflow;
- the complete cap-two signed two-letter word fixture;
- independently constructed collision and capacity-loss matrices;
- equality with the normal-form pullback;
- corrected radical dimension and raw-descent failure;
- the Green-mate square, reversed composition, and failure of the inverse claim.

The fixture has raw dimension 343, balanced dimension 7, and 312 killed basis states. Its corrected form has rank 7 and radical dimension 336. These are finite word-fixture dimensions, NOT seven-event relation dimensions or spectral-rank observations.

The general quotient-complex theorem is proved above using the source normal form, graded cutoff operation, and existing nondegenerate ambient pairings. No completed analytical limit, positivity theorem, or new formal proof-assistant verification is claimed.

References:

- `research/nima/nonminimal-relation-factorizations-descend-through-balanced-seam-complexes.md`;
- `relative-green-sewing-is-generated-by-slot-collisions-and-tail-flux.md`;
- `research/nima/the-attachment-opposite-comparison-needs-a-koszul-correction-and-a-distinct-green-dual.md`.
