# Local D03 Exit Class and the Generic-Q Kernel Criterion

## Record

Date: 2026-08-14

Status: proved for the finite local exit complex, its reciprocal occurrence
dual-line normalization, and the kernel-level generic-support no-go. The
global logarithmic Beck--Chevalley map remains unconstructed.

## Claim

Let

\[
A=\widetilde F_2,
\qquad Z=\widetilde F_1,
\qquad Q=A/Z
\]

for the corrected integral blowup of entry 107. The ambient pair-Rees
deformation retains the seven-generator relative quotient \(Q\), and its
strict \(D03\) exit block has raw occurrence attachment \(X_{03}\). After
the integral occurrence and normal contractions, the local comparison
complex is

\[
\boxed{
C_{03}^{\rm exit}
=
[R\xrightarrow{U_{03}}R],
\qquad
H^0=0,
\qquad
H^1=R/(U_{03}).
}
\]

The reciprocal occurrence operation is an evaluation of invertible
rank-one modules, not localization of the base ring. Put

\[
I_X=(X_{03})\subset R,
\qquad
I_X^\vee=\operatorname{Hom}_R(I_X,R).
\]

Since \(I_X\) is free with chosen geometric generator \(X_{03}\), its dual
generator obeys

\[
\operatorname{ev}(X_{03}^\vee\otimes X_{03})=1.
\]

Thus the raw class \([X_{03}]\) has the canonical occurrence-normalized
local value

\[
\boxed{[1]\in H^1(C_{03}^{\rm exit})=R/(U_{03})}
\]

without adjoining \(X_{03}^{-1}\) to \(R\). The one localization
suspension is essential: the nonzero class is in \(H^1\), not in the
vanishing ordinary \(H^0\).

This local class does not yet receive the global Yoneda class. The necessary
kernel criterion is the following. For any Rees, deformation-to-the-normal-
cone, or nearby-cycle source kernel \(\mathscr K\), a boundary-crossing
specialization can be nonzero only if

\[
\boxed{
\mathscr K_\eta
\longrightarrow
A\otimes R[\mathbf t^{\pm1}]
\longrightarrow
Q\otimes R[\mathbf t^{\pm1}]
\quad\text{is nonzero}.
}
\]

The generic fiber of the particular kernel must meet \(Q\). It is not
enough that the ambient pair-Rees deformation contains \(Q\).

For the expanded marked gallery, the seven supports are

\[
\begin{gathered}
\{x_1,x_3,x_5\},\quad
\{x_1,x_3\},\quad
\{E,x_1,x_3\},\quad
\{E,x_3\},\\
\{E,D03,x_3\},\quad
\{D03,x_3\},\quad
\{D03,x_0,x_3\}.
\end{gathered}
\]

Every one belongs to \(Z=\widetilde F_1\). Consequently the canonical
gallery Rees or multi-Rees kernel satisfies

\[
\boxed{
\mathscr K_{G,\eta}\longrightarrow Q[\mathbf t^{\pm1}]=0.
}
\]

It retains the expanded carrier

\[
\widetilde\xi
=x_1e_c+X_{03}x_1h_E+X_{03}e_r,
\qquad
d\widetilde\xi=X_{03}x_0c-x_1x_5v_+,
\]

the exceptional orientation, and the saturated normal resolution, but only
as a supported secondary class in \(\widetilde F_1\). It cannot by itself
identify the local generator with the image of \(e_F\).

The first missing arrow is now exactly

\[
\boxed{
\operatorname{sp}_G:
R\!\operatorname{Hom}(Q,F_0[2])
\longrightarrow
C_{03}^{\rm exit}[-1],
\qquad
\operatorname{sp}_G(e_F)\stackrel{?}{=}[1].
}
\]

Equivalently, once \(\operatorname{sp}_G\) exists, the first obstruction is

\[
o_G=\operatorname{sp}_G(e_F)-[1]
\in R/(U_{03}).
\]

Only after \(o_G=0\) may fixed-beta Cartier purity and entry 100's labelled
excess trace be composed to test

\[
\Theta_{03}^{\rm loc}
=
\left[\frac1{u_0u_1u_3u_5}\right]\otimes[dX_{03}].
\]

## Evidence

Exact certificate:

- `research/voevodsky/check_d03_blowup_yoneda_exit_hom.rs`

SHA-256:

```text
458bdc5dcb0196c6780008142b695522ec1742adfda215f9dac23e83c7d438a6
```

It verifies the ordinary and blown-up face and loaded-generator censuses,
all seven gallery supports, the zero gallery-to-\(Q\) projection, the
corrected \(\widetilde\xi\), the integral normal retract, the local exit
matrix, the principal-ideal dual evaluation, and the cohomological degree of
the local class. It explicitly reports the global specialization,
extraordinary push--pull, and \(\Theta_{03}\) equality as unconstructed.

Reproduce with:

```powershell
$src = "research/voevodsky/check_d03_blowup_yoneda_exit_hom.rs"
$exe = Join-Path $env:TEMP "marici-d03-blowup-yexit.exe"
rustfmt --edition 2021 --check $src
rustc --edition=2021 -D warnings -O $src -o $exe
& $exe | ConvertFrom-Json
```

Inherited inputs are entries 97, 100, 103, and 105--107.

## Boundary

- The ambient pair-Rees deformation and the gallery source kernel are
  different objects. Ambient generic \(Q\)-support proves no source-level
  generic \(Q\)-support.
- The local principal-ideal duality proves the normalized local class. It
  does not construct \(\operatorname{sp}_G\) or show that \(e_F\) maps to
  that class.
- The ordinary gallery restriction remains zero. Calling the nonzero
  \(H^1\) class a degree-zero ordinary cap is mistyped.
- The two labelled copies \(u_3^\vee,u_3\), Cartier orientation, and
  four-normal Cousin residue are independently established downstream data.
  Merely listing or multiplying their known outputs is not a
  Beck--Chevalley proof.
- Standard or multi-normal Rees construction preserves the support of the
  generic source. Additional normal gradings do not turn a kernel contained
  in \(F_1\) into a kernel meeting \(Q\).

This entry therefore falsifies only the shortcut

\[
\text{ambient Rees has }Q
\quad\Longrightarrow\quad
\text{gallery Rees supplies the }Q\text{-leg}.
\]

It does not prove that a boundary-crossing bivariant kernel cannot exist.

## Consequence

The smallest next construction should be a relative normal-Morse thimble,
not another deformation of the supported gallery. Let
\(\operatorname{st}^\vee(\widetilde G)\) denote the barycentric dual star of
the expanded gallery in the full blown-up associahedron. Test the candidate

\[
\boxed{
\mathscr T_{+;03}
=C_*^{\rm BM}\!\left(
\operatorname{st}^\vee_{\widetilde F_2}(\widetilde G),
\operatorname{st}^\vee_{\widetilde F_1}(\widetilde G);
\mathcal P_{\rm abs}
\right).
}
\]

Its relative interior must contain a literal \(Q\) coface, while its special
boundary must recover \(\widetilde\xi\). The decisive three-part test is

\[
\rho_\eta(\mathscr T_{+;03})\ne0,
\qquad
\partial_0[\mathscr T_{+;03}]=[\widetilde\xi],
\qquad
\operatorname{sp}_G(e_F)=[1].
\]

Failure of the first condition rejects the carrier immediately. Failure of
the second rejects its purity typing. Only after both pass should the
occurrence, can--var, repeated-normal excess, and physical-orientation
packets be attached.

## Outcome contract

```json
{
  "claim": "The D03 ambient exit complex has a canonical occurrence-normalized shifted generator [1] in R/(U_D03), but the canonical expanded-gallery Rees kernel has zero generic Q projection and therefore cannot identify that generator with the image of the global Yoneda class.",
  "status": "proved",
  "assumptions": [
    "The filtered triple and corrected stellar subdivision are those of entries 105 and 107.",
    "Occurrence uses lcm-labelled cellular modules, with I_X=(X_D03) treated as a rank-one module rather than by base localization.",
    "The expanded gallery source is the seven-support object enumerated above."
  ],
  "evidence_refs": [
    "research/voevodsky/check_d03_blowup_yoneda_exit_hom.rs",
    "ledger entries 97, 100, 103, and 105-107"
  ],
  "factorization_test": {
    "local_exit_complex": "passed",
    "principal_ideal_dual_evaluation": "passed without base inversion",
    "local_shifted_generator": "passed: [1] in H1",
    "gallery_generic_Q_projection": "falsified; exactly zero",
    "global_specialization_sp_G": "unconstructed",
    "Theta03_equality": "not proved"
  },
  "counterevidence": [
    "Every gallery support lies in F1_tilde.",
    "The ambient quotient Q is not a subobject of the gallery kernel.",
    "The prior positive checker assigned the missing specialization and push-pull conclusions rather than constructing their chain maps."
  ],
  "next_experiment": "Construct the relative dual-star/normal-Morse thimble T_{+;03}; first prove its generic Q projection is nonzero, then derive its special boundary xi_tilde and test sp_G(e_F)=[1]."
}
```
