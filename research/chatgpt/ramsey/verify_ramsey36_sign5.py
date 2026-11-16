"""Exact-integer verification of seven rank-five sign representations of R(3,6,17).
Data: B. McKay, https://users.cecs.anu.edu.au/~bdm/data/ramsey.html
Run: python verify_ramsey36_sign5.py
Each row is a non-unit real 5-vector; normalizing preserves its dot-product signs.
"""
from itertools import combinations, product

G6 = ['P??GaOo`XMGsIcT?pSLaGuA?', 'P?C?I_h`SDEQQcLAh`dU?tG?', 'P@oGQA?`ACcdCtDYC]Ah?goC', 'PG?OSAKccKGiGwJSI[@oWUA_', 'PGD?OkeO_WAEGQobP_s`cgU?', 'Ps`A?WIDGeCdGsQEKK?oLL_O', 'Ps`A?_KChFCiBoQSKCOoXL_O']
VECTORS = [[[-791, 34, 72, -16, -606], [20, -685, -72, -52, -723], [39, 683, -7, 18, -729], [-221, -73, -604, 527, -551], [-225, -101, -357, -770, -469], [51, -179, 715, 497, -455], [-31, 216, 669, -573, -419], [-268, 526, 490, 486, -418], [-231, -486, 682, -303, -391], [648, 225, -415, -432, -413], [16, -583, -572, -346, -460], [-47, 575, -583, 381, -426], [-43, -524, 144, 752, -370], [24, 569, 46, -713, -407], [670, -106, -216, 601, -364], [594, -555, 311, -361, -335], [648, 421, 548, 175, -270]], [[-753, -122, -94, -28, -639], [131, 577, -342, -35, -729], [-59, -651, 234, -32, -719], [195, -330, -777, -108, -487], [55, 360, 838, 147, -378], [-90, 161, -230, 864, -408], [-117, 20, 274, -840, -453], [-126, -225, 780, 304, -483], [-177, 291, -805, -255, -414], [763, -27, 48, -593, -252], [553, 8, 236, 671, -433], [68, 565, 92, 693, -433], [-100, -729, -262, 470, -412], [46, 600, 309, -656, -334], [168, -708, -68, -562, -389], [703, 251, -534, 115, -380], [636, -335, 646, 63, -250]], [[750, 207, -97, -22, -620], [623, -566, 55, 172, -509], [198, 717, 267, 146, -595], [71, -726, 446, 7, -519], [-779, 52, -241, 145, -557], [478, -100, 445, -688, -300], [317, 112, 600, 609, -396], [-143, 402, 767, 379, -293], [-428, -145, 639, -303, -544], [-453, -367, 121, 570, -566], [-295, 236, 109, -768, -505], [-48, -369, -259, 850, -267], [88, 159, -520, -634, -542], [393, -93, -669, 576, -241], [347, -207, -748, -302, -432], [-210, 819, -349, 279, -291], [-311, -625, -496, -443, -266]], [[21, -836, 39, -191, -512], [834, 143, 14, 74, -527], [-689, 250, 181, 210, -621], [264, 294, 639, -518, -408], [-233, 341, -520, -520, -538], [67, -223, -578, 620, -476], [78, -330, 559, 614, -443], [44, 675, 57, 565, -468], [30, 431, 677, 278, -527], [-151, 406, -633, 296, -570], [11, 510, 20, -741, -437], [-517, -435, 473, -500, -265], [431, -382, -448, -402, -553], [284, -588, 467, -406, -436], [-456, -554, -485, -221, -448], [587, -328, -249, 601, -353], [-572, -356, 287, 611, -301]], [[-779, 64, -15, -36, -623], [-299, -583, -204, 214, -695], [338, 652, -218, -212, -607], [327, -546, 448, -197, -596], [-229, 733, 147, 101, -615], [60, 474, 576, 591, -301], [243, -406, -407, 623, -471], [-84, 411, -496, -604, -463], [-234, -340, 584, -580, -390], [-373, 309, 461, -672, -318], [-327, -413, -628, -377, -431], [-165, 329, -348, 727, -464], [-224, -286, 737, 277, -499], [601, 152, 621, -354, -325], [587, -350, -244, -545, -421], [612, 288, -605, 240, -344], [357, -337, 404, 641, -430]], [[763, 82, -71, 45, -636], [-655, 152, -502, 160, -519], [-576, 188, -202, -615, -463], [-625, 107, 639, -217, -378], [-605, 133, 212, 580, -486], [69, 593, 535, -436, -410], [32, -637, 418, -334, -554], [25, -636, -232, -598, -428], [32, 570, -401, -567, -438], [-167, -589, -388, 387, -571], [57, 671, -415, 478, -383], [74, -532, 380, 471, -588], [288, 604, 315, 384, -552], [254, 83, 638, -515, -506], [264, -108, 534, 633, -483], [59, 120, -691, -574, -419], [232, -27, -583, 552, -548]], [[763, -19, 9, -38, -645], [-665, 311, -260, -540, -318], [-642, -485, 207, -360, -425], [-436, -199, -416, 622, -459], [-562, 528, 277, 391, -420], [171, -317, 649, 393, -544], [-84, -733, 133, 444, -492], [80, -84, 751, -366, -537], [58, -539, -534, -475, -442], [-119, 488, 473, -435, -579], [57, 787, -151, 390, -450], [-34, 281, -763, 472, -339], [118, 233, -660, -519, -476], [289, -541, -314, 492, -532], [291, 439, 174, 662, -504], [265, -500, 240, -683, -395], [116, 775, -163, -501, -329]]]

def edges_from_graph6(s):
    n = ord(s[0]) - 63
    bits = [((ord(c)-63) >> shift) & 1 for c in s[1:] for shift in range(5,-1,-1)]
    pairs = [(i,j) for j in range(1,n) for i in range(j)]
    return n, {frozenset(pair) for pair,bit in zip(pairs,bits) if bit}

def dot(a,b):
    return sum(x*y for x,y in zip(a,b))

def verify_ramsey(n,edge_set):
    assert not any(all(frozenset(edge) in edge_set for edge in combinations(T,2))
                   for T in combinations(range(n),3))
    assert not any(all(frozenset(edge) not in edge_set for edge in combinations(T,2))
                   for T in combinations(range(n),6))

if __name__ == '__main__':
    for k,(s,Q) in enumerate(zip(G6,VECTORS),1):
        n,E=edges_from_graph6(s)
        assert n == len(Q) == 17
        verify_ramsey(n,E)
        margins=[(-1 if frozenset((i,j)) in E else 1)*dot(Q[i],Q[j])
                 for i,j in combinations(range(n),2)]
        assert min(margins)>0
        print(f'Graph {k}: 17 nodes, {len(E)} edges; minimum integer dot margin {min(margins)}')
    cube=list(product((-1,1),repeat=4))
    E={frozenset((i,j)) for i,j in combinations(range(16),2) if dot(cube[i],cube[j])<0}
    verify_ramsey(16,E)
    print(f'4D sign-cube: 16 nodes, {len(E)} edges; triangle-free, independence < 6')
    switched=list(cube); switched[0]=tuple(-x for x in switched[0])
    E2={frozenset((i,j)) for i,j in combinations(range(16),2) if dot(switched[i],switched[j])<0}
    assert any(all(frozenset(edge) not in E2 for edge in combinations(T,2))
               for T in combinations(range(16),6))
    print('Switch one quaternion sign: the same SO(3) orientations now admit a six-node B-group.')

    # Gauge-invariance counterexample with no zero inner products.
    from math import cos, sin, pi
    q=[(cos(2*pi*i/5),sin(2*pi*i/5)) for i in range(5)]
    def signs(points):
        return {frozenset((i,j)) for i,j in combinations(range(5),2)
                if dot(points[i],points[j])<0}
    base=signs(q)
    changed=q.copy();changed[0]=tuple(-x for x in changed[0])
    switched=signs(changed)
    assert len(base)==len(switched)==5
    def triangle_parity(E,T):
        return sum(frozenset(e) in E for e in combinations(T,2))%2
    assert all(triangle_parity(base,T)==triangle_parity(switched,T)
               for T in combinations(range(5),3))
    assert not any(all(frozenset(e) in base for e in combinations(T,2))
                   for T in combinations(range(5),3))
    assert not any(all(frozenset(e) not in base for e in combinations(T,2))
                   for T in combinations(range(5),3))
    assert all(frozenset(e) in switched for e in combinations((0,1,4),2))
    assert all(frozenset(e) not in switched for e in combinations((0,2,3),2))
    print('C5 quaternion sign flip: unchanged triangle parities, but both forbidden 3-groups appear.')
