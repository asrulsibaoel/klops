<!-- markdownlint-disable -->

# Tutorials and API Overview  

## Tutorials  
- [`Klops Experiment`](/docs/tutorial.experiment.md): The complete tutorials on how to deal with machine learning experiments using Klops.
- [`Klops Deployment`](/docs/tutorial.deployment.md): The complete tutorials on how to deploy our machine learning projects.
- [`Klops Versioning`](/docs/tutorial.versioning.md): The complete tutorials on how to deal with data versioning. 

## Modules  

- [`experiment.experiment`](./experiment.experiment.md#module-experimentexperiment):  Main module for Klops MLflow Experiment.
- [`experiment.runner.base`](./experiment.runner.base.md#module-experimentrunnerbase):  The base abstract module for experiment runner.
- [`experiment.runner.basic`](./experiment.runner.basic.md#module-experimentrunnerbasic):  The basic implementation of experiment runner without any tuner.
- [`experiment.runner.gridsearch`](./experiment.runner.gridsearch.md#module-experimentrunnergridsearch):  The GridsearchCV implementation for experiment runner. 
- [`experiment.runner.hyperopt`](./experiment.runner.hyperopt.md#module-experimentrunnerhyperopt):  The hyperopt implementation for experiment runner.
- [`seldon_core`](./seldon_core.md#module-seldon_core): The Deployment init module.
- [`seldon_core.auth`](./seldon_core.auth.md#module-seldon_coreauth): Initial modules for auth.
- [`seldon_core.auth.default`](./seldon_core.auth.default.md#module-seldon_coreauthdefault): Default Module for Authentication Implementation
- [`seldon_core.auth.gke`](./seldon_core.auth.gke.md#module-seldon_coreauthgke): Google Kubernetes Engine (GKE) Module for Authentication Implementation
- [`seldon_core.auth.schema`](./seldon_core.auth.schema.md#module-seldon_coreauthschema): Kubernetes authentication Basic Schema module.
- [`seldon_core.deployment`](./seldon_core.deployment.md#module-seldon_coredeployment): Deployment Module for Seldon Core.
- [`seldon_core.exception`](./seldon_core.exception.md#module-seldon_coreexception): Seldon deployment exception handler module.
- [`versioning.helper`](./versioning.helper.md#module-versioninghelper):  The helper modules.
- [`versioning.versioning`](./versioning.versioning.md#module-versioningversioning):  The main versioning module.

## Classes  

- [`experiment.Experiment`](./experiment.experiment.md#class-experiment): 
- [`base.BaseRunner`](./experiment.runner.base.md#class-baserunner):  The base runner abstract module.
- [`basic.BasicRunner`](./experiment.runner.basic.md#class-basicrunner):  The basic implementation class for Experiment.
- [`gridsearch.GridsearchRunner`](./experiment.runner.gridsearch.md#class-gridsearchrunner):  The GridsearchCV implementation class for Experiment.
- [`hyperopt.HyperOptRunner`](./experiment.runner.hyperopt.md#class-hyperoptrunner):  The Hyperopt implementation class for Experiment.
- [`default.DefaultAuthentication`](./seldon_core.auth.default.md#class-defaultauthentication): Default Class Implementation for Kubernetes authentication.
- [`gke.GKEAuthentication`](./seldon_core.auth.gke.md#class-gkeauthentication): Google Kubernetes Engine (GKE) Class Implementation for Kubernetes authentication.
- [`schema.AbstractKubernetesAuth`](./seldon_core.auth.schema.md#class-abstractkubernetesauth): Abstract Class for Kubernetes get authentication
- [`deployment.SeldonDeployment`](./seldon_core.deployment.md#class-seldondeployment):  The main class to deploy the model.
- [`exception.SeldonDeploymentException`](./seldon_core.exception.md#class-seldondeploymentexception): Seldon Deployment Exception Class Handler.
- [`versioning.Versioning`](./versioning.versioning.md#class-versioning):  The main class for data versioning.

## Functions  

- [`experiment.start_experiment`](./experiment.experiment.md#function-start_experiment):  Start the experiments.
- [`helper.shell_executor`](./versioning.helper.md#function-shell_executor):  Shell executor helper.


---

_This documentation was developed by Koinworks Data Team._
