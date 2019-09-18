import torch	
import torch.nn as nn

from torchfid.fid_score import calculate_fid_given_paths

class FIDScore(nn.Module):
	def __init__(self, batch_size=50, dims=2048, use_cuda=False, verbose=False):
		super(FIDScore, self).__init__()
		if use_cuda:
			assert torch.cuda.is_available()
		self.batch_size = batch_size
		self.dims = dims
		self.use_cuda = use_cuda
		if verbose:
			if not use_cuda and torch.cuda.is_available():
				print('Hey. You might wanna use your cuda. To do so, set use_cuda=True')
		self.verbose = verbose

	def forward(self, path1, path2):
		fid = calculate_fid_given_paths([path1, path2], self.batch_size, self.use_cuda, self.dims)
		if self.verbose:
			print('FID Score: {:.2f}'.format(fid))
		return fid


