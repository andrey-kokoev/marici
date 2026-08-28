# Completion B Is Generically Fully Massable with the Declared Spinor Higgs

## Exact Clifford realization

Use Pauli matrices to realize the Euclidean Clifford algebra on the complex
Spin(5) spinor:

\[
\Gamma_1=\sigma_1\otimes\sigma_1,
\quad \Gamma_2=\sigma_2\otimes\sigma_1,
\quad \Gamma_3=\sigma_3\otimes\sigma_1,
\quad \Gamma_4=I\otimes\sigma_2,
\quad \Gamma_5=I\otimes\sigma_3.
\]

They obey \(\{\Gamma_a,\Gamma_b\}=2\delta_{ab}I_4\). The antisymmetric
Spin(5)-invariant form

\[
C=\begin{pmatrix}
0&0&1&0\\
0&0&0&-1\\
-1&0&0&0\\
0&1&0&0
\end{pmatrix}
\]

satisfies \(\Gamma_a^TC=C\Gamma_a\). For the complex spinor-Higgs vacuum
\(\phi\), its pseudoreal conjugate carrier is

\[
\widetilde\phi=C\phi^*.
\]

Define the exact intertwiners

\[
B(\phi)=
\begin{pmatrix}
C\Gamma_1\phi&\cdots&C\Gamma_5\phi
\end{pmatrix},
\qquad q(\phi)=C\phi.
\]

## Completion-B mass operator

Order the sixteen Weyl components as

\[
(S_4,V_5,X_4,n_0,n_1,n_2).
\]

Insert the six WP886 couplings as symmetric off-diagonal blocks:

\[
\begin{aligned}
SV\Phi &: y_1B(\phi), &
XV\Phi^* &: y_2B(\widetilde\phi),\\
Sn_0\Phi^* &: y_3q(\widetilde\phi), &
Sn_1\Phi &: y_4q(\phi),\\
Xn_1\Phi^* &: y_5q(\widetilde\phi), &
Xn_2\Phi &: y_6q(\phi).
\end{aligned}
\]

This defines an exact \(16\times16\) component mass matrix
\(\mathcal M_B(\phi,y_1,\ldots,y_6)\).

## Generic-rank certificate

At the exact witness

\[
\phi=(1,2,3,5)^T,
\qquad (y_1,\ldots,y_6)=(2,3,5,7,11,13),
\]

the determinant is

\[
\det\mathcal M_B=468887390507036217600\ne0.
\]

The determinant is a polynomial in the vacuum components and Yukawa
coefficients. One nonzero witness proves that full rank sixteen holds on a
nonempty Zariski-open parameter set. Completion B therefore needs no extra
scalar representation merely to make all sixteen one-family Weyl components
massive.

## What remains unselected

Full generic rank is not a numerical prediction. The six Yukawa coefficients
and the norm and orientation of the spinor-Higgs vacuum remain source
parameters. The zero-Yukawa locus has rank zero, and determinant-zero
hypersurfaces separate other rank-deficient cases. Anomaly cancellation and
massability do not choose a point away from them or fix the mass eigenvalues.

The calculation also does not yet include three-family Yukawa matrices,
finite widths, RG evolution, or detector resolution. Those enlarge the
parameter domain rather than supplying selection authority.

## Verdict

WP885's Completion-B mass-constructor gate is repaired: the declared spinor
Higgs suffices for generic full component rank. The completion fiber remains,
because both A and B are now massable and neither has source-fixed mass
parameters. This is a massability theorem and threshold-definition repair,
not a flavor selector.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp887_spin5_completion_b_component_mass_rank.py
~~~
