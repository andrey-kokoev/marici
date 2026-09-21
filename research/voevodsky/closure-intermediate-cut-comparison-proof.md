# Intermediate-cut comparison for a triple quotient

## Constructed theorem

For A --f--> B --g--> C --h--> D, form the triple homotopy quotient

`Z = ((D/A)/(B/A)) / ((C/A)/(B/A))`.

Its outer attachment map is the previously constructed naturality map between double cofibers. There are now two independently defined routes:

1. `Z -> (D/B)/(C/B) -> D/C`, collapsing A first;
2. `Z -> (D/A)/(C/A) -> D/C`, collapsing the common middle quotient B/A first.

Both intermediate maps and both complete routes are proved equivalences. The complete routes are compared by an explicit homotopy and hence by equality of equivalences. Their selected inverse functions are also compared.

Implementation: `agda/ClosureIntermediateCutComparison.agda`.
Regressions: `agda/ClosureIntermediateCutRegression.agda`.

## Construction rather than a compatibility assumption

`collapseA` and `collapseMiddle` are higher-inductively defined on the actual triple quotient. Their intermediate codomains differ. Neither route is defined to be the other route.

`cutComparison` compares the complete composites on every constructor. On the deepest attachment, the two formulas are respectively

`push (g (f a)) ((u meet v) meet w)`

and

`push (g (f a)) (u meet (v meet w))`.

Cubical interval meet is associative, so these formulas coincide while retaining the complete three-dimensional boundary data. The proof also checks all lower-dimensional faces.

The equivalence proof for `collapseA` uses the library's pushout-equivalence theorem on the span whose vertical maps are the already proved canonical rejoin equivalences. The naturality square supplies its commuting witness. `spanMapComparison` explicitly compares that library forward map to the constructor-defined map, removing the library's reflexivity concatenations with a path unit law.

The first complete route is therefore an equivalence. The independently proved `cutComparison` transfers that property to the second complete route. Cancellation with the known final rejoin equivalence proves `collapseMiddle` is an equivalence too. This is two-out-of-three applied to proved maps and homotopies, not an assumption of cut compatibility.

`equivalenceComparison` upgrades the homotopy to equality of equivalences using propositionality of the isEquiv witness. This does not truncate the underlying types or their paths. `inverseComparison` follows by applying inverse selection to that equality; it compares these equivalences' selected inverse functions, not a separately specified pair of constructor-defined inverse assemblies.

## Regression and verification

The fixture uses A=B=C=Bool, D=Unit, f=g=Boolean negation, and h the terminal map. Thus the deepest attachment domain is nonempty and both initial maps are nonidentity. The triple quotient is proved equivalent to the circle.

The regression checks:

- equality on the full triple attachment;
- its concrete target attachment normal form;
- the inverse-comparison family along the entire circle loop.

Fresh command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureIntermediateCutRegression.agda`

Final result: exit 0. Both modules use `--safe --cubical --guardedness`, without holes or postulates. Existing modules were not modified.

An initial full check timed out after 200 seconds, followed by an incremental regression timeout after 60 seconds. The source theorem itself checked, but inverse specialization unfolded large pushout equivalence proofs. The repair makes only the checked isEquiv witnesses abstract. Forward functions and attachment calculations remain transparent. After that change, both the incremental regression and a fresh dependency-closure check passed.

## Scope

This is a comparison of changes of an intermediate cut, not just target-postcomposition naturality. It supplies the next actual rebracketing cell.

It is not yet the pentagon comparing five assemblies for a longer filtration. It also does not identify the canonical constructor-based rejoin with the earlier opaque 3-by-3/univalence-transported implementation, and makes no analytical realization claim.

The next gate is to build the five longer-filtration assemblies with their boundary adjustments and compare the two paths of these intermediate-cut cells around the pentagon.
