This playbook performs a sanity test of a stable version of the OpenShift Ansible installer
against an Atomic Host.

The test accepts normal inventory data as like every other test in the repo, then uses that
data to generate a separate inventory that is used when running the OpenShift Ansible
installer playbook.

This playbook only does a sanity check that the installer completes successfully and
the expected pods are running afterwards.  This does **NOT** perform any conformance
testing or deployment of additional apps/projects afterwards.

### Prerequisites
  - Ansible version 2.2 (other versions are not supported)

  - Configure subscription data (if used)

    If running against a RHEL Atomic Host, you should provide subscription
    data that can be used by `subscription-manager`.  See
    [roles/redhat_subscription/tasks/main.yml](roles/redhat_subscription/tasks/main.yml)
    for additional details.


### Running the Playbook

To run the test, simply invoke as any other Ansible playbook:

```
$ ansible-playbook -i inventory tests/system-containers/main.yml
```

*NOTE*: You are responsible for providing a host to run the test against and the
inventory file for that host.
