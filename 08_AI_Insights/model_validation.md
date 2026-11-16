# Model Validation Notes

## Sales forecast

- Model: Linear Regression over monthly synthetic unit sales.
- Metric: Mean Absolute Error (MAE).
- Purpose: portfolio demonstration only; replace with time-series cross-validation and authorized sales history.

## Service risk

- Model: Logistic Regression predicting whether actual service time exceeds promised time.
- Features: promised minutes and actual minutes in the demonstration data.
- Metric: ROC-AUC.
- Limitation: actual minutes would not be available at prediction time in a production model; replace it with branch, service type, parts availability, booking load and vehicle age.
