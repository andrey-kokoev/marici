# Orientation is retained readout data, not a dispensable sign

## Fresh source evidence

The recovered physical pullback in ledger436 has primitive integral H1=L_plus, with rotation trivial and loaded reflection even: road orientation(-1) times polarity(-1) gives+1. RS2's Tate coefficient T_minus=Z/3 instead has rotation trivial and reflection-1. Read Nima's `polarity-orientation-twist.md`: it already distinguishes a character-level repair from a physically identified orientation line and generator comparison.

Here we test the declared common D3 action. The result does not assert that the project requires an identification of these differently typed readouts.

## The untwisted comparison is algebraically forbidden

For a D3-equivariant additive map f:L_plus->T_minus, put a=f(1). Reflection requires

    a=f(s1)=s f(1)=-a.

Thus2a=0 in Z/3, so a=0. Therefore

    Hom_D3(L_plus,T_minus)=0.

This is stronger than a failed rank test and independent of any analytic completion. Both rotations act trivially, so relabelling a reflection by a rotation does not change the obstruction.

The raw reduction n->n mod3 used in the previous finite-packet control is nonzero as an abelian-group map, but is NOT this equivariant comparison. No contradiction: that control did not supply a Tate/orientation identification.

## What a twist supplies, and what it does not

Let E_minus be an integral reflection-odd line with trivial rotation. Then

    Hom_D3(L_plus tensor E_minus,T_minus)=Z/3.

Equivalently the even source may map to T_minus tensor E_minus. There are two nonzero maps, not a uniquely selected normalized bridge. The reflection-odd character is the unique one-dimensional integral D3 character correcting the mismatch, but character matching alone supplies neither a geometric line comparison nor a canonical nonzero morphism.

The source's polarity factor is a candidate place to look for E_minus. Its known reflection sign is evidence for the character, not permission to discard that factor from the physical object. Source framings, supported geometry, normalization and transport must authorize any identification.

One can display the mathematical relative readout as

    r(n tensor e)=n e mod3.

If e is retained as an odd orientation coordinate, reflection sends e to-e and the reading transforms correctly. Fixing e=1 and then forgetting how that frame transforms recreates the original non-equivariant scalar map. This illustrates an orientation-decorated observation, not a newly admitted physical measurement.

## A separate obstruction survives the twist

The scalar trace of the existing physical packet is -3n times its retained coefficient beta. Reducing its integer coefficient mod3 gives zero. Multiplying by an orientation unit cannot change that. Thus correcting a character mismatch does not repair the information already lost by scalar trace followed by reduction.

There are two distinct operations to audit:

1. forget/change the orientation representation;
2. collapse the packet to a scalar divisible by3 and reduce.

Neither may be hidden in a claim that the objects have the same rank or torsion order.

## Refinement of the readout contract

Source actions and orientation/local-system labels belong to the declared types of V,Y,Z. Comparisons and intended readouts must respect them. In an equivariant setting, fiber constancy gives an equivariant factor only when F and O themselves are equivariant. A unique set-level factorization cannot certify an incorrectly typed physical comparison.

For derived or supported objects the same rule requires actual action/coherence witnesses; the finite character test is only a necessary gate. No topology can repair the zero-Hom obstruction while preserving the declared algebraic actions.

## Programme interpretation

The contract has now distinguished:

- a valid integral odd-to-odd Tate coefficient bridge;
- a realized even physical line with a diagonal compatible packet;
- a forbidden untwisted even-to-odd comparison;
- a character-compatible but not yet source-authorized twisted comparison;
- a separate scalar-forgetting loss that a sign twist cannot undo.

This is useful structural synthesis, not a reason to force an additional physical identification. A common calculus may contain both coefficient types and precisely delimit maps between them.

Next consolidate the spectral and integral examples into a source-indexed comparison diagram, marking proved, forbidden and source-conditional arrows. Do not build another local model merely to eliminate a typed obstruction that the common calculus can legitimately retain.

## Verification

`check_readout_orientation.py` extracts the source character data, enumerates the equivariant maps and twists modulo3, checks that reflection relabelling does not help, and verifies the independent scalar-trace loss. These are exact representation controls, not a construction of a physical orientation line.
