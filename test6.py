import matplotlib.pyplot as plt
fig, axs = plt.subplots(2, 2)
for a in axs:
    a.imshow([0])

for a in axs:
    a.set_xticklabels([])
    a.set_yticklabels([])

plt.subplots_adjust(wspace=0, hspace=0)
plt.show()