This playbook performs a simple test of a new Atomic Host cloud image.  It
assumes that there is no upgrade or rollback available and confirms that
neither is possible right out of the box. This playbook should run on the
Atomic Host variants of CentOS, Fedora, and Red Hat Enterprise Linux.

### Prerequisites
  - Configure necessary variables

    Confirm that you have the desired values in [vars/smoketest_vars.yaml](https://github.com/miabbott/atomic-host-tests/blob/master/vars/smoketest_vars.yaml)

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

The tests includes tasks that collect information about the system and
generates files on the host with that information.  This was included as
backward compatibility with existing Jenkins jobs used at Red Hat.  See the
appendix sections below for examples of these files that are generated.

If you would like to skip these tasks:

```
$ ansible-playbook -i inventory main.yaml --skip-tags jenkins
```

#### Example Test Output from CentOS Atomic Host (using `--skip-tags jenkins`)
```
$ ansible-playbook -i "192.168.122.120," -u cloud-user tests/new-image-smoketest/main.yaml --skip-tags jenkins

PLAY [Atomic Host new image smoketest] ****************************************

GATHERING FACTS ***************************************************************
ok: [192.168.122.120]

TASK: [Determine if Atomic Host] **********************************************
ok: [192.168.122.120]

TASK: [Init the is_atomic fact] ***********************************************
ok: [192.168.122.120]

TASK: [Set the is_atomic fact] ************************************************
ok: [192.168.122.120]

TASK: [Fail if system is not an Atomic Host] **********************************
skipping: [192.168.122.120]

TASK: [Register with subscription-manager] ************************************
skipping: [192.168.122.120]

TASK: [Eliminate existing data directory] *************************************
changed: [192.168.122.120]

TASK: [Make data directory] ***************************************************
changed: [192.168.122.120]

TASK: [Check for available upgrade] *******************************************
changed: [192.168.122.120]

TASK: [Check for available rollback] ******************************************
changed: [192.168.122.120]

TASK: [Remove all subscriptions] **********************************************
skipping: [192.168.122.120]

TASK: [Unregister via subscription-manager] ***********************************
skipping: [192.168.122.120]

PLAY RECAP ********************************************************************
192.168.122.120            : ok=8    changed=4    unreachable=0    failed=0
```

