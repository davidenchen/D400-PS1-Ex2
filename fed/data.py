def keep_countries(df, countries):
    try:
        return df[df["Country Name"].isin(countries)]
    except IndexError:
        raise("Country Name not in data frame columns")
    
def drop_cols(df, cols_to_drop):
    return df.drop(cols_to_drop, axis = 1)

def reshape_long(df, id_vars, var_name, value_name):
    return df.melt(id_vars, var_name=var_name, value_name=value_name)