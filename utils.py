import argparse
from typing import List

# helper class to process the --color argument


class ColorAction(argparse.Action):
    def __call__(self, parser: argparse.ArgumentParser, namespace: argparse.Namespace, values: List[str], option_string: str | None = None) -> None:
        if len(values) == 0:
            
        elif len(values) == 1:
            setattr(namespace, self.dest, values[0])
        else:
            setattr(namespace, self.dest, set(values))


# helper function to process the --camera argument
def camera_type(value):
    try:
        return int(value)
    except ValueError:
        return value
