# One global comparison carrier, with both routes and their mismatch retained

## Question and claim boundary

Operator: “let's do that. our objective is Understanding.” The question is whether the P-reference and E-reference routes are reductions of one global operation, and what is lost if their final record agreement is treated as the whole comparison.

SCC obligation: **route/coherencer compatibility**. This construction extends the existing rational-cochain model of native reference supports. It uses the already fixed whole-carrier fixture; it does not generate wiring from local readers. The native payloads remain unspecified. No physical field, phase or particle property is assigned to the new cochain coordinates.

Conjecture: both routes admit one global comparison model, with an explicit separation between ordinary square data, route mismatches and contractible fine-detail witnesses. Rivals: the local contractions fail to assemble; their formulas require static global signs; matching all local routes exhausts global data; or the previous 1/6 discrepancy is already evidence of phase holonomy.

## 1. The two routes really do fit one common global square complex

Fresh export from the native comparison constructor finds 36 square occurrences. Across the whole carrier:

- the four incoming channel edges per square give 60 distinct cross-P/E reference edges;
- the 72 same-role diagonals each belong to exactly one square occurrence;
- no diagonal is an incoming cross-P/E edge;
- every comparison triangle belongs to exactly one square occurrence.

Thus the E and P triangle collections are two subdivisions of the same abstract regular square-cell complex Q. This is a mathematical comparison carrier, not an assertion that native spatial cells are these squares. Cell orientation is chosen and retained per occurrence; no reading-independent sign is assigned to a charged cell.

| Complex | Vertices | Edges | Faces | Rational Betti numbers |
|---|---:|---:|---:|---|
| Q: common squares | 32 | 60 | 36 | (1,0,7) |
| E route | 32 | 96 | 72 | (1,0,7) |
| P route | 32 | 96 | 72 | (1,0,7) |
| Both triangle collections, K | 32 | 132 | 144 | (1,0,43) |

The last row is not simply another subdivision of Q. It retains both disks above each square, whose difference is a two-sphere. Collapsing it to Q would delete 36 independent classes. We do not make that collapse.

## 2. Retain a mean and a mismatch for every square

Write the cyclic labels as `0=P+,1=E+,2=P-,3=E-`. The oriented E triangles are `012,023`; the P triangles are `123,130`. For a fine 2-cochain b, define

```
e = b012 + b023,
p = b123 + b130,
Omega = (e+p)/2,
mu = e-p.
```

These definitions are applied simultaneously to all 36 squares. The reduced comparison carrier R consists of ordinary square cochains plus one additional degree-two mismatch coordinate mu per square:

```
R = C*(Q;Q) direct-sum Q^36 in degree 2.
```

Its dimensions are `(32,60,72)`. Its differential is the square incidence differential on the first summand and zero on the second. In particular, the coboundary of an edge cochain has equal E/P boundary sums, so it contributes no mu.

The two route readers are

```
rE(Omega,mu) = Omega + mu/2,
rP(Omega,mu) = Omega - mu/2.
```

Their common-record components agree identically. They agree on face data exactly when mu vanishes. Equality is tested rather than built into the carrier.

## 3. A whole-carrier contraction, with exact recovery witnesses

The projection p keeps all vertices and cross-P/E edges and uses the preceding mean/mismatch formula on faces. For the inclusion i, write the four oriented boundary edge values as `w0,w1,w2,w3` and set

```
w02 = (w0+w1-w2-w3)/2,
w13 = (w1+w2-w3-w0)/2.
```

Assign each E triangle the value `Omega/2+mu/4`, and each P triangle `Omega/2-mu/4`. The fine triangles' global orientations are handled explicitly in the implementation.

K is zero except from fine face cochains to diagonal-edge cochains:

```
(Kb)02 = (b023-b012)/2,
(Kb)13 = (b130-b123)/2.
```

Because the diagonal interiors are disjoint across the fixed global square complex, these formulas define single global maps, not separately fitted local packages. Exact checks give

```
pi=id,  dK+Kd=id-ip,  K²=0,  pK=0,  Ki=0,
```

and both i and p commute with their differentials. Consequently, arbitrary fine data can be recovered from the reduced data and the two retained witnesses:

```
x = i(px) + d(Kx) + K(dx).
```

The reduced packet alone is not lossless. For example, a pure diagonal edge has zero projection but survives in Kdx. Keeping the witnesses avoids identifying a cochain contraction with strict recovery of all fine values.

## 4. One operation gives both route formulas

Use the globally defined integrated Whitney product on K and transfer it once:

```
M(a,b) = p( i(a) cup_W i(b) ).
```

Neither route is selected in this definition. Both are readers of its result. The method `GlobalComparison.operation` implements this operation for homogeneous cochains on R. It is a binary operation compatible with the differential, not a claim of strict associativity or a completed BV action.

For ordinary square inputs (mu=0), the difference of the two readers is accounted for by one global bilinear homotopy. For each square define

```
L(w) = (-w01+w12-w23+w30)/12,
H(w,Omega) = L(w) Omega,
H(Omega,w) = Omega L(w),
```

with H zero on other degree pairs. H is face-valued and vanishes on boundary restrictions. It obeys

```
rE M(a,b)-rP M(a,b)
  = dH(a,b)+H(da,b)+(-1)^degree(a) H(a,db).
```

This is checked on all 16,384 ordered pairs of basis elements of C*(Q). The symmetrized L replaces the earlier asymmetric local representative. It is invariant under all four local P/E sign bindings; 8,640 edge-basis/frame checks pass. This does not require a static global sign convention.

## 5. Understanding the previous 1/6 discrepancy

For four rational vertex values f0,f1,f2,f3 and a face input Omega, the global operation returns

```
mean     = (f0+f1+f2+f3) Omega / 4,
mismatch = (f0-f1+f2-f3) Omega / 6.
```

Equivalently, the mismatch is `(sum of P values - sum of E values) Omega/6` in this cyclic frame.

The reason is elementary: in the E triangulation the P vertices belong to both triangles, whereas each E vertex belongs to one. The P triangulation reverses those multiplicities. Their average weights all four vertices equally.

For the vertex-0 basis input, the mean is `Omega/4` and the mismatch is `Omega/6`; reading the two routes gives `Omega/3` and `Omega/6`. A constant vertex probe has zero discrepancy. All four vertex coefficients are checked at all 36 squares.

Thus the previously observed 1/6 difference is explained by interpolation and incidence multiplicity. It is not, by itself, evidence of a phase or nontrivial holonomy. The homotopy identity also includes derivatives of the inputs: it must not be misreported as equality of the two outputs for every fixed nonclosed input.

## 6. What survives changes of cochain representative?

For a two-cochain, consider the declared cochain gauge change `b -> b+d a`.

- All 36 mu coordinates are unchanged.
- The seven periods of Omega on a basis of global square two-cycles are unchanged.

The checker constructs that cycle basis exactly. These 43 functionals are independent and their common kernel is precisely the 29-dimensional image of the edge coboundary in R2. They therefore classify degree-two rational cochains modulo this particular gauge relation.

An explicit separating packet has every mu equal to zero, so all local E/P routes agree, but has a nonzero global period. Another has mu=1 at one square and unchanged vertex records, so the route readers differ. Both packets are retained in the verification evidence. Neither packet is asserted to be a physically realized native state.

This explains the earlier decomposition `43=36+7`: 36 independent local route-sphere periods plus seven classes of the common square carrier. It does not turn either number into a physical dimension or establish an integral equivariant invariant.

## Disposition

Constructed: one whole-carrier cochain reduction retaining all 43 degree-two classes; two route readers; an operation derived once from the global Whitney product; and a global boundary-relative binary comparison homotopy on the common square inputs. The local-assembly and static-sign rivals fail, and explicit packets refute the claim that local agreement exhausts global data.

The missing physical/native input is now more specific: which native operation supplies the edge and face coefficients, including mu and the global periods? The four record identities do not supply those values. A complete higher associativity/BV structure, a closed loop of higher comparison transformations, and a native involution lift have not been constructed here. No Hopf or FKMM class is inferred.

## Verification

```sh
python -X utf8 research/strominger/checkers/check_su32_global_comparison.py
python -X utf8 research/aspect/scc/scc.py check su32-global-comparison-v1
```

All arithmetic uses standard-library exact fractions. The checker regenerates the native support export and validates source hashes. Counts: 308 fine-basis contraction/recovery checks; 16,384 global binary-homotopy checks; 8,640 sign-binding checks; 144 four-record interpolation checks; 328 two-sided-unit checks; seven constructed global cycles and 43 independent top-degree period functionals.

Artifacts:

- `checkers/check_su32_global_comparison.py`
- `results/su32-global-comparison-v1/verification.json`
- `results/su32-global-comparison-v1/square-carrier.json`
- `scc-models/su32-global-comparison-v1.json`

Initial construction was frozen before replay. Follow-up tests exposed the general four-record formula and checked the complete period map. Final freeze: `04e7b664ab03dea7fe847a628e86057f4ecfc4330dd7130cbb388de18c76abf5`. No earlier scientific packet or native routing implementation was changed.
