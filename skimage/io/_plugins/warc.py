__all__ = ['imread']

from skimage.util.dtype import convert
import imread as _imread

def imread(record, dtype=None):
    """Load an image from a WARC record.

    Parameters
    ----------
    record : WARC Record

    """
    im = _imread.imread_from_blob(record.payload)
    if dtype is not None:
        im = convert(im, dtype)
    return im
