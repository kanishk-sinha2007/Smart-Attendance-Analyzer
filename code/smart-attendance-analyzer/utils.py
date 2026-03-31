def calculate_attendance_percentage(attended, total):
    if total == 0:
        return 0
    return (attended / total) * 100


def classes_needed_to_reach(attended, total, required_percentage):
    """
    Calculate minimum number of consecutive classes to attend
    to reach required percentage.
    """
    x = 0
    while True:
        new_attended = attended + x
        new_total = total + x
        percentage = (new_attended / new_total) * 100

        if percentage >= required_percentage:
            return x
        x += 1


def classes_can_skip(attended, total, required_percentage):
    """
    Calculate how many classes can be skipped safely.
    """
    x = 0
    while True:
        new_attended = attended
        new_total = total + x
        percentage = (new_attended / new_total) * 100

        if percentage < required_percentage:
            return x - 1
        x += 1