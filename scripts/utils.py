import pandas as pd
import joblib

def display_top_features(model, feature_names, top_n=10):
    """
    Display the top features with the highest impact based on the ElasticNet model coefficients.

    Parameters:
    model (ElasticNetCV): Fitted ElasticNet model.
    feature_names (list): List of feature names.
    top_n (int): Number of top features to display.

    Returns:
    pd.DataFrame: DataFrame containing the top features and their coefficients.
    """
    coefficients = model.coef_
    coeff_df = pd.DataFrame({'Feature': feature_names, 'Coefficient': coefficients})
    coeff_df['abs_Coefficient'] = coeff_df['Coefficient'].abs()
    sorted_coeff_df = coeff_df.sort_values(by='abs_Coefficient', ascending=False)

    top_features = sorted_coeff_df.head(top_n)
    print(top_features[['Feature', 'Coefficient']])
    return top_features

def main():
    # Load the ElasticNet model
    elasticnet_model = joblib.load('models/elasticnet_model.joblib')
    
    # Load the feature names
    coeff_df = pd.read_csv('data/processed/elasticnet_coefficients.csv')
    feature_names = coeff_df['Feature'].tolist()
    
    # Display the top features
    top_features = display_top_features(elasticnet_model, feature_names)
    top_features.to_csv('data/processed/top_features.csv', index=False)
    print("Top features saved to data/processed/top_features.csv")

if __name__ == "__main__":
    main()
