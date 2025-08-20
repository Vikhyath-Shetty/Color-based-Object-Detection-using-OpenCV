import argparse
from utils import ColorAction, camera_type
from detection import detect_object


def main():
    argparser = argparse.ArgumentParser(prog="Object Detection using color")
    argparser.add_argument("--camera", default=0, type=camera_type,
                           help="Specifies the camera source")
    argparser.add_argument("--color", nargs='+', choices=["red", "green", "blue", "yellow"],
                           default=["red"], action=ColorAction, help="Specifies the color(s) of the object(s) to be detected")
    args = argparser.parse_args()
    try:
        print(
            "Running color based Object detection task...\nPress 'q' to exit")
        detect_object(args.camera, args.color)
    except RuntimeError as e:
        print(f"[ERROR]RuntimeError:{e}")
    except Exception as e:
        print(f"[ERROR]Unexpected error:{e}")
    finally:
        print("Task has been terminated!")


if __name__ == "__main__":
    main()
