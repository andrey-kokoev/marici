# A single sign recursion for a Clifford lift of the source square

Obligation: forward realization and compatibility of composition with reversal.
This is an exact finite algebraic prototype of the proposed recursion. It does
not identify algebraic word checks with all higher witnesses of the retained
source calculus.

## Construction

Use the declared Euclidean Clifford algebra Cl(2,0), represented by real matrices:

```text
e1 = [[1,0],[0,-1]]
e2 = [[0,1],[1,0]]
J  = e1 e2 = [[0,1],[-1,0]]
```

The generators square to one and anticommute; J squares to minus one.
For Q in this algebra define L(Q)=e1 Q e1 and R(Q)=e2 Q e2. These are adjoint
actions, rather than the previously tested left-multiplication actions.

L and R commute on the whole algebra. Their implementing products are J and -J,
which have the same adjoint action because the sign is central. The difference
between the two implementing products is 2J. Its scalar part is zero, and
reversion times the original gives 4. This is a nonzero lift difference over a
commuting square of actions.

The user's nested commutator of the two implementing products remains zero:
`[J,-J]=0`. The nonzero quantity in this construction is their difference. The
relative multiplicative discrepancy is the central sign -1.

## Connection with the actual source maps

The checker parses the proved swap images from `RetainedComparisonSeries.agda`.
Let v0 be the selected-point basis vector e00 and d=e01-e10. In the independent
source product, use the ordered basis

```text
v0 tensor v0, v0 tensor d, d tensor v0, d tensor d.
```

Map it respectively to 1, e1, e2, J. Source pullback by the first-factor swap
matches Ad(e1); pullback by the second-factor swap matches Ad(e2). The checker
verifies the intertwining on every basis vector, hence on the entire active
four-dimensional subspace by linearity.

This is an active-sector representation, not an identification with the entire
sixteen-dimensional source product. The odd vectors are unnormalized, so this
particular basis correspondence is not asserted to be an isometry. A physical
selection of this Clifford lift or its readout has not been derived.

## One recursive multiplication law

Write a signed basis element as s e1^a e2^b, with s in {+1,-1} and a,b in {0,1}.
Its normal form is the triple (s,a,b). Multiplication is

```text
(s,a,b) * (t,c,d) = (s t (-1)^(b c), a xor c, b xor d).
```

This determines the phase of every finite generator word. The retained packet
keeps the complete word/history in addition to this normal form. Different
histories can have the same normal form; an empty word and e1 e1 are an explicit
control. Appending a generator retains the preceding word, with exact recovery.

The sign sigma((a,b),(c,d))=(-1)^(b c) satisfies the cocycle equation

```text
sigma(g,h) sigma(g+h,k) = sigma(h,k) sigma(g,h+k).
```

Addition here is bitwise XOR. For g=(a,b), h=(c,d), k=(e,f), the two exponents
are b c + (b+d)e and d e + b(c+e). Both expand modulo two to b c + b e + d e.

Reversal is derived from the same multiplication:

```text
reverse(s,a,b) = (s (-1)^(a b), a, b).
reverse(g*h) = reverse(h)*reverse(g).
```

Each signed basis element is a unit and its reverse is its inverse. Double
reversal recovers the original element. These facts supply a coherent recursive
word calculus.

## Relation to the five rules

The checked algebraic instances are:

1. Independent forward adjoint actions commute while both lift orders are kept.
2. Reversal reverses multiplication order and returns inverse signed elements.
3. Every tested normalization of a reversed word gives the same signed result.
4. Every tested forward parenthesization gives the same signed result.
5. Reversing a parenthesized product and evaluating agrees with evaluating the
   reversed word, independently of the chosen parenthesization.

These are checks of this word-level realization. They do not supply comparisons
between arbitrary independently chosen higher source witnesses. In particular,
the cocycle and reversal laws close the word-coherence diagrams: this model does
not automatically generate a fresh nonzero residue at every higher level.

## Limits of the proposed scalar recurrence

The grade of a compared lift matters. The word e1 e2 e1 e2 represents -1, while
the empty word represents 1. They have the same adjoint action, but their lift
difference is the real scalar -2. Scalar versus bivector residue is therefore
not determined by an unspecified coherence-level index alone.

Ordinary squaring also fails as a general retention operation: the nonzero
Clifford element e1+J squares to zero. Its positive scalar norm, obtained from
reversion times the element, is 2. History retention and positive scalar readout
must remain separately specified. The proposed inherited-scalar recurrence is
not proved by the sign rule.

## Verification

```text
python research/nima/checkers/check_clifford_retained_order.py
python research/aspect/scc/scc.py check nima-clifford-retained-order
```

Exact checks exhaust all 64 grade cocycle cases, 512 signed associativity cases,
all signed reversal products, and 127 generator words through length six with
3239 parenthesizations. The source-sector intertwiner and the stated positive,
zero-commutator, real-residue and nilpotent controls pass.

Receipt: `results/clifford-retained-order.json`. No new Agda compilation or
physical derivation is claimed. No pre-existing source artifact was changed.
