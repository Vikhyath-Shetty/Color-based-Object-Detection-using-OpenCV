from typing import List, Tuple
from numpy.typing import NDArray
import numpy as np

HSVBound = NDArray[np.uint8]
HSVPair = Tuple[HSVBound, HSVBound]
HSVRange = List[HSVPair]
