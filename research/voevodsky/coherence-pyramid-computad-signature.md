# Coherence-pyramid computad signature

## Question

What is the smallest typed generator signature that represents the validated boundary of the Marici coherence pyramid without asserting unavailable composition or coherence laws?

## Claim boundary

This packet defines object, arrow, certificate, and 2-cell sorts. It is a computad signature, not yet a double category: composition constructors, associators, unitors, interchange, Beck–Chevalley invertibility, and completion functoriality remain separate research leaves.

## Object sorts

The signature separates five objects:

1. carriers with typed ports and source provenance;
2. finite Green objects with form and declared radical;
3. gauge presentations with kernel, quotient base, and quotient map;
4. closed forms with ambient space, dense domain, and radical;
5. completed quotient-form objects with coercivity data.

This prevents a finite positive Gram matrix from being silently identified with a closed quotient form.

## Variance-tagged generators

- `under_embedding` represents form-preserving Green inclusions.
- `over_quotient` represents kernel-typed gauge projections.
- `vertical_restriction` represents source-compatible base maps.
- `closed_form_comparison` represents form-domain isometries after radical descent.

No generator changes variance by coercion.

## Certificate sorts

- joint amalgamation retains the full cross pairing and joint positivity;
- pullback exactness retains the fiber product and transported kernel;
- completion retains common-core, closure, radical, coercivity, and minimum-modulus evidence;
- mixed squares retain boundary typing, commutation, and certificate transport.

## Two-dimensional generators

The initial cells express form preservation, kernel compatibility, candidate Beck–Chevalley comparison, and compatibility between finite restriction and closed comparison. Calling the Beck–Chevalley cell a candidate is deliberate: invertibility must be independently certified.

## Strongest falsification encoding

The signature refuses constructors corresponding to known counterexamples:

- coordinate projection without form preservation;
- quotient without identified kernel;
- unrestricted Green pushout;
- pairwise amalgamation without joint completion;
- closed-form identity inferred from dense-core equality;
- completion without radical and coercivity control.

The checker verifies that every generator references declared sorts, each variance class is explicit, required certificate families are present, and refusal rules cover the six established hostile classes.

## Disposition

The signature leaf is resolved at the generator level. The result is machine-readable at `research/voevodsky/coherence-pyramid-computad-signature.json`. It does not establish a category. The next dependency is the completion interface, followed by partial composition and coherence laws.

## Verification

- `research/voevodsky/coherence-pyramid-computad-signature.json`
- `research/voevodsky/checkers/check_coherence_pyramid_computad_signature.py`
- `research/voevodsky/results/coherence_pyramid_computad_signature.json`
