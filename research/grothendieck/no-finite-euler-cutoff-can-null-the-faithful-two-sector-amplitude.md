# No finite Euler cutoff can null the faithful two-sector amplitude

## Finite occupation amplitudes

For a finite prime cutoff \(X\), define

\[
F_X^+(z)=\prod_{p\leq X}\left(1-p^{-1/2}p^{-z}\right),
\qquad
F_X^-(z)=\prod_{p\leq X}\left(1-p^{-1/2}p^z\right)=F_X^+(-z).
\]

These are finite inverse-Euler amplitudes. No analytic continuation or zero
data enters their construction.

## Disjoint divisor walls

A plus factor vanishes precisely when

\[
z=-\frac12+\frac{2\pi ik}{\log p},
\]

and a minus factor vanishes precisely when

\[
z=\frac12+\frac{2\pi ik}{\log p}.
\]

Thus \(F_X^+\) and \(F_X^-\) cannot vanish at the same spectral point.

## Faithful quadratures

Define

\[
T_X=F_X^++F_X^-,
\qquad
A_X=F_X^+-F_X^-.
\]

If \(T_X=A_X=0\), linear reconstruction would give
\(F_X^+=F_X^-=0\), contradicting the disjoint walls. Hence

\[
(T_X(z),A_X(z))\neq(0,0)
\]

for every \(z\) and every finite cutoff.

## Seam norm

On \(z=it\),

\[
F_X^-(it)=\overline{F_X^+(it)},
\]

so

\[
|T_X(it)|^2+|-iA_X(it)|^2=4|F_X^+(it)|^2>0.
\]

The finite arithmetic relationship has a strict faithful norm on the seam.

## Where a new divisor can enter

No finite prime system creates a common null state. Any divisor not already
on the elementary walls must arise after the finite labelled substrate is
formed, through one or more of:

- infinite restricted-product completion;
- inversion from inverse-Euler determinant to zeta readout;
- archimedean augmentation;
- finite-part or determinant regularization;
- compression of the two quadratures to one scalar section.

Zeros of a completed scalar section are therefore not zeros already present
in finite Euler products.

## Deutsch–Popperian reformulation

The counterfactual task is narrower: construct an authorized completion that
starts from a nowhere-null finite two-quadrature system and produces an
off-seam scalar zero without violating source incidence.

A successful explanation would show that every authorized completion
preserves a nonzero complementary quadrature in both open sectors. A hostile
completion that creates an off-seam zero is the falsifier.

## Scope

This theorem concerns finite inverse-Euler amplitudes. It does not prove that
their infinite completion exists as a faithful pair or that the completed
Riemann section is their direct determinant.

## Result

At every finite prime cutoff, the two sectoral occupation amplitudes have
disjoint divisor walls and their faithful quadratures never vanish together.
The unresolved RH mechanism is entirely a completion, augmentation,
inversion, or projection phenomenon.
