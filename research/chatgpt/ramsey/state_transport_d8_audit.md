# State–transport candidate: framed nodes and directed edges

## Result

The proposed local algebra works when formulated as

T = C2 × C2,   S = T ⋊ C2 ≅ D8,

where D8 has eight elements and the extra involution exchanges the two transport axes. In this chosen model there is an **exact D8-equivariant bijection between eight framed nodes and eight directed elementary square edges**.

This is a construction and finite verification, not evidence that native Marici states or Ramsey carriers already satisfy these definitions.

## 1. Positions, frame, multiplication

Let v=(x,y)∈F2² be a position and f∈F2 choose an axis frame. A state is (v,f). Let J(x,y)=(y,x).

Multiplication is

(v,f)(w,g) = (v + J^f(w), f+g),

with bit addition. This is the semidirect product; it is not the direct product C2³.

Choose a=(1,0,0), b=(0,1,0), s=(0,0,1). Then

- a²=b²=s²=1;
- ab=ba;
- sas=b.

The f=0 subgroup is the Klein four-group. The composite q=as has order four, q²=ab, and sqs=q⁻¹. Hence the same D8 contains both the commuting V4 transport subgroup and the cyclic quarter-turn subgroup C4; they are not the same subgroup.

The element-order histogram is 1 identity, 5 involutions, 2 order-four elements. The unused direct product C2³ instead has 7 involutions and no order-four elements.

## 2. The node–arrow correspondence

A bare square vertex has two outgoing elementary edges. Its frame selects one:

F(x,y,0) = ((x,y) → (x+1,y)),
F(x,y,1) = ((x,y) → (x,y+1)).

All coordinates are bits. The resulting arrow stores its tail and the changed coordinate, so the inverse map recovers the framed node uniquely.

A group element g=(u,h) acts on an unframed position by u+J^h(v), and on an arrow by acting on both endpoints. The checker verifies

F(g·state) = g·F(state)

for all 8×8 choices. Thus this is not merely a cardinality match: the action is preserved.

### Reversal

Swapping arrow endpoints gives an involution. On framed states its formula is

(v,f) ↦ (v+e_f,f).

In group labels this is **right multiplication by a**. Physical frame transformations act on the left, so reversal commutes with every such transformation. It need not commute as left multiplication by a would; left and right actions are distinct.

## 3. Why the extra frame matters

For any two bare square vertices, exactly two D8 transformations carry the first to the second. Their effect on the unused direction is unresolved.

For any two framed states X,Y, exactly one transformation carries X to Y:

transport(X→Y) = Y X⁻¹.

These endpoint transports compose exactly. The checker verifies all 512 triples of framed states.

This is the concrete content of “state = transport plus C2”: the extra frame removes a twofold transporter ambiguity. More intrinsically the eight states form a D8 **torsor**. Identifying them with group elements requires choosing one reference state.

## 4. Color action and scope

Take coordinate-0 edges red and coordinate-1 edges blue. The transport subgroup V4 preserves each color. The extra frame involution s exchanges red and blue. Consequently:

- symmetry with fixed color names is V4;
- symmetry permitting the frame/color exchange is D8.

This exchange is an explicit assumption, not an automatic property of any given colored assembly.

There are four bare nodes, eight framed nodes, and eight elementary directed square edges. The action groupoid between framed states has **64** arrows including identities. The eight elementary edges used in F must not be confused with all those groupoid arrows. The construction gives a local incidence correspondence; a categorical node–arrow duality would require specifying the categories and how compositions correspond.

Nothing here asserts cut invariance, a forced fifth node, a tetrahedral realization, or a Ramsey threshold. Those require additional incidence and gluing rules beyond the verified group algebra.

## Reproduction

```sh
python research/chatgpt/ramsey/check_state_transport_d8.py
```

`state_transport_d8_results.json` contains the multiplication table, state/arrow dictionary, reversals, all 64 framed transporters, and verification flags. The checker exhausts 512 associativity triples and 512 framed-transport composition triples, as well as all state/action equivariance pairs.
