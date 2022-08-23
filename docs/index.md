<!-- markdownlint-disable -->

# API Overview

## Modules

- [`experiment.experiment`](./experiment.experiment.md#module-experimentexperiment): Main module for Klops MLflow Experiment.
- [`experiment.runner.base`](./experiment.runner.base.md#module-experimentrunnerbase): _summary_ The base abstract module for experiment runner.
- [`experiment.runner.basic`](./experiment.runner.basic.md#module-experimentrunnerbasic): _summary_ The basic implementation of experiment runner without any tuner.
- [`experiment.runner.gridsearch`](./experiment.runner.gridsearch.md#module-experimentrunnergridsearch): _summary_ The GridsearchCV implementation for experiment runner. 
- [`experiment.runner.hyperopt`](./experiment.runner.hyperopt.md#module-experimentrunnerhyperopt): _summary_ The hyperopt implementation for experiment runner.
- [`seldon_core`](./seldon_core.md#module-seldon_core): The Deployment init module.
- [`seldon_core.auth`](./seldon_core.auth.md#module-seldon_coreauth): Initial modules for auth.
- [`seldon_core.auth.default`](./seldon_core.auth.default.md#module-seldon_coreauthdefault): Default Module for Authentication Implementation
- [`seldon_core.auth.gke`](./seldon_core.auth.gke.md#module-seldon_coreauthgke): Google Kubernetes Engine (GKE) Module for Authentication Implementation
- [`seldon_core.auth.schema`](./seldon_core.auth.schema.md#module-seldon_coreauthschema): Kubernetes authentication Basic Schema module.
- [`seldon_core.deployment`](./seldon_core.deployment.md#module-seldon_coredeployment): Deployment Module for Seldon Core.
- [`seldon_core.exception`](./seldon_core.exception.md#module-seldon_coreexception): Seldon deployment exception handler module.
- [`versioning.helper`](./versioning.helper.md#module-versioninghelper): _summary_ THe helper modules.
- [`versioning.versioning`](./versioning.versioning.md#module-versioningversioning): _summary_ The main versioning module.

## Classes

- [`experiment.Experiment`](./experiment.experiment.md#class-experiment): _summary_
- [`base.BaseRunner`](./experiment.runner.base.md#class-baserunner): _summary_ The base runner abstract module.
- [`basic.BasicRunner`](./experiment.runner.basic.md#class-basicrunner): _summary_ The basic implementation class for Experiment.
- [`gridsearch.GridsearchRunner`](./experiment.runner.gridsearch.md#class-gridsearchrunner): _summary_ The GridsearchCV implementation class for Experiment.
- [`hyperopt.HyperOptRunner`](./experiment.runner.hyperopt.md#class-hyperoptrunner): _summary_ The Hyperopt implementation class for Experiment.
- [`default.DefaultAuthentication`](./seldon_core.auth.default.md#class-defaultauthentication): Default Class Implementation for Kubernetes authentication.
- [`gke.GKEAuthentication`](./seldon_core.auth.gke.md#class-gkeauthentication): Google Kubernetes Engine (GKE) Class Implementation for Kubernetes authentication.
- [`schema.AbstractKubernetesAuth`](./seldon_core.auth.schema.md#class-abstractkubernetesauth): Abstract Class for Kubernetes get authentication
- [`deployment.SeldonDeployment`](./seldon_core.deployment.md#class-seldondeployment): _summary_ The main class to deploy the model.
- [`exception.SeldonDeploymentException`](./seldon_core.exception.md#class-seldondeploymentexception): Seldon Deployment Exception Class Handler.
- [`versioning.Versioning`](./versioning.versioning.md#class-versioning): _summary_ The main class for data versioning.

## Functions

- [`experiment.start_experiment`](./experiment.experiment.md#function-start_experiment): _summary_ Start the experiments.
- [`helper.shell_executor`](./versioning.helper.md#function-shell_executor): _summary_ Shell executor helper.


---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
