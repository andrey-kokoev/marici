"""Hostiles for the bounded F41 certificate; no change to frozen net tests."""
import copy
import json
import unittest
import check_hodge_fourth_prime_controls as s


class FourthPrimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=json.loads(s.COUNTS.read_text(encoding='utf-8'))
        cls.receipt=json.loads(s.OUT.read_text(encoding='utf-8'))

    def rows(self,a):return copy.deepcopy([r for r in self.data['rows'] if r['a']==a])

    def test_primitive_moduli(self):
        self.assertEqual(s.find_moduli(),((6,1),(12,1,1),(6,1,0,1),(17,1,0,0,1),(12,2,0,0,0,1)))
        self.assertTrue(all(s.primitive_modulus(p) for p in s.find_moduli()))

    def test_reducible_modulus_not_admitted(self):
        self.assertFalse(s.primitive_modulus((40,0,1)))

    def test_beta_orientation_and_trace(self):
        self.assertEqual(s.elliptic_beta(),(5,4));self.assertEqual((5+s.I*4)%s.P,0)

    def test_two_models_and_residues(self):
        self.assertEqual({a:a%s.P for a in s.CONTROLS},s.CONTROLS)
        for a in s.CONTROLS:self.assertTrue(s.previous.joint.good_model(a,s.P))

    def test_ten_ordinary_eight_twisted_rows(self):
        self.assertEqual(len(self.data['rows']),10)
        self.assertEqual(sum('rho_Frobenius_fixed_V' in r for r in self.data['rows']),8)

    def test_fifth_field_full_orbit_coverage(self):
        r=self.rows(4)[4];self.assertEqual(r['q'],115856201)
        self.assertEqual(sum(j*v for j,v in enumerate(r['Frobenius_x_orbit_counts_by_length'])),r['q'])

    def test_every_unused_fifth_trace(self):
        for a in (4,12):self.assertEqual(len(s.reconstruct(self.rows(a),a)['rational_power_traces_through_degree5']),5)

    def test_fifth_trace_tampering_rejected(self):
        for a in (4,12):
            rows=self.rows(a);rows[4]['V']+=1
            with self.subTest(a=a):
                with self.assertRaisesRegex(ValueError,'unused fifth trace'):s.reconstruct(rows,a)

    def test_a_dependent_poles(self):
        for a in (4,12):
            rows=self.rows(a);self.assertEqual(rows[0]['rational_poles'],s.previous.joint.prime_poles(a,s.P))
            rows[0]['rational_poles']+=1
            with self.assertRaisesRegex(ValueError,'pole normalization'):s.reconstruct(rows,a)

    def test_incomplete_field_cycle_rejected(self):
        rows=self.rows(4);rows[4]['full_primitive_generator_cycle_verified']=False
        with self.assertRaisesRegex(ValueError,'field coverage'):s.reconstruct(rows,4)

    def test_incomplete_orbit_coverage_rejected(self):
        rows=self.rows(12);rows[4]['Frobenius_x_orbit_counts_by_length'][5]-=1
        with self.assertRaisesRegex(ValueError,'orbit coverage'):s.reconstruct(rows,12)

    def test_direct_audit_cannot_be_omitted(self):
        rows=self.rows(4);rows[3]['direct_ordinary_crosscheck']=False
        with self.assertRaisesRegex(ValueError,'direct crosscheck'):s.reconstruct(rows,4)

    def test_power_audit_cannot_be_omitted(self):
        rows=self.rows(12);rows[1]['twist_power_crosscheck']=False
        with self.assertRaisesRegex(ValueError,'twisted coverage'):s.reconstruct(rows,12)

    def test_independent_small_and_direct_twisted_counts(self):
        small=s.independent_counts()
        for a in (4,12):
            r=self.rows(a);self.assertEqual(small[a],[r[0]['V'],r[1]['V'],r[0]['rho_Frobenius_fixed_V']])

    def test_complete_CM_order_certificates(self):
        for r in self.receipt['finite_field_cases']:
            self.assertEqual(r['residual_modular_witnesses'][-1]['remaining_orders'],[])
            self.assertEqual(sum(len(w['orders_excluded']) for w in r['residual_modular_witnesses']),55)

    def polynomial_power(self,quadratic):
        c=[1]
        for _ in range(7):
            out=[0]*(len(c)+2)
            for j,x in enumerate(c):
                for k,y in enumerate(quadratic):out[j+k]+=x*y
            c=out
        return tuple(c)

    def test_synthetic_CM_positive_not_discarded(self):
        c=self.polynomial_power((1,-10,41))
        r=s.previous.arithmetic.cm_certificate(c,(5,4))
        self.assertEqual(r['geometric_reduction_Ei_multiplicity_in_complement'],7)

    def test_synthetic_other_CM_field_not_called_Ei(self):
        c=self.polynomial_power((1,-2,41))
        r=s.previous.arithmetic.cm_certificate(c,(5,4))
        self.assertEqual(r['geometric_reduction_Ei_multiplicity_in_complement'],0)

    def test_prediction_disposition_matches_certificates(self):
        negative=[r['a_mod41'] for r in self.receipt['finite_field_cases'] if r['geometric_reduction_Ei_multiplicity_in_complement']==0]
        self.assertEqual(self.receipt['negative_a_mod41'],negative)
        self.assertEqual(self.receipt['prediction_both_controls_CM_absent_survived'],len(negative)==2)

    def test_no_scope_promotion(self):
        for key in s.FALSE_CLAIMS:self.assertIs(self.receipt[key],False)
        self.assertIs(self.receipt['main_net_or_pins_modified'],False)
        self.assertEqual(self.receipt['base_net_pins'],'v54')

    def test_no_full41_census_claim(self):
        self.assertEqual(sorted({r['a'] for r in self.data['rows']}),[4,12])
        self.assertFalse(self.receipt['all41_residues_counted'])


if __name__=='__main__':unittest.main()
