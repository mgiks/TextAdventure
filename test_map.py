import unittest
import player_map


class TestMap(unittest.TestCase):
    def test_build_map(self):
        expected_map = [
            "□ ─ * ─ * ─ * ─ *",
            "|   |   |   |   |   ",
            "* ─ * ─ * ─ * ─ *",
            "|   |   |   |   |   ",
            "* ─ * ─ ▽ ─ * ─ *",
            "|   |   |   |   |   ",
            "* ─ * ─ * ─ * ─ *",
            "|   |   |   |   |   ",
            "* ─ * ─ * ─ * ─ *",
        ]

        coordinate = (2, 2)

        map_layout = player_map.Map._get_map_layout()
        built_map = player_map.Map._build_map(map_layout, coordinate)

        self.assertEqual(built_map, expected_map)
