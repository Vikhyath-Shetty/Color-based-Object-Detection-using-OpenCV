import argparse
from typing import List

# helper to process the color input


class ColorAction(argparse.Action):
    def __call__(self, parser: argparse.ArgumentParser, namespace: argparse.Namespace, values: List[str], option_string: str | None = None) -> None:
        if len(values) == 1:
            setattr(namespace, self.dest, values[0])
        else:
            setattr(namespace, self.dest, set(values))



