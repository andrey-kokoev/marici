"""Regression controls for the exact arithmetic used by the ground certificate."""
import unittest
import pentachoron_exact as e


class ExactFieldTests(unittest.TestCase):
    def test_basis_square_and_inverse(self):
        for index in range(16):
            x=e.F(tuple(int(i==index) for i in range(16)))
            expected=1
            for bit,square in enumerate((2,3,5,-1)):
                if index&(1<<bit):expected*=square
            self.assertEqual(x*x,e.F(expected))
            self.assertEqual(x*e.inverse(x),e.F(1))

    def test_mixed_field_inverse_and_conjugation(self):
        x=e.parse('1+sqrt(2)-sqrt(3)+sqrt(5)*I')
        self.assertEqual(x*e.inverse(x),e.F(1))
        self.assertEqual(x.conjugate().conjugate(),x)
        self.assertEqual((x*x.conjugate()).conjugate(),x*x.conjugate())

    def test_parser_and_radical_normalization(self):
        self.assertEqual(e.parse('sqrt(30)'),e.parse('sqrt(2)*sqrt(3)*sqrt(5)'))
        self.assertEqual(e.parse('(2-sqrt(2))*(sqrt(10)+sqrt(6)*I)/32'),
                         e.parse('(2*sqrt(10)-2*sqrt(5)+2*sqrt(6)*I-2*sqrt(3)*I)/32'))
        for text in ('sqrt(7)','1.2','__import__("os")','I.real','sqrt(2,3)'):
            with self.assertRaises((AssertionError,ValueError)):e.parse(text)

    def test_rational_sign_and_psd_controls(self):
        self.assertTrue(e.positive(e.parse('3-2*sqrt(2)')))
        self.assertFalse(e.positive(e.parse('2*sqrt(2)-3')))
        self.assertEqual(e.psd_rank([[e.F(1),e.F(1)],[e.F(1),e.F(1)]]),1)
        for A in ([[e.F(-1)]],[[e.F(),e.F(1)],[e.F(1),e.F()]]):
            with self.assertRaises(AssertionError):e.psd_rank(A)

    def test_kernel(self):
        A=[[e.F(1),e.parse('sqrt(2)')]];V=e.kernel(A)
        self.assertEqual(len(V[0]),1)
        self.assertTrue(e.zero(e.mm(A,V)))
        with self.assertRaises(ZeroDivisionError):e.inverse(e.F())


if __name__=='__main__':unittest.main()
