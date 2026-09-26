# Does retained coherence select the central phase?

Obligation: composition/reversal coherence and readout selection. The candidate
phase law is frozen before asking whether those conditions determine it.

## Finite source test

The two actual independent swap maps in `RetainedComparisonSeries` generate a
faithful action of G=(Z/2)^2 on the sixteen source pairs. A grade g=(a,b) records
which swaps were applied. Retain the full word separately from its grade.

A normalized sign lift is specified by sigma(g,h) in {+1,-1}:

```text
(s,g)*(t,h) = (s t sigma(g,h), g+h).
sigma(0,g)=sigma(g,0)=1.
```

Associativity is exactly the cocycle equation

```text
sigma(g,h) sigma(g+h,k) = sigma(h,k) sigma(g,h+k).
```

Both the trivial law sigma=1 and the preceding Clifford law
`sigma((a,b),(c,d))=(-1)^(bc)` satisfy it. Both have inverses, reversal
compatibility and double-inverse recovery. Both retain the same full source
word histories, with preceding-word recovery. Their projections give exactly
the same actual source permutations. Keeping the history therefore does not
force a nontrivial phase reading.

Exhaustive normalized sign-cochain classification gives:

| Constraint/equivalence | Result |
|---|---:|
| All normalized sign cocycles | 16 |
| Classes under sign-valued changes of lift | 8 |
| Require each elementary lifted swap to square to +1 | 4 cocycles |
| Classes with those elementary squares, under sign rephasing | 2 |
| All sign cocycles, modulo complex unit-phase rephasing | 2 |

The final two classes are distinguished by the generator commutator phase,
+1 versus -1. Complex rephasing cannot identify them. The complex-gauge check is
exhaustive: if two sign cocycles differ by a normalized U(1) coboundary, applying
it to (g,g) forces each rephasing value to be a fourth root of unity. Only 64
normalized rephasings need checking.

This classifies the stated finite central-extension model. It is not a theorem
that every possible native higher-source condition is exhausted by this model.

## What the Clifford choice adds

Once the four-dimensional algebra is fixed as Cl(2,0)=Mat_2(R), and the source
actions are the previously checked Ad(e1), Ad(e2), their inner lifts are fixed
up to nonzero scalar factors. The checker solves, on the full matrix basis,

```text
U q = Ad(e1)(q) U,    V q = Ad(e2)(q) V.
```

The respective solution spaces are precisely span(e1) and span(e2). For
invertible solutions their relative commutator is therefore -1. The same linear
calculation applies after complexifying the matrix algebra.

The trivial extension is not an alternative inner lift within that fixed
Clifford profile. It is an alternative coherent extension of the underlying
source action before the Clifford product and implementation policy are fixed.
For example, the source actions themselves have commuting four-by-four matrix
representatives on the observable-coordinate space; those are a different
representation from two-by-two inner implementers.

There is a concrete additional selection condition. Extend the signed basis
multiplication linearly to a four-dimensional twisted group algebra. The trivial
commutator class gives a commutative algebra, whose inner automorphisms are all
identity. Requiring the nontrivial source swaps to act by conjugation INSIDE that
algebra excludes this class. With the already declared positive generator
squares, the remaining phase class is the Clifford one.

This identifies where the extra assumption enters: inner implementation in the
chosen algebra. Being a function internal to a source type does not establish
being an inner automorphism of an associative algebra. Classical Hamiltonian
flows already have an internal Poisson-bracket description; replacing that by
associative commutators is additional structure.

## Hamiltonian translation test

For displacements u=(q,p), v=(r,s), define omega(u,v)=q s-p r and an exponent
`c_rate(u,v)=rate*omega(u,v)`. The phase candidate is
`exp(i*c_rate(u,v))`. Its cocycle, inverse and reversal identities hold for
EVERY real rate, including zero:

```text
c(u,v)+c(u+v,w) = c(v,w)+c(u,v+w).
c(u,-u)=0.
c(-v,-u)=-c(u,v).
```

`agda/PhaseLiftCocycle.agda` proves these exponent identities over an arbitrary
small commutative ring, with rate an explicit parameter. It also proves that
linear changes of coordinates multiply omega by their determinant. Consequently
linear symplectic covariance does not fix the rate either.

The complex exponential and continuum interpretation are supplied mathematics,
not an Agda construction of complex analysis. The Weyl convention identifies
rate=1/(2 hbar); no physical value of hbar follows from these identities. A
nontriviality requirement would exclude zero without determining the scale.

## Result

The tested coherence and retention conditions admit the classical trivial phase
and the nontrivial central phase. The fixed Clifford inner-implementation
profile selects the latter, but that profile was an added algebraic choice.
The corresponding continuum coherence laws also leave the phase scale free.

The next source-level question is precise: does the retained construction supply
an associative observable algebra and require its development maps to be inner?
This test does not claim that derivation, a full quantum theory, or a derived
physical action.

## Verification

```text
pwsh -NoProfile -File research/nima/checkers/check_phase_lift_cocycle.ps1 -Fresh
uv run --with sympy python research/nima/checkers/check_phase_selection.py
uv run --with sympy python research/aspect/scc/scc.py check nima-phase-selection
```

Fresh safe/cubical compilation of the generic exponent module passes. Exact
finite checks cover every normalized sign cochain, cocycle and gauge case,
all signed-group associativity/reversal laws, the actual source action,
retention controls through six letters, and the matrix intertwiner spaces.
Receipts: `results/agda-PhaseLiftCocycle.json` and `results/phase-selection.json`.
No existing owner source was changed; no full higher-source phase selector or
independent physical validation is claimed.
