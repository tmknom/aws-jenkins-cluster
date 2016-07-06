# aws-jenkins-cluster

## 使い方

### jenkins_masterのプロビジョニング

```bash
$ fab itamae_jenkins_master -H <ip_address>
```

### jenkins_slaveのプロビジョニング

```bash
$ fab itamae_jenkins_slave -H <ip_address>
```

### AWSの環境構築

一回だけやればOK。

```bash
$ fab build_vpc
$ fab build_security_group
$ fab build_ec2
```

### AWSの環境削除

すべてキレイにしたいなら。

```bash
$ fab delete_ec2
$ fab delete_security_group
$ fab delete_vpc
```

## インストール

```bash
$ git cloen git@github.com:tmknom/aws-jenkins-cluster.git
$ cd aws-jenkins-cluster
$ make
```

## 依存ツール

* AWS CLI
* Fabric
* terraform
* direnv
