class Position():
    def __init__(self) -> None:
        pass

    def init_start_position(self, position) -> None:
        left, top, width, height = position
        left_top_position = (left, top)
        right_top_position = (left + width, top)
        left_bottom_position = (left, top + height)
        right_bottom_position = (left + width, top + height)
        center_position = ((left + width) / 2, (top + height) / 2)
        self.__start_position = {
            'left_top_position': left_top_position,
            'right_top_position': right_top_position,
            'left_bottom_position': left_bottom_position,
            'right_bottom_position': right_bottom_position,
            'center_position': center_position
        }

    def get_start_position(self):
        return self.__start_position