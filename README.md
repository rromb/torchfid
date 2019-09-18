# torchfid
## Installable Version of https://github.com/mseitzer/pytorch-fid

## Installation
This code provides an easy way of using the pytorch implementation of the FID-Score calculation (see https://github.com/mseitzer/pytorch-fid)
in an installable fashion. To do so, just clone this repository with
```
git clone git@github.com:rromb/torchfid.git
cd torchfid
pip install -e .
```

The FID score can now easily be calculated as follows:

```python
from torchfid import FIDScore

fid_score = FIDScore(batch_size=50, verbose=True)
score = fid_score('path/to/data1_or_npz', 'path/to/data2')
```
