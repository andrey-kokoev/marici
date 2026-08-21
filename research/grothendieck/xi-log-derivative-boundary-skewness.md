# Reflection forces zero real boundary data for the Carathéodory target

## Boundary theorem

Let `L(s)=xi'(s)/xi(s)`. The functional equation and real structure give

`L(1-s)=-L(s)`,

and

`L(conjugate(s))=conjugate(L(s))`.

On the critical boundary `s=1/2+it`, reflection is complex conjugation.
Therefore, wherever `xi(s)` is nonzero,

`conjugate(L(s))=-L(s)`,

so

`Re L(1/2+it)=0`.

The completed logarithmic derivative is automatically tangent to the
imaginary axis on the critical boundary.

## Half-plane interpretation

The desired Carathéodory property is

`Re L(s)>=0` for `Re(s)>1/2`.

Its boundary value is already forced to zero. Away from zeros, `Re L` is
harmonic. The completed asymptotics give the positive orientation far to the
right. Thus an off-line zero is precisely an interior pole obstructing the
positive harmonic extension.

With appropriate unbounded-domain estimates, the maximum-principle picture
recovers the equivalence:

- no zeros in the open right critical half-plane permits the positive-real
  extension;
- a zero there creates a pole and destroys analyticity of any
  Carathéodory function;
- functional reflection then treats the left half-plane.

## Deutschian audit

This clarifies what has and has not been explained.

Explained:

- why the critical line is the boundary of the positive-real domain;
- why the boundary value is skew/self-adjoint rather than arbitrary;
- why the Möbius phase becomes unitary there;
- why Toeplitz positivity, Li positivity, and Hilbert--Pólya unitarity are
  the same compatibility condition.

Not explained:

- why arithmetic forbids interior poles.

Therefore the Carathéodory reformulation is a rigid unification, not a
shortcut around RH. A successful source proof must establish pole-freeness or
positive-realness by an arithmetic mechanism that does not presuppose the
zero divisor.

## Next attack

Seek an arithmetic Loewner/Herglotz representation for `L` in the right
critical half-plane whose representing measure is positive before zeros are
located. Failure to construct such a representation is the current central
falsifier.
