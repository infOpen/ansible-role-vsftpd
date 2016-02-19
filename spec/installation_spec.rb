require 'serverspec'

if ENV['TRAVIS']
    set :backend, :exec
end

if ['debian', 'ubuntu'].include?(os[:family])
    describe 'Specific Debian and Ubuntu family checks' do

        it 'install role packages' do
            packages = Array[ 'vsftpd', 'db5.3-util' ]

            packages.each do |pkg_name|
                expect(package(pkg_name)).to be_installed
            end
        end

        describe service('vsftpd') do
            it { should  be_running }
            it { should  be_enabled }
        end

        describe port(21) do
            it { should be_listening.on('127.0.0.1').with('tcp') }
        end

        describe process("vsftpd") do
            its(:user) { should eq "root" }
        end

        describe user('ftp') do
            it { should exist }
            it { should have_login_shell '/bin/false' }
        end
    end
end

describe iptables do
  it { should have_rule('-A INPUT -p tcp -m tcp --dport 21 -m conntrack --ctstate NEW,ESTABLISHED -m comment --comment "Allow ftp inbound connections on port 21" -j ACCEPT') }
  it { should have_rule('-A INPUT -p tcp -m tcp --dport 20 -m conntrack --ctstate RELATED,ESTABLISHED -m comment --comment "Allow ftp inbound connections on port 20" -j ACCEPT') }
  it { should have_rule('-A INPUT -p tcp -m tcp --dport 60000:60010 -m conntrack --ctstate NEW,RELATED,ESTABLISHED -m comment --comment "Allow passive inbound connections" -j ACCEPT') }
end

