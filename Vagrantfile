# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

VMS = {
  :trusty => {
    :box => "ubuntu/trusty64"
  }
}

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  VMS.each_pair do |name, options|

    config.vm.define name do |vm_config|

      # Set proper box
      vm_config.vm.box = options[:box]

      # Update system and install requirements
      vm_config.vm.provision "shell" do |sh|
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
      vm_config.vm.provision "shell" do |sh|
        sh.inline = "cd /vagrant \
                      && rm -f tests/__pycache__/*.pyc \
                      && py.test -v"
        sh.privileged = false
      end

      # Use trigger plugin to set environment variable used by Ansible
      # Needed with 2.0 home path change
      vm_config.vm.provision "trigger" do |trigger|
        trigger.fire do
          ENV['ANSIBLE_ROLES_PATH'] = '../'
        end
      end

      # Run Ansible provisioning
      vm_config.vm.provision "ansible" do |ansible|
        ansible.playbook  = "tests/test_vagrant.yml"
      end

      # Run Serverspec tests
      vm_config.vm.provision "serverspec" do |serverspec|
        serverspec.pattern = 'spec/*_spec.rb'
      end

    end
  end
end

