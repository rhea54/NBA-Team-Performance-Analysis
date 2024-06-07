import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import Ridge, LassoCV, ElasticNetCV
from sklearn.model_selection import cross_val_score

def fit_models(X, y):
    """
    Fit Ridge, Lasso, and ElasticNet models to the data and evaluate their performance.

    Parameters:
    X (np.ndarray): Feature matrix.
    y (np.ndarray): Target vector.

    Returns:
    dict: R-squared values for each model.
    ElasticNetCV: Fitted ElasticNet model.
    """
    results = {}

    # Fit the Ridge regression model with manual cross-validation
    ridge_alphas = np.logspace(-6, 6, 13)
    ridge_cv_scores = [cross_val_score(Ridge(alpha=alpha, max_iter=10000), X, y, cv=5).mean() for alpha in ridge_alphas]
    best_ridge_alpha = ridge_alphas[np.argmax(ridge_cv_scores)]
    ridge_model = Ridge(alpha=best_ridge_alpha, max_iter=10000)
    ridge_model.fit(X, y)
    results['Ridge'] = ridge_model.score(X, y)

    # Fit the Lasso regression model with cross-validation
    lasso_model = LassoCV(alphas=np.logspace(-6, 6, 13), cv=5, max_iter=10000)
    lasso_model.fit(X, y)
    results['Lasso'] = lasso_model.score(X, y)

    # Fit the ElasticNet regression model with cross-validation
    elasticnet_model = ElasticNetCV(alphas=np.logspace(-6, 6, 13), l1_ratio=[.1, .5, .7, .9, .95, .99, 1], cv=5, max_iter=10000)
    elasticnet_model.fit(X, y)
    results['ElasticNet'] = elasticnet_model.score(X, y)

    return results, elasticnet_model

def main():
    prepared_data = pd.read_csv('data/processed/prepared_data.csv')
    
    # Define the features and target
    features = prepared_data.columns.tolist()
    features.remove('W')
    X = prepared_data[features]
    y = prepared_data['W']

    # Standardize the features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Generate polynomial features
    poly = PolynomialFeatures(degree=2, include_bias=False)
    X_poly = poly.fit_transform(X_scaled)

    # Fit models and evaluate performance
    results, elasticnet_model = fit_models(X_poly, y)

    # Print the R-squared values
    for model_name, r_squared in results.items():
        print(f'R-squared for {model_name} regression: {r_squared:.2%}')

    # Save the ElasticNet model coefficients
    feature_names = poly.get_feature_names_out(features)
    coefficients = elasticnet_model.coef_
    coeff_df = pd.DataFrame({'Feature': feature_names, 'Coefficient': coefficients})
    coeff_df.to_csv('data/processed/elasticnet_coefficients.csv', index=False)
    print("Modeling completed. Coefficients saved to data/processed/elasticnet_coefficients.csv")

if __name__ == "__main__":
    main()





