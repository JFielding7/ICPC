def hardflor():
    input()
    lines = []
    x = y = 0

    for corner in input().split():
        if corner[0] == "W":
            x -= int(corner[1:])
        elif corner[0] == "E":
            x += int(corner[1:])
        elif corner[0] == "N":
            height = int(corner[1:])
            lines.append((x, y, y + height))
            y += height
        else:
            height = int(corner[1:])
            lines.append((x, y - height, y))
            y -= height

    lines.sort()
    open_sections = set()
    area = 0

    for x0, y0_lower, y0_upper in lines:
        prev_area = area

        for x1, y1_lower, y1_upper in open_sections.copy():
            curr_prev_area = area

            if y1_lower <= y0_lower and y0_upper <= y1_upper:
                area += (x0 - x1) * (y0_upper - y0_lower)
                open_sections.remove((x1, y1_lower, y1_upper))
                open_sections.add((x1, y1_lower, y0_lower))
                open_sections.add((x1, y0_upper, y1_upper))
                break
            elif y0_lower <= y1_lower and y1_upper <= y0_upper:
                area += (x0 - x1) * (y1_upper - y1_lower)
            elif y1_lower < y0_lower < y1_upper:
                area += (x0 - x1) * (y1_upper - y0_lower)
                open_sections.add((x1, y1_lower, y0_lower))
            elif y1_lower < y0_upper < y1_upper:
                area += (x0 - x1) * (y0_upper - y1_lower)
                open_sections.add((x1, y0_upper, y1_upper))

            if area != curr_prev_area:
                open_sections.remove((x1, y1_lower, y1_upper))

        if area == prev_area:
            open_sections.add((x0, y0_lower, y0_upper))

    print("THE AREA IS", area)


hardflor()
