This playbook perfoms a test of the rollback mechanism of `rpm-ostree`.  It
tests that the correct deployment is selected for boot after each rollback.

### Prerequisites
  - Configure subscription data (if used)

    If running against a RHEL Atomic Host, you should provide subscription
    data that can be used by `subscription-manager`.  See
    [common/rhel/subscribe.yaml](https://github.com/miabbott/atomic-host-tests/blob/test-readme/rhel/subscribe.yaml) for addiltional details.

### Running the Playbook

To run the test, simply invoke as any other Ansible playbook:

```
$ ansible-playbook -i inventory main.yaml
```

*NOTE*: You are responsible for providing a host to run the test against and the
inventory file for that host.

