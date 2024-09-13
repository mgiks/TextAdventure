class Map:

    map_layout = [
        ["□"] + ["*"] * 4,
        ["*"] * 5,
        ["*"] * 5,
        ["*"] * 5,
        ["*"] * 5,
    ]

    @classmethod
    def reset_map(cls):
        cls.map_layout = [
            ["*"] * 5,
            ["*"] * 5,
            ["*"] * 5,
            ["*"] * 5,
            ["*"] * 5,
        ]
