#!/usr/bin/python3


import dns.resolver as resolver
import sys, subprocess

record_types = ['A', 'AAAA', 'MX', 'NS', 'CNAME', 'PTR', 'SOA', 'TXT', 'SPF']
sub_domains = ['www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk', 'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'm', 'imap', 'test', 'ns', 'blog', 'pop3', 'dev', 'www2', 'admin', 'forum', 'news', 'vpn', 'ns3', 'mail2', 'new', 'mysql', 'old', 'lists', 'support', 'mobile', 'mx', 'static', 'docs', 'beta', 'shop', 'sql', 'secure', 'demo', 'cp', 'calendar', 'wiki', 'web', 'media', 'email', 'images', 'img', 'www1', 'intranet', 'portal', 'video', 'sip', 'dns2', 'api', 'cdn', 'stats', 'dns1', 'ns4', 'www3', 'dns', 'search', 'staging', 'server', 'mx1', 'chat', 'wap', 'my', 'svn', 'mail1', 'sites', 'proxy', 'ads', 'host', 'crm', 'cms', 'backup', 'mx2', 'lyncdiscover', 'info', 'apps', 'download', 'remote', 'db', 'forums', 'store', 'relay', 'files', 'newsletter', 'app', 'live', 'owa', 'en', 'start', 'sms', 'office', 'exchange', 'ipv4']


try:
	domain = sys.argv[1]

except IndexError:
	print(f'\nYou must specify a domain to check.\nExample: Python3 dns_check.py example.com\n')
	quit()

print(f'\n-----------------\n{domain.upper()}\n-----------------\n')

for rec_type in record_types:
	try:
		answer = resolver.resolve(domain, rec_type)
		for server in answer:
			print(f'{rec_type}: {server.to_text()}')
	except resolver.NoAnswer:
		print(f'{rec_type}: No Record')
		pass
	except resolver.NXDOMAIN:
		print(f'{domain} does not exist -- NXDOMAIN')
		quit()
	except KeyboardInterrupt:
		print(f'User Quit!')
		quit()

print(f'\n-----------------\n SUBDOMAINS\n-----------------\n')

subdomain = f'*.{domain}'
wildcard = subprocess.check_output([f'dig +short { subdomain}'], shell=True)
if wildcard:
	print(f"Wildcard Subdomain Found. Quitting.")
	quit()
else:
	for sub in sub_domains:
		subdomain = f'{sub}.{domain}'
		try:
			sub_answer = resolver.resolve(subdomain, 'A')
			if sub_answer:
				print(f' {subdomain}')
			else:
				sub_answer = resolver.resolve(subdomain, 'CNAME')
				if sub_answer:
					print(f' {subdomain}')
		except  resolver.NoAnswer:
			pass
		except resolver.NXDOMAIN:
			pass
		except KeyboardInterrupt:
			print(f'User Quit!')
			quit()
		except Exception as Err:  ## Catch everything else
			print(f'Error: {Err}')
			pass