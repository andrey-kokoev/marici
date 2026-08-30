# The completed theta orbit inhabits the local doubled-signal-to-history incidence

The remaining local arrow after event 10305 can be constructed before any
boundary pencil.

Let (Phi) be the completed bilateral theta forcing and let

[
(	au_L g)(u)=g(u+L),
qquad L=log p.
]

Use the reciprocally doubled prime signal fiber

[
mathcal S_p=mathbb C e_p^+oplusmathbb C e_p^-.
]

Define the source incidence

[
mathcal I_p(c_+,c_-)
=
p^{-1/2}
left(
c_+	au_LPhi,,
c_-	au_{-L}Phi
ight)
]

into the direct sum of the two object-indexed translated history source
spaces. Every ingredient is already source-authorized:

- (Phi) is the completed theta forcing;
- (	au_{pm L}) is Mellin translation;
- (p^{-1/2}) is the primitive Euler half-density;
- the two summands are the reciprocal signal doubling.

This is not a fitted map obtained from its endpoint matrix.

## Reflection covariance

Let reciprocal reflection exchange the signal basis,

[
R_{mathcal S}e_p^+=e_p^-,
qquad
R_{mathcal S}e_p^-=e_p^+,
]

and act on histories by ((Rg)(u)=g(-u)). Since (RPhi=Phi),

[
R	au_LPhi=	au_{-L}Phi.
]

Therefore

[
R_{mathcal H}mathcal I_p
=
mathcal I_pR_{mathcal S}.
]

The incidence has the required reciprocal typing before endpoint evaluation.

## Closed graph-space landing

For the relative source rung

[
mathcal E_w=L^1(mathbb R)cap L^2(mathbb R,w,du),
]

the rapid decay of (Phi) puts it in (mathcal E_w). At displacement (L),
use the transported weight (w_L(u)=w(u+L)). Translation is isometric:

[
|	au_LPhi|_{mathcal E_{w,L}}
=
|Phi|_{mathcal E_w}.
]

Hence

[
|mathcal I_p|
=
p^{-1/2}|Phi|_{mathcal E_w}
le
2^{-1/2}|Phi|_{mathcal E_w}.
]

Thus the local incidences are uniformly bounded in the object-indexed
topology. Composing with the already closed bilateral Volterra lift gives a
bounded map into the wall-extended relative history graph.

## Endpoint readout

The exact source moments are

[
M_-(Phi)=M_+(Phi)=rac12.
]

After passing to the comoving half-density endpoint frame, the two columns are

[
v_p^+
=
rac12
egin{pmatrix}
1\
p^{-1}
end{pmatrix},
qquad
v_p^-
=
rac12
egin{pmatrix}
p^{-1}\
1
end{pmatrix}.
]

Thus endpoint trace of (mathcal I_p) is exactly

[
V_p
=
rac12
egin{pmatrix}
1&p^{-1}\
p^{-1}&1
end{pmatrix},
]

rather than merely having the same scalar shadow. Its lower singular value is
at least (1/4).

## Prime typing

The map is defined fiberwise:

[
mathcal I^{(X)}
=
igoplus_{ple X}mathcal I_p.
]

Consequently it intertwines the prime idempotents exactly,

[
P_q^{mathcal H}mathcal I^{(X)}P_p^{mathcal S}
=
delta_{pq}mathcal I_p.
]

This rules out the shared-bath hostile at the signal-to-history interface.
Cutoff naturality is automatic for the orthogonal direct-sum assembly.

## What remains

The finite local incidence constructor is now inhabited and has:

- source derivation;
- reciprocal covariance;
- uniform object-indexed boundedness;
- exact endpoint normalization;
- exact prime diagonality;
- cutoff naturality.

The next gate is not local incidence existence. It is completion of the
primewise direct sum in the declared global source norm and compatibility of
that completion with the causal/anti-causal history relation. In particular,
the primitive coefficients are not square-summable in an unweighted Hilbert
sum, so the global domain must retain the projective exponential or
Laplace-rigged source topology. No completed boundary pencil follows yet.

## Source locators

- `research/nima/twisted-theta-histories-give-exact-normalized-completion-trace-columns.md`
- `research/nima/a-weighted-relative-sobolev-space-closes-the-bilateral-volterra-history.md`
- `research/nima/mellin-half-density-transport-exactly-preserves-the-bilateral-trace-frame.md`
- `research/nima/lossless-two-addition-colligation-requires-reciprocal-doubling.md`
- `research/nima/correction-the-primitive-trace-meets-the-doubled-signal-port-not-the-julia-defect-bath.md`
