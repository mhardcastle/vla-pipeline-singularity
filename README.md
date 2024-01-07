# vla-pipeline-singularity
Singularity recipe for the JVLA initial calibration/self-cal pipeline for continuum data

Contains:
* This README file
* Singularity recipe to build the image
* Python file to handle startup of CASA with correct measurement set
* Pipeline script for CASA.

Note that the recipe relies on a UK mirror of the CASA download as the download from the US can be very slow. Update the `wget` line in the recipe if this is a problem for you.

## build instructions

* Clone this repository and change into the cloned directory
* Optionally, set `SINGULARITY_CACHEDIR` and `SINGULARITY_TMPDIR` environment variables to a temporary directory with a large amount of free space
* `singularity build --fakeroot casa.sif casa.singularity`

The `--fakeroot` can be omitted if you have root access.

## run instructions

* Create a directory containing one (only one) measurement set and otherwise empty -- pipeline output will go here
* Change into this directory
* Unset `PYTHONPATH` and `LD_LIBRARY_PATH` if set
* `singularity run -B``pwd`` /path/to/casa.sif`

(The `-B``pwd``` should not be necessary, but it seems to be...)

A complete run of the continuum, Stokes I calibration and
self-calibration pipeline with JVLA continuum data should now start --
it may take several days.
