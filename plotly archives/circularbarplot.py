import matplotlib.pyplot as plt
import numpy as np

import arabic_reshaper
from bidi.algorithm import get_display

# Data
hashtags = ["خراسان", "فسازان", "ومپنا", "وفردا", "ودي", "کاما", "وثوق", "کدما", "دپارس", "ثنظام"]
values = [30.71, 21.65, 17.72, 17.65, 16.92, 15.94, 14.57, 14.22, 14.22, 14.22]
reshaped_hashtags=[]
for item in hashtags:
    reshaped_text= arabic_reshaper.reshape(item)
    bidi_text = get_display(reshaped_text)
    reshaped_hashtags.append(bidi_text)

# Convert values to a NumPy array for numerical operations
values = np.array(values)

# Parameters for the plot
N = len(reshaped_hashtags)
angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]  # Close the circular graph
values = np.append(values, values[0])  # Close the circular graph

# Set up the polar plot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
bars = ax.bar(angles[:-1], values[:-1], width=np.pi / 6, color=plt.cm.viridis(values[:-1] / max(values[:-1])), alpha=0.8)

# Customize the plot
ax.set_theta_offset(np.pi / 2)
ax.set_theta_direction(-1)

# Add labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(reshaped_hashtags, fontdict={'fontsize': 10}, va='center')
ax.yaxis.set_visible(False)  # Hide the radial axis

# Add title with Persian font
reshaped_text= arabic_reshaper.reshape("نمودار دایره‌ای هشتگ‌ها")
bidi_text = get_display(reshaped_text) 
plt.title(bidi_text, fontsize=15, va='bottom')

plt.show()



