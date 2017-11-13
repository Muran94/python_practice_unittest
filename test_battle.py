import unittest
import battle

class TestBattle(unittest.TestCase):
    def test_attack(self):
        self.assertEqual(battle.attack(), "プレイヤーは攻撃をした！")

    def test_defend(self):
        self.assertEqual(battle.defend(), "プレイヤーは防御をした！")

    def test_heal(self):
        self.assertEqual(battle.heal(), "プレイヤーは100HP回復した！")

    def test_use_item(self):
        self.assertEqual(battle.use_item(), "プレイヤーはアイテムを使用した！")

    def test_run_away(self):
        self.assertEqual(battle.run_away(), "プレイヤーは逃走した！")

if __name__ == "__main__":
    unittest.main()
