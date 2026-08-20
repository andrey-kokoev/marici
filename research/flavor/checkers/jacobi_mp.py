"""High-precision 3x3 complex Hermitian eigensolver (cyclic Jacobi) for
the WP9 hierarchy flow (marici.Figueiredo).

np.linalg.eigh loses the smallest eigenpair once lam_min / ||H|| drops
below ~1e-16; the WP9 tau-flow reaches 1e-60 and beyond.  This solver
uses mpmath Jacobi sweeps with unitary 2x2 rotations; it is used only
for tau slices where float64 eigh is unreliable, and is validated
against eigh at tau = 1..4 to 1e-12.
"""
import mpmath as mp


def eigh3_mp(H, dps=120, max_sweeps=200):
    """H: 3x3 nested lists of complex.  Returns (eigenvalues ascending,
    eigenvectors as columns) using mpmath arithmetic at `dps` digits."""
    old = mp.mp.dps
    mp.mp.dps = dps
    try:
        A = [[mp.mpc(H[i][j]) for j in range(3)] for i in range(3)]
        # enforce exact hermiticity
        for i in range(3):
            A[i][i] = mp.mpf(A[i][i].real)
        for i in range(3):
            for j in range(i + 1, 3):
                v = (A[i][j] + mp.conj(A[j][i])) / 2
                A[i][j] = v
                A[j][i] = mp.conj(v)
        U = [[mp.mpc(1) if i == j else mp.mpc(0) for j in range(3)]
             for i in range(3)]
        diag_scale = max(abs(A[i][i]) for i in range(3))
        tol = diag_scale * mp.mpf(10) ** (-(dps - 25))
        for _ in range(max_sweeps):
            off = max(abs(A[0][1]), abs(A[0][2]), abs(A[1][2]))
            if off < tol:
                break
            for p, q in ((0, 1), (0, 2), (1, 2)):
                hpq = A[p][q]
                if abs(hpq) < tol:
                    continue
                app, aqq = A[p][p].real, A[q][q].real
                magn = abs(hpq)
                phase = hpq / magn
                theta = (aqq - app) / (2 * magn)
                t = (1 if theta >= 0 else -1) / (abs(theta)
                                                 + mp.sqrt(theta**2 + 1))
                c = 1 / mp.sqrt(1 + t**2)
                s = t * c
                # rotation: J[p,p]=c, J[q,q]=c, J[p,q]=s*phase,
                # J[q,p]=-s*conj(phase); A <- J^H A J, U <- U J
                sph = s * phase
                spc = -s * mp.conj(phase)
                for k in range(3):
                    akp = A[k][p]
                    akq = A[k][q]
                    A[k][p] = c * akp + spc * akq
                    A[k][q] = sph * akp + c * akq
                for k in range(3):
                    apk = A[p][k]
                    aqk = A[q][k]
                    A[p][k] = c * apk + mp.conj(spc) * aqk
                    A[q][k] = mp.conj(sph) * apk + c * aqk
                # hermiticity cleanup of touched diagonal
                A[p][p] = mp.mpf(A[p][p].real)
                A[q][q] = mp.mpf(A[q][q].real)
                A[p][q] = A[q][p] = mp.mpc(0)
                for k in range(3):
                    ukp = U[k][p]
                    ukq = U[k][q]
                    U[k][p] = c * ukp + spc * ukq
                    U[k][q] = sph * ukp + c * ukq
        evals = [(A[i][i].real, i) for i in range(3)]
        evals.sort()
        vals = [v for v, _ in evals]
        # NOTE: eigenvectors are returned as mpc, NOT downconverted to
        # float64: at large flow tau the small mixing components fall below
        # 1e-308 and would flush to 0.0, corrupting CKM quartic ratios.
        vecs = [[U[r][i] for r in range(3)] for _, i in evals]
        # vecs[k] = eigenvector (column) for vals[k]
        return vals, vecs
    finally:
        mp.mp.dps = old


def v_ckm_mp(Yu, Yd, dps=120):
    """V_CKM = Uu^dag Ud with mass-ordered columns, mpmath path.
    Yu, Yd: 3x3 nested lists of complex."""
    Hu = [[sum(Yu[i][k] * Yu[j][k].conjugate() for k in range(3))
           for j in range(3)] for i in range(3)]
    Hd = [[sum(Yd[i][k] * Yd[j][k].conjugate() for k in range(3))
           for j in range(3)] for i in range(3)]
    _, Uu = eigh3_mp(Hu, dps)
    _, Ud = eigh3_mp(Hd, dps)
    # Uu[i][k] = component k of the i-th mass-ordered eigenvector;
    # V = Uu^dag Ud pairs eigenvector i of u with eigenvector j of d
    return [[sum(Uu[i][k].conjugate() * Ud[j][k] for k in range(3))
             for j in range(3)] for i in range(3)]
