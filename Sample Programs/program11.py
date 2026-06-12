def clean_data(df, is_null_value_fill=False, is_null_drop=False):
    if is_null_drop:
        new_df=df.drop_na()
        return new_df
    elif is_null_value_fill:
        new_df=df.ffill()

def get_EDA(df):
    pass
    # 

while True:
    pass 
    # Take user input as file or file path
    # ask user to enter 1 or 2 or 0