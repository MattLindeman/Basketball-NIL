import streamlit as st
import pandas as pd

prediction_df = pd.read_csv('2025Predictions.csv')
other_data_df = pd.read_csv('maindata.csv')
nil_df = pd.read_csv('NIL_Pred.csv')

st.title('BYU Basketball NIL Project')

st.write('2018-2024 Player Data from Sports Reference Website')
st.markdown('<sub>Filter options can be left blank and multiple options can be selected per filter</sub>', unsafe_allow_html=True)
st.markdown('<sub>If filter options selected are incompatable the full table will be displayed</sub>', unsafe_allow_html=True)

# Create filter options
players = sorted(other_data_df['Player'].unique())
teams = sorted(other_data_df['School'].unique())
conferences = sorted(other_data_df['Conf'].unique())
years = sorted(other_data_df['Year'].unique())

# Filter by players
selected_players = st.multiselect('Select Player(s)', players)
# Filter by teams
selected_teams = st.multiselect('Select Team(s)', teams)
# Filter by conferences
selected_conferences = st.multiselect('Select Conference(s)', conferences)
# Filter by years
selected_years = st.multiselect('Select Season(s)', years)

# Apply filters to the data
filtered_df = other_data_df[
    (other_data_df['Player'].isin(selected_players) if selected_players else other_data_df['Player'].notnull()) &
    (other_data_df['School'].isin(selected_teams) if selected_teams else other_data_df['School'].notnull()) &
    (other_data_df['Conf'].isin(selected_conferences) if selected_conferences else other_data_df['Conf'].notnull()) &
    (other_data_df['Year'].isin(selected_years) if selected_years else other_data_df['Year'].notnull())
]

# Display the filtered data or original data if no filters are selected
if filtered_df.empty:
    st.write(other_data_df.reset_index(drop=True))
else:
    st.write(filtered_df.reset_index(drop=True))


st.markdown('<h2>2025 Player Predictions<h2>', unsafe_allow_html=True)

# Merge the prediction_df with the Weighted_IWP column from nil_df
merged_df = prediction_df.merge(nil_df[['School', 'Player', 'Weighted_IWP']], on=['School', 'Player'], how='left')

# Rename the Weighted_IWP column to 'NIL%' if it exists
if 'Weighted_IWP' in merged_df.columns:
    merged_df.rename(columns={'Weighted_IWP': 'NIL%'}, inplace=True)

# Filter options
players = sorted(prediction_df['Player'].unique())
selected_player = st.selectbox('Select Player', [''] + players)

# Filter DataFrame based on selected player
filtered_df = prediction_df[prediction_df['Player'] == selected_player]

# Display player information, predicted metrics, and percentile ranks
if not filtered_df.empty:
    st.write(f"**Player:** {filtered_df['Player'].iloc[0]}  \n"
             f"**Class:** {filtered_df['Class'].iloc[0]}  \n"
             f"**Position:** {filtered_df['Pos'].iloc[0]}  \n"
             f"**School:** {filtered_df['School'].iloc[0]}  \n"
             f"**Conference:** {filtered_df['Conf'].iloc[0]}  \n"
             f"\n"
             f"**Predicted 2024-2025 Metrics:**  \n"
             f"PER: {filtered_df['Predicted_PER'].iloc[0]}   |   "
             f"BPM: {filtered_df['Predicted_BPM'].iloc[0]}   |   "
             f"WS/40: {filtered_df['Predicted_WS40'].iloc[0]}  \n"
             f"\n"
             f"**Percentile Ranks of Predicted Metrics:**  \n"
             f"PER Percentile Rank: {filtered_df['PER_Percentile_Rank'].iloc[0]}  |  "
             f"BPM Percentile Rank: {filtered_df['BPM_Percentile_Rank'].iloc[0]}   |    "
             f"WS/40 Percentile Rank: {filtered_df['WS40_Percentile_Rank'].iloc[0]}  \n"
             f"\n"
             f"**NIL Player Value:**  \n"
             f"Percent Worth of Team Budget: {merged_df['NIL%'][merged_df['Player'] == selected_player].iloc[0]}")
else:
    st.write("No data available for the selected player.")
    
st.markdown('<sub>Percentile ranks are compared to Big 12 players only</sub>', unsafe_allow_html=True)

st.markdown('<h2>2025 Player Predictions (by team)<h2>', unsafe_allow_html=True)

# Filter options
teams = sorted(merged_df['School'].unique())
selected_team = st.selectbox('Select Team', teams, index=teams.index('Brigham Young'))

# Filter DataFrame based on selected team
filtered_df_team = merged_df[merged_df['School'] == selected_team]

# Display the filtered DataFrame
st.write(filtered_df_team.reset_index(drop=True))