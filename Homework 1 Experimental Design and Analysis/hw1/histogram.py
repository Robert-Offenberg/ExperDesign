import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

# loading df2 from url
# URL to the CSV file
url = 'https://raw.githubusercontent.com/cam-alvarez/Personal-Portfolio-and-Blog/main/public/2020-tristatecounty-crashdata.csv'
df2 = pd.read_csv(url, low_memory=False, parse_dates=['CRASH_DATE'])

# Add month to dataframe

df2['MONTH']=df2['CRASH_DATE'].dt.month_name()


# Group by 'COUNTY_TXT' and 'CALENDAR_YEAR', then count crashes
crashes_by_county_year = df2.groupby(['MONTH', 'COUNTY_TXT']).size().reset_index(name='Crashes')
print (crashes_by_county_year)
# Plot histograms for each county using Seaborn
g = sns.histplot(df2, x='COUNTY_TXT', hue='MONTH')
#g.map(sns.histplot, 'Crashes')
plt.show()
