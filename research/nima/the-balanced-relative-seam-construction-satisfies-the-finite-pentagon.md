# The balanced relative seam construction satisfies the finite pentagon

## Result

At a fixed finite source and common capacity, the four-factor balanced seam comparison satisfies the associativity pentagon as a diagram of chain maps. The source-constructed relative Green currents have the same total along all five binary normalization schedules. Factorization descent commutes with this comparison on the associated layer.

There is no new pentagon correction parameter. The associator preserves the ordered factors and is signless; tensor-of-shifts maps retain their prescribed Koszul signs. Corrected opposite reversal remains a different operation.

The exact regression includes nine events—four diamond relations plus one extra marked event—so it tests nonminimal balancing rather than only the critical eight-event product basis.

## 1. Inputs

Use:

- `nonminimal-relation-factorizations-descend-through-balanced-seam-complexes.md`;
- `the-attachment-opposite-comparison-needs-a-koszul-correction-and-a-distinct-green-dual.md`;
- `../grothendieck/relative-green-sewing-is-generated-by-slot-collisions-and-tail-flux.md`;
- `../voevodsky/relative-green-currents-descend-through-balanced-factorizations.md`.

The last note supplies relative paired descent, including its non-diagonal feature tests. This note addresses the four-factor coherence of those maps and currents, rather than repeating the ordinary-sector paired comparison.

Let S be the finite free marked source, I its terminal-record ideal, B=S/I, C=I/I^2, and G^r=I^r/I^(r+1). Let T_B be the source two-term seam complex and T_R its function-valued analytical refinement over the fixed typed memory algebra R.

Both complexes are termwise projective on their respective left and right coefficient sides. Their ordinary iterated balanced tensors therefore compute the indicated derived tensors. The source result identifies C^(tensor_B r) with G^r and embeds its shift into the bottom cycles of the balanced seam target.

## 2. The five objects and their canonical normal form

For four factors, label the bracketings

```
A = (((12)3)4)
B = ((1(23))4)
C = (1((23)4))
D = (1(2(34)))
E = ((12)(34)).
```

All products here are balanced over the same coefficient algebra. The two pentagon routes are A->B->C->D and A->E->D.

Each term of each parenthesized complex has a canonical normal form: multiply only the adjacent outer coefficient buffers at the tensor interfaces. In bottom degree it is

`R tensor_D K_A tensor_D R tensor_D K_A tensor_D R
   tensor_D K_A tensor_D R tensor_D K_A tensor_D R`.

It retains four actual seam edges, five coefficient buffers, and their endpoint types. Higher-degree terms replace the appropriate seam-letter factors by their cut-vertex terms, without permuting the surviving slots.

For a balanced tensor, these are canonical isomorphisms: the local identification R tensor_R R -> R is multiplication with its unit inverse. They are not inverse maps for unbalanced external compression.

Define each associator by these canonical balanced identifications. Both pentagon composites are the same flattening/rebracketing map, hence agree strictly on this model. This is also the standard tensor associator; no source-dependent identification is fitted afterward.

## 3. The differential and suspension checks

For homogeneous factors of degrees d1,...,d4, the differential acting in factor i has sign

`(-1)^(sum_(j<i) d_j)`.

Recursive evaluation in any of the five trees gives this same sign. The checker verifies all degree patterns in {-1,0}^4. An associator does not exchange factors and contributes no additional Koszul sign.

For shifts p1,...,p4, use the established comparison

`sigma_(p,q)(u tensor v)=(-1)^(q deg(u)) u tensor v`.

Normalizing all individual shifts to the total shift has sign

`(-1)^(sum_(i<j) p_j d_i)`.

Every ordered pair of leaves occurs at exactly one split in a binary tree, proving tree independence. This also proves compatibility with the shifted differential. The checker tests 10000 degree/shift configurations, including an explicit failure when a required suspension sign is omitted.

Four bottom seam cycles alone would be an inadequate sign test: the relevant sum of six odd-pair contributions is even. Mixed degrees and shifts are therefore included.

Opposite reversal still reverses factor order and uses the separately established normalization c_r=(-1)^(r(r-1)/2). Nothing in the signless associativity pentagon identifies that reversal with Green contragredience.

## 4. Normalization from rich external records

A bottom external record has four seam factors

`(u0 | edge1 | v0), ..., (u3 | edge4 | v3)`.

Normalization retains every seam letter and replaces the eight memory buffers by

`u0, v0 u1, v1 u2, v2 u3, v3`.

Only the three artificial factorization cuts inside those joined buffers are removed. No feature crosses a seam letter.

A binary tree specifies one order for performing these three mergers. In the checker the five schedules are

`123, 213, 231, 321, 132`.

They yield the same forward map N by associative coefficient multiplication. Work at one common capacity, on admitted templates for which no merger overflows. This is not an assertion that multiplication preserves an arbitrary top-degree external state.

## 5. The current follows the first new match

For each elementary merger use the supplied collision-current constructor: enumerate distinct fine shapes whose images first match, then assign their vacuum incidence or labelled feature-current packet. Each feature pair keeps its own spectral arguments, denominator, signature channel, and spatial current variable. The root-state pairing remains one external factor.

For a normalization schedule with successive partial maps N_i, the transported total is

`T_total = T_1 + N_1^* T_2 + (N_2 N_1)^* T_3`.

If a pair of fine shapes already matches, no correction is created. If its final shapes do not match, none is created. Otherwise it first matches at exactly one stage in every schedule. Its ordered feature pairing, fixed weights, and root packet are identical regardless of which stage that is.

Thus all five schedules give the same current, selected directly by the final normalization N. This is a constructor-level proof, not a definition of the current as a Gram difference.

It follows that both pentagon routes have the same relative packet

`(N^* q_normal, T_N)`

and the same identity

`q_external + T_N = N^* q_normal`.

Associators between already balanced normal forms only reassociate their fixed tensor factors; they create no further collisions. The nontrivial current belongs to normalization from the rich external records, not to an invented phase or anomaly on the associator itself.

## 6. Finite current regression

The checker uses six internal memory slots in the three adjacent suffix/prefix pairs. Each slot has retained degree zero or one, and each interface retains two possible intermediate-vertex labels. This gives 512 fine shapes and 262144 ordered pairs.

It checks all five normalization schedules on every pair. Exactly 13312 pairs create new matches. For each, the retained formal packet includes the original spectral labels, signature parities, root factor, and memory-weight exponent. All five transported totals agree entrywise.

These are bounded rich-record fixtures, not a claim that every such shape is a distinct arithmetic source path. They involve no overflow at the chosen common capacity. The packets are formal products of the existing slot kernels, not sampled Clark values or newly evaluated tail integrals.

The source tail-current identities and function-valued transfer are supplied by the two relative-sewing input theorems. Neither seam-letter weights nor memory weights are changed in the present comparison.

## 7. Descent and the nine-event hostile

Let F_4=I tensor_D I tensor_D I tensor_D I and let m:F_4->G^4 be multiplication followed by the layer quotient. The preceding descent theorem gives

`N j_external = j_balanced m`.

Since every tree computes the same N, changing the factorization and changing parentheses commute after normalization. The corrected pulled-back form factors as

`j_external^*(q_external+T_N)
 = m^*(j_balanced^* q_normal)`.

This is descent of the corrected sum. Its two summands need not descend separately, and no radical of the restricted source self-pairing is quotiented.

For an explicit nonminimal test take four diamond relations a,b,c,d and an extra event e. Slide e across each of the three relation-factor interfaces, for example

`(a e) b c d = a (e b) c d`.

The raw external seam records have different cut labels. The checker verifies that both sides have the same nonzero balanced normal form for all five trees, and that this normal form is closed. Twelve fixtures cover all three interfaces, forgotten and retained e, and both all-forgotten and mixed relation types. Independent vertex-potential coordinates retain the actual typed source actions; they are not spectral sample values.

The general statement is not limited to these twelve examples: the hereditary-flatness theorem identifies the entire factorization kernel with balancing, and the normal-form maps implement that balancing. No full nine-event rank or new dimension formula is inferred from the fixtures.

## 8. Shifted attachments and observations

For the four-factor layer the source quotient model is

`B tensor_S^L G^3 = G^3 direct-sum G^4[1]`.

The bottom cycle inclusion is G^4[4]->J_(R,4). Its attachment realization therefore uses J_(R,4)[-3], placing the product observation in degree -1. Every parenthesization gives the same map following the connecting projection.

Contragredient duality reverses both pentagon routes and takes that projection to the corresponding inclusion in degree +1. The existing beta comparison supplies the paired presentation. The collision currents do not alter the differential or the connecting morphism.

These are statements about the coefficient complexes and their existing paired realizations. A full receiver calculation retains its actual vertex carriers and module actions; a noncritical corner dimension is not substituted for a multiplicity of root states.

## 9. What is closed and what remains

Closed at the declared finite cutoff:

- the four-factor balanced chain pentagon;
- tensor-of-shifts compatibility, without an extra associator sign;
- path independence of the source-constructed relative current;
- compatibility of this comparison with associated-layer factorization descent.

The argument is structural for finite iterated balanced tensors; the four-factor fixture checks the first pentagon explicitly. It does not establish a completed infinite-packet receiver, uniform estimates, or noncollapse of an inverse/projective limit. It also does not make raw and balanced carriers isometric or extend the collision rule to overflow, weight-changing, or seam-crossing operations.

## Verification

`uv run python research/nima/checkers/check_balanced_relative_pentagon.py`

Artifact: `results/balanced-relative-pentagon.json`.

Passed: five parenthesizations, 160 differential-sign checks, 10000 degree/shift configurations, 262144 typed shape pairs, 13312 new-match packet comparisons, and twelve nonminimal nine-event balancing fixtures.

No new Agda verification or numerical spectral Green computation is claimed.
