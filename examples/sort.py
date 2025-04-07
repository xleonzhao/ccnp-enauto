def ip_sort_key(ip):
    """Convert an IP address string to a tuple of integers for sorting."""
    x = tuple(map(int, ip.split(".")))
    print(x)
    return x

def sort_ip_addresses(ip_list):
    """Sort a list of IPv4 addresses."""
    return sorted(ip_list, key=ip_sort_key)

# Example list of IPv4 addresses
ip_list = ["192.168.1.100", "10.0.0.1", "172.16.0.5", "192.168.1.1", "10.0.0.255"]

# Sorting the list
sorted_ips = sort_ip_addresses(ip_list)
print(sorted_ips)

y = [(4, 5, 6), (1, 2, 3), (7, 8, 9)]
y2 = sorted(y)
print(y2)