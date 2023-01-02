import pandas as pd

def remove_rows_with_missing_ratings(df):
    """Remove rows with missing values in the rating columns."""
    return df[df['Cleanliness_rating'].notna() & df['Accuracy_rating'].notna() & df['Location_rating'].notna() & df['Check-in_rating'].notna() & df['Value_rating'].notna()]

def combine_description_strings(df):
    """Combine the list items in the "Description" column into the same string."""
    def remove_empty_quotes(string_list):
        """Remove empty quotes from a list of strings."""
        return [s for s in string_list if s]

    df['Description'] = df['Description'].apply(
        lambda x: x[16:] if isinstance(x, str) and x.startswith('About this space') else x
    )
    df['Description'] = df['Description'].apply(
        lambda x: ' '.join(remove_empty_quotes(x[1:-1].split(', '))) if isinstance(x, str) and x.startswith('[') else x
    )
    return df[df['Description'].notna()]

def set_default_feature_values(df):
    """Replace empty values in the "guests", "beds", "bathrooms", and "bedrooms" columns with the number 1."""
    df.loc[:, ['guests', 'beds', 'bathrooms', 'bedrooms']] = df[['guests', 'beds', 'bathrooms', 'bedrooms']].fillna(1)
    return df



def clean_tabular_data(df):
    """Clean the data in a tabular dataset."""
    df = remove_rows_with_missing_ratings(df)
    df = combine_description_strings(df)
    df = set_default_feature_values(df)
    return df

if __name__ == "__main__":
    # Load the raw data in using pandas
    df = pd.read_csv('listing.csv')
    # Call clean_tabular_data on it
    df = clean_tabular_data(df)
    # Save the processed data as clean_tabular_data.csv in the same folder as you found the raw tabular data.
    df.to_csv('listing_clean.csv', index=False)
