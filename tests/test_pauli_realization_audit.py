import importlib.util
from itertools import combinations
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
PATH=ROOT/'research/chatgpt/ramsey/pauli_realization_audit.py'
spec=importlib.util.spec_from_file_location('audit',PATH)
audit=importlib.util.module_from_spec(spec);spec.loader.exec_module(audit)

def dense_rank(rows):
    matrix=[[r>>j&1 for j in range(len(rows))] for r in rows];rank=0
    for column in range(len(rows)):
        pivot=next((i for i in range(rank,len(rows)) if matrix[i][column]),None)
        if pivot is None:continue
        matrix[pivot],matrix[rank]=matrix[rank],matrix[pivot]
        for i in range(rank+1,len(rows)):
            if matrix[i][column]:matrix[i]=[a^b for a,b in zip(matrix[i],matrix[rank])]
        rank+=1
    return rank

class PauliAuditTests(unittest.TestCase):
    def test_all_small_graphs(self):
        # Exhaust all labelled graphs through five vertices; independently check
        # Gaussian rank, graph6 roundtrip, Pauli strings and independent sets.
        for n in range(1,6):
            pairs=list(combinations(range(n),2))
            for graph in range(1<<len(pairs)):
                rows=[0]*n
                for bit,(i,j) in enumerate(pairs):
                    if graph>>bit&1:rows[i]|=1<<j;rows[j]|=1<<i
                self.assertEqual(audit.decode_graph6(audit.encode_graph6(rows)),rows)
                self.assertEqual(audit.binary_rank(rows),dense_rank(rows))
                realization=audit.factor_paulis(rows)
                self.assertEqual(realization['qubits']*2,dense_rank(rows))
                for i,j in pairs:
                    anticommutes=sum(a!='I' and b!='I' and a!=b for a,b in zip(realization['paulis'][i],realization['paulis'][j]))%2
                    self.assertEqual(anticommutes,rows[i]>>j&1)
                for size in range(n+1):
                    brute=next((list(s) for s in combinations(range(n),size) if all(not(rows[i]>>j&1) for i,j in combinations(s,2))),None)
                    self.assertEqual(audit.independent_witness(rows,size),brute)
                self.assertEqual(audit.complement(audit.complement(rows)),rows)

    def test_published_artifact(self):
        artifact=json.loads((PATH.parent/'pauli-realization-audit.json').read_text())
        expected=[{'3':1,'4':2},{'6':1},{'7':2,'8':5},{'8':2,'9':13,'10':115,'11':61}]
        for catalogue,histogram in zip(artifact['catalogues'],expected):
            self.assertEqual(catalogue['qubit_histogram'],histogram)
            self.assertEqual(catalogue['sha256'],audit.EXPECTED_SHA256[catalogue['file']])
            for record in catalogue['records']:
                rows=audit.decode_graph6(record['graph6'])
                self.assertEqual(dense_rank(rows),record['binary_rank'])
                self.assertEqual(audit.factor_paulis(rows),record['pauli_realization'])
        deletion=artifact['single_edge_deletions']
        self.assertEqual(deletion['valid_parent_edge_pairs'],618)
        self.assertEqual(deletion['qubit_change_histogram'],{'-1':153,'0':287,'1':178})
        self.assertEqual(artifact['catalogues'][-1]['edge_saturated_count'],18)
        self.assertEqual(len(deletion['minimum_catalogue_records']),2)
        for record in deletion['minimum_catalogue_records']:
            self.assertEqual(record['degrees'],[6]*22)
            self.assertEqual(record['valid_deletions'],0)
            self.assertEqual(len(record['forbidden_commuting_sevens_by_deleted_edge']),66)
            rows=audit.decode_graph6(record['graph6'])
            for edge,witness in record['forbidden_commuting_sevens_by_deleted_edge'].items():
                i,j=[int(v)-1 for v in edge.split(',')];modified=rows[:]
                modified[i]^=1<<j;modified[j]^=1<<i
                vertices=[v-1 for v in witness]
                self.assertEqual(len(set(vertices)),7)
                self.assertTrue(all(not(modified[a]>>b&1) for a,b in combinations(vertices,2)))
        for change,example in deletion['change_witnesses'].items():
            original=audit.decode_graph6(example['parent_graph6']);changed=audit.decode_graph6(example['graph6'])
            i,j=[v-1 for v in example['deleted_edge_1based']]
            self.assertTrue(original[i]>>j&1)
            original[i]^=1<<j;original[j]^=1<<i
            self.assertEqual(original,changed)
            self.assertTrue(audit.triangle_free(changed))
            self.assertIsNone(audit.independent_witness(changed,7))
            self.assertEqual(dense_rank(changed)//2-example['parent_qubits'],int(change))

    def test_deletion_shortcut(self):
        rows=audit.decode_graph6('Dhc') # C5
        for j in range(len(rows)):
            for i in range(j):
                if not(rows[i]>>j&1):continue
                changed=rows[:];changed[i]^=1<<j;changed[j]^=1<<i
                available=((1<<len(rows))-1)&~(rows[i]|rows[j]|(1<<i)|(1<<j))
                self.assertEqual(audit.independent_witness(rows,1,available) is None,
                                 audit.independent_witness(changed,3) is None)

    def test_invalid_graph6(self):
        with self.assertRaises(ValueError):audit.decode_graph6('not a graph')

if __name__=='__main__':unittest.main()
