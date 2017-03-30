def main():
	x=open ("settings.py",'r');
	salida=x.read()
	x.close()
	print salida

if __name__ == "__main__":
    main()

