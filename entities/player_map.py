from copy import deepcopy


class Map:
    map_layout = [
        ["□"] + ["*"] * 4,
        ["|   " * 5],
        ["*"] * 5,
        ["|   " * 5],
        ["*"] * 5,
        ["|   " * 5],
        ["*"] * 5,
        ["|   " * 5],
        ["*"] * 5,
    ]

    def _build_map(raw_schema, current_position):
        schema = deepcopy(raw_schema)

        x = current_position[0]
        y = current_position[1]

        print(x)
        print(y)

        schema[y][x] = "▽"

        for row in range(len(schema)):
            schema[row] = " ─ ".join(schema[row])

        return schema

    @classmethod
    def _get_map_layout(cls):
        return cls.map_layout

    @classmethod
    def get_map(cls, coordinates):
        current_position = coordinates[-1]

        map_schema = cls._build_map(cls.map_layout, current_position)

        for row in map_schema:
            print(row)
