# Full history changes the scope of the Clark Jordan test

## New source

`research/grothendieck/full-universal-history-from-ordered-closure-and-compatible-jets.md` constructs the degree-completed history H(V)=product_r V^(tensor r), with compatible finite quotients, universal filtered evaluation, comparison inverses, and deconcatenation.

This supplies one all-order algebraic object. The four-jet history used in our finite calculations is its quotient, not the full comparison algebra.

## The three-dimensional Jordan subspace belongs to the four-jet quotient

For the actual two orders (2,3) and (3,2), let d=S_(2,3)^(-1)S_(3,2)-1. Its leading degree-two part is

    d_2 = -e_0 e_1 + e_1 e_2 + e_1 e_3.

In the four-jet quotient d^3=0. In the full history d^3 is nonzero: its leading degree-six part is d_2^(tensor 3), and the coefficient of the word (0,1,0,1,0,1) is -1. This was freshly verified through order six using the prior `universal_history.py` implementation and the actual arithmetic windows.

More generally d^k has nonzero leading degree 2k. Thus right multiplication by 1+d does not preserve span(1,d,d^2) in the full history:

    d^2(1+d)=d^2+d^3.

The finite Jordan invariant-form equations therefore apply to a form on the four-jet quotient, or a form proved to descend there. They are not necessary equations for the unrestricted three-vector restriction of a full-history invariant form. Contributions involving d^3 and higher enter the full invariance identities.

In particular, the previous proposed nonzero scalar L=Q(1,d^2), with the associated three-dimensional invariant matrix, is a finite-quotient comparison target. It is not the sole governing test for the all-order Clark realization.

## A separate topological constraint

The full formal degree topology supplies no faithful continuous Hilbert norm. Every basic neighborhood of zero contains an entire high-degree subspace F^N, including every scalar multiple of each of its vectors. If a norm were continuous at zero, one such neighborhood would lie in its unit ball. Scaling forces that norm to vanish on F^N.

The same argument applies to a jointly continuous sesquilinear scalar form q. Continuity at (0,0) gives neighborhoods U,V on which |q| is bounded. Since U contains F^N, scaling its vectors forces q(F^N,V)=0. The neighborhood V is absorbing under scalar multiplication, so q(F^N,H)=0. Likewise some F^M lies in the right radical. Such a form factors through a finite jet on each side.

Consequently a faithful analytical realization of all history coefficients requires an analytical topology or a growth-restricted subalgebra different from the unrestricted formal degree completion. Formal filtered universality alone does not construct a bounded Clark realization.

## Corrected comparison plan

There are two distinct tasks:

1. Finite packet: compare the already defined four-jet observer, with any explicitly required metric descent. The exact Jordan and fixed-port obstructions remain valid at this strength.
2. Full history: specify a complete filtered analytical receiver and its chamber map, prove convergence/continuity in its actual topology, and only then test its Green form. The universal theorem transports all compositions and inverse jets once that receiver is supplied.

The native terminal Clark cut receiver remains a potentially order-forgetting evaluation; the full universal source preserves information even when a receiver discards it. That receiver audit must not be confused with a claim that the universal history itself collapses.

The all-order formal adjoint, if comparison units are required to be isometric, has d^*=(1+d)^(-1)-1=-d+d^2-d^3+..., whose four-jet projection gives the earlier formula. Its analytical realization needs a convergence or functional-calculus statement in the chosen receiver.

## Verification scope

The nonzero degree-six coefficient and its zero four-jet projection were checked with exact integer arithmetic. The topology argument and all-order leading-degree statement are proofs above. No analytical Clark receiver or full-history Green metric is claimed by this note.
