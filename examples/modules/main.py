import mypackage as pkg

a=3
b=5
pkg.greet()
pkg.greet('hello, world')
print(f"{a} + {b} = {pkg.add(a,b)}")
print(f"{a} * {b} = {pkg.times(a,b)}")
