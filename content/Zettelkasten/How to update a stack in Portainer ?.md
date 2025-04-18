When deploying a service through docker compose and using portainer, you basically need to do the following : 

* stop the stack, 
* make sure all containers have been deleted, 
* Go to the editor of the Stack
![[Pasted image 20250418122020.png]]
* (optionaly) make any modifications on the images mentioned in the compose file if required
* click *Update the stack* and *re-pull image and redeploy*

![[Pasted image 20250418121928.png]]