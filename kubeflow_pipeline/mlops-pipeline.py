import kfp
from kfp import dsl

###components of the pipeline

def data_processing_op():
    return dsl.ContainerOp(
        name="Data Processing",
        image="rajamohan4urs/my-mlops-app:latest",
        command=["python", "src/data_processing.py"],
        )


def model_training_op():
    return dsl.ContainerOp(
        name="Model Training",
        image="rajamohan4urs/my-mlops-app:latest",
        command=["python", "src/model_training.py"],
        )

###pipeline definition
@dsl.pipeline(
    name="MLOps Pipeline",
    description="MLOps pipeline using Kubeflow Pipelines"
)

def mlops_pipeline():
    # Define the pipeline steps
    data_processing = data_processing_op()
    model_training = model_training_op().after(data_processing)

# Compile the pipeline
if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        pipeline_func=mlops_pipeline,
        package_path="mlops_pipeline.yaml"
    )