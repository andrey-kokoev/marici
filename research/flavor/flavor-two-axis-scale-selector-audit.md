# Two-axis flavor-scale selector audit: WP458

## Question

Do the admitted dynamical flavon action, current constraints, poles, and widths select a numerical value of (g_F f/v), or do they only identify it after observation?

## Independent source freedoms

WP447 fixes

\[
f^2=6\mu^2,
\]

so the target is

\[
q_F=\frac{g_Ff}{v}=\sqrt6g_F\frac{\mu}{v}.
\]

The source theory admits both (g_F>0) and (mu/v>0) independently. Varying either while holding the other fixed changes (q_F). Therefore selecting (q_F) requires a constructor that removes at least the product-changing direction in this two-dimensional source-label family.

The currently admitted probes do not do so:

- the zero-momentum flavor-current kernel depends on (mu^{-2}) and exactly deletes (g_F);
- the triplet pole mass reads (g_F mu);
- the fractional width reads (g_F^2/(4 pi));
- their joint rank-two readout reconstructs the realized parameters but does not reduce their prior source domain.

These are constraints or readouts, not selectors.

## Minimal relational portal attack

Test the strongest coefficient-independent-looking classical repair. Add a real singlet (sigma) and the scale-invariant positive relations

\[
[X_i,X_j]=i\kappa\sigma\epsilon_{ijk}X_k,
\qquad
\sum_i\operatorname{Tr}X_i^2=6\kappa^2\sigma^2,
\qquad
\sigma^2=cH^\dagger H,
\]

with positive dimensionless source labels (kappa,c). Using (H^dagger H=v^2/2), its irreducible vacuum gives

\[
\frac f v=\kappa\sqrt{3c},
\qquad
q_F=g_F\kappa\sqrt{3c}.
\]

The portal removes the continuous state dilation from the ratio but leaves three product-changing theory labels (g_F,kappa,c). Setting any of them to a convenient number is a new source postulate, not a stationary prediction. The portal is a relational scale rigidifier conditional on its labels; it is not yet a numerical selector.

## Gauge-running attack

On the admitted light flavor-gauge spectrum there are six Dirac fundamental quarks and three real adjoint flavons. For (SU(3)_F), the one-loop coefficient is

\[
b_0=\frac{11}{3}C_A-\frac43T_Fn_D-\frac16T_An_s
=11-4-\frac32=\frac{11}{2}.
\]

Thus

\[
\beta(g_F)=-\frac{b_0}{16\pi^2}g_F^3
\]

has only (g_F=0) as a one-loop fixed point. The admitted perturbative running supplies dimensional transmutation after a boundary condition, not a finite selected gauge coupling. This statement is deliberately limited to one loop; higher-loop gauge-scalar fixed points require a separately frozen complete coupling system.

## Disposition

Current status of (q_F):

- source selection: absent;
- relational rigidification of (f/v): available only after adding the displayed portal and its unfixed labels;
- physical readout: algebraically faithful through WP457;
- experimentally executable readout: not yet established;
- low-energy current constraint: response map exists, full likelihood remains open.

The smallest constructive successor must supply both a source-authorized finite normalization of (g_F) and a source-authorized value of (kappa sqrt(c)), or one joint fixed relation for their product. It must then survive the complete fitted flavor ensemble and the detector gate. Neither a measured pole nor a fitted portal coefficient counts as that source constructor.

## Smallest exact falsifiers

- The portal ratio retains dependence on the radial state (sigma).
- The portal target becomes independent of all (g_F,kappa,c) without adding a new law.
- The admitted one-loop beta function has a positive finite zero.
- Any current packet already reduces the source-label family before experimental conditioning.
