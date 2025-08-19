import argparse
from utils import ColorAction, camera_type


def main():
    argparser = argparse.ArgumentParser(prog="Object Detection using color")
    argparser.add_argument("--camera", default=0, type=camera_type,
                           help="Specifies the camera source")
    argparser.add_argument("--color", nargs='*', choices=["red", "green", "blue", "yellow"],
                           default="red", action=ColorAction, help="Specifies the color(s) of the object(s) to be detected")
    args = argparser.parse_args()
    print(f"Camera:{args.camera} {type(args.camera)}\n Color:{args.color}  {type(args.color)}")


if __name__ == "__main__":
    main()
