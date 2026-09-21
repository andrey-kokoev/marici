# The residual port restores the labelled two-seam comparison

## Result and exact strength

Keeping the already determined residual port gives a continuous, label-preserving paired comparison for the first two-seam attachment. It descends through the actual relation and balancing kernels, reproduces the prescribed Clark pairing, and commutes with cut refinement using transported tail states.

This does NOT make the arithmetic operator alone realize arbitrary window pairings. The residual is retained explicitly. The construction is a triangular change of coordinates on the existing even/moment data, not a new independent arithmetic channel, fitted metric, or semilocal operator equivalence.

Inputs:

- `window-moment-defects-obstruct-the-even-port-arithmetic-attachment-comparison.md`;
- `window-arithmetic-defects-are-transported-tail-boundaries-not-feature-cutoff-commutators.md`;
- `../voevodsky/a-subtracted-gamma-shift-operator-completes-the-one-slot-euler-green-form.md`;
- `../voevodsky/the-completed-first-filtered-extension-has-a-nonzero-balanced-attachment.md`.

## 1. Prescribed ports, fixed domain

Fix a compact Euler spectral interior K and gamma with

`gamma<eta<=Im z<=Y<beta`, `|z|<=Z` on K.

Write H_gamma for the weighted feature half-line space and D_gamma for its unrestricted-trace derivative graph domain. The independently constructed operator L_ar:D_gamma->H_gamma is bounded; let C_ar be a bound.

For forcing f define

`U_f(z)=sqrt(2) X_f(z) exp(i z u)`,

`W_f(z)=sqrt(2) i X_f'(z) exp(i z u)`,

`V_f(z)=W_f(z)-L_ar U_f(z)`.

The letter substitution is

`Psi_K(f)=(U_f,V_f)`

into P_K=C(K;D_gamma) direct-sum C(K;H_gamma), with the sum norm. It is linear. It retains the given ordered spectral arguments; the two components do not introduce independent copies of f.

Put epsilon=beta-Y and delta=eta-gamma. The existing trace bounds give

`C_U=sqrt(1+Z^2)/sqrt(2 epsilon delta)`,

`C_W=1/sqrt(2 epsilon delta)`.

Consequently

`||Psi_K(f)||_(P_K) <= C_Psi ||f||_beta`,

`C_Psi=(1+C_ar) C_U+C_W`.

No division by X_f, inversion of Clark features, or nonvanishing window amplitude assumption is used.

## 2. The paired form is forced by the existing two ports

On pairs (u,v),(u',v') in D_gamma direct-sum H_gamma define

`Q_res((u,v),(u',v'))
 = q_ar(u,u') + <u,v'>_0 + <v,u'>_0`.

Every bracket is the original UNWEIGHTED half-line pairing. This form is bounded by

`B ||(u,v)|| ||(u',v')||`, with `B=max(1,2 C_ar)`.

To see why it is prescribed rather than fitted, start with the fixed even/moment swap form

`Q_swap((u,w),(u',w'))=<u,w'>_0+<w,u'>_0`.

Substitute w=v+L_ar u and w'=v'+L_ar u'. Its expression is exactly Q_res. Thus the only change is the invertible triangular coordinate map

`(u,w) -> (u,w-L_ar u)`

on D_gamma direct-sum H_gamma. The even/moment swap form is itself the fixed sum/difference presentation of the original two-sheet signature. Nothing is chosen to match a sampled Gram.

For every pair of actual forcings and every w,z in K,

`Q_res(Psi_K(f)(w),Psi_K(g)(z))=K_Clark(f,g;w,z)`.

For exponential states the individual half-line denominators remain -i(z-conjugate(w)). The equality is pairwise, not division by an aggregate packet denominator.

The form has separately bounded arithmetic, even/residual and residual/even contributions. These labels are not identified with the previously defined bulk/forcing tail-current labels. The latter still have their independent source definitions.

## 3. Letter substitution and source-kernel descent

Keep vacuum, actual edge labels, coefficient-buffer endpoints and all physical memory/seam multipliers unchanged. Apply Psi_K to every retained forcing slot, using projective tensor products of P_K for ordered histories. Concatenation and fixed-shape tensor reassociation commute with this letter substitution.

In a diamond, the four window forcings are a,b+c,a+b,c. Both components of Psi_K preserve

`a+(b+c)-(a+b)-c=0`.

More generally, every finite zero formal terminal record remains zero under this linear tensor substitution. It therefore annihilates the original record ideal I, rather than defining a new ideal from the arithmetic form.

Construct the path derivative D_Psi and its balanced two-seam version D_(2,Psi) on these records. Their product identities are unchanged:

`D_Psi(I^2)=0`,

`D_(2,Psi)(ab)=D_Psi(a) tensor_balanced D_Psi(b)` for a,b in I,

`D_(2,Psi)(I^3)=0`.

Action-balancing follows from associativity of coefficient concatenation and the same terminal recorder. Different presentations of the same product therefore have the same balanced image. This is genuine source-kernel descent, not descent inferred from equality of a scalar form.

## 4. The first attachment map

Use the existing strictly exact source sequence and model

`P=I^2/I^3`, `E=I/I^3`, `C=I/I^2`,

`K_src=[P -> E]`, in degrees -1,0,

with the declared common completion or its justified presentation-scale version. The new coefficient seam target uses the P_K letters, with the same boundary insertions and balancing.

Define

`F_Psi^(-1)(p)=(0,D_(2,Psi)(p))`,

`F_Psi^0(e)=(D_Psi(e),0)`

into T_Psi[-1] direct-sum J_(Psi,2)[-1]. The chain equations are D_Psi(I^2)=0 and closure of the relation derivative cycles. The joint term factors through the same connecting projection K_src->P[1]. The attachment shift is unchanged.

For the genuine four-event product consisting of a singly retained diamond and a forgotten diamond, this map retains the two labelled one-feature sectors used in the obstruction note. Their residual terms now reproduce their original Clark observations instead of incorrectly setting the window residual to zero.

This is a comparison of coefficient attachment complexes. Actual root-state factors of a full receiver remain external and are not duplicated.

## 5. Bounds and completion

Let c=max(1,C_Psi). On a record with m retained forcing slots, substitution has norm at most c^m. Thus the existing forcing-resolved feature-radius scale gives

`||Psi_records(x)||_(s,b) <= ||x||_(forcing,s,c b)`.

Its differential remains bounded by the old insertion estimate: moving a P_K letter from seam to memory changes only the existing multiplier tau/sqrt(w_seam). Projective tensor reassociation is contractive on a fixed shape. Normalization retains its cut-l1 bound.

The forcing-resolved source estimates consequently extend F_Psi to the unweighted factorial source and to the inherited actual-letter source quotients at enlarged radii. The finite source kernels remain annihilated by continuity. No new Gamma-weighted factorization comparison is inferred.

For the paired observations, choose a feature radius with b^2>=B. Tensoring the one-letter form bound then costs no more than the two weighted record norms. Vacua retain their separate unit incidence form. The shape-l1 estimates control the admitted matching sums. Thus the pairwise comparison extends from finite source records by density on these declared domains.

This does not assert that the P_K projective completion equals an output-only analytical Hilbert completion, or that every observer in one has a preimage in the other.

## 6. Normalization, relative pairings and window refinement

For an admitted artificial-cut normalization N, letter substitution obeys

`N_Psi Psi_external = Psi_balanced N_forcing`.

Each arrow follows from ordered tensor concatenation, not a choice of a cut section. The balanced pairings agree on source-generated records because the one-letter forms agree and the same vacuum, edge and slot labels are retained.

The source collision currents are sums of products of those same pairwise slot forms over the prescribed newly matching shapes. Hence their transformed values agree as well. This transports the existing TOTAL relative-packet identity; it does not redefine its correction by a desired Gram discrepancy or identify its separately labelled bulk/forcing pieces with arithmetic terms.

For a forcing window [a,b], the residual port is the already proved boundary difference

`V_(1_[a,b] f)=mathcal B_a(f)-mathcal B_b(f)`.

At a refinement point c the same transported state appears with opposite signs. The previous total-variation bound controls the sum over refined windows independently of partition size. Thus the residual-port substitution commutes with chamber refinement as well as algebraic buffer normalization. Neither operation resets the tail at a new cut.

All identities retain the ordered spectral pairs on compact interiors. No boundary spectral continuation is invoked.

## 7. What has and has not been repaired

Closed: the first labelled two-seam paired attachment comparison WITH the determined residual retained; its source-kernel descent, explicit radius bounds, and refinement compatibility.

Not repaired: the arithmetic-only even-port comparison. For general windows V_f is nonzero, exactly as the previous obstruction proves. On the prepared full-theta family it vanishes, recovering the one-slot theorem.

The residual carries existing moment information in different coordinates. Giving it an independent arithmetic interpretation, eliminating it, proving equivalence with the full semilocal operator, or obtaining a completed perfect-duality theorem are separate tasks. No positivity claim is added.

The subsequent `../grothendieck/all-prime-tate-leakage-diverges-on-the-common-euler-source-domain.md` rules out the unregularized all-prime full-line L2 operator limit even on positive prepared Euler states. The present construction uses the convergent weighted HALF-LINE operator/form, not that nonexistent limit. Its residual port records a window moment defect; it is not the negative-half-line Tate leakage, does not cancel that leakage, and does not promote compressed-form convergence to full-line operator convergence.

## Verification

`uv run --with sympy python research/nima/checkers/check_residual_port_attachment.py`

Checks verify the triangular signed-form identity with a non-real operator fixture, its two-slot tensor identity, chamber refinement, and actual nonminimal two-factor balancing for forgotten and retained interface arrows. The analytic domain and completion statements follow from the displayed bounds and the existing forcing-resolved construction.
