# Working with Petri
## Introduction

* [Petri FAQ](https://kb.wixpress.com/pages/viewpage.action?title=Petri&spaceKey=hoopoe)
* Petri can be used for feature toggles (by devs) and for A/B testing (product).
* Typical flow after opening an experiment:
    * When a user visits the site eligibility for a given experiment is checked.
    * 50% chance to get either A or B by each user.
    * Result is logged for BI.
    * Conversion rate is measured from aggregated data and analyzed.
    * Expand the experiment scope or change the experiment probabilities.
    * Make a decision, either 100% for A or B for A/B test or ON/OFF for FTs.
    * Remove the code related to the experiment.
    * Close the experiment (via guineapig) and delete the spec.
* There are 2^N different redering possibilities for a user, either A or B for each experiment.
* Specs:
    * Definition of a test key and scope (who is the user run for).
    * Created by devs in client or server code.
* Experiment:
    * Conducted in code by devs.
* A/B Test vs Feature Toggle:
    * Feature toggle - test a specific feature for a given population.
    * A/B Test - Random selection of either version A or version B with given probabilities.
    * A/B tests persist via cookie or via DB for registered users.
    * Feature Toggles have no BI or persistence.
    * FTs do not log to BI, need to track errors.
* Filters:
    * Enables gradula exposure.
    * All sorts of filters exists such as population filters, wix users only, wix employees.
    * Custom criterion filters can also be defined.
    * Exclusion filters can be comnstructed by geolocation.
    * DO NOT USE `In Meta Sites`.
    
* Some pages (like My Account) can only run experiments for registered users.
* To define a spec extend the `SpecDefiniion` class and override `customize` using the `ExperimentSpecBuilder`.
* When calling `laboratory.condectExperiment` the result is logged to BI.
* It is possible to call all experiments for a scope using `laboratory.conductAllInScope` (**DO NOT CONDUCT FOR A SCOPE THAT IS NOT YOURS!**).
* Note that the call to `conductExperiment` does not have to be called when the page is loaded (depending on the experiment).
* Whenever a GA is done lifecycle triggers a call to `sync-specs` that will scan the JAR and add all specs to the main BI logging system.
* Experiments can be created in Guineapig (both A/B tests and FTs).
* The system ensures a consistent experience for a given user, therefore it is not possible to un-expand the scope of an experiment.
* The convention is that `A` is the old behaviour and `B` is the new behaviour (important for statistical reasons).
* Editor experiments that affect users cannot be used as experiments on public view for users of users.
* When running an experiment on a public view the information is not stored via cookie (since it is a user site), therefore you need to set a unique identifier for a user (such as customerID in E-Comm).

## Defining an Experiment In Guineapig
* When defining an Experiment via guineapig the terms Scope and Product are interchangeable.
* Always add a detailed description when creating an experiment.
* The creators of experiments/specs that are about to be closed or are stale are informed of this via email.
* It is possible to duplicate an experiment.
* A history of the experiment changes is saved and can be viewed via guineapig.
* Under `Experiment Report` is it possible to see how many users got A or B and a breakdown by specific servers.
* It is possible by using the `Override Parameters` to force an experiment for a given session (good for QA/debugging), simply copy the parameters to the request URL.
* Under `View Specs` you can see all available specs and also delete them (good for debugging problems).
* When a user overlaps for 2 test groups (such as a US user that uses EN language) it is not possible to know which experiment will run (assuming both experiments share the same spec).