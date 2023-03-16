import pandas as pd
import matplotlib.pyplot as plt

# load the data
df = pd.read_pickle('data/chi_Chat_time_series_most_crime_CBGs_06_19_updated.p')

# drop records before March 2019 as the average time open data for 311 requests is not present before then
df = df.loc[df['Date'] >= pd.datetime(2019,3,3)]

# loop through unique Census Block Groups and create separate plots for each
for cbg in df['Census Block Group'].unique():
    
    # subset the data for the current Census Block Group
    sub_df = df[df['Census Block Group'] == cbg]
    
    # create the plot
    fig, ax = plt.subplots(figsize=(6,6))
    #ax.plot(sub_df['Date'], sub_df['Total Crime'], label='Total Crime')
    ax.plot(sub_df['Date'], sub_df['Sanitation/Sewer Issue Average Time Open'], label='Sanitation/Sewer Issue Avg Time Open')
    ax.plot(sub_df['Date'], sub_df['Street Light Repairs Average Time Open'], label='Street Light Repairs Avg Time Open')
    ax.plot(sub_df['Date'], sub_df['Street Repairs Average Time Open'], label='Street Repairs Avg Time Open')
    ax.set_xlabel('Date')
    ax.set_ylabel('311 Request Ave. TIme Open in Days')
    ax.set_title('Census Block Group {}'.format(cbg))
    ax.legend()
    
    # set a separate y axis scale for the Total Crime variable
    ax2 = ax.twinx()
    ax2.plot(sub_df['Date'], sub_df['Total Crime'], label='Total Crime', color='grey')
    ax2.set_ylabel('Total Crime Count')
    ax2.tick_params(axis='y', labelcolor='black')
    ax2.legend()
    
    # rotate x axis label 90 degrees
    #plt.xticks(rotation=90)
    fig.autofmt_xdate(rotation=45)
    # show the plot
    plt.show()