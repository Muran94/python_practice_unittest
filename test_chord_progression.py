import unittest
import chord_progression as cp

class TestChordProgression(unittest.TestCase):
    def test_get_key(self):
        # 正常系
        self.assertEqual(cp.get_key("c"), "Key: C")
        self.assertEqual(cp.get_key("C"), "Key: C")
        self.assertEqual(cp.get_key("cm"), "Key: Cm")
        self.assertEqual(cp.get_key("Cm"), "Key: Cm")
        self.assertEqual(cp.get_key("cM"), "Key: Cm")
        self.assertEqual(cp.get_key("CM"), "Key: Cm")
        self.assertEqual(cp.get_key("d"), "Key: D")
        self.assertEqual(cp.get_key("D"), "Key: D")
        self.assertEqual(cp.get_key("e"), "Key: E")
        self.assertEqual(cp.get_key("E"), "Key: E")
        self.assertEqual(cp.get_key("f"), "Key: F")
        self.assertEqual(cp.get_key("F"), "Key: F")
        self.assertEqual(cp.get_key("g"), "Key: G")
        self.assertEqual(cp.get_key("G"), "Key: G")
        self.assertEqual(cp.get_key("a"), "Key: A")
        self.assertEqual(cp.get_key("A"), "Key: A")
        self.assertEqual(cp.get_key("b"), "Key: B")
        self.assertEqual(cp.get_key("B"), "Key: B")

        # 異常系
        with self.assertRaises(ValueError):
            cp.get_key("jet")

if __name__ == "__main__":
    unittest.main()
