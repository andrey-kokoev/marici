# Inertia cycle types carry a canonical ghost Frobenius system

Epistemic-graph event: 1382.

## Correct type

The power map on a nonabelian wreath-product automorphism group is generally
not a group homomorphism, so it is not an endofunctor of the original
labelled rig groupoid.  It becomes functorial on the inertia groupoid.

An inertia object is a pair `(X,sigma)` consisting of a finite labelled
component object and one automorphism.  A morphism conjugates `sigma`.  For
every positive intrinsic semiring element `n`, define

`F_n(X,sigma)=(X,sigma^n)`.

Conjugation commutes with powers, so this is a well-defined inertia
endofunctor.  It satisfies the strict composition law

`F_m composed F_n=F_(mn)`.

## Ghost coordinates

Project `sigma` to its permutation of the finite component set and define

`w_r(X,sigma)=|Fix(sigma^r)|`.

These fixed-point counts are invariant under conjugacy and are derived from
the finite component object.  They obey

`w_r(F_n(X,sigma))=w_(rn)(X,sigma)`.

Thus power endofunctors act on the ghost sequence by index shift.  For an
intrinsic prime element `p` of the conditional initial semiring, `F_p` is a
canonical prime-indexed operation.  Unlike the identity Adams operation on
`pi_0`, it is nontrivial: on a `p`-cycle, `F_p` turns the cycle into the
identity permutation.

## Strength and limitations

This is the first nontrivial Frobenius-composition system derived from the
conditional finite-component groupoid without choosing a numerical matrix.
It lives on inertia/cycle data, not on `pi_0` and not on norm homology.

However:

- the underlying `D4_ab` rig remains an algebraic quotient without shared
  physical authorization;
- `w_r` uses finite fixed-point readout, but no cohomological grading or
  alternating trace has been derived;
- the construction supplies dynamical cycle data, not yet closed points over
  finite fields; and
- no spectral weight `p^(-s)` or archimedean factor is present.

## Next determinant gate

For a finite permutation representation `V_X`, the standard exact identity

`exp(sum_(r>=1) w_r u^r/r)=det(1-u sigma | V_X)^(-1)`

can now be tested internally cycle by cycle.  This yields rational dynamical
Euler factors.  The remaining hostile question is whether any source rule
associates the intrinsic prime `p` to a typed inertia object without manually
choosing a `p`-cycle.

## Scope

No physical quotient, geometric Frobenius, arithmetic closed-point object,
or global Euler product is asserted.
