This playbook performs a simple test of the upgrade and rollback mechanisms
that are present in an Atomic Host.  This playbook also supports testing
a new tree that was delivered via `rpm-ostree rebase`.  This playbook should
run on the Atomic Host variants of CentOS, Fedora, and Red Hat Enterprise Linux.

### Prerequisites
  - Configure necessary variables

    Confirm that you have the desired values in [vars/smoketest_vars.yaml](/vars/smoketest_vars.yaml)

  - Configure subscription data (if used)

    If running against a RHEL Atomic Host, you should provide subscription
    data that can be used by `subscription-manager`.  See
    [rhel/subscribe.yaml](/rhel/subscribe.yaml) for addiltional details.

### Running the Playbook

Before running the playbook, decide if you are testing the
`rpm-ostree upgrade` path or `rpm-ostree rebase` path.

When testing the `upgrade` path, you will need to exclude the `rpm_ostree_rebase`
tag, like so:

```
$ ansible-playbook -i inventory main.yaml --skip-tags rpm_ostree_rebase
```

When testing the `rebase` path, you will need to exclude the `rpm_ostree_upgrade`
tag and possibly the `subscription_manager` tag.  Additionally, you will need to
provide values to certain variables either individually via the command line or
via a YAML file on the command line.

```
$ ansible-playbook -i inventory main.yaml --skip-tags subscription_manager,rpm_ostree_upgrade -e "@rebase_vars.yaml"
```

Example YAML variable file:

```yaml
---
ostree_remote_name: "new-atomic"
ostree_remote_url: "https://dl.fedoraproject.org/pub/fedora/linux/atomic/24/"
ostree_refspec: "new-atomic:fedora-atomic/f24/x86_64/docker-host"
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

#### Example Test Output from Fedora Atomic Host
```
$ ansible-playbook -i inventory main.yaml

PLAY [Atomic Host new tree smoketest] *****************************************

GATHERING FACTS ***************************************************************
ok: [192.168.122.160]

TASK: [Determine if Atomic Host] **********************************************
ok: [192.168.122.160]

TASK: [Init the is_atomic fact] ***********************************************
ok: [192.168.122.160]

TASK: [Set the is_atomic fact] ************************************************
ok: [192.168.122.160]

TASK: [Fail if system is not an Atomic Host] **********************************
skipping: [192.168.122.160]

TASK: [Register with subscription-manager] ************************************
skipping: [192.168.122.160]

TASK: [Eliminate existing data directory] *************************************
changed: [192.168.122.160]

TASK: [Make data directory] ***************************************************
changed: [192.168.122.160]

TASK: [Gather list of installed RPMs] *****************************************
changed: [192.168.122.160]

TASK: [Get initial atomic version] ********************************************
changed: [192.168.122.160]

TASK: [Upgrade to latest tree] ************************************************
changed: [192.168.122.160]

TASK: [restart hosts] *********************************************************
<job 20977754493.1852> finished on 192.168.122.160

TASK: [wait for hosts to come down] *******************************************
ok: [192.168.122.160 -> 127.0.0.1]

TASK: [wait for hosts to come back up] ****************************************
ok: [192.168.122.160 -> 127.0.0.1]

TASK: [Gather list of installed RPMs] *****************************************
changed: [192.168.122.160]

TASK: [Get upgraded atomic version] *******************************************
changed: [192.168.122.160]

TASK: [Check /etc/redhat-release (RHEL)] **************************************
skipping: [192.168.122.160]

TASK: [Check /etc/redhat-release (Fedora)] ************************************
changed: [192.168.122.160]

TASK: [Check /etc/redhat-release (CentOS)] ************************************
skipping: [192.168.122.160]

TASK: [Record content of /etc/redhat-release] *********************************
changed: [192.168.122.160]

TASK: [Record content of /etc/os-release] *************************************
changed: [192.168.122.160]

TASK: [Record output from 'atomic host status'] *******************************
changed: [192.168.122.160]

TASK: [Extract version and commit ID from 'atomic host status'] ***************
changed: [192.168.122.160]

TASK: [Set facts (version, commit ID, redhat-release, os-release)] ************
ok: [192.168.122.160]

TASK: [Check for ostree signature] ********************************************
skipping: [192.168.122.160]

TASK: [Record ostree signature] ***********************************************
changed: [192.168.122.160]

TASK: [Collect info about "key" packages] *************************************
changed: [192.168.122.160] => (item=atomic)
changed: [192.168.122.160] => (item=docker)
changed: [192.168.122.160] => (item=docker-selinux)
changed: [192.168.122.160] => (item=etcd)
changed: [192.168.122.160] => (item=flannel)
changed: [192.168.122.160] => (item=kernel)
changed: [192.168.122.160] => (item=kubernetes)
changed: [192.168.122.160] => (item=kubernetes-client)
changed: [192.168.122.160] => (item=kubernetes-master)
changed: [192.168.122.160] => (item=kubernetes-node)
changed: [192.168.122.160] => (item=python-docker-py)

TASK: [Collect info about "atomic" packags] ***********************************
skipping: [192.168.122.160]

TASK: [Diff the RPM lists] ****************************************************
failed: [192.168.122.160] => {"censored": "results hidden due to no_log parameter", "changed": true, "rc": 1}
...ignoring

TASK: [Generate the smoke test content with a template] ***********************
changed: [192.168.122.160]

TASK: [Generate the version content with a template] **************************
changed: [192.168.122.160]

TASK: [Rollback to previous deployment] ***************************************
changed: [192.168.122.160]

TASK: [restart hosts] *********************************************************
<job 983452127592.2642> finished on 192.168.122.160

TASK: [wait for hosts to come down] *******************************************
ok: [192.168.122.160 -> 127.0.0.1]

TASK: [wait for hosts to come back up] ****************************************
ok: [192.168.122.160 -> 127.0.0.1]

TASK: [Remove all subscriptions] **********************************************
skipping: [192.168.122.160]

TASK: [Unregister via subscription-manager] ***********************************
skipping: [192.168.122.160]

PLAY RECAP ********************************************************************
192.168.122.160            : ok=31   changed=18   unreachable=0    failed=0

```

#### Appendix: Example 'atomic_smoke_output.txt'
```
# cat atomic_smoke_output.txt
# cat /etc/redhat-release
Fedora release 23 (Twenty Three)

# cat /etc/os-release
NAME=Fedora
VERSION="23 (Twenty Three)"
ID=fedora
VERSION_ID=23
PRETTY_NAME="Fedora 23 (Twenty Three)"
ANSI_COLOR="0;34"
CPE_NAME="cpe:/o:fedoraproject:fedora:23"
HOME_URL="https://fedoraproject.org/"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=23
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=23
PRIVACY_POLICY_URL=https://fedoraproject.org/wiki/Legal:PrivacyPolicy

# ostree show "6d9211c3fa"
commit 6d9211c3fa620d57787b9d3ae79af982202be9919d408f96eb35e4cc12b6a6a5
Date:  2016-03-02 21:10:48 +0000
Version: 23.75

Key Packages
atomic-1.8-3.gitcc5997a.fc23.x86_64
docker-1.9.1-6.git6ec29ef.fc23.x86_64
docker-selinux-1.9.1-6.git6ec29ef.fc23.x86_64
etcd-2.2.1-2.fc23.x86_64
flannel-0.5.4-1.fc23.x86_64
kernel-4.4.2-301.fc23.x86_64
kubernetes-1.1.0-0.17.git388061f.fc23.x86_64
kubernetes-client-1.1.0-0.17.git388061f.fc23.x86_64
kubernetes-master-1.1.0-0.17.git388061f.fc23.x86_64
kubernetes-node-1.1.0-0.17.git388061f.fc23.x86_64
python-docker-py-1.5.0-1.fc23.noarch

RPM Diffs between 23.70 and 23.75
====================================
--- initial_rpm_list.txt        2016-03-03 19:51:17.461000000 +0000
+++ upgraded_rpm_list.txt       2016-03-03 19:52:04.050000000 +0000
@@ -36,7 +36,7 @@
 crypto-policies-20151104-1.gitf1cba5f.fc23.noarch
 cryptsetup-1.6.8-2.fc23.x86_64
 cryptsetup-libs-1.6.8-2.fc23.x86_64
-curl-7.43.0-5.fc23.x86_64
+curl-7.43.0-6.fc23.x86_64
 cyrus-sasl-lib-2.1.26-25.2.fc23.x86_64
 dbus-1.10.6-1.fc23.x86_64
 dbus-glib-0.106-1.fc23.x86_64
@@ -87,7 +87,7 @@
 glibc-common-2.22-10.fc23.x86_64
 glib-networking-2.46.1-1.fc23.x86_64
 gmp-6.0.0-12.fc23.x86_64
-gnupg2-2.1.9-1.fc23.x86_64
+gnupg2-2.1.11-1.fc23.x86_64
 gnutls-3.4.9-1.fc23.x86_64
 gpgme-1.4.3-6.fc23.x86_64
 grep-2.22-6.fc23.x86_64
@@ -111,14 +111,14 @@
 iscsi-initiator-utils-6.2.0.873-29.git4c9d6f9.fc23.x86_64
 iscsi-initiator-utils-iscsiuio-6.2.0.873-29.git4c9d6f9.fc23.x86_64
 json-glib-1.0.4-2.fc23.x86_64
-kernel-4.3.5-300.fc23.x86_64
-kernel-core-4.3.5-300.fc23.x86_64
-kernel-modules-4.3.5-300.fc23.x86_64
+kernel-4.4.2-301.fc23.x86_64
+kernel-core-4.4.2-301.fc23.x86_64
+kernel-modules-4.4.2-301.fc23.x86_64
 keyutils-1.5.9-7.fc23.x86_64
 keyutils-libs-1.5.9-7.fc23.x86_64
 kmod-22-2.fc23.x86_64
 kmod-libs-22-2.fc23.x86_64
-krb5-libs-1.14-8.fc23.x86_64
+krb5-libs-1.14-9.fc23.x86_64
 kubernetes-1.1.0-0.17.git388061f.fc23.x86_64
 kubernetes-client-1.1.0-0.17.git388061f.fc23.x86_64
 kubernetes-master-1.1.0-0.17.git388061f.fc23.x86_64
@@ -137,7 +137,7 @@
 libcollection-0.7.0-27.fc23.x86_64
 libcom_err-1.42.13-3.fc23.x86_64
 libcroco-0.6.8-7.fc23.x86_64
-libcurl-7.43.0-5.fc23.x86_64
+libcurl-7.43.0-6.fc23.x86_64
 libdaemon-0.14-9.fc23.x86_64
 libdb-5.3.28-13.fc23.x86_64
 libdb-utils-5.3.28-13.fc23.x86_64
@@ -189,10 +189,10 @@
 libsolv-0.6.14-7.fc23.x86_64
 libsoup-2.52.2-1.fc23.x86_64
 libss-1.42.13-3.fc23.x86_64
-libssh2-1.6.0-3.fc23.x86_64
-libsss_idmap-1.13.3-3.fc23.x86_64
-libsss_nss_idmap-1.13.3-3.fc23.x86_64
-libsss_sudo-1.13.3-3.fc23.x86_64
+libssh2-1.6.0-4.fc23.x86_64
+libsss_idmap-1.13.3-5.fc23.x86_64
+libsss_nss_idmap-1.13.3-5.fc23.x86_64
+libsss_sudo-1.13.3-5.fc23.x86_64
 libstdc++-5.3.1-2.fc23.x86_64
 libtalloc-2.1.5-2.fc23.x86_64
 libtasn1-4.5-2.fc23.x86_64
@@ -243,9 +243,9 @@
 oddjob-0.34.3-1.fc23.x86_64
 oddjob-mkhomedir-0.34.3-1.fc23.x86_64
 openldap-2.4.40-14.fc23.x86_64
-openssh-7.1p2-3.fc23.x86_64
-openssh-clients-7.1p2-3.fc23.x86_64
-openssh-server-7.1p2-3.fc23.x86_64
+openssh-7.1p2-4.fc23.x86_64
+openssh-clients-7.1p2-4.fc23.x86_64
+openssh-server-7.1p2-4.fc23.x86_64
 openssl-1.0.2f-1.fc23.x86_64
 openssl-libs-1.0.2f-1.fc23.x86_64
 os-prober-1.70-1.fc23.x86_64
@@ -255,7 +255,7 @@
 p11-kit-trust-0.23.2-1.fc23.x86_64
 pam-1.2.1-2.fc23.x86_64
 passwd-0.79-6.fc23.x86_64
-pcre-8.38-5.fc23.x86_64
+pcre-8.38-6.fc23.x86_64
 pinentry-0.9.6-4.fc23.x86_64
 pkgconfig-0.28-9.fc23.x86_64
 plymouth-0.8.9-11.2013.08.14.fc23.x86_64
@@ -293,8 +293,8 @@
 python3-requests-2.9.1-1.fc23.noarch
 python3-setuptools-18.0.1-2.fc23.noarch
 python3-six-1.9.0-3.fc23.noarch
-python3-sssdconfig-1.13.3-3.fc23.noarch
-python3-urllib3-1.13.1-1.fc23.noarch
+python3-sssdconfig-1.13.3-5.fc23.noarch
+python3-urllib3-1.13.1-3.fc23.noarch
 python3-websocket-client-0.32.0-1.fc23.noarch
 python-chardet-2.2.1-3.fc23.noarch
 python-docker-py-1.5.0-1.fc23.noarch
@@ -305,7 +305,7 @@
 python-requests-2.9.1-1.fc23.noarch
 python-setuptools-18.0.1-2.fc23.noarch
 python-six-1.9.0-3.fc23.noarch
-python-urllib3-1.13.1-1.fc23.noarch
+python-urllib3-1.13.1-3.fc23.noarch
 python-websocket-client-0.32.0-1.fc23.noarch
 qrencode-libs-3.4.2-5.fc23.x86_64
 quota-4.02-4.fc23.x86_64
@@ -313,29 +313,29 @@
 readline-6.3-6.fc23.x86_64
 rootfiles-8.1-18.fc23.noarch
 rpcbind-0.2.3-6.rc1.fc23.x86_64
-rpm-4.13.0-0.rc1.11.fc23.x86_64
-rpm-build-libs-4.13.0-0.rc1.11.fc23.x86_64
-rpm-libs-4.13.0-0.rc1.11.fc23.x86_64
+rpm-4.13.0-0.rc1.12.fc23.x86_64
+rpm-build-libs-4.13.0-0.rc1.12.fc23.x86_64
+rpm-libs-4.13.0-0.rc1.12.fc23.x86_64
 rpm-ostree-2015.11-1.fc23.x86_64
-rpm-plugin-selinux-4.13.0-0.rc1.11.fc23.x86_64
-rpm-python3-4.13.0-0.rc1.11.fc23.x86_64
+rpm-plugin-selinux-4.13.0-0.rc1.12.fc23.x86_64
+rpm-python3-4.13.0-0.rc1.12.fc23.x86_64
 rsync-3.1.1-8.fc23.x86_64
 screen-4.3.1-2.fc23.x86_64
 sed-4.2.2-11.fc23.x86_64
-selinux-policy-3.13.1-158.6.fc23.noarch
-selinux-policy-targeted-3.13.1-158.6.fc23.noarch
+selinux-policy-3.13.1-158.7.fc23.noarch
+selinux-policy-targeted-3.13.1-158.7.fc23.noarch
 setools-console-3.3.8-8.fc23.x86_64
 setools-libs-3.3.8-8.fc23.x86_64
-setup-2.9.8-2.fc23.noarch
+setup-2.10.1-1.fc23.noarch
 shadow-utils-4.2.1-3.fc23.x86_64
 shared-mime-info-1.5-2.fc23.x86_64
 shim-0.8-8.x86_64
 slang-2.3.0-4.fc23.x86_64
 socat-1.7.2.4-5.fc23.x86_64
 sos-3.2-2.fc23.noarch
-sqlite-3.11.0-1.fc23.x86_64
-sqlite-libs-3.11.0-1.fc23.x86_64
-sssd-client-1.13.3-3.fc23.x86_64
+sqlite-3.11.0-2.fc23.x86_64
+sqlite-libs-3.11.0-2.fc23.x86_64
+sssd-client-1.13.3-5.fc23.x86_64
 strace-4.11-1.fc23.x86_64
 sudo-1.8.15-1.fc23.x86_64
 systemd-222-14.fc23.x86_64
```

#### Appendix: Example 'atomic_version.txt'
```
# cat atomic_version.txt
23.75 (6d9211c3fa)
```
