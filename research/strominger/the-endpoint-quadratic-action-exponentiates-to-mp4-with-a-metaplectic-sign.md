# The Endpoint Quadratic Action Exponentiates to Mp4 with a Metaplectic Sign

## Real form from the source dagger

On the Bargmann-compatible smooth endpoint domain,

\[
E_{ij}^\dagger=-F_{ij},
\qquad
H_{ij}^\dagger=H_{ji}.
\]

The source dagger therefore selects ten skew-symmetric real generators.
For each of the three symmetric index pairs, take

\[
E_{ij}+F_{ij}
\qquad\text{and}\qquad
i(E_{ij}-F_{ij}).
\]

These supply six generators. The degree-preserving block contributes

\[
iH_{11},\quad iH_{22},\quad
H_{12}-H_{21},\quad i(H_{12}+H_{21}),
\]

for a total of ten. They form the real symplectic Lie algebra
\(\mathfrak{sp}(4,\mathbb R)\).

## Mathematical exponentiation

The smooth \(D\)-domain from the first-order factorization contains the
finite-particle core. Those vectors are analytic for all quadratic generators.
The analytic-vector integration theorem therefore exponentiates the real Lie
algebra representation to a unitary representation of the simply connected
cover. The oscillator relations identify its minimal global group as the
metaplectic double cover

\[
Mp(4,\mathbb R)\longrightarrow Sp(4,\mathbb R).
\]

## Exact sign obstruction

Consider rotation in the \(u\) canonical plane. Its oscillator Hamiltonian is

\[
H_u=u\partial_u+\frac12.
\]

On \(u^nv^r\),

\[
e^{-i\theta H_u}
=
e^{-i\theta(n+1/2)}.
\]

At \(\theta=2\pi\), this is

\[
e^{-2\pi i(n+1/2)}=-1
\]

for every \(n\). Yet a \(2\pi\) rotation is the identity in the classical
symplectic group. At \(4\pi\), the quantum action returns to \(+1\).

Therefore the endpoint representation does not descend to an honest unitary
representation of \(Sp(4,\mathbb R)\). The metaplectic sign is an unavoidable
global coherence class.

## Meaning for the tower programme

The local Lie algebra closes strictly, its common analytic domain is derived,
and its real form exponentiates. Nevertheless global composition remembers one
additional binary datum. This is the first genuine global anomaly in the
endpoint control tower:

```text
local quadratic controls: sp(4,R)
global executable mathematical group: Mp(4,R)
forgotten datum under projection to Sp(4,R): metaplectic sign
```

The sign is not a numerical normalization and cannot be removed by vertex
rescaling. It is the holonomy of a noncontractible loop in the classical
control group.

## Remaining physical authority

Mathematical exponentiation is now constructed. Physical execution remains a
separate question. A source instrument must declare which one-parameter
metaplectic groups are admissible, how the central sign is observed or
quotiented, and how boundary-support restrictions transform.

Treating the representation as an ordinary linear \(Sp(4,\mathbb R)\) action
would erase a carrier-level lift datum. This does not by itself make the sign
observable: projective rays and internal adjoint readouts both quotient it.
Operational visibility requires an independently authorized coherent reference
sector and a cross-sector observation port.

## Relation to RH

The metaplectic sign is a global operator-topology effect, but it does not
orient Grothendieck's infinite-dimensional conormal current. It supplies no
finite-jet route around the global RH obstruction.

## Evidence replay

The checker verifies the ten skew-adjoint real generators, double-cover sign,
four-pi return, parity independence, and analytic-vector radius through degree
two hundred.

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/endpoint_mp4_exponentiation_and_sign_checks.py
```

Machine-readable results are written to
`research/strominger/results/endpoint_mp4_exponentiation_and_sign_checks.json`.
