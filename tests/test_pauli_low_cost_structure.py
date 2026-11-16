import importlib.util
from itertools import combinations
import json
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
DIRECTORY=ROOT/'research/chatgpt/ramsey'
sys.path.insert(0,str(DIRECTORY))
import pauli_low_cost_structure as structure
from pauli_realization_audit import decode_graph6

def multiply(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(2))for j in range(2)]for i in range(2)]

class LowCostStructureTests(unittest.TestCase):
    def test_direct_cycle_search(self):
        cycle=[(1<<((i-1)%7))|(1<<((i+1)%7)) for i in range(7)]
        found,count=structure.parity_closed_heptagons(cycle)
        self.assertEqual(count,1);self.assertEqual(set(found),{127})
        # A single external neighbor violates parity but leaves the induced C7 intact.
        tail=cycle+[1];tail[0]|=1<<7
        found,count=structure.parity_closed_heptagons(tail)
        self.assertEqual(count,1);self.assertEqual(found,{})
        # Two incident cycle vertices restore external parity.
        tail[7]|=1<<3;tail[3]|=1<<7
        found,_=structure.parity_closed_heptagons(tail)
        self.assertIn(127,found)
        # A chord destroys that induced cycle.
        chord=cycle[:];chord[0]|=1<<3;chord[3]|=1
        self.assertEqual(structure.parity_closed_heptagons(chord),({},0))

    def test_catalogue_discriminator(self):
        data=json.loads((DIRECTORY/'pauli-low-cost-structure.json').read_text())
        self.assertEqual(len(data['records']),191)
        self.assertEqual(data['feature_table'],[
            {'qubits':8,'parity_closed_heptagons':4,'records':2},
            {'qubits':9,'parity_closed_heptagons':0,'records':13},
            {'qubits':10,'parity_closed_heptagons':0,'records':115},
            {'qubits':11,'parity_closed_heptagons':0,'records':61}])
        for record in data['records']:
            rows=decode_graph6(record['graph6'])
            heptagons,count=structure.parity_closed_heptagons(rows)
            self.assertEqual(count,record['induced_heptagon_count'])
            self.assertEqual(len(heptagons),len(record['parity_closed_heptagons']))
            if heptagons:
                xor=0
                for mask in heptagons:xor^=mask
                self.assertEqual(xor,0)
                self.assertEqual(len(set(structure.span(list(heptagons)))),8)
                for a,b in combinations(heptagons,2):self.assertIn((a&b).bit_count(),[1,3])
                for mask in heptagons:
                    outside=[(rows[i]&mask).bit_count()for i in range(22)if not(mask>>i&1)]
                    self.assertEqual(sorted(outside),[0]+[2]*14)

    def test_exact_compression_certificates(self):
        data=json.loads((DIRECTORY/'pauli-low-cost-structure.json').read_text())
        matrices={'I':[[1,0],[0,1]],'X':[[0,1],[1,0]],'Z':[[1,0],[0,-1]],'W':[[0,-1],[1,0]]}
        for record in data['records']:
            cert=record['compression_certificate']
            if cert is None:continue
            rows=decode_graph6(record['graph6']);masks=[]
            for relation in cert['independent_relations']:
                vertices=[i-1 for i in relation['vertices_1based']]
                mask=sum(1<<i for i in vertices);masks.append(mask)
                self.assertTrue(all((row&mask).bit_count()%2==0 for row in rows))
                sign=1
                for qubit in range(8):
                    product=matrices['I']
                    for vertex in vertices:product=multiply(product,matrices[cert['pauli_realization']['paulis'][vertex][qubit]])
                    self.assertIn(product,[[[1,0],[0,1]],[[-1,0],[0,-1]]]);sign*=product[0][0]
                self.assertEqual(relation['ordered_pauli_product'],'+I' if sign==1 else '-I')
            # Independence checked by distinct subset sums, not the rank routine.
            self.assertEqual(len(masks),6);self.assertEqual(len(set(structure.span(masks))),64)
            indices=[i-1 for i in cert['nonsingular_principal_vertices_1based']]
            self.assertEqual(len(indices),16);self.assertEqual(len(set(indices)),16)
            minor=[sum(((rows[i]>>j)&1)<<k for k,j in enumerate(indices))for i in indices]
            self.assertEqual(len(set(structure.span(minor))),65536)

if __name__=='__main__':unittest.main()
