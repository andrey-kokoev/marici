# Implemented native generating grammar

Generated from `native-core.json`; source definitions, not this transcription, govern the types.

## Formation

```text
h:Header; children:(i:Arity h)->Node(Inputs h i) |- table-node h children : Node(Result h)
Graph = Sigma(A:Type l).Node A
Package = Sigma(g:Graph).Value g; Value = fst
```

For every supplied universe level, header parameters and well-founded typed child family. Arity may be infinite; a finite number of schemas is not a finite-state or finite-branching assertion.

| Header | Parameters | Ports | Child types | Result type |
|---|---|---|---|---|
| atom-header | A:Type l | empty | none | A |
| E-header | I:Type l; F:I->Type l | I | F i | Sigma I F |
| P-header | I:Type l; F:I->Type l | I | F i | (i:I)->F i |
| paths-header | A:Type l; x,y:A | Unit | A | x = y |
| maps-header | A,B:Type l | Bool | false:A; true:B | A->B |
| equivalences-header | A,B:Type l | Bool | false:A; true:B | A equiv B |
| retain-header | A,B:Type l; x:A | Bool | false:A; true:B | B (with A,x retained in syntax) |
| comparison-header | A,B:Type l; e:A equiv B | Bool | false:A; true:B | Sigma(x:A).Sigma(y:B).e(x)=y |

## Rule schemas

Each application requires derivations at ALL its premise ports. Universe lifts are suppressed in this table, not in the source.

| Rule | Parameters | Premises | Output |
|---|---|---|---|
| E-kind | I; F:I->Package; i:I | F j for EVERY j:I, including unselected branches | E-package I F i |
| P-kind | I; F:I->Package | F i for every i:I | Pi-package I F |
| compare-kind | a,b:Package; e:Ty a equiv Ty b; p:e(value a)=value b | a and b | comparison-package a b e p |
| identity-kind | a:Package | a | identity-comparison a |
| inverse-kind | a,b,e,p as in compare-kind | comparison-package a b e p | inverse-comparison a b e p, retaining original comparison |
| compose-kind | a,b,c; e:Ty a equiv Ty b; f:Ty b equiv Ty c; pointed witnesses p,q | comparison(a,b,e,p) and comparison(b,c,f,q) | compose-comparisons a b c e f p q, retaining both comparisons |
| higher-kind | g:Graph; x,y:Value g; p,q:x=y; alpha:p=q | path-package g x y p and path-package g x y q | higher-package g x y p q alpha |
| reflexivity-kind | a=(g,x):Package | a | path-package g x x refl |
| path-lift-kind | c,d:Graph; e:Value c equiv Value d; x,y:Value c | Package of the actual equivalence e | lift-paths c d e x y, retaining e |
| distribution-kind | I; J:I->Type l; F:(i:I)->J i->Package; v:Pi_i Sigma_j Ty(F i j) | Every F i j AND the marked left-hand package with value v | Pointed comparison Pi_i Sigma_j F(i,j) equiv Sigma_f Pi_i F(i,f(i)) |
| E-congruence-kind | I; F,H:I->Package; e_i and p_i pointed comparisons; selected i:I | Every comparison(F j,H j,e_j,p_j) | Pointed E comparison, retaining the full family of comparisons |
| P-congruence-kind | I; F,H:I->Package; e_i and p_i pointed comparisons | Every comparison(F i,H i,e_i,p_i) | Pointed Pi comparison, retaining the full family of comparisons |

## Retained derivations

```text
a:Admit q |- seed a : Resolve q
r:Rule; ds:(i:Arity r)->Resolve(input r i) |- apply r ds : Resolve(output r)
```

A literal requires its actual certificate. No fallback admits arbitrary packages.

Empty admission does not imply empty closure: a zero-arity P application has no premise obligations.

## Equality and coverage

Cubical type-theoretic equality of the full dependent syntax/package; neither equal scalar readouts nor equal value types erase constructors or retained witnesses.

The source supplies package/rule/port and retained-closure equivalences with the legacy system. This covers all constructors of the named datatypes, not arbitrary repository operations.

## Existing amplitude interpretation

| Expression | Native derivation |
|---|---|
| zero-expr | Run.seed zero-seed |
| one-expr | Run.seed one-seed |
| factor | Run.seed (factor-seed a) |
| binary | Run.apply P-kind over Port={operator,left,right}; operator is a certified seed and children are translated recursively |

A P application retains operator and operand records; it does not derive scalar addition or multiplication from an unlabelled table. Component multiplication is separately constructed by recursion in ComponentArithmetic.

## External boundaries

- This is exhaustive for the named native datatypes, not all repository sector operations.
- No completeness theorem currently maps the nine-row comparison-successor policy contract into these native rules.
- The retained-path ledger and natural component arithmetic now have exhaustive definition censuses and computational rules in semantic-extensions.json. The path ledger's operational interpretation into native Resolve remains open.
- No finite serialization or equality-decision procedure for arbitrary supplied types, functions or higher witnesses is asserted.

## Sources

- [nodes](../../../research/nima/agda/IndexedConstructorTables.agda)
- [rules](../../../research/nima/agda/NativeTableRules.agda)
- [resolve](../../../research/nima/agda/IndexedResolutionTransport.agda)
- [closure](../../../research/nima/agda/NativeTableResolution.agda)
- [legacy_nodes](../../../research/nima/agda/WholePackageSigmaPi.agda)
- [legacy_rules](../../../research/nima/agda/WholePackageResolution.agda)
- [amplitude](../../../research/nima/agda/NativeAmplitudeResolution.agda)
- [arithmetic](../../../research/nima/agda/ComponentArithmetic.agda)
- [arithmetic_bridge](../../../research/nima/agda/NativeComponentArithmetic.agda)
- [specification](../../../research/nima/native-table-equivalence.md)
