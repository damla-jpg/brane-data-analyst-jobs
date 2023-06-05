# brane-data-analyst-jobs
## Requires
[brane](https://github.com/epi-project/brane)

## Building
```
cd brane-data-analyst-jobs
```

Build the dataset entity for brane (only needs to be done once at the beginning)
```
brane data build <path_to_data.yml>
```

Build the code that executes the data
```
brane build <path_to_container.yml>  # builds packages individually
OR
./build.sh    # builds all 3 packages
```

## Testing
```
brane test <package_name>
```
then use arrow keys and enter to select your preferred option

## Running
After building the packages:
```bash
brane run pipeline.bs   # requires visualization and compute
OR
brane run pandas_sample.bs  # requires panda_branes
```

## Errors
### Docker sock not found
**Error**:
```
error: Failed to execute workflow: Failed to execute task 'give_row' (image 'compute:1.0.0@sha256:5eafe9911e86c492d4965cbf48694ce72c6b4b925d7dc8782e01a588aa038ff7') as a Docker container: Failed to inspect image 'compute:1.0.0' (sha256:5eafe9911e86c492d4965cbf48694ce72c6b4b925d7dc8782e01a588aa038ff7): error trying to connect: No such file or directory (os error 2)

error: Failed to run offline VM: Failed to run workflow: Failed to execute workflow: Failed to execute task 'give_row' (image 'compute:1.0.0@sha256:5eafe9911e86c492d4965cbf48694ce72c6b4b925d7dc8782e01a588aa038ff7') as a Docker container: Failed to inspect image 'compute:1.0.0' (sha256:5eafe9911e86c492d4965cbf48694ce72c6b4b925d7dc8782e01a588aa038ff7): error trying to connect: No such file or directory (os error 2)

```
**Cause**:
`docker.sock` file is not in the place brane expected.

**Solution**:
Run
```
sudo find / -name "docker.sock"
```
and copy the location on the `docker.sock`

Now run
```
brane test -s <copied_location> <package_name>
```
the `-s` tells brane to use the sock at a specific location

## Example
```
brane data build ./data/jobs/data.yml
brane build ./packages/compute/container.yml
brane test compute
OR
brane test -s /home/copied/path/to/docker.sock compute
```

One liner:
```
brane data build ./data/jobs/data.yml && brane build ./packages/compute/container.yml && brane test compute
```
