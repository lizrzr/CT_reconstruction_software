import numpy as np
import astra
import math
import matplotlib.pyplot as plt
# Assuming 'projs' is already defined and is a 3D numpy array
# clearvars -except projs label recon projs1 V2
# 从temp中读取数据
projs = np.load('./temp/projs.npy')
SOD = 552
DOD = 82
det_width = 0.085
det_count = 1024

# create geometries
angles = np.linspace(0, 2*math.pi, 720)
proj_geom = astra.create_proj_geom('cone', det_width, det_width, det_count, det_count, angles, SOD, DOD)
w = 768  # volume dimensions
h = 768
FOV = (det_width * det_count) * SOD / (2 * (SOD + DOD))
min_x = -FOV
max_x = FOV
min_y = -FOV
max_y = FOV
min_z = min_x * h / w
max_z = -min_z
vol_geom = astra.create_vol_geom(w, w, h, min_x, max_x, min_y, max_y, min_z, max_z)

# create forward projection
proj_id = astra.data3d.create('-proj3d', proj_geom, projs.T)

# reconstruct
recon_id = astra.data3d.create('-vol', vol_geom, 0)
cfg = astra.astra_dict('FDK_CUDA')
cfg['ProjectionDataId'] = proj_id
cfg['ReconstructionDataId'] = recon_id
fdk_id = astra.algorithm.create(cfg)
astra.algorithm.run(fdk_id)
V = astra.data3d.get(recon_id)

V2 = V[384, :, :]
# 利用numpy保存V2为jpg
plt.imsave('output.jpg', V2, cmap='gray')




