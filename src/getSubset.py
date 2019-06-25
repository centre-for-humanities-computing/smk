import pandas as pd
# import a CSV into Pyhton with Panda
data_url = "sub_smk.csv"
df = pd.read_csv(data_url)

# get only the column with the urls
sub_df = df[['medium_image_url']]
# save as a CSV-file
sub_df.to_csv("sub_smk.csv")