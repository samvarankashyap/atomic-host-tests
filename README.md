# atomic-tests
A collection of tests for Atomic Host

This repo contains a number of Ansible playbooks that can be used to run
tests against an Atomic Host.

The directory structure attempts to break out functionality into separate
sub-directories where appropriate.  For example, the `common` directory has
a set tasks that could be run anywhere and the `rhel` directory contains
tasks would only be run on RHEL Atomic Host.

The tests use `include:` to bring in tasks to the test rather than roles.
This was done in hopes that re-use of tasks could be achieved rather than
copying the same tasks into a role structure for each test.

Please see the individual test directories for details about what the test
performs.
