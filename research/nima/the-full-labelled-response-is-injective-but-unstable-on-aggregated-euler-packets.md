# The full labelled response is injective but unstable on aggregated Euler packets

## Result and attribution

The compact prepared-profile output equivalence does not extend stably to the norm-summable vertical Euler packet class after spectral aggregation. There are unit strong-port inputs, represented by uniformly first-moment-bounded coefficient measures on one fixed Euler line, whose ENTIRE five-label output tends to zero.

The full labelled map is nevertheless injective: its last two coordinates are weak copies of the actual inputs. Its range on the full Banach port domain is nonclosed. Thus the failure is inverse stability, not a new full-output kernel.

Voevodsky's concurrent `../voevodsky/the-reduced-rigged-arithmetic-response-is-compact-with-nonclosed-range.md` proves the central compactness and oscillating-source estimates for the reduced response. This note applies those estimates to the full five-label map and supplies explicit uniformly controlled vertical Bochner presentations. It does not claim a new proof of reduced-map compactness.

## 1. Freeze the full output and source norms

Let gamma>1/2, D_gamma be the unrestricted-trace weighted half-line H1 space, and H_gamma its weighted L2 space. Use the Banach port

`V=D_gamma direct-sum H_gamma`

with sum norm. The full output is the already prescribed map

`O(u,r)=(B_rig u,-leak_rig u,J_end beta_end(u),r,u)`

into the sum-norm labelled response space

`H_-^+ direct-sum H_-^- direct-sum C^2
       direct-sum H_-^+ direct-sum H_-^+`.

The last coordinates have NEGATIVE-weight response norms, not the strong input norms. All outputs, including leakage, remain present.

The preceding rigged theorem proves O bounded. If O(u,r)=0, its fourth and fifth coordinates force r=0 and u=0 almost everywhere, since the weighted inclusions are injective. Thus this FULL map has zero kernel, independently of whether the reduced Tate/endpoint map has one.

## 2. A unit strong-port sequence with vanishing output

Take a nonzero real chi in C_c^infinity((a,b)), 0<a<b, and define

`f_n(u)=n^(-1) exp(i n u) chi(u)`.

Put A0=||chi||_Hgamma^2 and A1=||chi'||_Hgamma^2. Direct differentiation gives

`||f_n||_Dgamma^2=A0+(A0+A1)/n^2`.

Let N_n=||f_n||_Dgamma and set u_n=f_n/N_n, r_n=0. Then ||(u_n,0)||_V=1 and N_n stays bounded above and away from zero.

The supplied reduced-response proof gives

`||Atilde_infty E_+ f_n||_L2=O(log(2+n)/n)`.

It uses logarithmic growth of the fixed gamma multiplier and the frequency translation of the Schwartz Fourier transform of chi. The prime response is O(1/n) by its H_gamma->H_- bound, and the endpoint outputs are O(1/n).

The additional output coordinates do not repair this:

`r_n=0`,

`||u_n||_(H_-^+) <= ||u_n||_L2=O(1/n)`.

Splitting the full response into positive and negative pieces changes its norm only by a fixed factor. Therefore

`||O(u_n,0)||_response=O(log(2+n)/n) ->0`.

This is an approximate-null sequence for the ENTIRE labelled response. No endpoint, weak copy, negative test channel or residual label has been discarded.

## 3. These inputs belong to the declared vertical Bochner class

Fix sigma>gamma+1/2 and put alpha=sigma-1/2. Extend chi smoothly by zero to the real line and let

`h(u)=exp(alpha u) chi(u)`.

It is smooth and compactly supported. Choose its Schwartz Fourier density g with convention

`h(u)=integral_R exp(-i t u) g(t) dt`.

Define the actual complex measures

`dmu_n(t)=g(t+n) dt/n`.

Changing variables shows, on u>=0,

`integral exp(-(alpha+i t)u) dmu_n(t)
 =n^(-1) exp(i n u) chi(u)=f_n(u)`.

These are vertical Euler superpositions at s=sigma+i t. Their first absolute moments satisfy

`integral (1+|t|) d|mu_n|(t)
 <= (1+1/n) integral |g(v)|dv
      +(1/n) integral |v||g(v)|dv`.

Both integrals are finite. Dividing mu_n by N_n therefore gives uniformly bounded first-moment measures representing the unit vectors u_n. The Bochner integrals converge in D_gamma, exactly as in the declared infinite-packet source class.

The residual coordinate is zero termwise, so these are superpositions of the residual-zero Euler port states (e_s,0). If expressed using the prepared full-theta states sqrt(2)xi(s)e_s, divide the coefficients by that nonzero scalar on Re s=sigma. The required norm-weighted Bochner integral is unchanged; finite unweighted variation of those rescaled coefficients is not asserted.

Thus the hostile is not an unrestricted formal spectral sum or merely a source outside the stated packet class.

## 4. Why compact-profile recovery is unaffected

The prepared-sector theorem retains a compact spectral parameter set and continuous labelled profiles u(z)=a(z)e_z, r(z)=d(z)e_z. Its inverse constants depend on that fixed compact set.

Here the spectral support is unbounded and the profiles are AGGREGATED into one function of u. The same smooth source can have nonunique measure presentations, and no individual spectral labels remain in the aggregated port. The source has a fixed spatial support, so this example isolates loss of derivative/frequency control rather than spatial escape.

The endpoint reconstruction for a single retained exponential profile is not an inverse for this aggregation operation. Its compact-sector bounded inverse and nonzero attachment witness remain valid.

## 5. Nonclosed full-output range and exact scope

O is a bounded injective map between the specified Banach port and response spaces. If its range were closed, the bounded inverse theorem would imply

`||(u,r)||_V <= C ||O(u,r)||_response`.

Section 2 contradicts this. Hence its full Banach range is not closed.

No claim of compactness of O on the entire port V is needed. In particular the residual inclusion H_gamma->H_-^+ need not be compact. The reduced response's compactness and the explicit r=0 hostile already settle the required stability question.

On the vertical Bochner class the same sequence rules out any uniform recovery estimate in the strong port norm, even with a fixed bound on the first absolute coefficient moment. That class need not itself be complete in the induced port norm, so the Banach closed-range conclusion is stated for V, not inferred for an unspecified packet completion.

The nonzero kernel of the endpoint-subtracted negative response on certain infinite packets is a different result. Here the entire labelled map remains injective. Likewise, ordinary-L2 leakage obstructions are neither used as a substitute for this inverse estimate nor removed by it.

## 6. Disposition

Closed: full-output inverse instability on a uniformly controlled aggregated vertical packet family, injectivity of the five-label map on its actual port domain, and nonclosed range on the full Banach port.

The next recovery claim would need additional source regularity, a restricted spectral/spatial class, or a deliberately weaker reconstruction topology. A new norm defined solely by the response would describe a response completion, not establish equivalence with the old strong source norm.

## Verification

`uv run --with sympy python research/nima/checkers/check_aggregated_full_output_instability.py`

The checker verifies the oscillating graph-norm identity, the vertical density translation, and exact moment/log-weight majorants. The rigged operator estimates are the supplied analytic theorem; the first-moment Bochner representation and full-output conclusion are proved above.
