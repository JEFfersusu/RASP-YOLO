# Ultralytics YOLO 🚀, AGPL-3.0 license

__version__ = "8.2.5"

from ultralytics.data.explorer.explorer import Explorer
from ultralytics.models import YOLO, YOLOWorld
from ultralytics.utils import ASSETS, SETTINGS
from ultralytics.utils.checks import check_yolo as checks
from ultralytics.utils.downloads import download

settings = SETTINGS
__all__ = (
    "__version__",
    "ASSETS",
    "YOLO",
    "YOLOWorld",
    "checks",
    "download",
    "settings",
    "Explorer",
)
