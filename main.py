import argparse
from utils import ColorAction


if __name__ == "__main__":
    argparser = argparse.ArgumentParser(prog="Object Detection using color")
    argparser.add_argument("--camera", nargs=1, default=0,
                           help="Specifies the camera source")
    argparser.add_argument("--color", nargs='*', choices=["red", "green", "blue", "yellow"],
                           default="red", action=ColorAction, help="Specifies the color(s) of the object(s) to be detected")
    args = argparser.parse_args()
    print(f"camera value is {args.camera}\ncolor value is {args.color}")
