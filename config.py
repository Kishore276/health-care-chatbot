# Model Training Configuration

## Data Preprocessing
batch_size = 32
validation_split = 0.2
test_split = 0.1
random_state = 42

## Feature Engineering
n_components_pca = 50
scaling_method = 'standard'  # 'standard' or 'minmax'

## Model Hyperparameters

### Random Forest
rf_n_estimators = 100
rf_max_depth = 20
rf_min_samples_split = 5
rf_min_samples_leaf = 2

### XGBoost
xgb_n_estimators = 200
xgb_max_depth = 7
xgb_learning_rate = 0.1
xgb_subsample = 0.8

### SVM
svm_kernel = 'rbf'
svm_C = 10
svm_gamma = 0.001

### Deep Learning
dl_epochs = 100
dl_learning_rate = 0.001
dl_dropout_rate = 0.3
dl_batch_size = 32

### LSTM
lstm_units_1 = 128
lstm_units_2 = 64
lstm_dropout = 0.3
lstm_epochs = 100

### CNN
cnn_filters_1 = 64
cnn_filters_2 = 128
cnn_kernel_size = 3
cnn_dropout = 0.4

## Training Settings
early_stopping_patience = 10
reduce_lr_patience = 5
checkpoint_monitor = 'val_accuracy'
checkpoint_mode = 'max'
