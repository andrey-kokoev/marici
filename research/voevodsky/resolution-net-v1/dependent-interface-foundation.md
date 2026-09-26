# Dependent interfaces: an alignment, not a universal evaluator

Freshly checked `agda/ResolutionNetDependentInterface.agda` with safe Cubical Agda and --ignore-interfaces. The check also rebuilds the imported upstream index/coherence regression. Log: results/agda-dependent-interface.log. Earlier whole-prototype audit receipts predate these new modules and are not fresh receipts for them.

## What the new theorem says

Supplying an input x and then dependent evidence y has two equivalent presentations:

    Σ (x : Γ → X), ((γ : Γ) → Y(x γ))
        ≃
    Γ → Σ (x : X), Y(x)

The proof constructs the maps in both directions and checks both inverse laws. This is the standard context-comprehension property, not a novel principle invented for resolution nets. A dependent continuation likewise has equivalent curried and uncurried presentations:

    ((x : X) → (y : Y(x)) → Z(x,y))
        ≃
    ((z : Σ X Y) → Z(z))

Executing a supplied input against its continuation is the same dependent application in either presentation. Together with the preceding substitution laws, this gives a recognizable mathematical account of interface composition rather than a resemblance between two separately defined machines.

Transport respects composition by an explicit equality proof. Unlike ordinary function-composition laws in the semantic model, it is not asserted to be strict definitional equality. Retaining that distinction is necessary for higher coherence.

## An obstruction is part of the result

The circle-cover family admits no global section. Consequently a well-formed interface Y(x) need not admit a coherent function providing an inhabitant for every x. The formal no-total-supplier theorem imports that proved obstruction.

This does not claim a theorem about arbitrary external algorithms or eliminate local inputs. It says that mathematical problem formation and a total internal solution are different. Alignment must preserve this difference rather than introducing a universal evaluator that silently fabricates answers.

## Foundational conclusion

The evidence points toward dependent type theory with computational transport as a common foundation. The generic Resolve closure is a useful free construction over rules, but its substitution laws alone are not a replacement for that foundation.

Two limitations now stand out:

1. The model inherits its dependent functions and transport computation from Cubical Agda. It does not supply an independent syntax/reduction system or prove such a system normalizing.
2. Ordinary context functions allow copying inputs. Physical exclusive ownership is not forced by this model; resource-sensitive computation needs additional structure such as linear contexts or an explicit authority interpretation.

The next substantive construction should expose syntax and directed reduction for a small dependent fragment, checking substitution and preservation against this model. Merely adding another theorem whose evaluation is already delegated to Agda would not establish an independent computational realization.
