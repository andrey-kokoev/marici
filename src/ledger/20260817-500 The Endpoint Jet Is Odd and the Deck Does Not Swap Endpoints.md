# Entry 500 — The Endpoint Jet Is Odd and the Deck Does Not Swap Endpoints

Entries 497--499 used the wrong action of the mechanical deck involution.
The orbit-completion checker defines

\[
\rho(a)=-a,
\qquad
\rho(b)=b,
\qquad
\rho(u)=u.
\]

In particular,

\[
L_1=b+1-u
\]

is fixed.  Orbit conjugation exchanges \(L_2^-\) and \(L_2^+\); it does not
replace \(b+1\) by \(1-b\), and it does not exchange the endpoints
\(b=\pm1\).

## Correct character

Naturality of the three-gradient Koszul differential gives

\[
\rho(e_a)=-e_a,
\qquad
\rho(e_u)=e_u,
\]

because \(K_a\) is odd and \(K_u\) is even.  Therefore both representatives
constructed in Entries 495--496 are anti-invariant:

\[
\rho(a^3e_u)=-a^3e_u,
\qquad
\rho(a^2e_a)=-a^2e_a.
\]

Thus

\[
\boxed{
\text{the derived }u\text{-Bockstein and its endpoint normal derivative lie
in the minus character.}
}
\]

## Corrections to Entries 497--499

- Entry 497's claim that deck orientation combines the two endpoints into
  one invariant line is false; the deck fixes each endpoint.
- Entry 498's \(1-b\) conjugate chart is not supplied by orbit completion;
  both lattices retain the same \(L_1=b+1-u\) factor.
- Entry 499's addition of this class to the plus target degree is therefore
  unjustified.  Its arithmetic rank repair is conditional and does not
  identify the plus defect.

The algebraic results of Entries 493--496 remain valid after retyping: the
deformation gradient is necessary, ordinary \(u=0\) specialization loses the
\(a^3\) socle, the \(u\)-Bockstein restores it generically, and that class
vanishes on ordinary endpoint fibers.  These facts now belong to the odd
comparison, where they may interact with the established \(D-2\) defect.

## Consequence

The invariant defect of Entry 473 is again unresolved.  It cannot be
identified with the odd socle Bockstein.  The even conormal module
\(I/I^2\cong R\) has several Cartier layers; selecting the odd top layer was
the source of the character mismatch.  The plus comparison must instead
track the even layers \(1,a^2\) through the derived specialization.

## Next gate

Repeat the Euler specialization calculation on the even conormal generators
\(1\) and \(a^2\), keeping their images as a two-generator filtered module.
Determine which even combination, if any, produces the single plus defect
without borrowing the odd \(a^3\) Bockstein.

The mechanical character audit is
`research/voevodsky/check_soft_axis_endpoint_character_correction.py`.
