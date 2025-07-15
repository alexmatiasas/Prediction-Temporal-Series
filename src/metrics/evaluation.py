from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def evaluate_model(y_true, y_pred, name="Model"):
    mae = mean_absolute_error(y_true, y_pred)
    rmse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    
    print(f"{name} → MAE: {mae:.2f} | RMSE: {rmse:.2f} | R²: {r2:.4f}")
    return {"mae": mae, "rmse": rmse, "r2": r2}