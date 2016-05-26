## Testing an artifact that changed to bootstrap-war:
1. Speak to server team and let them know you are doing this.
2. Change the parent in pom.xml to:
	
	```
    <parent>
        <groupId>com.wixpress</groupId>
        <artifactId>wix-server-bootstrap-war-parent</artifactId>
        <version>100.0.0-SNAPSHOT</version>
    </parent>
	```
3. Create a new repo from the original artifacts repo but change the `groupId` of the new artifact, for instance `<groupId>com.wixpress</groupId>` will become `<groupId>com.wixpress.test</groupId>` and leave the `artifactId` as is.
4. Goto lifecycle and add your new repo to CI.
5. RC and GA at least once.
6. Add a new service to fryingpan:
	* `Artifact Type` should be `auto-war`.
	* The port **MUST** be identical to the one defined in the original service.
	* Leave the `_api` and `RPC` mappings blank as well as the `Public Mount Point`.
	* Define the `Mount Point` to be the same as the original service.
	* Turn on `Is Bootstrap`.
7. If you want to test this on staging you can now simply deploy BOTH artifacts via `chix` and then make sure that your new artifact is the one running and listening on the port you defined.