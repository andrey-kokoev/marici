# Native composition is retained witness composition, not averaging

## Direct implementation inspection

Inspected `agda/NativeTableRules.agda`, particularly Native.compose-comparisons, compose-filler, Congruence, Distribution, and Parameters/Arity/input/output for compose-kind. Also inspected `agda/WholePackageResolution.agda` for the matching rule and Resolve application.

For packages a,b,c and pointed equivalences e:Ty(a)~=Ty(b), f:Ty(b)~=Ty(c), native composition is literally

    remember (comparison-package a b e p)
      (remember (comparison-package b c f q)
        (comparison-package a c (compEquiv e f)
          (cong (equivFun f) p followed-by q))).

The two input ports are the supplied a-to-b and b-to-c comparison packages. They share the same typed middle package b. The underlying action is f composed with e; the marked-value witness is transported and composed. Both parents remain retained.

No sum, division, family mass, matrix reference or numerical readout occurs in this definition. This does not prohibit numeric data in supplied atoms; it means the generic operation does not select a numerical averaging law for them.

## What the other native operations do

| Operation | Actual behavior | Not implied |
|---|---|---|
| Pi-package | Retains a dependent family and selects its family of values | Arithmetic average of the values |
| E-package | Retains the family with a specified selected index/value | Uniform sampling or an index selected by physics |
| Pi-congruence | Applies supplied equivalences componentwise at the same index | Independent all-pairs incidence |
| Distribution | Reorganizes a dependent product of sums into a sum of dependent products, with inverse | Numerical reduction or removal of arbitrary witness histories |
| compose-kind | Composes the two supplied pointed comparisons through a shared middle package | Choosing all composable pairs from a collection, or a weighting on them |
| Resolve.apply | Applies a formed rule given derivations of each input | Selecting that rule as physical dynamics |
| reify-history | Packages the entire retained derivation as a next-level value | A reduced physical state or rung assignment |

Thus it was misleading to frame the native calculus itself as waiting to choose among three averages. Its comparison operation already acts on complete witnessed packages. The member/family/global alternatives belong to proposed response interpretations and family-level operations, which must be explicitly connected to this native composition.

## Exact missing interface

A numerical response realization must say what it assigns to a native pointed comparison and how that assignment respects its composition and identity. An identity-preserving representation would require rho(id)=I and rho(f composed e)=rho(f)rho(e), with appropriate typed spaces. A weaker response adapter must retain and account for its actual defect rather than silently claim these equations.

This is already constrained by `source-swap-transport-scope.md`, the theory-page two-channel discussion, and the joint-probe/mean-fluctuation results: actual witnesses and fixture amplitudes are distinct channels. Faithful encoding alone does not make fixture responses a representation. Supplied nontrivial amplitudes cannot be justified merely by the existence of a comparison equivalence.

For a family operation one must additionally provide an actual native rule application with its index/port domain and derivations. Only then can the incidence of its response terms be extracted. A correct generic compose function does not choose which pairs a physical process executes.

## Practical consequence

Do not add another averaging dynamics to resolve this issue. Start from an actual retained comparison derivation already admitted by the seed policy and inspect its available response/readout adapter. Use the existing defect-aware transport if its hypotheses match. Any claim that this realizes a horizontal rung map must provide the specific source/target packages and the rung4 observation compatibility, not just a scalar equality.

This audit establishes the native operation's exact semantics by implementation inspection; it adds no new theorem, checker or dynamics and does not claim a full physical generator has been selected.
