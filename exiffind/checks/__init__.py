from .date_before import check as before
from .date_after import check as after
from .height import check as height
from .width import check as width
from .orientation import check as orientation
from .software import check as software
from .author import check as author
from .model import check as model
from .manufacturer import check as manufacturer
from .speed import check as speed
from .exposure import check as exposure
from .aperture import check as aperture
from .fnumber import check as fnumber
from .xresolution import check as xresolution
from .yresolution import check as yresolution

checks = (
    before,
    after,
    width,
    height,
    author,
    software,
    orientation,
    model,
    manufacturer,
    speed,
    exposure,
    aperture,
    fnumber,
    xresolution,
    yresolution
)