# The CCM semilocal scaling quotient stops before the Xi determinant

Sequence claim: `seqclaim-4ba8ad8af7897580aca929e3` (1398).

Epistemic-graph event: 1443.

## Source audited

Alain Connes, Caterina Consani, and Henri Moscovici, *Zeta zeros and prolate
wave operators* (2024):
https://alainconnes.org/wp-content/uploads/Zeta-zeros-and-prolateproofs-final-2024.pdf

This is the closest published construction found so far to our proposed
Weil-radical/scaling quotient.  The comparison below separates what the paper
actually proves from the additional operator and determinant claims needed in
our lane.

## What is genuinely obtained

At the archimedean place the source map is

`E(f)(u)=u^(1/2) sum_(n>=1) f(nu)`.

The paper identifies its range with the radical mechanism for the Weil form.
Under the multiplicative Fourier transform, specially constructed Hermite
combinations satisfy (Proposition 3.6)

`F_mu(E(psi_j^+/-))(s)=R_j^+/-(s) Xi(s)`.

Consequently, multiplication by `s` on the quotient of the Hadamard
topological ring `H_<=1` by the closure of their span has spectrum precisely
the nontrivial zeta zeros (with `1/2+is` the zeta variable).

This result is not made circular by the preceding display of Xi's Hadamard
product.  The polynomials `R_j^+/-` come from explicit Hermite combinations;
the proposition then uses the independently known factorization through Xi.
It is a valid algebraic/topological spectral quotient.

For a finite set `S` of places containing infinity, Proposition 4.1 proves

`F_mu(E_S(f))(s) = product_(p in S\{infinity}) L_p(1/2-is)
                   F_mu(w_infinity f)(s)`.

Theorem 1 supplies a canonical Hilbert realization of the semilocal scaling
cyclic pair and a spectral measure proportional to the squared absolute value
of this finite product of local factors.  Thus the finite-place arithmetic is
source-derived and exact.

## Why this does not close our operator gate

The following objects must not be conflated:

1. The self-adjoint scaling operator exists on the unquotiented semilocal
   Hilbert space and becomes multiplication by the real spectral variable.
2. Proposition 3.6's exact zero spectrum is on a quotient of the topological
   ring of entire functions, not a Hilbert quotient equipped with a proved
   self-adjoint realization.
3. The prolate construction conditions the scaling operator and reproduces
   low-lying/infrared zeros in a limiting regime.  The introduction states the
   zero relation as the action on a quotient when `lambda -> infinity`, while
   presenting the semilocal program as a strategy joining infrared and
   ultraviolet evidence.
4. Every semilocal `S` in the theorem is finite.  Its measure contains only a
   finite product of local Euler factors, not the completed global Xi.
5. The paper contains no Fredholm, zeta-regularized, or modified determinant
   identity equating a determinant of the quotient operator to Xi.

Therefore it does not produce a single cutoff-independent self-adjoint
compact-resolvent operator `A` for which

`det_2(I-z A^(-1))=Xi(z)/Xi(0)`.

Nor does it prove positivity of every finite-prime Weil form `Q_n`; the paper
opens by recalling that the conjunction of these properties is equivalent to
RH and offers the semilocal trace formula as the Hilbert framework in which to
attack them.

## Theorem-level audit

**CCM compatibility theorem.**  The archimedean CCM map `E` realizes the same
global radical-quotient architecture isolated in Ledgers 1395--1397, and its
semilocal extension supplies exact finite-place Euler multipliers and a
self-adjoint ambient scaling generator.  It therefore validates the
provenance of the Weil boundary preshape.

**CCM insufficiency theorem.**  The results cited above do not imply a fixed
self-adjoint compact-resolvent quotient operator with completed-Xi
determinant.  Exact zero recovery occurs in an entire-function quotient;
Hilbert self-adjointness occurs for the ambient finite-place scaling pair; and
the prolate spectral comparison is limiting.  No cited theorem identifies all
three structures on one operator.

## Smallest falsifier for an overclaim

Take `S={infinity,p}`.  The canonical semilocal spectral density is

`|L_infinity(1/2-is)L_p(1/2-is)|^2 ds`.

Changing an omitted prime `q != p` leaves this Hilbert pair unchanged, whereas
completed Xi changes by the nonconstant factor `L_q(1/2-is)`.  Hence no fixed
finite-`S` determinant can equal completed Xi.  Any claimed passage must add a
controlled `S -> all places` limit and prove preservation of domain,
self-adjointness, compact resolvent, and determinant convergence.  Those are
exactly the missing gates.

## Physical provenance

The construction is adelic/analytic.  It does not supply the unavailable
physical relative-chain pushforward from the coefficient--Betti system.
Accordingly it strengthens the analytic source lane without altering the
separate physical-readout audit.

## Next attack

Use the finite-`S` Weil forms as a directed family of indefinite boundary
forms.  Determine whether their radicals and conditioned scaling resolvents
admit a canonical limit before assuming positivity.  A successful limit must
either prove Pick positivity or expose a persistent negative direction; only
after that should the conditional determinant theorem of Ledger 1382 be
attached.
