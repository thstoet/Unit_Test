
def foo():
	print(foo)
	raise RuntimeError 

try:								#bissle rumspielen
	e = 5/0
	#foo()
	#e = a + b

	
except ZeroDivisionError:
	print("ZeroDivisionError")

except RuntimeError:
		print("Runtime Error")
#except Exception:
#	print("Normalo")

