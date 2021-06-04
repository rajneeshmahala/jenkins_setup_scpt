import os
os.system(sudo yum install -y yum-utils)
os.system(sudo yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo)
os.system(sudo yum install docker-ce docker-ce-cli containerd.io)
os.system(docker run -p 8080:8080 -p 50000:50000 -d -v jenkins_home:/var/jenkins_home jenkins/jenkins)

