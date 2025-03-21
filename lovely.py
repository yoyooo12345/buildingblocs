import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit.components.v1 as components
import random


st.title("Habitat Loss in endangered species")
st.subheader("By Team Packers")
st.header("THE PROBLEM")

years = [1980, 1985, 1990, 1995 ,2000, 2005, 2010, 2015, 2020
]

melted_area = [0, 400000, 750000, 1000000, 900000 ,1500000, 1600000, 1750000, 2000000

]

fig, ax = plt.subplots(1,1)
ax.plot(years, melted_area)
ax.set_title("Sea Ice Loss")
ax.set_xlabel("Year")
ax.set_ylabel("Melted Area (KM²)")
st.pyplot(fig)

st.subheader("We need to do more. Polar bears are losing their habitats... and they're not the only ones.")

st.subheader("Poaching")
st.write("Asian elephants are poached for their ivory tusks and other body parts.")

st.subheader("Habitat Loss and Degradation")
st.write("Coastal development, pollution, and climate change-related issues like rising sea levels and storm surges, destroy or damage nesting and foraging habitats. ")



st.title("Conservation Actions Done for the Wildlife")
np.random.seed(42)
n_movies = 100
genres = ["Polar Bears", "Green Sea Turtles", "Asian Elephants", "All"]
data = {
    "Genre": np.random.choice(genres, n_movies),
}
df = pd.DataFrame(data)


#  TASK 4.1: Move the following components to an st.sidebar.
st.header("Filters")
selected_genres = st.multiselect("Select animals:", options=genres, default=genres)




data = {'Animals': ['Polar Bears', 'Polar Bears',
           'Green Sea Turtles', 'Green Sea Turtles', 'Green Sea Turtles', 'Green Sea Turtles',
           'Asian Elephants', 'Asian Elephants', 'Asian Elephants',
           'All'],
        'Stakeholders': ['Communities, Industries', 'Arctic Communities',
             'Fisheries', 'WWF, Governments, Industries, Communities', 'WWF, Governments, Industries, Communities', 'Researchers',
             'WWF, Local Communities', 'WWF, Local  Communities', 'Governments',
             'Governments, Organisations, Schools'],
        'Action': ['Mitigation against climate change', 'Reducing human-polar bear conflict',
                   'Reducing bycatch', 'Establishment of Marine Protected Areas', 'Reduction of overharvesting and illegal trade', 'Satellite tracking',
                   'Protecting habitats (e.g. biological corridors, protected areas)', 'Reducing human-elephant conflict (e.g. fencing of settlements)', 'Anti-poaching laws',
                   'Education and raising awareness'],
        'Rationales': ['Reduce greenhouse gases that give rise to global warming that melts habitats', 'Reduce killing of polar bears due to disturbance to arctic community',
                       'Reduce number of turtles being unintentionally discarded and killed', 'Ensures turtles have safe places to carry out daily routines for proper development and reproduction', 'Reduce number of turtles being killed for shells, meat and eggs', 'Tracks turtles migration patterns and feeding areas to anticipate where turtles may contact fishing gear, then implementing physical protection measures',
                       'Ensures elephants have safe places to carry out daily routines for proper development and reproduction', 'Reduce killing of elephants due to disturbance to community', 'Reduce number of elephants killed for skin, tusks etc.',
                       'Enlightens the public about conservation, leading more more people taking action']}
df = pd.DataFrame(data)
st.title("Conservation Actions Done for the Wildlife")
st.dataframe(df) 
print(df.loc[df['Animals'] == '___'])


st.subheader("But we can do more!")

st.title("WHAT WE CAN DO")
st.image("C:/Users/User/buildingblocs/public/picture.jpg")


st.image("C:/Users/User/buildingblocs/public/pictyures.jpg")

st.image("C:/Users/User/buildingblocs/public/asdfasd.jpg")
