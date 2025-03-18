import meraki

# Defining your API key as a variable in source code is discouraged.
# This API key is for a read-only docs-specific environment.
# In your own code, use an environment variable as shown under the Usage section
# @ https://github.com/meraki/dashboard-api-python/


### Step-1 --- establish a session

API_KEY = "161df6224c6d2c8b9a1edfbc89868a85088bb9e2"
dashboard = meraki.DashboardAPI(API_KEY,
                                output_log=False,
                                print_console=False)

### Step-2 --- gety a list of the organizations

organizations = dashboard.organizations.getOrganizations()
# print(organizations)

myfmt = "{:24s}{:2s}{:45s}{:2s}{:20s}"
print(myfmt.format("Org ID", "|", "Org Name", "|", "Org URL"))
print("-" * 100)
for org in organizations:
    print(myfmt.format(org['id'], "|", org['name'], "|", org['url']))
print()
org = organizations[0]

### Step-3 --- Get a list of all the networks for the Cisco DevNet organization

networks = dashboard.organizations.getOrganizationNetworks(org['id'],
                                                           total_pages='all')
print(myfmt.format("Network ID", "|", "Network Name", "|", "Tags"))
print("-" * 100)
for net in networks:
    print(myfmt.format(net['id'], "|", net['name'], "|", str(net['tags'])))
print()

### Step-4 --- Get a list of all the devices that are part of the Always On Network

devices = dashboard.organizations.getOrganizationDevices(org['id'],
                                                        total_pages='all')
print(myfmt.format("Device Model", "|", "Serial", "|", "MAC"))
print("-" * 100)
for dev in devices:
    print(myfmt.format(dev['model'], "|", dev['serial'], "|", dev['mac']))
print()