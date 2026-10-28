# F736 fixed-sector source dictionary and intrinsic response continuity

## Prior sources freshly inspected

- `research/voevodsky/the-four-function-response-map-is-continuous-into-two-schwartz-and-two-relative-history-rungs.md`;
- `research/voevodsky/the_four_boundary_traces_share_a_weighted_second_order_relative_graph_domain_20260910.md`;
- `research/voevodsky/four-function-response-sheaf-compresses-all-moving-seam-fourier-saturations.md`;
- `research/voevodsky/source-derived-fourier-sewing-identification-closure-ledger.md`;
- the existing physical/half-density conventions in `research/strominger/archimedean-cutoff-entry-v1.md` and `research/strominger/finite-observer-encoder-v1.md`.

The fixed-sector dictionary below is a direct analytical extraction from these formulas, not a fresh certification or a completed native F736 witness. No tests were run.

## 1. Intrinsic topology for the response coordinate already exists

The response-continuity paper proves, independently of merely transporting a topology,

    R(f)=(B_f,Q_f,A_f,C_f)
      : Schwartz -> Schwartz direct_sum Schwartz
          direct_sum H_relative^2 direct_sum H_relative^2,

where

    B_f(a)=f(a),
    Q_f(a)=integral exp(-2 pi i a x) f(x) dx,
    A_f(a)=integral_(-infinity)^a f(x) dx,
    C_f(a)=PV integral exp(-2 pi i a x) f(x)/x dx.

It gives

    A_f'=f, A_f''=f',
    C_f'=-2 pi i Q_f, C_f''=-2 pi i Q_f',

and the history endpoints

    A_f(-infinity)=0, A_f(+infinity)=integral f,
    C_f(-infinity)=+i pi f(0),
    C_f(+infinity)=-i pi f(0).

Thus the response coordinate for the comparison graph need not remain justified only by a chosen transported topology.

## 2. Correct common trace domain has TWO derivatives

The four-trace note defines the translated weight w_a(u)=(1+|u-a|)^(1+epsilon), epsilon>0, and norm

    ||F||_relative,a,2^2
      = |F(-infinity)|^2+|F(+infinity)|^2
        +integral w_a (|F'|^2+|F''|^2).

The trace

    Gamma_a F=(F(-infinity),F(+infinity),F(a),F'(a))

is continuous. Endpoint/value control alone at first order does not control pointwise flux F'(a). The second derivative is essential. Volterra maps a derivative-regular source into this graph, with flux equal to the original source density.

This supplies the source-reached value/flux continuity needed by full response presentations. It does not identify an unrelated external arithmetic current with a functional on that graph.

## 3. Exact fixed-sector coordinate dictionary

Use the frozen compact physical convention, not an unstated replacement:

    h in C_c^infinity(R)                      [log source amplitude],
    f(x)=x^(-1/2) h(log x), x>0              [physical half-density],
    f(x)=0, x<=0.

Because h has compact log support, f is smooth and compactly supported AWAY from zero. It is therefore an actual Schwartz input to R(f). On every fixed log-support stage, h->f and its inverse h(u)=exp(u/2)f(exp u) are continuous in the corresponding smooth test topologies. This follows by the chain rule on the fixed compact annulus.

Keep the two Fourier operations distinct:

    m_h(t)=integral_R h(u)exp(-itu)du         [log Mellin multiplier],
    Q_f(a)=integral_R f(x)exp(-2 pi i a x)dx  [additive physical Fourier].

They are NOT the same function with a renamed argument. If the response is instead applied to h itself, its Fourier coordinate is Q_h(a)=m_h(2 pi a), but that is a different response presentation R(h), requiring the actual h/f comparison before substitution.

The Fourier-sewing ledger supplies the oriented half-density/Mellin transport, including the Tate reflection multiplier. It explicitly excludes absolute radialization and an unsupported identification of quarter turn with a reciprocal swap. No new sewing normalization needs to be guessed.

## 4. Mellin endpoints are explicit response observations in this sector

With the frozen m_h convention,

    ell_plus(h)=m_h(i/2)=integral h(u)exp(u/2)du,
    ell_minus(h)=m_h(-i/2)=integral h(u)exp(-u/2)du.

Substitute x=exp u and h(u)=x^(1/2)f(x):

    ell_plus(h)=integral_0^infinity f(x)dx=A_f(+infinity),
    ell_minus(h)=integral_0^infinity f(x)dx/x=C_f(0).

The second integral is ordinary here: f vanishes near zero, so the PV prescription at0 adds no ambiguity.

Therefore the full endpoint pair can be read from the physical response by

    beta(h)=(A_f(+infinity),C_f(0)).

This is NOT identification of both Mellin endpoints with the limiting values C_f(+/-infinity). Indeed f(0)=0 here, so those latter limits are zero. Distinguishing endpoint traces from seam evaluation avoids that incorrect identification.

The intrinsic history graph controls A_f(+infinity) and C_f(0), hence gives response-side continuity for both endpoint observations on these admitted images. This does not establish endpoint bounds on the independently completed regular Plancherel carrier.

## 5. The physical calibrated flux and volume are also fixed

The full value channel is B_f(x)=f(x), while the log source is

    h(log x)=sqrt(x)B_f(x).

At x=4^k,

    h(2k log2)=2^k B_f(4^k),

which is the previously frozen encoder calibration, now displayed on the entire compact physical source rather than only its five packets.

At the identity x=1,

    h(0)=f(1)=B_f(1).

Thus the scalar source density in the physical centered trace can be carried as this exact response evaluation in the matched one-sector convention. It must not be replaced by the encoder observation Gram. Matching the full semilocal theorem's observer convention still requires its stated source normalization; the identity-value agreement alone does not identify every local spectral term.

## 6. Convolution-star convention in these coordinates

For the frozen log Fourier convention and convolution involution,

    h_star(u)=conjugate(h(-u)),
    m_(h_star)(z)=conjugate(m_h(conjugate z)).

Hence the two endpoint values swap under conjugation. The physical half-density involution is

    f_star(x)=x^(-1)conjugate(f(1/x)), x>0.

This is obtained by transporting h_star through the same half-density chart. It is consistent with the unitary-dilation operator adjoint. A printed reflection formula with an additional minus in the Mellin argument must be converted before use; this dictionary does not certify that different source convention globally.

No source-star/dagger construction is needed for the inverse-equivalence mate route, but these formulas prevent an incorrect endpoint swap if polarity is used independently.

## 7. Consequence for the actual fixed-cutoff carrier attempt

The prior fixed-sector trace norm estimate from v12, intrinsic response continuity above, and explicit endpoint/identity-value formulas now fit one concrete source dictionary:

    h -> f -> R(f),
    h -> A_h -> ordered cutoff trace,
    h -> volume density h(0)=B_f(1),
    h -> beta(h)=(A_f(+infinity),C_f(0)).

Retain the full represented h/f source relation in the comparison graph. For word charts whose source variable is physical f, the fourth inverse is B-projection. For word charts written in log h coordinates, the recovery is B-projection FOLLOWED by h(u)=exp(u/2)B(exp u). These are conjugate source conventions, not literally the same map symbol.

This is useful actual input for the open carrier task; it should not remain an abstract request to 'match endpoint normalization'. The remaining coordinate audit includes the exact local spectral distribution and cutoff/reference conventions, common-domain compatibility of the declared spectral chart, and the topology of the regulator family.

After those are instantiated, the distinct modification-level comparison must identify the inherited H234 witness and its inverse mate, not merely observe that the carrier has the same scalar coordinates. Both bottom/filler pairs still use one H736.

## Disposition

Prior research supplies intrinsic full-response continuity, a correct second-order value/flux domain, and exact Fourier response transport. Combined with the frozen physical half-density convention, it yields explicit response formulas for both Mellin endpoint observations and the source identity density in this sector.

This is a substantial normalization/continuity component of the fixed-cutoff carrier construction, not proof of all semilocal/native stages, regulator-family estimates, positive external metrics or the analytical F736 filler.
