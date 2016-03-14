## Staging

* To ssh use: `ssh root@my.staging.server.com -p41278`, password is `NEVERPUTREALPASSWORDONGITHUB`.
* All running projects are deployed in (or symlinked to): `/opt/wix/project_name`:
	* The configuration files are in `etc`.
	* The actual jar (sometimes more than 1 version) is in `webapp`.
	* You can change the actual jar that is being run by the service by changing 	  the xml file located in `context`.
* In order to start/restart all services use `startall`/`restartall`.
* All installed Wix services can be seen at `/etc/init.d`, can use start/stop/status like normal services.
* Logs are in `/var/logs`:
	* `insane.log` contains EVERYTHING.
	* `sane.log` does not.
	* Requests are in `service_name_requests.log`.
	* Experiment results are in `service_name_wix.bi`.

### Chix

* Chix is a UI that enables you to see and modify all the Wix projects that are deployed on the machine.
* Located at `chix.stagingserverdomain.wix.com`.
* Enables remote debugging on port `service_running_port + 2`.
* To restart a deployment that was started from the UI (even if it failed) use `chef-client`, this will make chef run the last recipe it was requested to run.
* If you see `running exception handlers` at the end of the deployment logs it does not mean that the deployment failed.

### Jako
* Makes the staging environment as close as possible to the production environment.
* Enables copying of all FT and A/B tests.
* Can copy all data for a specific user in order to debug something in that specific users' flow.
* When copying production data (like FT for instance) it will be copied for all projects that are deployed on the machine.