from typing import Tuple, Union
from werkzeug import Response as Response_


Response = Union[Tuple[Union[Response_, str], int], Response_]
