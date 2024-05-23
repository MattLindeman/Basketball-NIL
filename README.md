# Basketball-NIL

This project is aimed around helping the BYU Basketball coaching staff determine, roughly, how much NIL money could be allocated to a player. I went about this by training a few machine learning models to predict how a players PER, BPM, and WS/40 would change going into the next season and if they were to transfer into the Big 12 Conference. The models use all of the statistics in the advanced player numbers section of the sports reference website. The models were trained on the previous 5 seasons of data (18-23). There is a separate model for each metric that is being predicted (PER, BPM, WS/40). The models are tested on how accurate they are at predicting the 23-24 (this year) season data, then fine tuned to minimize the error (numeric distance from actual player’s metrics). The projections are then heavily weighted to how a player performed this most recent season and attempts to project how they would play if they were in the Big 12 next season. Then the NIL% or NIL player worth budget number is calculated largely based on the average wins added by a player that typically has those numbers of PER, BPM, and WS/40.

I created a streamlit dashboard that makes it easy to look up players and their projected metrics/NIL value: [CBB NIL](https://byubasketballnil.streamlit.app)

### Files:

2025Predictions.csv contains the predicted metrics data

NIL_Pred.csv contains the predicted NIL value data

maindata.csv contains the player data from the sports reference website

main.py and requirements.txt are used to create the streamlit app

main.ipynb contains the code for how I manipulated the data and built the models
