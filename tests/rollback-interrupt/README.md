This playbook tests the ability to interrupt the `rpm-ostree rollback`
operation.  The system should not be negatively impacted after an interrupt
(or multiple interrupts) of the `rollback` operation.  Additionally, the
system should be able to complete a `rollback` operation after it had been
interrupted.

The playbook performs the interrupt via a bash script that is included at
[common/scripts/atomic_rollback_interrupt.sh](/common/scripts/atomic_rollback_interrupt.sh)

### Prerequisites
  - Configure subscription data (if used)

    If running against a RHEL Atomic Host, you should provide subscription
    data that can be used by `subscription-manager`.  See
    [rhel/subscribe.yaml](/rhel/subscribe.yaml) for addiltional details.

### Running the Playbook

To run the test, simply invoke as any other Ansible playbook:

```
$ ansible-playbook -i inventory main.yaml
```

To change the amount of times that the `rollback` operation should be interrupted,
you can use the `iterations` variable which can be passed to the playbook like this:

```
$ ansible-playbook -i inventory main.yaml -e "interations=10"
```

The default value for `iterations` is 1.

*NOTE*: You are responsible for providing a host to run the test against and the
inventory file for that host.

