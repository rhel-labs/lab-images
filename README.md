# Purpose
Build container images (traditional and bootc) used in labs.

## Image types
There are two basic types of images:
- infrastructure
- exercise targets

### Infrastructure images
These are used during labs to provide services for the environment or the user. 
These update based on need, renovate process

example: The internal lab container registry

### Excercise targets
These are directly interacted with by the lab user and referred to during exercise blocks. 
These are updated based on the schedule and behavior, manual process

example: Image mode reinstall target
