from utils import (
    calculate_attendance_percentage,
    classes_needed_to_reach,
    classes_can_skip,
)


def main():
    print("=== Smart Attendance Analyzer ===\n")

    try:
        total_classes = int(input("Enter total classes conducted: "))
        attended_classes = int(input("Enter classes attended: "))
        required_percentage = float(input("Enter required attendance percentage: "))

        if attended_classes > total_classes:
            print("\nError: Attended classes cannot exceed total classes.")
            return

        attendance = calculate_attendance_percentage(attended_classes, total_classes)

        print(f"\nCurrent Attendance: {attendance:.2f}%")

        if attendance < required_percentage:
            print("Status: AT RISK ❌")

            needed = classes_needed_to_reach(
                attended_classes, total_classes, required_percentage
            )

            print(
                f"You need to attend the next {needed} classes continuously to reach {required_percentage}%."
            )

        else:
            print("Status: SAFE ✅")

            can_skip = classes_can_skip(
                attended_classes, total_classes, required_percentage
            )

            print(
                f"You can skip the next {can_skip} classes without dropping below {required_percentage}%."
            )

    except ValueError:
        print("\nInvalid input. Please enter numeric values only.")


if __name__ == "__main__":
    main()