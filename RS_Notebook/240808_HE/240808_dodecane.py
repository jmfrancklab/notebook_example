# In[1]:

get_ipython().magic(u'load_ext pyspecdata.ipy')
from itertools import cycle
import matplotlib.pyplot as plt
import numpy as np

# Samples name
# 1. 10 mM TEMPO-SO4 w0 = 20 in dodecane, filename: 240808_10mM_TS_W20_C10
# 2. 10 mM TEMPO-SO4 w0 = 30 in dodecane, filename: 240808_10mM_TS_W30_C10
# 3. 31.6 mM TEMPO-SO4 w0 = 20 in dodecane, filename: 240808_31.6mM_TS_W20_C10
# 4. 31.6 mM TEMPO-SO4 w0 = 30 in dodecane, filename: 240808_31.6mM_TS_W30_C10
# 5. 100 mM TEMPO-SO4 w0 = 20 in dodecane, filename: 240808_100mM_TS_W20_C10
# 6. 100 mM TEMPO-SO4 w0 = 30 in dodecane, filename: 240808_100mM_TS_W30_C10

d10_w20 = find_file("240808_10mM_TS_W20_C10.DSC", exp_type = "francklab_esr/romana") # 10 mM TEMPO-SO4 w0 = 20 in dodecane
d10_w30 = find_file("240808_10mM_TS_W30_C10.DSC", exp_type = "francklab_esr/romana") # 10 mM TEMPO-SO4 w0 = 30 in dodecane

d31_w20 = find_file("240808_31.6mM_TS_W20_C10.DSC", exp_type = "francklab_esr/romana") # 31.6 mM TEMPO-SO4 w0 = 20 in dodecane
d31_w30 = find_file("240808_31.6mM_TS_W30_C10.DSC", exp_type = "francklab_esr/romana") # 31.6 mM TEMPO-SO4 w0 = 30 in dodecane

d100_w20 = find_file("240808_100mM_TS_W20_C10.DSC", exp_type = "francklab_esr/romana") # 100 mM TEMPO-SO4 w0 = 20 in dodecane
d100_w30 = find_file("240808_100mM_TS_W30_C10.DSC", exp_type = "francklab_esr/romana") # 100 mM TEMPO-SO4 w0 = 30 in dodecane

# In[2]:

d10_w20.chunk_auto("harmonic", "harmonic")  # the harmonic is typically stored so that we need to do this
d10_w20 = d10_w20['phase',0]['harmonic',0]

d10_w30.chunk_auto("harmonic", "harmonic")  # the harmonic is typically stored so that we need to do this
d10_w30 = d10_w30['phase',0]['harmonic',0]

d31_w20.chunk_auto("harmonic", "harmonic")  # the harmonic is typically stored so that we need to do this
d31_w20 = d31_w20['phase',0]['harmonic',0]

d31_w30.chunk_auto("harmonic", "harmonic")  # the harmonic is typically stored so that we need to do this
d31_w30 = d31_w30['phase',0]['harmonic',0]

d100_w20.chunk_auto("harmonic", "harmonic")  # the harmonic is typically stored so that we need to do this
d100_w20 = d100_w20['phase',0]['harmonic',0]

d100_w30.chunk_auto("harmonic", "harmonic")  # the harmonic is typically stored so that we need to do this
d100_w30 = d100_w30['phase',0]['harmonic',0]

# In[3]:

figure(dpi=300, figsize=(8,4))
plot(d10_w20, label="$w_0 = 20$")
plot(d10_w30, label="$w_0 = 30$")
title("10 mM TEMPO-SO$_4$ in Dodecane")
legend()

# In[4]:

figure(dpi=300, figsize=(8,4))
plot(d31_w20, label="$w_0 = 20$")
plot(d31_w30, label="$w_0 = 30$")
title("31.6 mM TEMPO-SO$_4$ in Dodecane")
legend()

# In[5]:

figure(dpi=300, figsize=(8,4))
plot(d100_w20, label="$w_0 = 20$")
plot(d100_w30, label="$w_0 = 30$")
title("100 mM TEMPO-SO$_4$ in Dodecane")
legend()

# In[6]:

figure(dpi=300, figsize=(8,10))
plot(d10_w20, label="10 mM $w_0 = 20$")
plot(d10_w30, label="10 mM $w_0 = 30$")
offset = 50
plot(d31_w20+offset, label="31.6 mM $w_0 = 20$")
plot(d31_w30+offset, label="31.6 mM $w_0 = 30$")
offset = 100
plot(d100_w20+offset, label="100 mM $w_0 = 20$")
plot(d100_w30+offset, label="100 mM $w_0 = 30$")
title("TEMPO-SO$_4$ in Dodecane")

#reversing legend order
handles, labels = plt.gca().get_legend_handles_labels()
legend(handles[::-1], labels[::-1])

# modifying number of gridlines
import matplotlib.ticker as ticker

ax = plt.gca()

# Major grid lines
ax.xaxis.set_major_locator(ticker.MultipleLocator(20))  # Change 1 to your desired major grid spacing
ax.yaxis.set_major_locator(ticker.MultipleLocator(50)) # Change 50 to your desired major grid spacing

#ax.set_yticklabels([])

# # Minor grid lines
ax.xaxis.set_minor_locator(ticker.MultipleLocator(10))  # Change 0.5 to your desired minor grid spacing
ax.yaxis.set_minor_locator(ticker.MultipleLocator(25))  
grid(which='both')

# In[7]:


