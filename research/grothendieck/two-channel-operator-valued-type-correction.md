# The two-channel square must be operator-valued, not four scalar traces

The two-channel determinant `ad-bc` is the smallest local interference cell,
but it cannot be interpreted as four global scalar explicit-formula
channels.

For a finite conjugation-stable divisor truncation `D` of size `N`, exact
conjugation matching is the permutation matrix

```
G_(rho,sigma)=1 if sigma=conjugate(rho), else 0.        (1)
```

It has rank `N`. Any expression using `m` separable scalar channels,

```
G_(rho,sigma)=sum_(k=1)^m f_k(rho)g_k(sigma),           (2)
```

has rank at most `m`. Hence exact matching requires `m>=N`. In particular,
four scalar entries arranged into one numerical `2x2` square do not realize
the graph correspondence for arbitrarily large windows.

This does not destroy the two-channel mechanism. It corrects its type. The
matrix must be

```
Q(T) in M_2(A),                                        (3)
```

where `A` is an operator algebra or correspondence category retaining the
unbounded internal label space. Equivalently, the scalar four-cycle is a
local cell repeated fiberwise, and scalarization occurs only after an
operator determinant, trace, or torsion construction.

## Why the spectral copy map is not the construction

On the zero-divisor Hilbert space, the conjugation copy map supplies the
required full-rank graph projector exactly. But it is defined from the Xi
zeros and their atomic basis. Using it to define the entries of `Q` would be
spectrally tautological. The source problem is to construct an analogous
dagger-Frobenius/copy correspondence from arithmetic or topology, then prove
that its scalarized determinant agrees with Xi.

The paired coefficient--Betti Mackey object has the right categorical shape:
pullback and transfer are adjoint, and difference incidence is Fourier-dual
to spectral copying in finite abelian models. Yet no admitted infinite
arithmetic Fourier equivalence identifies that source correspondence with
the Xi divisor graph.

## Revised architecture

The surviving form is therefore

```
Q_P(T) = [A_P(T) B_P(T); C_P(T) D_P(T)]                (4)
```

on two polarizations of a cutoff correspondence module `H_P`. Its two
matching composites are operators

```
A_P D_P  and  B_P C_P,                                 (5)
```

and their noncommutative difference is scalarized only through a
determinant-class construction. The finite cutoff rank must grow with the
arithmetic window; a fixed rank-two numerical matrix is insufficient.

For noncommuting entries, the scalar formula `ad-bc` is not automatically a
well-defined determinant. A valid proposal must specify the determinant
notion—ordinary determinant after finite realization, Fredholm determinant,
graded torsion, or another source-defined scalarization—and prove cyclicity
and cutoff compatibility rather than assuming them.

## Falsifiers

A proposal fails if:

1. it replaces the graph projector by finitely many separable scalar traces;
2. its internal rank stays bounded while the divisor/source window grows;
3. it uses the Xi zero basis to define the source copy map;
4. it writes `AD-BC` for noncommuting operators without defining a valid
   scalar determinant or torsion;
5. scalarization occurs before prime--archimedean interference.

The next constructive target is a finite-cutoff operator-valued square built
from source incidence, with growing internal rank and a compatible
determinant-line scalarization. This is a type theorem and rank no-go, not an
Xi operator or RH proof.
