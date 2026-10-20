# General dependent extensions: transport, composition, projection and native admission

## Result

The structural core of the proposed coherent extension system is now a generic
Agda theorem package, instantiated by the existing retained-feedback construction.
It is not another six-arrow counting model.

The theorem is conditional on typed witness families and their compatible maps.
The source-admission policy remains explicit; forming a dependent sum does not
discover which task signatures or rule parameters a source permits.

The mathematics uses the existing Cubical library's dependent-sum equivalence
construction, rather than claiming a new underlying theorem about Sigma types.
The new work assembles its relevant laws, relative-fiber classification and
native admission interface, and checks the actual feedback instance against it.

## General structure and maps

A Family contains

    X : Type,
    W : X -> Type,
    Total(F)=Sigma(x:X) W(x).

A map of families contains BOTH a base map f:X->Y and witness maps

    g_x:W(x)->V(f(x)).

Its total map is (x,w)->(f(x),g_x(w)). Identity, composition and associativity
laws are checked without assuming that X or its witness fibers are sets.
The witnesses remain data; they are not replaced by mere existence assertions.

If the base map and every witness map are equivalences, the total map is an
equivalence. Lifted comparisons preserve identities and composites, with a
checked associativity equality. Actual supplied paths between family comparisons
and paths between those paths map to the corresponding comparisons of total
extensions. These maps consume those witnesses; they do not invent missing ones.

This is not an all-dimensional categorical coherence theorem. In particular,
this generic result does not identify the prior feedback example's forward lift
with its separately defined backward lift or prove a forward-squared identity.

## Dependent composition and natural reassociation

Two successive extension fibers combine as

    Sigma((x,w):Sigma(x:X)W(x)) V(x,w)
      ~= Sigma(x:X) Sigma(w:W(x)) V(x,w).

The checked isomorphism retains x,w,v exactly and has both inverse laws.
Reassociation commutes with compatible maps of all three fields. The second
fiber can be empty or depend nontrivially on the first witness; replacing it by
a constant Cartesian factor is not licensed.

Thus dependent composition and transport are parts of the same reusable
construction, rather than independent observations from a finite seed model.

## What the fiber classification actually says

For the PARTICULAR retained projection

    pi:Sigma(x:X)W(x)->X,

the formal module proves both directions:

    pi is an equivalence iff every W(x) is contractible.

One direction explicitly constructs the inverse using the fiber centers. The
other recovers W(x) as a retract of the contractible homotopy fiber of pi.
An empty W(x) excludes every total extension lying over that boundary. A
noncontractible W(x) obstructs equivalence of this projection.

This is a RELATIVE statement over the retained boundary. A noncontractible fiber
does not imply that the total type has a larger cardinality or cannot be
abstractly equivalent to the base by some different map.

A finite hostile makes the distinction explicit: a two-point base with fiber
sizes zero and two has a two-point total space. The underlying sets are
abstractly equivalent, but the retained projection is constant onto one base
point and is not an equivalence. An arbitrary bijection would change which
boundary the records belong to.

This corrects any overly broad reading of 'noncontractible fibers generate a
new type': they obstruct equivalent RE-PRESENTATION BY THE DECLARED PROJECTION.
The earlier finite source-path examples separately establish genuine carrier
size changes under their own nonempty finite hypotheses.

## Native admission is a parameter, not a hidden conclusion

The new NativeAdmission module reuses the actual twelve-schema Rule and Resolve
families. Its interface has:

- a configuration x;
- a task type Tasks(x);
- an explicit source-policy predicate Admit(x,task,rule).

The complete extension evidence is

    Witness(x,task)
      = Sigma(r:Rule) [Admit(x,task,r) x Premises_S(r)],

where Premises_S(r) is the actual dependent family of native premise derivations.
The compiler returns (output(r),apply(r,premises)). Reification retains the full
configuration, selected task, rule, source-admission evidence, premises and
resulting native history, with exact recovery theorems.

This unifies task admission and application without pretending that coherence
selects the predicate Admit. No task enumerator, source-free rule selector or
universal automatic admission proof is introduced. Compatibility of an arbitrary
policy/compiler with source transport would still need its actual witnesses.

## The existing feedback loop is a checked instance

Instantiate the general family with:

    X = retained-feedback Total,
    W(c) = Questions(c),

using a universe lift for the small outgoing-edge fiber. The previously proved
whole-payload equivalence supplies the base comparison, and the seed's outgoing-
edge equivalences supply its witness comparisons.

The new applicationEquiv is obtained from the GENERIC dependent-extension theorem.
The concrete feedback interpreter realizes its square:

    move(realize(application))
      = realize(applicationEquiv(application)).

Applying the native history interpreter gives equality of the native complete
endpoints and retained Resolve histories as well. This binds the general theorem
to the working implementation rather than leaving it as unrelated abstraction.

## Conjecture status

The following general structural components are now checked:

1. compatible base/fiber transport of whole extensions;
2. identity/composition/associativity laws and lifting supplied comparison paths;
3. dependent extension reassociation and its naturality square;
4. precise relative projection-fiber classification;
5. explicit source-admission compilation with whole evidence recovery;
6. the retained feedback construction as a concrete native instance.

What remains conjectural is source determination of the admissible task policies
and their fully coherent closure under the intended constructors. The dependent-
sum theorem does not settle that substantive admission question. Neither does it
supply arbitrary higher fillers or a physical interpretation of recursive depth.

## Verification

    python research/strominger/checkers/check_coherent_dependent_extensions.py

Fresh headless Agda closure with `--ignore-interfaces` passes under Agda 2.8.0.1 /
Cubical 0.9. New modules use safe Cubical/guardedness, with no postulates or holes.
No unsupported indexed-match warning is introduced.

A negative control keeps the base identity but attempts to identify a Boolean
witness fiber with a unit fiber using an identity equivalence. The kernel rejects
it at the fiber type (exit 42). A base equivalence alone is not sufficient.

Finite regressions cover all 40 fiber-size profiles with up to three base points
and fiber sizes zero through two, 12 transport-composition cases, dependent
reassociation, and the equal-cardinality/non-equivalent-projection hostile.
These finite controls do not replace the general Agda theorems.

Artifacts:

- `agda/CoherentDependentExtensions.agda`
- `agda/CoherentExtensionNativeInstance.agda`
- `agda/negative/BadBaseOnlyExtensionComparison.agda`
- `checkers/check_coherent_dependent_extensions.py`
- `results/coherent-dependent-extensions.json`
- `results/coherent-dependent-extensions-positive.log`
- `results/coherent-dependent-extensions-negative.log`

Source hashes are stable across verification. Only Strominger-owned sources,
checkers and reports were edited; dependency interfaces may be refreshed by Agda.
No physical claim, graph publication, commit or push.
