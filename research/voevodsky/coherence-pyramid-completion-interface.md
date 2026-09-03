# Finite-to-closed-form completion interface

## Question

How can the coherence-pyramid computad admit completion of finite Green systems without promoting finite positivity into an unsupported closed-form theorem?

## Claim boundary

This packet defines a partial constructor interface and executable admission logic. It does not construct Mosco convergence, a strong-resolvent limit, or the radial comparison map for the Stieltjes sector.

## Constructor

`complete_finite_form_system` accepts three typed inputs:

1. a finite diagram with restriction maps and form-preservation cells;
2. an independently defined candidate limit form on a dense common core;
3. comparison maps from finite objects into that candidate.

The constructor is partial. Missing analytic evidence is refusal, not an object with weakened semantics.

## Certificate decomposition

The admission certificate keeps six independent families:

- source independence excludes fitting the limit or comparison to the desired conclusion;
- domain data prove density, closability, closure-domain identity, and core invariance;
- convergence data provide Mosco or strong-resolvent control and positivity of the closed limit;
- radical data identify finite and limiting radicals and prove quotient descent;
- coercivity data give strictly positive quotient coercivity and reduced minimum modulus;
- coherence data compare restriction with completion.

These families are not interchangeable. Core equality does not imply closure; finite positivity does not imply radical stability; dense range does not imply quotient coercivity.

## Output

Successful admission returns:

- a closed-form object;
- its completed radical quotient with coercivity bound;
- cells from finite restrictions into the completion and through radical descent.

It does not return a general functor. Composition compatibility, associativity, Beck–Chevalley, and uniqueness are deferred to later leaves.

## Falsification suite

The checker validates one complete exact fixture and mutates it into six hostile fixtures:

1. negative closed limit;
2. domain escape;
3. new limiting radical;
4. quotient coercivity loss;
5. reduced-minimum-modulus collapse;
6. circular comparison.

Each hostile fixture is refused for its first typed defect. This turns the earlier analytic counterexamples into constructor-level behavior.

## Disposition

The completion-interface leaf is resolved as a typed partial constructor. The interface is compatible with the computad signature but does not yet compose. The next leaf is partial horizontal and vertical composition; it must specify how completion certificates are transported across composites.

## Verification

- `research/voevodsky/coherence-pyramid-completion-interface.json`
- `research/voevodsky/checkers/check_coherence_pyramid_completion_interface.py`
- `research/voevodsky/results/coherence_pyramid_completion_interface.json`
- `research/voevodsky/unbounded-r-zeta-identity-typing-audit.md`
