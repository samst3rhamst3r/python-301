
import unittest
from clirpg import Item, Creature, Hero, Opponent, Room, Map

class TestCreature(unittest.TestCase):

    def setUp(self):
        self.obj = Creature('test_creature', 5, 5, 5)
    
    def test_take_dmg(self):
        self.assertEqual(self.obj.take_dmg(2), 3)

    def test_take_max_dmg(self):
        self.assertEqual(self.obj.take_dmg(7), 0)
    
    def test_attack(self):
        attack = self.obj.attack()
        self.assertGreaterEqual(attack, 0)
        self.assertLessEqual(attack, 5)
    
    def test_defend(self):
        defend = self.obj.defend()
        self.assertGreaterEqual(defend, 0)
        self.assertLessEqual(defend, 5)
    
    def test_is_dead(self):
        self.obj.take_dmg(5)
        self.assertTrue(self.obj.is_dead())
    
    def test_is_not_dead(self):
        self.obj.take_dmg(2)
        self.assertFalse(self.obj.is_dead())

class TestHero(unittest.TestCase):

    def setUp(self):
        self.potion = Item("potion", consumable=True, rest_effect=lambda hp: hp + 2)   
        self.obj = Hero('test', 5, 5, 5)
    
    def test_heal(self):
        self.obj.take_dmg(3)
        self.obj.heal(1)
        self.assertEqual(self.obj.get_curr_hp(), 3)
    
    def test_max_heal(self):
        self.obj.heal(1)
        self.assertEqual(self.obj.get_curr_hp(), 5)
    
    def test_add_to_pack(self):
        self.obj.add_to_pack(self.potion)
        self.assertEqual(len(self.obj.pack), 1)
        self.assertEqual(self.obj.pack["potion"]["quantity"], 1)
    
    def test_rem_from_pack(self):
        self.obj.add_to_pack(self.potion)
        self.obj.rem_from_pack("potion")
        self.assertEqual(len(self.obj.pack), 0)
    
    def test_equip_items(self):
        self.assertEqual(len(self.obj.equipped_items), 0)
        self.obj.add_to_pack(self.potion)
        self.obj.equip_items()
        self.assertEqual(len(self.obj.equipped_items), 1)
        self.assertEqual(len(self.obj.pack), 0)
    
    def test_unequip_items(self):
        self.obj.add_to_pack(self.potion)
        self.obj.equip_items()
        self.obj.unequip_items()
        self.assertEqual(len(self.obj.equipped_items), 0)

if __name__ == "__main__":
    unittest.main()