# atomic-host-tests
This repo will contain a number of Ansible playbooks that can be used to run
tests against an Atomic Host.

### Why Ansible?
The reasons for choosing Ansible playbooks are mainly 1) ease of use, 2)
portability, and 3) simplicity.

1. Ansible is a well-known tool and there is plenty of documentation
available for users to rely on.

1. Ansible requires only a small amount of functionality on the system
under test (basically SSH), so playbooks can be used across multiple
platforms with little changes necessary.

1. Fail fast and early.  When a task in Ansible fails, the whole playbook
fails (for the most part).  Thus, if something fails during the execution,
that is a good indication that something broke.

### Directory Layout
The directory structure attempts to break out functionality into separate
sub-directories where appropriate.  For example, the `common` directory has
a set tasks that could be run anywhere and the `rhel` directory contains
tasks would only be run on RHEL Atomic Host.

The tests use `include:` to bring in tasks to the playbook rather than using
roles.  This was done in hopes that re-use of tasks could be achieved rather
than copying the same tasks into a role structure for each playbook.

### Running Playbooks
Please see the individual test directories for details on how to run the
playbooks and any specific options/configurations that are required.

For example, the [new tree smoketest README](/tests/new-tree-smoketest/README.md).
