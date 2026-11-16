import importlib.util
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path
import sys
import unittest

HERE=Path(__file__).resolve().parents[1]/'research/chatgpt/ramsey'
sys.path.insert(0,str(HERE))
from ramsey_extension_repair import add_vertex, toggle
from heptagon_near_extremal_counterexample import graph
from pauli_realization_audit import decode_graph6, encode_graph6, independent_witness, triangle_free

def is_independent(rows,mask):return all(not(row&mask)for i,row in enumerate(rows)if mask>>i&1)

def independent_subsets(rows,size):
    return [sum(1<<i for i in vs)for vs in combinations(range(len(rows)),size)if all(not(rows[i]>>j&1)for i,j in combinations(vs,2))]

class ExtensionRepairTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.data=json.loads((HERE/'ramsey-extension-repair.json').read_text())

    def test_general_edge_hitting_repair_equivalence(self):
        # Every four-vertex H0 and every set of added nonedges, every N,
        # and independent-set thresholds 3 and 4. No Ramsey catalogue involved.
        pairs=list(combinations(range(4),2))
        for assignments in product(range(3),repeat=len(pairs)):
            before=[0]*4;after=[0]*4;added=[]
            for state,(i,j)in zip(assignments,pairs):
                if state:
                    after[i]|=1<<j;after[j]|=1<<i
                if state==1:before[i]|=1<<j;before[j]|=1<<i
                if state==2:added.append((i,j))
            for threshold in(3,4):
                old_dangers=independent_subsets(before,threshold)
                extension_dangers=independent_subsets(before,threshold-1)
                covered=lambda mask:any(mask>>i&1 and mask>>j&1 for i,j in added)
                old_covered=all(covered(mask)for mask in old_dangers)
                for neighbors in range(16):
                    criterion=triangle_free(after)and is_independent(after,neighbors)and old_covered and all(covered(mask)for mask in extension_dangers if not(mask&neighbors))
                    extended=add_vertex(after,neighbors)
                    actual=triangle_free(extended)and independent_witness(extended,threshold)is None
                    self.assertEqual(criterion,actual)

    def test_frozen_edges_and_all_neighborhood_certificates(self):
        packet=self.data['deletion_obstruction'];base=graph();core=decode_graph6(packet['frozen_core_graph6'])
        self.assertEqual(len(packet['frozen_edges']),42)
        for item in packet['frozen_edges']:
            changed=toggle(base,item['edge_0based']);mask=sum(1<<i for i in item['independent_seven_after_deletion_0based'])
            self.assertEqual(mask.bit_count(),7);self.assertTrue(is_independent(changed,mask))
        complete=set()
        for size in range(7):complete.update(independent_subsets(core,size))
        witnesses=packet['candidate_neighborhood_witnesses']
        self.assertEqual(len(witnesses),4572);self.assertEqual({w['neighbor_mask']for w in witnesses},complete)
        for witness in witnesses:
            neighborhood=witness['neighbor_mask'];six=witness['disjoint_old_independent_six_mask']
            self.assertEqual(neighborhood&six,0);self.assertEqual(six.bit_count(),6)
            self.assertTrue(is_independent(base,six))

    def test_exact_cycle_of_deletion_conflicts(self):
        packet=self.data['deletion_obstruction'];core=decode_graph6(packet['frozen_core_graph6'])
        all_sevens=set(independent_subsets(core,7));self.assertEqual(len(all_sevens),210)
        self.assertEqual(set(packet['core_independent_seven_masks']),all_sevens)
        minimal=set(packet['minimal_forbidden_deletion_masks'])
        self.assertEqual(minimal,{(1<<i)|(1<<((i+10)%21))for i in range(21)})
        support_masks=set()
        for item in packet['cycle_edge_deletion_supports']:
            seven=item['independent_seven_mask']
            required=sum(1<<i for i in range(21)if seven>>i&1 and seven>>((i+1)%21)&1)
            self.assertEqual(required,item['required_deletion_mask']);support_masks.add(required)
            self.assertTrue(any(required&pair==pair for pair in minimal))
        self.assertTrue(minimal<=support_masks)
        f=[0,1]
        while len(f)<=22:f.append(f[-1]+f[-2])
        self.assertEqual(packet['valid_deletion_set_count'],f[20]+f[22])

    def test_constructive_paths_and_blocker_cover(self):
        for name,count in [('unrestricted_repair',11),('regular_repair',13)]:
            packet=self.data[name];rows=graph();self.assertEqual(len(packet['path']),count)
            for step in packet['path']:
                i,j=step['edge_0based'];self.assertEqual(bool(rows[i]>>j&1),step['operation']=='delete')
                rows=toggle(rows,(i,j));self.assertEqual(encode_graph6(rows),step['graph6'])
                self.assertTrue(triangle_free(rows));self.assertIsNone(independent_witness(rows,7))
            neighbors=sum(1<<v for v in packet['new_vertex_neighbors_0based']);final=add_vertex(rows,neighbors)
            self.assertEqual(encode_graph6(final),packet['final_graph6'])
            self.assertTrue(triangle_free(final));self.assertIsNone(independent_witness(final,7))
        packet=self.data['unrestricted_repair'];self.assertEqual(packet['remaining_blocker_counts'],[17,10,4,0])
        coverage=packet['added_edge_blocker_coverage'];uncovered=set(packet['blockers_after_deletions'])
        self.assertEqual(len(uncovered),17)
        for item in coverage:
            i,j=item['edge_0based'];hit={s for s in packet['blockers_after_deletions']if s>>i&1 and s>>j&1}
            self.assertEqual(hit,set(item['covered_blocker_masks']));uncovered-=hit
        self.assertFalse(uncovered)
        self.assertEqual(packet['degree_four_vertices_0based'],[4,7])

    @unittest.skipUnless(importlib.util.find_spec('pysat'),'optional python-sat dependency')
    def test_checked_lower_bound_formula_digests(self):
        from ramsey_regular_repair_search import build as regular
        from ramsey_unrestricted_repair_search import build as unrestricted
        for name,built in [('ramsey-unrestricted-repair-10.json',unrestricted(10)),('ramsey-regular-repair-4-addition-at-most.json',regular(4,at_most=True))]:
            receipt=json.loads((HERE/name).read_text());clauses,_,nvars=built
            text=f'p cnf {nvars} {len(clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n'for c in clauses)
            self.assertEqual(sha256(text.encode()).hexdigest(),receipt['cnf_sha256'])
            self.assertEqual(receipt['status'],'UNSAT');self.assertTrue(receipt['proof_independently_checked'])
            self.assertEqual(receipt['independent_check']['cnf_sha256'],receipt['cnf_sha256'])
            self.assertEqual(receipt['independent_check']['proof_sha256'],receipt['proof_sha256'])

if __name__=='__main__':unittest.main()
