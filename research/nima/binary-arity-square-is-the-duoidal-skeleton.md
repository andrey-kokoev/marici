# The binary arity square is the duoidal skeleton

## Source identification

The four intrinsic arity types are

\[
V_1=(1,1),\qquad
V_2=(1,*),\qquad
V_3=(*,*),\qquad
V_4=(*,1).
\]

Writing `0` for unary and `1` for many gives the Gray cycle

\[
(0,0)\to(0,1)\to(1,1)\to(1,0)\to(0,0).
\]

The source rotation is

\[
r(x,y)=(y,1-x),
\qquad r^4=1.
\]

Independent input and output flips generate the square's `C2 x C2` symmetry. The quarter rotation extends this to the stated dihedral action.

## Two composition directions

The prior all-arity theorem supplies two independent operations on the marked occurrence system.

### Horizontal direction

Rooted-subtree substitution and scalar associahedral refinement compose source histories. Product faces factor into associahedral factors, and the trivial rooted substitution is the unit.

### Vertical direction

Physical cut coactions add channel/output structure. Disjoint cut sets satisfy

\[
G_EG_F=G_FG_E,
\]

and the empty cut set is the unit.

### Interchange

For cuts transverse to selected scalar block factors, the all-arity theorem proves strict mixed Beck--Chevalley base change. In double-monoidal notation this is the interchange comparison

\[
(a\boxtimes b)\otimes(c\boxtimes d)
\longrightarrow
(a\otimes c)\boxtimes(b\otimes d),
\]

and it is an identity on the strict occurrence-level transverse subcomplex after the canonical factor identifications.

Associativity comes from rooted substitution and disjoint cut-set union. Unit compatibility comes from trivial substitution and the empty cut. Higher coherence reduces to product-associahedral facet incidence, exactly as stated in the all-arity proof.

Hence the marked transverse occurrence system carries a **strict duoidal module structure** over its two refinement directions. Calling it a module is precise: the source theorem constructs the two actions on the occurrence/cellular carrier; it does not construct every tensor product on an ambient category of arbitrary analytic objects.

## Meaning of the four vertices

The arity square classifies the four endpoint types of the two actions:

| Vertex | Type | Constructor role |
|---|---|---|
| `V1` | `(1,1)` | unary source/state |
| `V2` | `(1,*)` | expansion/coaction |
| `V3` | `(*,*)` | relation or channel interaction |
| `V4` | `(*,1)` | synthesis/trace |

The diagonals retain two different factorizations:

\[
V_1V_3:	ext{ simultaneous input/output arity change},
\]

\[
V_2V_4:	ext{ expansion--synthesis or variance exchange}.
\]

The tetrahedral coordinate `tau` records the lift between these diagonal factorizations. It is coherence/polarization data over the arity square.

## Fourier interpretation

On the analytic realization, Fourier transport exchanges

\[
*\quad\longleftrightarrow\quad\cdot
\]

between convolution and pointwise-product charts. This is a strong monoidal equivalence between the two typed chart presentations:

\[
\mathcal F(f*g)=\mathcal Ff\cdot\mathcal Fg,
\qquad
\mathcal F(fg)=\mathcal Ff*\mathcal Fg.
\]

Fourier therefore rotates the analytic realizations of the two arity directions. It is not the interchange law itself. The interchange law is the mixed Beck--Chevalley cell supplied by rooted substitution versus physical cutting.

This distinction resolves the earlier ambiguity:

- the binary arity square is the object/type skeleton;
- rooted substitution and cut coaction are the two monoidal actions;
- Beck--Chevalley is the interchange cell;
- Fourier is the chart equivalence exchanging the analytic products;
- the tetrahedral `tau`-fiber retains competing diagonal factorizations.

## Scope

The strict theorem applies to cuts transverse to the scalar block factors on the marked product-associahedral occurrence complex. Nontransverse physical divisors and finite-`alpha'` loaded-current realizations remain outside that theorem. On those extensions the interchange may become a derived or lax Beck--Chevalley transformation rather than an identity.

`check_arity_square_duoidal_contract.py` verifies the Gray cycle, order-four rotation, independent flips, units, and strict transverse set-level interchange.
