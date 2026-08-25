# The PSZ spin-memory source and readout are puncture distributions

## Result

The source-derived subleading map does not have the finite Laurent target of
the parity-kernel engine.  Its source coordinates are hard angular-momentum
records at named punctures, and its target is a distribution on the sphere
subsequently paired with Green kernels and contours.

For a source puncture `xi`, the PSZ Green function is

\[
 G(\xi;z)=\log\frac{(\xi-z)(\bar\xi-\bar z)}
 {(1+\xi\bar\xi)(1+z\bar z)}.
\]

Away from the incidence divisor `z=xi`, direct differentiation gives

\[
 \partial_{\bar\xi}G
 =\frac{1+\xi\bar z}
 { (\bar\xi-\bar z)(1+\xi\bar\xi)},
 \qquad
 \partial_\xi\partial_{\bar\xi}G
 =-\frac1{(1+\xi\bar\xi)^2}.
\]

Distributionally,

\[
 \partial_\xi\partial_{\bar\xi}G
 =2\pi\delta^2(\xi-z)-\frac12\gamma_{\xi\bar\xi},
 \qquad
 \gamma_{\xi\bar\xi}=\frac2{(1+\xi\bar\xi)^2}.
\]

Equation (6.9) of the grounded PSZ source packet therefore has, per hard
puncture, the source-generated response

\[
 \mathcal R_\xi(z)
 =-8G\gamma_{\xi\bar\xi}\operatorname{Im}\left[
 L_{u\xi}\,\partial_{\bar\xi}G
 +\frac{i}{2}h_\xi\,
 \partial_\xi\partial_{\bar\xi}G\right].
\]

The independent source labels are `xi`, `L_uxi`, and `h_xi`, subject to the
physical total-angular-momentum relations.  They are not Laurent numerator
coefficients.

## 1. The pipeline and the location of the engine

The source-derived subleading pipeline is

\[
 \{(\xi_k,L_k,h_k)\}_k
 \longrightarrow
 T_{uz}\ \text{and}\ \partial_{[\bar z}N_{z]}
 \longrightarrow
 \operatorname{Im}[\partial_{\bar z}D_z^3C_{zz}]
 \longrightarrow
 \operatorname{Im}[D_z^2C_{zz}]
 \longrightarrow
 \{\Delta_\mathcal C u\}_{\mathcal C}.
\]

The parity engine's grade-three magnetic expression matches the third object
only as a local differential formula.  It does not identify the source of
`C_zz`, the distributional target, the inverse Green step, or the contour
pairing.  In particular, clearing `(1+z*bar(z))` denominators and retaining
every formal numerator coefficient is not a PSZ readout operation.

## 2. Complete local ports versus one contour

The orbital kernel has a simple pole at `bar(z)=bar(xi)`.  Its residue is
nonzero and proportional to `L_uxi`.  For distinct named punctures, the full
local distribution separates the orbital source coefficients by their pole
supports.  The spin coefficient multiplies a delta function at the same
puncture plus the required sphere zero-mode subtraction.  Retaining the
distributional port therefore separates `h_xi` as well.

This gives a source-side reconstruction principle:

\[
 \text{all local puncture residues and delta coefficients}
 \Longrightarrow \{L_{u\xi},h_\xi\}_\xi
\]

before imposing the independently declared conservation relations.

A single contour is a proper projection of this target and generally has a
kernel.  The complete family of contours is equivalent to the underlying
curl distribution only after the Green operator, its `l<=1` quotient, and
the total-sphere compatibility condition are retained.  Thus single-contour
blindness is physical readout selection; it is not an engine tower.

## 3. Observable quotient

The physical quotient visible in the source is:

- exact shifts `N_z -> N_z+partial_z X`, with real `X`, are removed by the
  imaginary curl;
- `l<=1` scalar zero modes are removed by the sphere Green operator;
- total angular momentum conservation removes the gauge-mixing residual in
  the soft/constraint comparison;
- antipodal matching relates the `I+` and `I-` records but is not gauge.

No rational de Rham quotient of the engine folded one-form appears in the
PSZ measurement definition.  Engine residue classes therefore do not survive
or vanish under this physical observable quotient: they are outside the
source image before that question is reached.

## 4. Target verdict

The target equality proposed by the engine application is false:

\[
 \boxed{
 Y_{\mathrm{physical}}
 =\mathcal D'(S^2)_{\mathrm{curl},\,l\ge2}
 \xrightarrow{\text{Green/contour pairings}}
 \mathbb R^{\{\mathcal C\}},
 \qquad
 Y_{\mathrm{physical}}\ne
 Y_{g,\mathbb Z}^{\mathrm{full}}.}
\]

The inequality is typed, not dimensional: one side is a real/distributional
source-derived target with support and zero-mode relations; the other is a
free integral lattice of formal Laurent numerator rows.  A comparison can be
built only after choosing a puncture expansion chart and a completion, and
that comparison is neither injective nor onto at finite cutoff because it
omits the coherent tail and distributional delta ports.

## 5. Classification of the named engine classes

For the currently grounded smooth and punctured sources:

| class | source constructible? | reaches PSZ physical target? |
|---|---:|---:|
| tower `D_g,a` | no | no |
| `E1` | no; also wrong grade | no |
| `E2` | no; also wrong grade | no |

This is not a claim that the physical target annihilates them.  They have no
preimage under the derived physical constructor.  Their correct status is
**inaccessible engine capability**, not zero physical record.

## Evidence

`checkers/physical_spin_readout_constructor_checks.py` verifies the regular
Green derivatives, distributional zero-mode decomposition, pole residues,
distinct-support reconstruction matrix, and the non-equivalence of a finite
Laurent truncation with the puncture response.

