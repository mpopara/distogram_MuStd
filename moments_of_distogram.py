"""
Compute moments of distogram (mean and standard deviation),
and plot them onto upper and lower triangle of residue-residue matrix
"""
import pathlib
import numpy as np
import matplotlib as mpl
import pathlib
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes	



### set plot properties#####
plt.rcParams['svg.fonttype'] = 'none'
mpl.rcParams['font.sans-serif']="Arial"
plt.rcParams['figure.figsize'] = 3.5, 3
params = {'legend.fontsize': 6,
          'legend.handlelength': 2}

plt.rcParams['legend.frameon'] = True
plt.rcParams['legend.fancybox'] = True
mpl.rcParams['axes.linewidth'] = 0.3

mpl.rcParams['axes.labelsize'] = 8
mpl.rcParams['xtick.labelsize'] = 6
mpl.rcParams['ytick.labelsize'] = 6
mpl.rcParams['xtick.major.width'] = 0.3
mpl.rcParams['ytick.major.width'] = 0.3
mpl.rcParams['xtick.minor.width'] = 0.3
mpl.rcParams['ytick.minor.width'] = 0.3
mpl.rcParams['xtick.major.size'] = 2
mpl.rcParams['ytick.major.size'] = 2
mpl.rcParams['xtick.minor.size'] = 1 # half of the major ticks length
mpl.rcParams['ytick.minor.size'] = 1

plt.rcParams.update(params)


####################################


distPath = pathlib.Path("C:/user/folder")



axis_path = distPath / "distogram_axis.npy"
axis = np.load(axis_path)
axis2 = axis**2.0


dist = np.load(distPath / 'distogram.npy')


nx, ny, nz = dist.shape    

mean = np.zeros((nx, ny), dtype=np.float32)
var = np.zeros((nx, ny), dtype=np.float32)


  
for ix in range(nx):
    for iy in range(ny):            

        # mean distance
        mean[ix, iy] = np.dot(dist[ix, iy, :], axis) / np.sum(dist[ix, iy, :])

        # Distibtion width
        var[ix, iy] = np.dot(dist[ix, iy, :], axis2) / np.sum(dist[ix, iy, :]) - mean[ix, iy]**2.0

   



# combine mu and stdev in single array

m_sd = np.triu(mean) + np.sqrt(np.clip(np.tril(var),0, 1e9))


s=np.tril(m_sd)
s[np.triu_indices(s.shape[0], -1)] = np.nan

m=np.triu(m_sd)
m[np.tril_indices(m.shape[0], -1)] = np.nan

fig, ax = plt.subplots()

fig.subplots_adjust(bottom=0.1, top=0.9, left=0.1, right=0.8)

ax_twin = ax.twinx()
ax_twin.invert_yaxis()




imS=ax.imshow(s, cmap='Greys', vmin=0, vmax=20)

axins1 = inset_axes(ax,
                    width="5%",  # width = 40% of parent_bbox width
                    height="40%",  # height : 5%
                    loc='lower left',
                    bbox_to_anchor=(1.05,0,1,1),
                    bbox_transform=ax.transAxes,
                    borderpad=0)
  
imM=ax.imshow(m, cmap='RdPu', vmin=0, vmax=50)
axins2 = inset_axes(ax,
                    width="5%",  # width = 40% of parent_bbox width
                    height="40%",  # height : 5%
                    loc='lower left',
                    bbox_to_anchor=(1.05, 0.6,1,1),
                    bbox_transform=ax.transAxes,
                    borderpad=0) 
               


fig.colorbar(imS, cax=axins1, format='%.0f').set_label(label=r'$\sigma_{R}$ [Å]', size=8)
fig.colorbar(imM, cax=axins2, format='%.0f').set_label(label=r'$\mu_{R}$ [Å]', size=8)



ax.set_xlabel('residue number')
ax.set_ylabel('residue number')
ax.set_xlim(-0.5, 269.5)
ax.set_ylim(269.5, -0.5)


ax_twin.set_xlim(-0.5, 269.5)
ax_twin.set_ylim(269.5, -0.5)
ax_twin.set_yticklabels([])
ax_twin.set_yticks([])



fig.savefig(distPath/'mean_std_300dpi.png',dpi=300, transparent=True)
fig.savefig(distPath/'mean_std.svg', transparent=True)

   
