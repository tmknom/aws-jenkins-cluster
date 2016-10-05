# aws-jenkins-cluster

## AMIの作り方

後で自動化予定。。

1. Amazon Linux の AMI からインスタンス作成
2. jenkins_base のプロビジョニング
3. プロビジョニング後のインスタンスを AMI 化
4. jenkins_base の AMI から 2 つインスタンス作成
5. jenkins_master と jenkins_slave をそれぞれプロビジョニング
6. プロビジョニング後のインスタンスを AMI 化


## 各タスクの使い方

### jenkins_baseのプロビジョニング

```bash
$ fab itamae_jenkins_base -H <ip_address>
```

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
