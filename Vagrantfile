# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"

  # Update system and install requirements
  config.vm.provision "shell" do |sh|
    sh.inline = "test -d /tmp/ansible \
                  || (sudo apt-get update \
                  && sudo apt-get install python-pip curl git -y \
                  && sudo pip install paramiko PyYAML Jinja2 httplib2 \
                                      six pytest \
                  && cd /tmp \
                  && git clone https://github.com/ansible/ansible.git \
                  && cd ansible \
                  && git checkout v2.0.0-0.8.rc3 \
                  && git submodule init \
                  && git submodule update \
                  && sudo make install)"
  end

  # Run pytest tests for filter plugins
  config.vm.provision "shell" do |sh|
    sh.inline = "cd /vagrant && rm -f tests/__pycache__/*.pyc && py.test -v"
    sh.privileged = false
  end

  # Run Ansible provisioning
  config.vm.provision "ansible" do |ansible|

    # Playbook used to test role
    ansible.playbook  = "tests/test_vagrant.yml"
  end

  # Run Serverspec tests
  config.vm.provision "serverspec" do |serverspec|

    # Define spec files pattern
    serverspec.pattern = 'spec/*_spec.rb'
  end

end

