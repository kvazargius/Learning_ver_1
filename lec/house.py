
def main():
    x, y = 300, 400
    width, height = 200, 300

    draw_house(x, y, width, height)


def draw_house(x, y, width, height):
    """
    function is drawing house - width and height from a reference point
    :param x: координата x середины дома
    :param y: координата y низа фундамента дома
    :param width: полная ширина дома (фундамент или вылеты крыши включены)
    :param height: полная высота
    :return: None
    """
    print('рисую домик...', x, y, width, height)
    foundation_height = 0.05 * height
    walls_height = 0.5 * height
    walls_width = 0.9 * width
    roof_height = height - walls_height - foundation_height

    draw_foundation(x, y, width, foundation_height)
    draw_walls(x, y - foundation_height, walls_height, walls_width)
    draw_house_roof(x, y - foundation_height - walls_height, width, roof_height)


def draw_foundation(x, y, width, height):
    print('Рисую фундамент: ', x, y, width, height)
    pass


def draw_walls(x, y, width, height):
    print('Рисую стены: ', x, y, width, height)
    pass


def draw_house_roof(x, y, width, height):
    print('Рисую крыши: ', x, y, width, height)
    pass


main()
