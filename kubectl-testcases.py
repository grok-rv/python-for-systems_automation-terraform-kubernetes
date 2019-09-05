'''
Author: Ramu Reddy

This python script is used to run kubernetes test cases and output to a kubectl-result.txt file x
All you have to do is change the user = <your  uid> , ssh_key = <your uam pub key> ,  hostname details of the server where kubectl commands can be run

I ran this from "XXX" jump server which can access the server where kubectl commands can be run

'''
import paramiko
import os

hostname='fqdn of kubectl or genesis server'
user='username'
ssh_key='path-to-your-key.pub'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=user, key_filename=ssh_key)

def kubectl(command):
  print('######################################')
  stdin, stdout, stderr = ssh.exec_command(command)
  with open('/home/user/kubectl-result.txt','a+') as file:

    file.write('#################################################\n')
    file.write('\n')
    file.write(command)
    file.write('\n')
    for line in stdout.readlines():
      file.write(line.decode('utf8'))
  file.close()

def taskName(*taskname):
  kubeconfig = "--kubeconfig=/etc/kubernetes/admin/kubeconfig.yaml"
  for name in taskname:
    if name == 'comp401':
      print('####################################################')
      print('comp-401: check if all nodes are healthy and in ready state')
      comp401 = 'sudo kubectl get nodes -o wide'+ ' '+ str(kubeconfig)
      kubectl(comp401)
    elif name == 'comp402':
      print('########################################################')
      print('comp-402: check if all pods are healthy')
      comp402 = 'sudo kubectl get po --all-namespaces'+ ' '+str(kubeconfig)+ ' | grep -v Running | grep -v Completed'
      kubectl(comp402)
    elif name == 'comp403':
      print('########################################################')
      print('comp-403: list the stateful sets of all namespaces and make sure they are running')
      comp403 = 'sudo kubectl get sts --all-namespaces'+ ' '+ str(kubeconfig)
      kubectl(comp403)
    elif name == 'comp404':
      print('########################################################')
      print('comp-404: check  if all jobs are executed and running fine . desire and succesful matching')
      comp404 = 'sudo kubectl get jobs --all-namespaces'+ ' '+ str(kubeconfig)
      kubectl(comp404)
    elif name == 'comp405':
      print('########################################################')
      print('comp-405: verify daemon sets. check if all the daemon sets are started and matching the desired count')
      comp405 = 'sudo kubectl get ds --all-namespaces'+ ' '+ str(kubeconfig)
      kubectl(comp405)
    elif name == 'comp406':
      print('########################################################')
      print('comp-406: get deployments of all namespaces and they are matching the desired')
      comp406 = 'sudo kubectl get deployment --all-namespaces'+ ' '+ str(kubeconfig)
      kubectl(comp406)
    elif name == 'comp407':
      print('########################################################')
      print('comp-407: verify kubernetes namespaces and all are in active state')
      comp407 = 'sudo kubectl get ns'+ ' '+ str(kubeconfig)
      kubectl(comp407)
    elif name == 'comp409':
      print('########################################################')
      print('comp-409: verify the physical volumes claims are in Bound state for ucp services')
      comp409 = 'sudo kubectl get pvc -n ucp'+ ' '+ str(kubeconfig)
      kubectl(comp409)
    elif name == 'comp410':
      print('########################################################')
      print('comp-410: Check the kubernetes event errors for openstack ns')
      comp410 = 'sudo kubectl get events -n openstack'+ ' '+str(kubeconfig)+ ' '+' | grep error'
      kubectl(comp410)
    elif name == 'comp411':
      print('########################################################')
      print('comp-411: Check the kubernetes event errors for tenant-ceph namespace')
      comp411 = 'sudo kubectl get events -n tenant-ceph'+ ' '+str(kubeconfig)+' '+' | grep error'
      kubectl(comp411)
    elif name == 'comp412':
      print('########################################################')
      print('comp-412: Check the kubernetes event errors for osh-infra namespace')
      comp412 = 'sudo kubectl get events -n osh-infra'+ ' '+str(kubeconfig)+ ' '+' | grep error'
      kubectl(comp412)
    elif name == 'comp413':
      print('########################################################')
      print('comp-413: Check the kubernetes event errors for kube-system namespace')
      comp413 = 'sudo kubectl get events -n kube-system'+ ' '+str(kubeconfig)+ ' '+' | grep error'
      kubectl(comp413)
    elif name == 'comp414':
      print('########################################################')
      print('comp-414: Check the kubernetes events for ucp namespace')
      comp414 = 'sudo kubectl get events -n ucp'+ ' '+str(kubeconfig)+ ' '+' | grep error'
      kubectl(comp414)
    elif name == 'comp415':
      print('########################################################')
      print('comp-415: Verify the endpoints for openstack namespace')
      comp415 = 'sudo kubectl get endpoints -n openstack'+ ' '+ str(kubeconfig)
      kubectl(comp415)
    elif name == 'comp416':
      print('########################################################')
      print('comp-416: Verify the endpoints for ceph namespace')
      comp416 = 'sudo kubectl get endpoints -n ceph'+ ' '+ str(kubeconfig)
      kubectl(comp416)
    elif name == 'comp417':
      print('########################################################')
      print('comp-417: Verify the endpoints for tenant-ceph namespace')
      comp417 = 'sudo kubectl get endpoints -n tenant-ceph'+ ' '+ str(kubeconfig)
      kubectl(comp417)
    elif name == 'comp418':
      print('########################################################')
      print('comp-418: Verify the endpoints for ucp namespace')
      comp418 = 'sudo kubectl get endpoints -n ucp'+ ' '+ str(kubeconfig)
      kubectl(comp418)
    elif name == 'comp419':
      print('########################################################')
      print('comp-419: Verify the ingress cofig for openstack services')
      comp419 = 'sudo kubectl get ingress -n openstack'+ ' '+ str(kubeconfig)
      kubectl(comp419)
    elif name == 'comp420':
      print('########################################################')
      print('comp-420: Verify the ingress cofig for ucp services ')
      comp420 = 'sudo kubectl get ingress -n ucp'+ ' '+ str(kubeconfig)
      kubectl(comp420)
    elif name == 'comp421':
      print('########################################################')
      print('comp-421:  Verify the ingress cofig for ceph services')
      comp421 = 'sudo kubectl get ingress -n ceph'+ ' '+ str(kubeconfig)
      kubectl(comp421)
    elif name == 'comp422':
      print('########################################################')
      print('comp-422: verify the physical volumes claims are in Bound state for openstack namespace')
      comp422 = 'sudo kubectl get pvc -n openstack'+ ' '+ str(kubeconfig)
      kubectl(comp422)
    elif name == 'comp423':
      print('########################################################')
      print('comp-423: verify the physical volumes claims are in Bound state for osh-infra namespace')
      comp423 = 'sudo kubectl get pvc -n osh-infra'+ ' '+ str(kubeconfig)
      kubectl(comp423)
    elif name == 'comp424':
      print('########################################################')
      print('comp-424: verify the physical volumes are configured for openstack namespaces.')
      comp424 = 'sudo kubectl get pv -n openstack'+ ' '+ str(kubeconfig)
      kubectl(comp424)
    elif name == 'comp425':
      print('########################################################')
      print('comp-425: verify the physical volumes are configured for ucp namespaces.')
      comp425 = 'sudo kubectl get pv -n ucp'+ ' '+ str(kubeconfig)
      kubectl(comp425)
    elif name == 'comp426':
      print('########################################################')
      print('comp-426: verify the physical volumes are configured for osh-infra namespaces.')
      comp426 = 'sudo kubectl get pv -n osh-infra'+ ' '+ str(kubeconfig)
      kubectl(comp426)
    elif name == 'comp427':
      print('########################################################')
      print('comp-427: Verify pod disruption budgets are configured for pods')
      comp427 = 'sudo kubectl get pdb -n openstack'+ ' '+ str(kubeconfig)
      kubectl(comp427)
    elif name == 'comp428':
      print('#########################################################')
      print('comp-428: Verify kubernetes cluster components health statuses')
      comp428 = 'sudo kubectl get cs'+ ' '+ str(kubeconfig)
      kubectl(comp428)
    else:
      print("error")

taskName('comp401','comp402','comp403','comp404','comp405','comp406','comp407','comp409','comp410','comp411','comp412','comp413','comp414','comp415','comp416','comp417','comp418','comp419','comp420','comp421','comp422','comp423','comp424','comp425','comp426','comp427','comp428')

ssh.close()
