<!-- markdownlint-disable -->

# Tutorials and API Overview  

## Tutorials  
- [`Klops Experiment`](/docs/tutorial.experiment.md): The complete tutorials on how to deal with machine learning experiments using Klops.
- [`Klops Deployment`](/docs/tutorial.deployment.md): The complete tutorials on how to deploy our machine learning projects.
- [`Klops Versioning`](/docs/tutorial.versioning.md): The complete tutorials on how to deal with data versioning.  

## Modules

- [`config`](./config.md#module-config): Config Module for generic purposes.
- [`experiment`](./experiment.md#module-experiment): The main experiment module
- [`experiment.exception`](./experiment.exception.md#module-experimentexception): Experiment exception module.
- [`experiment.experiment`](./experiment.experiment.md#module-experimentexperiment): Main module for Klops MLflow Experiment.
- [`experiment.runner`](./experiment.runner.md#module-experimentrunner): Main module tobe called for experiment runner.
- [`experiment.runner.base`](./experiment.runner.base.md#module-experimentrunnerbase): Base runner module.
- [`experiment.runner.basic`](./experiment.runner.basic.md#module-experimentrunnerbasic): Experiment Runner Module without tuner.
- [`experiment.runner.gridsearch`](./experiment.runner.gridsearch.md#module-experimentrunnergridsearch)
- [`experiment.runner.hyperopt`](./experiment.runner.hyperopt.md#module-experimentrunnerhyperopt)
- [`seldon_core`](./seldon_core.md#module-seldon_core): The Deployment init module.
- [`seldon_core.auth`](./seldon_core.auth.md#module-seldon_coreauth): Initial modules for Auhtentication method.
- [`seldon_core.auth.default`](./seldon_core.auth.default.md#module-seldon_coreauthdefault): Default Module for Authentication Implementation
- [`seldon_core.auth.gke`](./seldon_core.auth.gke.md#module-seldon_coreauthgke): Google Kubernetes Engine (GKE) Module for Authentication Implementation
- [`seldon_core.auth.schema`](./seldon_core.auth.schema.md#module-seldon_coreauthschema): Kubernetes authentication Basic Schema module.
- [`seldon_core.deployment`](./seldon_core.deployment.md#module-seldon_coredeployment): Deployment Module for Seldon Core.
- [`seldon_core.exception`](./seldon_core.exception.md#module-seldon_coreexception): Seldon deployment exception handler module.
- [`versioning`](./versioning.md#module-versioning): Versioning Control Main Module. Based on DVC.
- [`versioning.helper`](./versioning.helper.md#module-versioninghelper)
- [`versioning.versioning`](./versioning.versioning.md#module-versioningversioning): Main module for versioning Control.

## Classes

- [`exception.ExperimentFailedException`](./experiment.exception.md#class-experimentfailedexception): Experiment Failed Exception
- [`exception.InvalidArgumentsException`](./experiment.exception.md#class-invalidargumentsexception): Invalid Arguments Passed
- [`exception.LogMetricException`](./experiment.exception.md#class-logmetricexception): Log Metric Exception
- [`exception.UnknownExperimentTunerTypeException`](./experiment.exception.md#class-unknownexperimenttunertypeexception): Unknown Experiment Tunner Exception
- [`experiment.Experiment`](./experiment.experiment.md#class-experiment): Main class for MLflow Experiment. This class would wrap the MLFlow client and     it's experiments features.
- [`base.BaseRunner`](./experiment.runner.base.md#class-baserunner): Abstract class as Base runner implementation.
- [`basic.BasicRunner`](./experiment.runner.basic.md#class-basicrunner): Experiment Runner Implementation Class without tuner.
- [`gridsearch.GridsearchRunner`](./experiment.runner.gridsearch.md#class-gridsearchrunner): GridSearchCV Runner Implementation.
- [`hyperopt.HyperOptRunner`](./experiment.runner.hyperopt.md#class-hyperoptrunner): The HyperOptRunner Implementation.
- [`default.DefaultAuthentication`](./seldon_core.auth.default.md#class-defaultauthentication): Default Class Implementation for Kubernetes authentication.
- [`gke.GKEAuthentication`](./seldon_core.auth.gke.md#class-gkeauthentication): Google Kubernetes Engine (GKE) Class Implementation for Kubernetes authentication.
- [`schema.AbstractKubernetesAuth`](./seldon_core.auth.schema.md#class-abstractkubernetesauth): Abstract Class for Kubernetes get authentication
- [`deployment.SeldonDeployment`](./seldon_core.deployment.md#class-seldondeployment): CRUD Kubernetes operation class implementation for Seldon ML Deployment.
- [`exception.SeldonDeploymentException`](./seldon_core.exception.md#class-seldondeploymentexception): Seldon Deployment Exception Class Handler.
- [`versioning.Versioning`](./versioning.versioning.md#class-versioning): Versioning control for klops. Based on DVC.

## Functions

- [`experiment.start_experiment`](./experiment.experiment.md#function-start_experiment): The function that wrap all the basic Experiment class do. This make the process more easier.
- [`helper.shell_executor`](./versioning.helper.md#function-shell_executor): Command line executor wrapper.


---

_This documentation created with love by [Koinworks Data Team](https://koinworks.com)._
