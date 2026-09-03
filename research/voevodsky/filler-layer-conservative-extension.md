# Filler layer as a conservative extension

## Question

Does adding filler fibers and selections impose new equations on the original five-sort computad?

## Claim boundary

The result concerns the finite declared signature under many-sorted partial-algebra semantics with empty extension sorts permitted. It does not prove a model-category or unbounded homotopical universal property.

## Forgetful projection

Let \(U\) discard the four extension sorts and every incident extension symbol. It preserves the five base sorts, four one-generators, six cell classes, and five laws identically.

## Empty expansion

Every base model has an expansion \(E_0\) interpreting boundary data, fillers, relative classes, and completed fillers as empty, with all extension constructors empty partial maps. Therefore

\[
U E_0=\operatorname{id}.
\]

No new equation between base terms can be forced by the extension: any such equation would have to hold in every empty expansion and hence already hold in the underlying base model.

## Inhabited fixture

A second finite fixture adds one boundary datum, two distinct fillers, and one shared relative class. Forgetting this inhabited extension returns exactly the same base model. Thus representative multiplicity changes no base operation or law.

## Relative universal property

For a fixed base model and specified chain/filler data satisfying the layer laws, interpretations of the extended signature are precisely law-preserving realizations of those data. This property is relative to supplied extension data; the extension does not manufacture them.

## Disposition

The filler layer is a conservative finite-signature extension of the coherence-pyramid computad. It adds expressive power without strengthening old equations. Stronger homotopical universality remains unclaimed.

## Verification

- `research/voevodsky/filler-layer-conservative-extension-contract-v1.json`
- `research/voevodsky/checkers/check_filler_layer_conservative_extension.py`
- `research/voevodsky/results/filler_layer_conservative_extension.json`
