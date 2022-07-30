from collections import namedtuple


DataIngestionConfig=namedtuple("DataIngestionConfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])



# for data validation we only need schema file path . Wherever that schema file is located that path we need to specify
#DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path","report_file_path","report_page_file_path"])

# For feature Engineering 

#DataTransformationConfig = namedtuple("DataTransformationConfig", ["add_bedroom_per_room",
#                                                                   "transformed_train_dir",
#                                                                   "transformed_test_dir",
#                                                                   "preprocessed_object_file_path"])

# configuration for model training .
# when we train our model, we have to export that model as pickle file, so that location we can specify through 
# trained_model_file_path.
# If we are training our model and if my model is not giving better accuracy than our base accuracy 
# then we will not accept our model.

#ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["trained_model_file_path","base_accuracy"])

# model_evaluatio_file_path contain some file which will have information about all the models that are in production.
# time_stamp: whenever you are doing the comparison with the base model, at what time you have done that comparison, that
# time stamp we are going to store in that location 

#ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path","time_stamp"])

# export_dir_path: where I will export my trained model

#ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"])

# All above information we will provide through Yaml file . Just like csv file, excel file, jason file 

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"]) 