# Complete detector laws identify the classical reference parameters

## Scoped result

Constructed a partial mathematical witness for `identifiability-and-robustness-test`: four unconditional history probabilities identify efficiency eta, recovery gamma and initial readiness r within the classical reference family, provided eta,r>0 and all words share the same parameters and initial readiness.

This is structural identifiability of **exact model laws**, not parameter estimation from observations. It does not identify a unique CP completion, native source law or apparatus. The full programme node remains open.

Contract: `contracts/physics-detector-law-inverse.v1.json`.
Checker: `checkers/check_physics_detector_law_inverse.py`.

## Exact inverse

Prepare the input words 1,01,11,101 at the mathematical level, with common initial readiness r. Preparation changes optical input, not memory inside a word. Define

```
a = P(C | 1)       = eta*r
b = P(NC | 01)     = eta*(r+gamma*(1-r))
v = P(NC | 11)     = eta*((1-eta)*r+gamma*(1-r))
w = P(CNC | 101)   = eta^2*r*gamma.
```

These are full unconditional record probabilities, with every N retained. The formula for w follows because the first click leaves dead memory, the empty middle bin recovers with probability gamma, and the last photon clicks with probability eta.

Subtracting b-v gives `eta²*r=a*eta`. Therefore

```
eta   = (b-v)/a
r     = a/eta
gamma = w/(a*eta).
```

When a>0 and eta>0, this is unique. Any two admissible reference-family parameters with the same four coordinates must coincide. The checker verifies forward reconstruction; this is not a generic acceptance rule for an arbitrary full dataset or an unknown instrument family.

## Why three of these coordinates do not suffice

Without b, the parameters

```
(eta,gamma,r) = (1/2,1/4,1/4)
(eta,gamma,r) = (1/4,1/2,1/2)
```

give identical `a=1/8`, `v=5/32`, `w=1/64`. They differ at b: 7/32 versus 3/16. All parameters lie inside the previously declared conditioning box.

In general a,v,w determine eta*gamma and eta+gamma but can leave a swap ambiguity, with readiness adjusted to preserve eta*r. This is an exact alias of this chosen three-coordinate projection, not a proof that every possible three-coordinate design fails.

## Deterministic conditioning on the admitted box

Take eta,gamma in [1/4,1/2] and r in [1/4,3/4]. For two admissible reference-family points, assume each of a,b,v,w differs by at most delta. Write differences as Delta.

The box gives `a>=1/16`, `eta>=1/4`, `a<=3/8`, `eta<=1/2`, `r<=3/4`, `gamma<=1/2`.

Using `eta=(b-v)/a`,

`|Delta eta| <= (2+1/2)*delta/(1/16) = 40 delta`.

Using `r=a/eta`,

`|Delta r| <= delta/(1/4) + (3/4)|Delta eta|/(1/4) <=124 delta`.

Let q=a*eta, so `q>=1/64` and

`|Delta q| <= (1/2)delta+(3/8)|Delta eta|`.

Using `gamma=w/q`,

`|Delta gamma| <= [delta+(1/2)|Delta q|]/(1/64) <=560 delta`.

These inequalities hold over the entire box, not just the finite fixtures. They are conservative pairwise deterministic inverse bounds for points on the reference family. They do not turn arbitrary noisy/off-family coordinates into a valid parameter confidence region.

The large recovery constant is scientifically relevant: even structural uniqueness does not imply well-conditioned inference at the charter's 1/100 discrepancy. At that tolerance these loose bounds can be vacuous. Sharper local bounds or additional source constraints would be a separate mathematical task, not grounds for pretending parameters have been identified accurately.

## Boundaries and retained gates

At r=0 or eta=0, a vanishes and this inverse fails; additional histories or a separately specified initial condition are needed. The result requires common initial readiness across the different input-word laws. Word-dependent initialization can invalidate the inverse; an algebraic fit alone does not certify that common-source assumption.

Postselecting clicks changes the coordinates and their denominators. Dropped no-click outcomes cannot be repaired by interpreting selected frequencies as a,b,v,w. The merged-environment CP rival remains identical on the classical laws, regardless of how well eta,gamma,r are recovered. Source-law and physical-authority gates remain separate.

Measurement work remains parked.

## Verification

Fresh exact rational controls cover 125 parameter triples, 500 complete-word normalizations and 15,625 pairwise inverse-conditioning checks. They also exhibit the three-coordinate swap alias and reject zero initial readiness, zero efficiency, selected conditional frequencies and a specific incompatible word-dependent initialization. The proof above establishes the unrestricted inverse and inequalities; finite tests corroborate them.

Scope controls reject full-node closure, empirical parameter estimates and extending the conditioning box to zero efficiency without a new proof. Inputs are hash-checked before and after execution.

```
python research/nima/checkers/check_physics_detector_law_inverse.py
python research/aspect/scc/scc.py check physics-programme-v18
```
