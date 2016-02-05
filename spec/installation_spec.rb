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

