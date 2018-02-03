import matplotlib.pyplot as plt
import numpy as np

a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)
plt.imshow(a, interpolation='NONE', cmap='bone', origin='lower')


plt.xticks(())
plt.yticks(())
plt.savefig('images3.jpg')
plt.show()