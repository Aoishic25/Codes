import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

#Treemap 1
'''
world_data=pd.read_csv(r'/Users/aoishonthgo/Downloads/countries of the world.csv')
print(world_data.head())

fig=px.treemap(world_data,
               path=['Region','Country'],
               values='Population',
               color='GDP ($ per capita)',
               color_continuous_scale='Plasma',   #Viridis, Plasma, RdBu
               width=1000,height=600,
               title="World Population Distribution Color-encoded by GDP")
fig.show()'''

#Treemap 2
df=pd.read_csv(r'/Users/aoishonthgo/Downloads/Pokemon.csv')
labels = np.array(['HP','Attack','Defense','Sp. Atk','Sp. Def','Speed'])

#1. Get stats for Bannette (index 386) and Duskull
stats_bannette=df.loc[386,labels].values
stats_duskull=df[df['Name']=='Duskull'][labels].values[0]

#2. Close the circular plots
angles=np.linspace(0,2*np.pi,len(labels),endpoint=False)
stats_bannette=np.concatenate((stats_bannette,[stats_bannette[0]]))
stats_duskull=np.concatenate((stats_duskull,[stats_duskull[0]]))
angles=np.concatenate((angles,[angles[0]]))

#3. Plotting
fig=plt.figure()
ax=fig.add_subplot(111,polar=True)

#First Pokemon (Bannette)
ax.plot(angles,stats_bannette,'o-',linewidth=2,label='Bannette')
ax.fill(angles,stats_duskull,alpha=0.25)

#Second Pokemon (Duskell)
ax.plot(angles,stats_duskull,'o-',linewidth=2,label='Duskull')
ax.fill(angles,stats_duskull,alpha=0.25)

#Formatting
ax.set_thetagrids((angles*180/np.pi)[0:6],labels)
plt.title('Bannette v/s Duskull')
plt.legend(loc='upper right',bbox_to_anchor=(1.3, 1.1))
plt.grid(True)
plt.show()